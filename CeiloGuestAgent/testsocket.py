import socket
import time

if __name__ == '__main__':
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    #sock.connect("/var/lib/libvirt/qemu/channels/centosga.com.redhat.rhevm.vdsm")
    sock.connect("/var/lib/libvirt/qemu/com.redhat.rhevm.vdsm.instance-00000002.sock")
    print sock.recv(1024)
    print sock.recv(1024)
    print sock.recv(1024)
    print sock.recv(1024)
    time.sleep(2)
    sock.send('1')

    sock.close()