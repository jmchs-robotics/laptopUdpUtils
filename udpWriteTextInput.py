#
# udpWriterTextInput.py
#
# use: udpWriterTextInput.py [port [ip_address]]
# port default is 59330
# ip_address default is local network broadcast address, 
#  from 'ifconfig |grep roadcast'
#
# write the text input from keyboard to UDP socket.
#

from socket import *
import sys
import os
import re

# default ip set to broadcast address
# ip = '192.168.1.255'
f = os.popen( 'ifconfig |grep "roadcast"')
a = f.read()
a = re.search( 'cast[:\s](\d+\.\d+\.\d+\.\d+)', a)
ip = a.group(1)

port = 59330

# user-supplied ip and port
if len(sys.argv) >= 2:
  port = int( sys.argv[1])
  if len(sys.argv) >= 3:
    ip = sys.argv[2]
print( "Writing to %s:%s" % ( ip, port))
print( "Type a character or message and it'll be sent when you hit <Enter>")

s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
    b = raw_input()
    s.sendto( b, ( ip, port))
