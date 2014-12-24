import logging
from time import strftime
from time import sleep
from guestagent import GuestAgent
from logUtils import SimpleLogAdapter
from vmchannels import Listener


_VMCHANNEL_DEVICE_NAME = 'com.redhat.rhevm.vdsm'
# This device name is used as default both in the qemu-guest-agent
# service/daemon and in libvirtd (to be used with the quiesce flag).
_QEMU_GA_DEVICE_NAME = 'org.qemu.guest_agent.0'


def _makeChannelPath(deviceName):
    # return constants.P_LIBVIRT_VMCHANNELS + self.id + '.' + deviceName
    return "/var/lib/libvirt/qemu/channels/centosga."+deviceName


if __name__ == '__main__':

    log_filename = '/var/log/ceiloga/vds_bootstrap_complete.'+strftime("%Y%m%d_%H%M%S")+'.log'
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=log_filename,
                    filemode='w')
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    mylogger = logging.getLogger("centos-ga")
    mylogger.addHandler(ch)
    #_guestSocketFile = _makeChannelPath(_VMCHANNEL_DEVICE_NAME)
    #_guestSocketFile = _makeChannelPath(_QEMU_GA_DEVICE_NAME)
    _guestSocketFile = "/var/lib/libvirt/qemu/com.redhat.rhevm.vdsm.instance-00000002.sock"
    mylog = SimpleLogAdapter(mylogger, {"vmId": 'centos-ga'})
    channelListener = Listener(mylog)
    guestAgent = GuestAgent(_guestSocketFile, channelListener, mylog)

    try:
        channelListener.settimeout(30)
        channelListener.start()

        guestAgent.connect()
        #guestAgent.desktopLock()
        while(True):
            print guestAgent.getGuestInfo()
            print guestAgent.guestDiskMapping
            print(guestAgent.isResponsive())
            if guestAgent and guestAgent.isResponsive():
                print guestAgent.getStatus()
            sleep(1)
    except Exception:
        mylog.exception("Failed to connect to guest agent channel")

    pass