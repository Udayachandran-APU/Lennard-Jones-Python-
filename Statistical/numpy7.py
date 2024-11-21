#To-do:
#1 make random velocity proportional to pottential
    #to make it bounce off really fast when they are too close together
#2 low-priority: Convert to numpy to make more effectient

import random, math, time, copy, csv
import matplotlib.pyplot as plt
import numpy as np

box_size = 150 #volume
ep = 1 #minimum pottential in u-units (uday-units)
sig = 100 #distance in u-units where pottential is zero
offset_limit = 2 #temp

def show(particles, save):
    fig = plt.figure()
    ax = fig.add_subplot()#projection="3d")
    for particle in particles:
        ax.scatter(particle[0], particle[1])#,particle[2])
    if save is True: plt.savefig("particles.jpg") 
    plt.show()

def spawn_particles_np(n, box_size=box_size):
    return np.random.randint(0, box_size, size=(n,n))

def random_offset_np(particles, box_size=box_size, offset_limit=offset_limit):
    # Generate random offsets for all particles
    offsets = np.random.randint(-offset_limit, offset_limit + 1, size=particles.shape)
    # Add offsets to particles
    updated_particles = particles + offsets
    # Check which particles are clipped
    clipped_mask = (updated_particles < 0) | (updated_particles >= box_size)
    print(clipped_mask)
    # Adjust clipped particles: Set all coordinates of clipped particles to -offset_limit
    updated_particles = np.clip(updated_particles, 0, box_size - 1)
    clipped_particles = np.any(clipped_mask, axis=1)  # Identify rows that have at least one clip
    updated_particles[clipped_particles] = particles[clipped_particles] - offset_limit

import numpy as np

def compute_potentials(particles, ep=ep, sig=sig):
    particles = np.array(particles)  # Ensure particles is a numpy array
        # Compute pairwise distances
    diffs = particles[:, np.newaxis, :] - particles[np.newaxis, :, :]
    distances = np.sqrt(np.sum(diffs ** 2, axis=-1))


    # Avoid division by zero by masking diagonal (distance from a particle to itself)
    np.fill_diagonal(distances, np.inf)

    # Compute the Lennard-Jones potential
    inv_distances = 1.0 / distances
    inv_distances6 = inv_distances ** 6
    potentials = 4 * ep * (sig ** 12 * inv_distances6 ** 2 - sig ** 6 * inv_distances6)

    # Compute the total potential energy (only sum the upper triangle to avoid double counting)
    total_potential_energy = np.sum(np.triu(potentials))  # Divide by 2 only for upper triangle sum

    return total_potential_energy, potentials


#3x3 tester
'''
size = 200
distances = [
    [0,0,0],
    [0,0,0], 
    [0,0,0]]
with open("bacon3part.csv", "w", newline="\n") as csvfile:
    for i in range(50, size):
        distances[0][1] = distances[1][0] = i
        for j in range(50, size):
            distances[0][2] = distances[2][0] = j
            for k in range(50, size):
                distances[1][2] = distances[2][1] = k
                potts = pottential(distances)
                pott = compute(potts)
                writer = csv.writer(csvfile)
                writer.writerow([distances[0][1], distances[0][2], distances[1][2], pott])
'''
#4x4 tester
'''
distances = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

# Open the CSV file for writing
with open("bacon4x4.csv", "w", newline="\n") as csvfile:
    writer = csv.writer(csvfile)  # Initialize CSV writer
    
    for i in range(2000):  # Loop over range
        # Populate the distances matrix symmetrically
        distances[0][1] = distances[1][0] = i
        distances[0][2] = distances[2][0] = i
        distances[0][3] = distances[3][0] = i
        distances[1][2] = distances[2][1] = i
        distances[1][3] = distances[3][1] = i
        distances[2][3] = distances[3][2] = i

        # Compute the potential and other required values
        potts = pottential(distances)
        pott = compute(potts)

        # Write the distances and computed potential to the CSV
        writer.writerow([distances[0][1], distances[0][2], distances[0][3], 
                         distances[1][2], distances[1][3], distances[2][3], pott])
'''

particles = spawn_particles()
iteration = 0
info = []

while True:
    distance_ = distance(particles)
    potts = pottential(distance_)
    pott = compute(potts)
#debug point
    offset_particles = random_offset(particles)
    distance_o = distance(offset_particles)
    potts_o = pottential(distance_o)
    pott_o = compute(potts_o)
    
'''
    #Send to LOCAL minima

    negative_pott = pott<0
    negative_pott_o = pott_o<0
    if negative_pott and negative_pott_o: 
        comparisn = pott > pott_o
    elif not negative_pott and not negative_pott_o:
        comparisn = pott > pott_o
    else:
        comparisn = abs(pott) > abs(pott_o)
'''
    
    #Send to GLOBAL minima
'''
    ratio = pott_o/pott if pott != 0 else 2
    print(ratio)
    if ratio < random.random()*10:
        comparisn = True
    else:
        comparisn = False

    if comparisn: #Without using ratio and shit so doesn't account for local minima
        particles = offset_particles
        print("yeah ")
    else:
        print("no ")
    
    #Write data to CSV
    data = [distance_[0][1], distance_o[0][1], pott, pott_o]
    file_name = "eggs2.csv"
    if iteration == 0:
        with open(file_name, 'w', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(data)
    else:
        with open(file_name, 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(data)
    
    if iteration >= 10000:
        break
    iteration+=1
    '''
#show(particles, save=True)    
