import numpy as np
import matplotlib.pyplot as plt
import os
from initialize import k, m, y, vx, vy, outdir, save_dir

if not os.path.isdir(save_dir):
        os.mkdir(save_dir)

# Load the position value from the data files about the two stars
x1 = np.loadtxt(f"{save_dir}/{outdir}/ball_001.txt", usecols=2, skiprows=1)
y1 = np.loadtxt(f"{save_dir}/{outdir}/ball_001.txt", usecols=3, skiprows=1)

x2 = np.loadtxt(f"{save_dir}/{outdir}/ball_002.txt", usecols=2, skiprows=1)
y2 = np.loadtxt(f"{save_dir}/{outdir}/ball_002.txt", usecols=3, skiprows=1)

xc = np.loadtxt(f"{save_dir}/{outdir}/ball_cen.txt", usecols=2, skiprows=1)
yc = np.loadtxt(f"{save_dir}/{outdir}/ball_cen.txt", usecols=3, skiprows=1)

xa = np.loadtxt(f"{save_dir}/{outdir}/ball_ana.txt", usecols=2, skiprows=1)
ya = np.loadtxt(f"{save_dir}/{outdir}/ball_ana.txt", usecols=3, skiprows=1)

err = np.loadtxt(f"{save_dir}/{outdir}/ball_cen.txt", usecols=8, skiprows=1)
err = err[-1]

# Plot section
axis_size  = 12
title_size = 14


title = f"k = {k}, m = [{m[0]}, {m[1]}], vx = [{vx[0]}, {vx[1]}], vy = [{vy[0]}, {vy[1]}]"
plt.figure(figsize=(9, 9))
plt.plot(x1, y1, label="ball1", color="blue", linewidth=3)
plt.plot(x2, y2, label="ball2", color="red", linewidth=3)
plt.plot(xc, yc, label="center mass", color="green", linestyle="--",linewidth=3)
plt.plot(xa, ya, label="analytical solution", color="black", linestyle=":", linewidth=3)
plt.xlabel("x (m)", fontsize=axis_size)
plt.xlim(-10, max(y))
# plt.xlim(-100, 100)
plt.ylabel("y (m)", fontsize=axis_size)
plt.ylim(0, max(y)+10)
plt.title(f"{title}, error = {err:.3e}", fontsize=title_size)
plt.legend(loc="upper right", fontsize=axis_size)
plt.savefig(f"{save_dir}/{outdir}.png", bbox_inches="tight", dpi=300)

