#!/usr/bin/env python

import os
import sys
import datetime

"""
Zips and unzips using built-in zip utility on a mac
"""

def zip_file(file):
    #Get user
    USER = os.environ["USER"]
    now = datetime.datetime.now()
    timestamp = "%s-%s-%s_%s%s%s"%(now.month,now.day,now.year,now.hour,now.minute,now.second)
    file = sys.argv[1]
    default_location = "/Users/%s/Desktop/"%USER
    zip = "zip -r %s%s-%s.zip %s -x '*.DS_Store' -x '__MACOSX'"%(default_location,file,timestamp,file)
    #print(zip)
    os.system(zip)
    #print("COMMAND: %s"%zip)
    print("%s-%s.zip saved to: %s"%(file,timestamp,default_location))

def unzip_file(file):
    print("in unzip_file.. exiting..")
    sys.exit()

def menu(file):
    choice = int(input("1: zip file/folder\n2: unzip file/folder\n0:Quit\n"))
    if choice == 1:
        zip_file(file)
    elif choice == 2:
        unzip_file(file)
    elif choice == 0:
        print("exiting...")
        sys.exit()
    else:
        print("Please choose from above menu... exiting..")
        sys.exit()

if __name__ == "__main__":
    try:
        file = sys.argv[1]
        menu(file)
    except IndexError:
        print("Requires file/folder name.")
        sys.exit()


