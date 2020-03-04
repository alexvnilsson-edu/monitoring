#!/usr/bin/python3

from gpiozero import CPU

def get_cpu_temp():
    cpu = CPU()
    return cpu.temperature

