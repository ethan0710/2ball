import numpy as np
from scipy.constants import g

def rk4(yin, t, h, func):
    
    # implement the RK4 method
    k1 = func(yin, t)

    y2 = yin + 0.5 * h * k1
    k2 = func(y2, t + 0.5*h)

    y3 = yin + 0.5 * h * k2
    k3 = func(y3, t + 0.5*h)

    y4 = yin + h * k3
    k4 = func(y4, t + h)
    
    # Compute ynext
    ynext = yin + h/6*(k1 + 2*k2 + 2*k3 + k4)
    return ynext

def initialize(m, x, y, vx, vy):
    m1, m2 = m
    # Compute x, y of the two balls (m)
    x1  = x[0]
    y1  = y[0]
    x2  = x[1]
    y2  = y[1]
    xc  = (m1*x1 + m2*x2) / (m1 + m2)
    yc  = (m1*y1 + m2*y2) / (m1 + m2)
    sep1 = np.sqrt((x1 - xc)**2 + (y1 - yc)**2)
    sep2 = np.sqrt((x2 - xc)**2 + (y2 - yc)**2)
    sep = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    # Compute vx, vy of the two balls (m/s)
    vx1 = vx[0]
    vy1 = vy[0]

    vx2 = vx[1]
    vy2 = vy[1]
    v1  = np.sqrt(vx1**2 + vy2**2)
    v2  = np.sqrt(vx2**2 + vy2**2)
    vxc = (m1*vx1 + m2*vx2) / (m1 + m2)
    vyc = (m1*vy1 + m2*vy2) / (m1 + m2)
    vc  = np.sqrt(vxc**2 + vyc**2)
    
    ax1 = 0
    ax2 = 0
    ay1 = -g
    ay2 = -g

    # Initialize two Star objects
    ball1 = Ball(1, m1, x1, y1, vx1, vy1, ax1, ay1)
    ball2 = Ball(2, m2, x2, y2, vx2, vy2, ax2, ay2)

    # print(f"force = {f}")

    return ball1, ball2, sep1, sep2, sep
   
def update(time, dt, ball1, ball2, sep, k):
    ball1_in = [ball1.x, ball1.y, ball1.vx, ball1.vy, ball1.ax, ball1.ay]
    ball2_in = [ball2.x, ball2.y, ball2.vx, ball2.vy, ball2.ax, ball2.ay]
    
    # Update x, y, vx, vy of the two stars using the RK4 method
    ball1_update = rk4(ball1_in, time, dt, func)
    ball1.x, ball1.y, ball1.vx, ball1.vy, ball1.ax, ball1.ay = ball1_update
    new_v1 = np.sqrt(ball1.vx**2 + ball1.vy**2)
    ball2_update = rk4(ball2_in, time, dt, func)
    ball2.x, ball2.y, ball2.vx, ball2.vy, ball2.ax, ball2.ay = ball2_update

    # Compute the new force between ball1 and ball2 (mv^2/r)
    new_r = np.sqrt((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2)
    xdir = (ball1.x - ball2.x) / new_r
    ydir = (ball1.y - ball2.y) / new_r
    # f = ball1.mass * abs(new_v1**2 - new_vc**2) / new_sep
    # print(abs(new_v1**2 - new_vc**2))
    f = k * (new_r - sep)
    fx1 = f * (-xdir)
    fy1 = f * (-ydir) - ball1.mass * g
    fx2 = f * (xdir)
    fy2 = f * (ydir) - ball2.mass * g

    # Update ax and ay of the two stars
    # fx, fy = m*ax, m*ay
    ball1.ax = fx1/ball1.mass
    ball1.ay = fy1/ball1.mass 
    ball2.ax = fx2/ball2.mass
    ball2.ay = fy2/ball2.mass


def func(ball_in, time):
    N = np.size(ball_in)
    k = np.zeros(N)
    
    # The differential value of balls
    k[0] = ball_in[2]  # dx/dt  = vx
    k[1] = ball_in[3]  # dy/dt  = vy
    k[2] = ball_in[4]  # dvx/dt = ax
    k[3] = ball_in[5]  # dvy/dt = ay
    k[4] = 0           # No update here
    k[5] = 0           # No update here
    
    return k

class Ball:

    # Define properties in a Ball class
    id: int
    mass: float
    x: float
    y: float
    vx: float
    vy: float
    ax: float
    ay: float
    
    # Function used for initializing the Btar class
    def __init__(self, id: int, mass: float, x: float, y: float, 
                 vx: float, vy: float, ax: float, ay: float) -> None:
        self.id = id
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay

def ball_center(ball1:Ball, ball2:Ball):
    # Calculate the parameter about the center of mass between ball 1 and ball 2
    mc  = ball1.mass + ball2.mass
    xc  = center(ball1.x, ball2.x, ball1.mass, ball2.mass)
    yc  = center(ball1.y, ball2.y, ball1.mass, ball2.mass)
    vxc = center(ball1.vx, ball2.vx, ball1.mass, ball2.mass)
    vyc = center(ball1.vy, ball2.vy, ball1.mass, ball2.mass)
    axc = center(ball1.ax, ball2.ax, ball1.mass, ball2.mass)
    ayc = center(ball1.ay, ball2.ay, ball1.mass, ball2.mass)

    ballc = Ball(3, mc, xc, yc, vxc, vyc, axc, ayc)
    return ballc

def center(x1, x2, m1, m2):
    xc = (x1*m1 + x2*m2) / (m1 + m2)
    return xc

def analytical(m, x, y, vx, vy, t):
    mc  = m[0] + m[1]
    xc  = center(x[0], x[1], m[0], m[1])
    yc  = center(y[0], y[1], m[0], m[1])
    vxc = center(vx[0], vx[1], m[0], m[1])
    vyc = center(vy[0], vy[1], m[0], m[1])
    xa = xc + vxc * t
    ya = yc + vyc * t - 0.5 * g * t**2
    
    return mc, xa, ya
    

if __name__ == "__main__":
    m1 = 1
    m2 = 1
    vx1 = 1
    vx2 = -1
    print(center(vx1,vx2,m1,m2))

