# 2ball
Numerical simulations about the trajectory of two balls which connected by a spring.<br><br><br>

## The Description about each files
main.py  --> Processing the numerical simulation program.  
initialize.py  --> Input the initial condition and some setting.  
animation.py  --> Create the .mp4 file for watching.  
visualization.py   --> Create the .png file for looking the trajectory of the two balls.  
physics.py  --> The functions which using in the program.

## Setup (in initialize.py, all parameters are SI units.)
k is the elastic constant\
dt is the change of the time between each steps\
(Warning: please check k*dt < 1)

m is an arrray which input [m1, m2], the left elments is the mass of ball 1, and right is the ball 2.\
x and y are also array which the forms are like m, x represents x-direction position and y represents y-direction position.\
vx and vy are also array which the forms are likem, vx represents x-direction velocity and y represents y-direction velocity.

noutput is how many number of snapshots will be print out (if end time is at tmax)

save_dir is the directory that save the data, figures and animation. If you don't change the name, all data will save there.

process_visual is the Boolean value. If true, after processing main.py will process visualization.py.\
process_anime is the Boolean value. If true, after processing main.py will process animation.py

## How to process 2ball
If you want to process 2ball directory after you setting up the parameters in initialization.py

1. cd into 2ball directory (cd 2ball)
2. type "python main.py"
3. waiting for programing
4. Done!

