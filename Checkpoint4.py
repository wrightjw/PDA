"""Program to calculate and plot log_power against time for given dataset"""

import math
import matplotlib.pyplot as plt

"""Function to plot data"""

def plotting(time_data,power_data):
    plt.plot(time_data,power_data)
    plt.title("Dataset plot of log power against time")
    plt.xlabel("Time, seconds")
    plt.ylabel("Log Power")
    plt.xlim(0.0, (len(time_data)/25000.0)) #Giving limits of interval
    plt.show()

    return

"""Main Function"""

def main(): 

    filename = str(input("Enter the file name: ")) # Calling for file
    filein = open(filename, "r") # Open file for reading
    input_data = filein.readlines() # Read in data as list of strings
    
    condensed_data = [] # Input data with \n removed
    cleaned_data = [] # Data without \n or comments
    voltage_data = [] # Data for voltage
    current_data = [] # Data for current
    power_data = [] # Data calculated as power
    log_power = [] # Log power
    time_data = [] # Time intervals

    for line in input_data: # Removing \n
        without_n = line[:-1]
        condensed_data.append(without_n)

    for line in condensed_data: #Removing lines with HASHTAG
        if "#" in line:
            pass
        else:
            cleaned_data.append(line)

    """Splitting voltage and current into 2 lists"""

    for line in cleaned_data:
        elements = line.split(" , ")
        voltage_data.append(elements[0]) # Putting first element into voltage data
        current_data.append(elements[1]) # Putting second element into voltage data

    """Adding times to time_data list"""
    start = 0.0
    for i in range(0,len(cleaned_data)):
        time = start + i/25000.0
        time_data.append(time)

    """Calculating Log Power and Adding to List power_data"""

    for i in range(0,len(cleaned_data)):
        power=float(voltage_data[i])*float(current_data[i]) # Calculating Power
        logpower=math.log(power) # ln(power)
        power_data.append(logpower)

    plotting(time_data,power_data)
         
    filein.close()

main()
