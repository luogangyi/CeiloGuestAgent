import logging
from guestagent import GuestAgent
from logUtils import SimpleLogAdapter
from vmchannels import Listener


_VMCHANNEL_DEVICE_NAME = 'com.redhat.rhevm.vdsm'
# This device name is used as default both in the qemu-guest-agent
# service/daemon and in libvirtd (to be used with the quiesce flag).
_QEMU_GA_DEVICE_NAME = 'org.qemu.guest_agent.0'

def _makeChannelPath(deviceName):
    # return constants.P_LIBVIRT_VMCHANNELS + self.id + '.' + deviceName
    return "/var/lib/libvirt/qemu/channels/"+deviceName


if __name__ == '__main__':
    mylogger = logging.getLogger("centos-ga")
    _guestSocketFile = _makeChannelPath(_VMCHANNEL_DEVICE_NAME)
    mylog = SimpleLogAdapter(mylogger, {"vmId": 'centos-ga'})
    channelListener = Listener(mylog)
    guestAgent = GuestAgent(_guestSocketFile, channelListener, mylog)
    pass