from machine import ADC, Pin
import utime
import statistics


def get_capacitator_measurements():
    '''
    This function reads five times the ADC signal and returns the mean and std of those measurements. 
    
    '''
    soil_adc = ADC(Pin(26))
    five_measurements = []
    while len(five_measurements) <= 5:
        five_measurements.append(soil_adc.read_u16())
        utime.sleep(3)
    return statistics.mean(five_measurements), statistics.stdev(five_measurements) 

## It is useful to allow users to choose between reading and saving data. 

if __name__ == '__main__':

    type_of_measurement = str.lower(input('Read (R) / Save (S) \n'))

    if type_of_measurement == 's' or type_of_measurement == 'save':
            
        my_measure = get_capacitator_measurements()
            
        with open('out.txt', 'a') as f:  #This file is stored on the Raspberry, not PC!!
            f.write(str(my_measure) + '\n')
        
    elif type_of_measurement == 'r' or type_of_measurement == 'read':
        print(get_capacitator_measurements())
        
    else: 
        print('Please, choose between reading or saving data')