#!/usr/bin/python3

from database import Database
from sensors import cpu

database = Database()

temperature=cpu.temperature()
database.log_entry(temperature)
