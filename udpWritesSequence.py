#
# udpWriteSequence.py
#
# use: udpWriteSequence.py [port [ip_address]]
# port default is 59330
# ip_address default is local network broadcast address, 
#  from 'ifconfig |grep roadcast'
#
# Write a sequence of text lines to UDP socket.
#

from socket import *
import sys
import os
import re
import time

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
b = '10.00, 11.12, 12.22, 13.33, L'
c = '0.00, 0.00, 12.22, 13.33, C'
d = '0.00, 0.00, 12.22, 13.33, R'
print( "Writing the following string at 2 Hz: \n%s" % b)

s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

i = 0
while i < 60:
    i += 1
    s.sendto( b, ( ip, port))
    time.sleep( 0.0333333333)

i = 0
while i < 30:
    i += 1
    s.sendto( c, ( ip, port))
    time.sleep( 0.0333333333)

i = 0
while i < 60:
    i += 1
    s.sendto( d, ( ip, port))
    time.sleep( 0.0333333333)
