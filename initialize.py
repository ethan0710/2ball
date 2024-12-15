# The initial condition about the parameters

k = 1000    # Elastic constant (kg/s^2)

m = [1, 1] # ball1, ball2 mass (kg)

x = [0.0, 0.0]   # ball1, ball2 x-position (m)
y = [200.0, 203.0] # ball1, ball2 y-position (m)

vx = [30.0, 30.0] # ball1, ball2 velocity x (m/s) (recommend 30 m/s)
vy = [0.0, 0.0]
step      = 0                    # the number of step         
dt        = 0.0001                 # The change of time between each step
time      = 0.0                  # The time at current step
tmax      = 20.0                 # End of the simulation time
noutput   = 500                  # number of snapshots
ninterval = int(tmax/dt/noutput) # interval between file outputs

outdir = f"traj_k{k}_m{m[0]}-{m[1]}_vx{vx[0]}-{vx[1]}_vy{vy[0]}-{vy[1]}" # output directory name

save_dir = "clockwise" # The directory name for saving figure and animation

process_visual = True  # Process visualization.py when call main.py
process_anime  = True  # Process animation.py when call main.py


