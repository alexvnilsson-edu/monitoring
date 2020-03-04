from gpiozero import CPUTemperature

def temperature():
    cpu = CPUTemperature()
    return cpu.temperature
