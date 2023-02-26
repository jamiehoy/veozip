#!/opt/homebrew/bin/python3

"""
Zips and unzips using built-in zip utility on a mac
"""

import os
import sys
import datetime

def zip_file(file):

    """
    Compresses file/folder using built-in zip
    """

    #Get user
    current_user = os.environ["USER"]

    #Timestamp
    now = datetime.datetime.now()
    #timestamp = "%s-%s-%s_%s%s%s"%(now.month,now.day,now.year,now.hour,now.minute,now.second)
    timestamp = f"{now.month}.{now.day}.{now.year}.{now.hour}.{now.minute}.{now.second}"

    #Filename taken in as a argument
    file = sys.argv[1]
    #default_location = "/Users/%s/Desktop/"%current_user
    default_location = f"/Users/{current_user}/Desktop/"

    #Command String
    #compress_file = ("zip -r %s%s-%s.zip %s -x '"
    #"*.DS_Store' -x '__MACOSX'"%(default_location,file,timestamp,file))
    #compress_file = f"zip -r {default_location}{file}-{timestamp}.zip {file} -x '*.DS_Store' -x '__MACOSX'"
    compress_file = (
    f"zip -r {default_location}{file}-{timestamp}.zip {file}"
    f" -x '*.DS_Store'"
    f" -x '__MACOSX'"
)
    os.system(compress_file)
    #print("%s-%s.zip saved to: %s"%(file,timestamp,default_location))
    print(f"{file}-{timestamp}.zip saved to: {default_location}")

def menu(file):

    """
    Display a simple menu
    """

    choice = int(input("1: zip file/folder\n0: Quit\n"))
    if choice == 1:
        zip_file(file)
    elif choice == 0:
        print("exiting...")
        sys.exit()
    else:
        print("Please choose from above menu... exiting..")
        sys.exit()

if __name__ == "__main__":

    #Ensure an argument is passes (file/folder name)
    try:
        arg = sys.argv[1]
        menu(arg)
    except IndexError:
        print("Requires file/folder name.")
        sys.exit()
