# ENGR2050_08_jasayles.py
# Ethan Sayles
# Mar 30, 2017
import numpy as np
from matplotlib import pyplot as plt

#Class function for the range equation
class Range():
    def __init__(self, Xo, Yo, Vo, theta):                           #Initial bounds of the projectile
        self . Xo = Xo
        self.Yo = Yo
        self.Vo = Vo
        self.theta = np.deg2rad(theta)
        
    def x_calc(self, ro, vo, stop, step):                             #Function to find the x values
        t = np.arange(0, stop, step)
        x = []
        for i in t:
            x.append(ro + (vo * i))                                          #Range equation in the x axis
        return (x)
        
    def y_calc(self, ro, vo, stop, step):                              #Function to find the y values
        t = np.arange(0, stop, step)
        y = []
        for i in t:
            y.append(ro + (vo * i) + (.5 * -9.8 * (i ** 2)))       #Range equation in the y axis
        return (y)
        
    def plotable(self):
        vx = self.Vo * np.cos(self.theta)                                #x component of the velocity
        vy = self.Vo * np.sin(self.theta)                                 #y component of the velocity
        t_hmax = vy / 9.8                                                       #Theoretical time of the maximum height
        maxx_h = max(self.y_calc(self.Yo, vy, 2, 1e-2))        #Maximum y value
        max_h_dist =  (self.Xo + (vx * t_hmax))                       #x distance of the max theoretical height
        max_h = (self.Yo + (vy * t_hmax) + (.5 * -9.8 * (t_hmax ** 2)))        #Maximum theoretical height
        t_max = (-vy - np.sqrt((vy ** 2) - (4 * .5 * -9.8 * self.Yo))) / -9.8        #Time when the object hits the ground
        max_dist =  (self.Xo + (vx * t_max))                                                     #Distances at which the object hits the ground
        zero_h = (self.Yo + (vy * t_max) + (.5 * -9.8 * (t_max ** 2)))               #Height when the object hits the ground (0)
        points = [self.x_calc(self.Xo, vx, 2, 1e-2), self.y_calc(self.Yo, vy, 2, 1e-2), max_h_dist, max_h, max_dist, zero_h, t_max, maxx_h]
        return(points)
        
#Class to plot the points of a Range instance
class Plot():
    def __init__(self, function):
        self.func = function
    def show(self):                                                                                #function to plot the point of self.func
        plt.plot(self.func.plotable()[0], self.func.plotable()[1])               #plot the graph
        plt.plot(self.func.plotable()[2], self.func.plotable()[3],  'ro')     #plot the maximum height point
        plt.plot(self.func.plotable()[4], self.func.plotable()[5],  'ro')      #plot the point when the object hits the ground
        plt.title("Trajectory Motion",  fontsize = 20)
        plt.xlabel("Distance (m)",  fontsize=10)
        plt.ylabel("Height (m)",  fontsize=10)
        print ("The max theoretical height of the red function is %f meters." %(self.func.plotable()[3]))
        print ("The max height in the given bounds of the red function is %f meters." %(self.func.plotable()[7]))
        print ("The object from the red function reaches the ground after %f seconds." %(self.func.plotable()[6]))
        plt.show()
    def multiple(self, f):
        plt.plot(f.plotable()[0], f.plotable()[1])               #plot the graph
        plt.plot(f.plotable()[2], f.plotable()[3],  'ro')     #plot the maximum height point
        plt.plot(f.plotable()[4], f.plotable()[5],  'ro')      #plot the point when the object hits the ground



#Conditional to check for test cases
if __name__ == '__main__':
    f = Range(0, 0, 20, 45)
    f2=Range(f.plotable()[2], f.plotable()[3],15, 10)
    f3=Range(f2.plotable()[2], f2.plotable()[3],17, 5)
    f4=Range(f3.plotable()[2], f3.plotable()[3],13, 30)
    plot = Plot(f)
    plot.multiple(f4)
    plot.multiple(f3)
    plot.multiple(f2)
    plot.show()


        
    

    
