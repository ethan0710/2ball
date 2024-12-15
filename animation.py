import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from tqdm import tqdm
from initialize import k, m, y, vx, vy, outdir, save_dir

if not os.path.isdir(save_dir):
        os.mkdir(save_dir)

title = f"k = {k}, m = [{m[0]}, {m[1]}], vx = [{vx[0]}, {vx[1]}], vy = [{vy[0]}, {vy[1]}]"

# Load the data
data1 = np.loadtxt(f"{save_dir}/{outdir}/ball_001.txt", skiprows=1)
data2 = np.loadtxt(f"{save_dir}/{outdir}/ball_002.txt", skiprows=1)

time = data1[:,0]

# Plot section
fig, ax = plt.subplots(figsize=(9, 9))  
ball1_plot,  = ax.plot([], [], label="ball 1", color="blue", marker='o')  # Ball 1
ball2_plot,  = ax.plot([], [], label="ball 2", color="red", marker='o')   # Ball 2
string_plot, = ax.plot([], [], label="string", color="black")             # String
ax.set_xlabel("x (m)")
ax.set_xlim(0, max(y) + 10)
# ax.set_xlim(-100, 100)    
ax.set_ylabel("y (m)")
ax.set_ylim(0, max(y) + 10)
ax.legend()

# Initialize animation
def init():
    ball1_plot.set_data([], [])
    ball2_plot.set_data([], [])
    string_plot.set_data([], [])
    return ball1_plot, ball2_plot, string_plot

# Update the animation
def update_frame(frame):
    x1, y1 = data1[frame, 2], data1[frame, 3]
    x2, y2 = data2[frame, 2], data2[frame, 3]
    ball1_plot.set_data([x1], [y1])
    ball2_plot.set_data([x2], [y2])
    string_plot.set_data([[x1,x2]], [[y1,y2]])

    # Update the time
    ax.set_title(f"{title}, time = {time[frame]:2f}") 
    return ball1_plot, ball2_plot, string_plot

frames = len(data1)
ani = animation.FuncAnimation(fig, update_frame, frames=tqdm(range(frames)), init_func=init, blit=True)

ani.save(f"{save_dir}/{outdir}.mp4", fps=30, writer="ffmpeg", dpi=300, extra_args=['-vcodec', 'libx264'])