#!/usr/bin/python3

import os, datetime, re, getpass, logging
from systemd import journal
from time import sleep, strftime, time
from database import Database
from sensors import cpu

database = Database()

# script variables
script_path=os.path.splitext(__file__)[0]
script_basename=os.path.basename(script_path)
script_name=re.sub('[^0-9a-zA-Z]+', '', script_basename)

# get username from getpass
username=getpass.getuser()

temperature=cpu.temperature()
database.log_entry(temperature)

datetime_now = datetime.datetime.now()
datetime_str = datetime_now.strftime("%Y-%m-%d %H:%M:%S")

print(f"[{script_name} {datetime_str}] CPU Temp.: {temperature}") 
