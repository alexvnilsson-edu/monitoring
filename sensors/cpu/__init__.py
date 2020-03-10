from gpiozero import CPUTemperature

def get_cpu_temp():
    cpu = CPUTemperature()
    return cpu.temperature
