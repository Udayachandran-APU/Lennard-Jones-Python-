
import random, copy, math
import numpy as np
'''
def random_offset(particles):
    offset_limit = 10
    for particle in particles:
        print(particle, "before")
        particle[0] += random.randint(-offset_limit, offset_limit)
        particle[1] += random.randint(-offset_limit, offset_limit)
        particle[2] += random.randint(-offset_limit, offset_limit)
        print(particle, "after")
    return particles

particles = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
offset_limit = 5
random_offset(particles)
'''

import numpy as np
offset_limit = 10
box_size = 1000
def spawn_particles_np(n, box_size=box_size):
    return np.random.randint(0, box_size, size=(n,n))

import numpy as np
ep = 1
sig = 1
def pottential(particles, dimensions="3d", ep=ep, sig=sig, ): #calculates distance and pottential
    pott_table = []
    for particle1 in particles:
        temp_array = []
        for particle2 in particles:
            if dimensions.lower() == "3d":
                r = math.sqrt((particle2[0]-particle1[0])**2 + (particle2[1]-particle1[1])**2)#+ (particle2[2]-particle1[2])**2)
            else:
                r = math.sqrt((particle2[0]-particle1[0])**2 + (particle2[1]-particle1[1])**2+ (particle2[2]-particle1[2])**2)
            pottential = 0 if r == 0 else 4*ep*(((sig/r)**12) - ((sig/r)**6))
            temp_array.append(pottential)
        pott_table.append(temp_array)
    return pott_table

def pottential_np(particles, dimensions="3d", ep=ep, sig=sig): #calculates distance and pottential
    pott_array = np.array(size=particles.shape)
    for particle1 in particles:
        temp_array = np.array()
        for particle2 in particles:
            if dimensions.lower() == "3d":
                r = math.sqrt((particle2[0]-particle1[0])**2 + (particle2[1]-particle1[1])**2)#+ (particle2[2]-particle1[2])**2)
            else:
                r = math.sqrt((particle2[0]-particle1[0])**2 + (particle2[1]-particle1[1])**2+ (particle2[2]-particle1[2])**2)
            pottential = 0 if r == 0 else 4*ep*(((sig/r)**12) - ((sig/r)**6))
        np.append(pott_array, pottential)



sig = 100
def f(r):
    ep = 1
    return 4*ep*(((sig/r)**12) - ((sig/r)**6))

r_min = 2**(1/6)*sig
#print(f(10e10-0.00001))
print(f(r_min))
print(r_min)

print(-2.8599907823613805e-11 > -5.189129449997532e-10)

x = spawn_particles_np(5, 100)
y = random_offset_np(x)
print(x)
print(y)


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Optimized positions
optimized_positions = [
    [0.0, 0.0, 0.0],
    [1.12246205, 0.0, 0.0],
    [0.56123102, 0.97194844, 0.0]
]

# Convert to arrays for plotting
x, y, z = zip(*optimized_positions)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot particles
ax.scatter(x, y, z, c='r', s=100, label="Particles")

# Annotate points
for i, (xi, yi, zi) in enumerate(zip(x, y, z)):
    ax.text(xi, yi, zi, f'P{i}', color='blue', fontsize=10)

# Set plot limits
ax.set_xlim([-0.5, 1.5])
ax.set_ylim([-0.5, 1.5])
ax.set_zlim([-0.5, 1.5])

# Labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Visualization of Optimized Particle Positions')

# Show legend and plot
ax.legend()
plt.show()
