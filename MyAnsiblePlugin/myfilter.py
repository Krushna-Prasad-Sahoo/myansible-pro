# cd filter_plugins/
# vi myfilter.py

import os
import time
import datetime as dt
d = dt.date.today()
aaj = 'To{1} is {0:%d}, the {2} is {0:%B} and {3} is {0:%Y}.'.format(d, "day", "month", "year")
class FilterModule(object):
    def filters(self):
        return {
            'KPS_filter':self.KPS_filter,
        }
    def KPS_filter(self, kps_variable):
        if kps_variable == 'kps':
           os.system("clear")
           print("\n")
           os.system("tput setaf 6")
           print("          ***************--------- Welcome KP ----------***************")
           time.sleep(2)
           print("\n")
           os.system("tput setaf 5")
           print(aaj)
           os.system("tput setaf 3")
           print("\nSee your system process tree : ")
           print("\n")
           os.system("tput setaf 7")
           time.sleep(3)
           os.system("pstree")
           time.sleep(6)
           os.system("clear")
           os.system("tput setaf 6")
           print("\n          ***************--------- Welcome KP ----------***************")
           time.sleep(1)
           os.system("tput setaf 3")
           print("See the detailed process status :\n")
           os.system("tput setaf 7")
           os.system("ps  -au")
           time.sleep(3)
           print("\n")
           time.sleep(2)
           os.system("tput setaf 3")
           print("See the status")
           print("\n")
           time.sleep(2)
           os.system("tput setaf 7")
           os.system("sestatus")
           time.sleep(6)
           print("\n")
           os.system("clear")
           print("\n")
           time.sleep(1)
           os.system("clear")
           print("\n")
           os.system("tput setaf 3")
           print("\n          ***************--------- Thank You KP :) ----------***************")
           print("\n\t\t Now you see the Job Search Results & News Article  ..")
           time.sleep(2)
           os.system("tput setaf 7")

        else:
          os.system("clear")
          print()
          os.system("tput setaf 3")
          print("\n\tAuthorization Failed ..")
          time.sleep(3)
          print("\tSorry !! You are not KP, try Again :(")
          os.system("tput setaf 7")
          print()
          quit()
