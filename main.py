import numpy as np
import os
from scipy.constants import g
from time import time as t
from physics import initialize, update, ball_center, analytical
from initialize import k, m, x, y, vx, vy, step, dt, time, tmax, noutput, ninterval, outdir, save_dir, process_visual, process_anime

start = t() # Start to calculate the costing time
print(f"g = {g}")

ball1, ball2, sep1, sep2, sep = initialize(m, x, y, vx, vy)

# open a directory which contains two files for the output data
if not os.path.isdir(f"{save_dir}"):
        os.mkdir(f"{save_dir}")

if not os.path.isdir(f"{save_dir}/{outdir}"):
        os.mkdir(f"{save_dir}/{outdir}")

f1 = open(f'{save_dir}/{outdir}/ball_001.txt','w')
f2 = open(f'{save_dir}/{outdir}/ball_002.txt','w')
f3 = open(f'{save_dir}/{outdir}/ball_cen.txt','w')
f4 = open(f'{save_dir}/{outdir}/ball_ana.txt','w')
# with open(f'{outdir}/ball_001.txt','w') as f1:
#     with open(f'{outdir}/ball_002.txt','w') as f2:
f1.write('# time mass x y vx vy ax ay \n')
f2.write('# time mass x y vx vy ax ay \n')
f3.write('# time mass x y vx vy ax ay err \n')
f4.write('# time mass x y \n')

while time <= tmax:

    update(time, dt, ball1, ball2, sep, k)               # Update the parameters about ball 1 and ball 2
    ballc = ball_center(ball1, ball2)                    # Calculate the parameters of center mass
    mc, xa, ya = analytical(m, x, y, vx, vy, time)       # Calculate the analytical solution of cneter mass
    err = np.sqrt((ballc.x - xa)**2 + (ballc.y - ya)**2) # Calculate the error about the center mass

    time += dt

    if step % ninterval == 0:
        f1.write(f"{time:e} {ball1.mass:e} {ball1.x:e} {ball1.y:e} \
                {ball1.vx:e} {ball1.vy:e} {ball1.ax:e} {ball1.ay:e}\n")   
        f2.write(f"{time:e} {ball2.mass:e} {ball2.x:e} {ball2.y:e} \
                {ball2.vx:e} {ball2.vy:e} {ball2.ax:e} {ball2.ay:e}\n")
        f3.write(f"{time:e} {ballc.mass:e} {ballc.x:e} {ballc.y:e} \
                {ballc.vx:e} {ballc.vy:e} {ballc.ax:e} {ballc.ay:e} {err:e}\n")
        f4.write(f"{time:e} {mc:e} {xa:e} {ya:e}\n")   
        
    step += 1
    if ball1.y <= 0 or ball2.y <= 0:
        break

f1.close()
f2.close()
f3.close()
f4.close()
end = t() # End of calculating costing time

print(f"Done, costing time = {(end - start):e}")

if process_visual == True:
    os.system("python visualization.py")
    print("Sucess visualization!")

if process_anime == True:
    # Warning: when process animation.py, also process visualization.py as well
    os.system("python animation.py")
    print("Sucess animation!")