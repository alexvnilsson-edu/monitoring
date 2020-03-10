#!/usr/bin/python3

from database import Database
from sensors import cpu

database = Database()

temperature=cpu.get_cpu_temp()
database.log_entry(temperature)
