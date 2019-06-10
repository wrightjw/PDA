"""Programs to calculate trajectory of projectiles or ratio of kinetic energy of projectiles at given angles of projection"""

import math
import matplotlib.pyplot as plt

"""Function to call for initial conditions depending on the program"""

def initial_conditions(program):

    if program == 'TRAJECTORY': #Asks for inputs for trajectory program
        v_0 = float(input("Enter the magnitude of the initial velocity in m/s: ")) # Prompting for initial velocity
        theta = float(input("Enter the angle of projection in degrees: ")) # Prompting for angle of projection
        beta = float(input("Enter the normalised drag coefficient : ")) # Prompting for normalised drag coefficient
        dt = float(input("Enter the step interval in seconds: ")) # Promoting for step interval
        g = 9.81 #Defining gravitational constant
        vx_0 = float(v_0*math.cos(math.radians(theta))) #Calculating initial velocity in horizontal direction
        vy_0 = float(v_0*math.sin(math.radians(theta))) #Calculating initial velocity in vertical direction        
        
        return vx_0,vy_0,theta,beta,dt,g
    
    elif program == 'RATIO': #Asks for inputs for ratio program
        v_0 = float(input("Enter the initial velocity in m/s: ")) # Prompting for initial velocity
        beta = float(input("Enter the drag coefficient : ")) # Prompting for normalised drag coefficient
        dt = float(input("Enter the step interval in seconds: ")) # Promoting for step interval
        g = 9.81 #Defining gravitational constant

        return v_0,beta,dt,g

    else: #Typo prevention
        print("USER ERROR: Program name must be typed as asked for above. Type: TRAJECTORY or RATIO . ")
    
"""Function to calculate the trajectory"""

def trajectory(vx_0,vy_0,theta,beta,dt,g):

    velocity_x = [vx_0]  #Horitzontal velocity list
    velocity_y = [vy_0] #Vertical velocity list
    displacement_x = [0.0] #Horitzontal displacement list starting at x=0
    displacement_y= [0.0] #Vertical displacement list starting at y=0

    for i in range(0,100000):

        magnitude_velocity = float((velocity_x[i]**2+velocity_y[i]**2)**0.5) #Calculating initial magnitude of velocity

        vx = velocity_x[i]+dt*(-1*beta*magnitude_velocity*velocity_x[i]) #Calculating each X direction of velocity at each point for given acceleration
        velocity_x.append(vx)
        vy = velocity_y[i]+dt*(-1*beta*magnitude_velocity*velocity_y[i])-dt*g #Calculating each Y direction of velocity at each point 
        velocity_y.append(vy)

        x = displacement_x[i] + dt*velocity_x[i] #Calculating each X direction displacement for given time
        displacement_x.append(x)
        y = displacement_y[i] + dt*velocity_y[i] #Calculating each Y direction displacement for given time
        displacement_y.append(y)

        if y<=0:
            break
    
    """Plotting vertical displacement against horizontal displacement"""
    
    plt.plot(displacement_x,displacement_y)
    plt.title("Displacement Plot of Trajectory of a Particle")
    plt.xlabel("Horizontal Displacement (m)")
    plt.ylabel("Vertical Displacement (m)")
    plt.xlim(0.0, max(displacement_x))
    plt.ylim(0.0,max(displacement_y))
    plt.show()
    
    return

"""Function to calculate the ratio of final kinetic energy to initial kinetic energy against launch angle for given inputs"""

def ratio(v_0,beta,dt,g):

    theta_values = [0.0] #List of thetas between 0 and 90
    KE_ratios = [] #List of kinetic energy ratios
    velocity_x0 = [] #List of horizontal components of initial velocities for each theta
    velocity_y0 = [] #List of vertical components of initial velocities for each theta

    theta = 0.0 #Setting initial theta value
    while theta < 90:
        if theta<0:
            break
        else:
            theta = float(theta)+0.001 #Dividing theta into strips
            theta_values.append(theta)
            
    for i in range(0,len(theta_values)):

            vx_0 = v_0*math.cos(math.radians(theta_values[i])) #Calculating initial horizontal velocity for each theta
            velocity_x0.append(vx_0)
            vy_0 = v_0*math.sin(math.radians(theta_values[i])) #Calculating initial vertical velocity for each theta
            velocity_y0.append(vy_0)

            velocity_x = [vx_0] #List of horizontal velocities for each theta as it projects
            velocity_y = [vy_0] #List of vertical velocities for each theta as it projects
            displacement_y= [0.0] #Vertical displacement list starting at y=0
    
            for i in range(0,10000):

                magnitude_velocity = float((velocity_x[i]**2+velocity_y[i]**2)**0.5) #Calculating initial magnitude of velocity

                vx = velocity_x[i]+dt*(-1*beta*magnitude_velocity*velocity_x[i]) #Calculating each X direction of velocity at each point for given acceleration
                velocity_x.append(vx)
                vy = velocity_y[i]+dt*(-1*beta*magnitude_velocity*velocity_y[i])-dt*g #Calculating each Y direction of velocity at each point 
                velocity_y.append(vy)

                y = displacement_y[i] + dt*velocity_y[i] #Calculating each Y direction displacement for given time
                displacement_y.append(y)

                if y<0:
                    break

            KE_ratio = float((velocity_x[-1]**2)+(velocity_y[-1]**2))/float((v_0)**2) #Calculating kinetic energy ratio - same as (Vf)^2/(Vs)^2
            KE_ratios.append(KE_ratio)

    """Plotting the ratio of final kinetic energy to initial kinetic energy against launch angle"""
    
    plt.plot(theta_values,KE_ratios)
    plt.title("Graph of ratio of kinetic energies of finish to start against angle")
    plt.xlabel("Launch angle (degrees)")
    plt.ylabel("Ratio of final kinetic energy to initial kinetic energy")
    plt.xlim(0.0, 90.0)
    plt.show()
    
    return

def main():

    program = str(input("Type TRAJECTORY for trajectory program or type RATIO for ratio program: ")) #Asking which program to run
    start = initial_conditions(program) #Calling for initial conditions for program

    if program == 'TRAJECTORY':
        trajectory(start[0],start[1],start[2],start[3],start[4],start[5]) #Calling for trajectory function under given inputs
    elif program == 'RATIO':
        ratio(start[0],start[1],start[2],start[3]) #Calling for ratio function under given inputs
    else:
        print("Try again.") #Typo prevention

main()
