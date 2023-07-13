from scipy import *                   
from math import *
import numpy
import datetime                                                     
import time                           
import random
import matplotlib.pyplot as plt                    

Begin_Time = 0.0
End_Time = 0.0
    
#THe path where to save the file of the random walk is set
#PATH="D:\\"

#To measure the execution time
Begin_Time = time.time()

#Beginning time
print(datetime.datetime.now())

#Number of steps of the random walk
#It is not recomended to set N > 10^7 as the code will be too slow, instead go to my FORTRAN repo.
N = 1000000

#Since the equation is dimensionless there is no need of declaring values for the physcal constants of the equation (there is none).
#Again since the equation is dimensionless the magnitude of dt does not have to be provided although I include it so
#the user can experiment changing the magnitude and notice no change at all in the behaviour of the walks. 
dt = 1.0

V_t = random.gauss(0,1)
Steps_Array = [V_t]
Nmbr_Given_Steps=0

out_file=open("Random_Walk.txt","w")

for i in range(N): 
    
    #The random step is performed
    V_t_plus_dt = (V_t*dt) + sqrt(dt)*random.gauss(0,1)
    V_t = V_t_plus_dt

    #The random step is stored to the propper array if manipulation is desired
    Steps_Array.append(V_t)

    #The random step is stored to a file for visualization
    #Multiplying by 1000 is to shorten the amount of decimal numbers to be considered
    V_Print = int(V_t*1000)
    
    #If resolution of the date needs to be preserved comment line 47 and uncomment the following
    #V_Print = V_t

    out_file.write(str(V_Print)+"\n")

    #Counting the number of given steps by the walk
    Nmbr_Given_Steps+=1
    

#
out_file.close()

print("Given steps ",Nmbr_Given_Steps)

#Ending time
print(datetime.datetime.now())

#To quickly visualize the random walk, not recomended if N (N > 10^7)is to big.
#plt.plot(Steps_Array, color='red')
#plt.show()

#To measure execution time
End_Time = time.time()
Ex_Time = End_Time - Begin_Time
print(Ex_Time)


