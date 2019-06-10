"""Program to compute the displacement of a particle in damped harmonic oscillator for given inputs of damping conditions"""

import math
import matplotlib.pyplot as plt

"""Calculating Over Damped Solution"""

def over_damped(omega_zero, gamma, t):

    p=math.sqrt((gamma**2)/4 - omega_zero**2) #Calculating p
    a = 1 #Value of a
    b = (gamma)/(2*p) #Calculating b

    over_damped = math.exp(-0.5*gamma*t)*(a*math.cosh(p*t)+b*math.sinh(p*t)) #Calculating over damped solution

    return over_damped

"""Calculating Critical Damped Solution"""

def critical_damped(omega_zero, gamma, t):
    a = 1 #Value of a
    b = (gamma)/2 #Calculating b

    critical_damped = math.exp(-0.5*gamma*t)*(a+b*t) #Calculating critical damped solution

    return critical_damped

"""Calculating Under Damped Solution"""

def under_damped(omega_zero, gamma, t):

    omega = math.sqrt(omega_zero**2-(gamma**2)/4) #Calculating omega
    a = 1 #Value of a
    b = gamma/(2*omega) #Calculating b

    under_damped = math.exp(-0.5*gamma*t) * (a*math.cos(omega*t)+b*math.sin(omega*t)) #Calculating under damped solution

    return under_damped

"""Creating plot"""

def plotting(x,y,omega_zero):

    ub = 5*math.pi/(omega_zero) #Calculating upper bound for x-range

    plt.plot(x,y, "r") #Plotting gathered data
    plt.title("Graph of displacement against time for given damping conditions") #Title
    plt.xlabel("Time, seconds") #X-Axis Label
    plt.xlim(0.0,ub) #Limits X-Axis to range 0.0 to Upper Bound
    plt.ylabel("Displacement, m") #Y-Axis Label
    plt.show()

    return

"""Main program"""

def main():

    gamma=float(input("Enter the value gamma: ")) #Call for input of gamma
    omega_zero=float(input("Enter the natural frequency: ")) #Call for input of omega null
    points=int(input("Enter the number of points you wish to plot: ")) #Call for interval accuracy

    tdata = [0.0, (5*math.pi)/(omega_zero*points)] #Gathering list of time values
    for i in range(0,points):
        t = (5*math.pi)/(omega_zero*points)
        t += (tdata[i+1])
        tdata.append(t)

    displacementdata=[] #Gathering displacement data
    for i in tdata:
        if gamma > 2 * omega_zero: #Solving if over damped
            displacement = over_damped(omega_zero, gamma, i)
            displacementdata.append(displacement)
        elif gamma == 2 * omega_zero: # Solving if critical damped
            displacement = critical_damped(omega_zero, gamma, i)
            displacementdata.append(displacement)
        else: # Solving if under damped
            displacement = under_damped(omega_zero, gamma, i)
            displacementdata.append(displacement)

    plotting(tdata,displacementdata,omega_zero) #Plot function

main()
