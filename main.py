#!/usr/bin/python3

import os, datetime, re, getpass, logging
from systemd import journal
from time import sleep, strftime, time
#from gpiozero import CPUTemperature
from sensors import cpu

# script variables
script_path=os.path.splitext(__file__)[0]
print(script_path)
script_basename=os.path.basename(script_path)
print(script_basename)
script_name=re.sub('[^0-9a-zA-Z]+', '', script_basename)
print(script_name)

#log = logging.getLogger(script_name)
#log.addHandler(JournalHandler())
#log.setLevel(logging.INFO)

# get username from getpass
username=getpass.getuser()

# directories
home_dir=os.path.join("/", "home", username)

if not os.path.isdir(home_dir):
    print(f"Expecting path \"{home_dir}\" to be an existing directory.")
    print(f"Try 'sudo mkdir -p /home/{username} && sudo chown -R {username}:{username} /home/{username}'")
    exit()

#logs_dir=os.path.join(home_dir, "logs")
#log_file=os.path.join(logs_dir, "temp-monitor.csv")

#cpu = CPUTemperature()
#cpu_temp=cpu.temperature

temperature=cpu.temperature()


datetime_now = datetime.datetime.now()
datetime_str = datetime_now.strftime("%Y-%m-%d %H:%M:%S")

print(f"[{script_name} {datetime_str}] CPU Temp.: {temperature}")

journal.send(
        MESSAGE=f"[{script_name} {datetime_str}] CPU Temp.: {temperature}",
#        priority=journal.Priority.INFO,
        cpu_temp=temperature,
)
#log.info(f"[{datetime_str}] CPU temperature={temperature}")

#with open(log_file) as log:
#    while True:
#        temp = cpu.temperature
