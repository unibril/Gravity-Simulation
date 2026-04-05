import math 
import time
import os 

def draw_grid(A,B,grid_size,initial_position):
    os.system('cls')
    grid = [['.'] * grid_size for _ in range(grid_size)]
    grid[grid_size // 2][grid_size // 2] = A.symbol
    scale = grid_size / (initial_position * 2)
    grid_col = int(grid_size // 2 + B.x * scale)
    grid_row = int(grid_size // 2 - B.y * scale) 
    if 0 <= grid_row < grid_size and 0 <= grid_col < grid_size:
        grid[grid_row][grid_col] = B.symbol
    for row in grid:
        print(' '.join(row))
    
    

class Body:
    def __init__(self, x, y, vx, vy, mass, symbol):
        self.x      = x        
        self.y      = y
        self.vx     = vx       
        self.vy     = vy       
        self.mass   = mass
        self.symbol = symbol


masses = int(input("Enter mass of body B: "))
mass_a = int(input("Enter mass of body A: "))


initial_position = int(input("Enter initial position of body B (x coordinate): "))
velocity_angle = int(input("Enter angle of initial velocity of body B (in degrees, 0 = right, 90 = up): "))

initial_velocity_magnitude = int(input("Enter magnitude of initial velocity of body B: "))
initial_velocity_y_component = initial_velocity_magnitude * math.sin(math.radians(velocity_angle))
initial_velocity_x_component = initial_velocity_magnitude * math.cos(math.radians(velocity_angle))

g = float(input("Enter gravitational constant G (Use a high value like 10000 for a stronger gravity and a more dramatic simulation): "))

dt = float(input("Enter time step dt (Use a small value like 0.001 for smoother motion): "))

A = Body(x=0, y=0, vx=0, vy=0, mass=mass_a, symbol='A')
B = Body(x=initial_position, y=0, vx=initial_velocity_x_component, vy=initial_velocity_y_component, mass=masses, symbol='B')

print("Please press ctl+c to stop the simulation. The simulation will automatically stop on a collision or escape.")
while True:
    r = math.sqrt((B.x - A.x)**2 + (B.y - A.y)**2)
    if r < 5:  
        print("Collision detected! Simulation stopped.")
        break
    elif r > 1000:  
        print("Body B has escaped the gravitational pull of Body A. Simulation stopped.")
        break

    f = g * A.mass * B.mass / (r**2)
    fx = f * (A.x - B.x) / r
    fy = f * (A.y - B.y) / r

    
    #ACCELERATION aaba
    ax = fx / B.mass
    ay = fy / B.mass

    #VELOCITY UPDATE
    B.vx += ax * dt
    B.vy += ay * dt

    #POSITION UPDATE
    B.x += B.vx * dt
    B.y += B.vy * dt


    print((B.x, B.y), r, math.hypot(B.vx, B.vy))
    draw_grid(A, B, grid_size=40, initial_position=initial_position)
    time.sleep(dt)
    

