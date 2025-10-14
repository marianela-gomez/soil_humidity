from machine import ADC, Pin
import utime
import statistics


def get_capacitator_measurements():
    soil_adc = ADC(Pin(26))
    five_measurements = []
    while len(five_measurements) <= 5:
        five_measurements.append(soil_adc.read_u16())
        utime.sleep(3)
    return statistics.mean(five_measurements), statistics.stdev(five_measurements)

my_measure = get_capacitator_measurements()

with open('out.txt', 'a') as f:
    f.write(str(my_measure))
