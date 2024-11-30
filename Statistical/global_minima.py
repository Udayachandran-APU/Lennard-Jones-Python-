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
offset_limit = 1 #temp

def show(particles, save):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    for particle in particles:
        ax.scatter(particle[0], particle[1],particle[2])
    if save is True: plt.savefig("global_minima_particles.jpg") 
    plt.show()


def spawn_particles(n):
    particles = []
    for i in range(n):
        particle = [random.randint(0, box_size), random.randint(0, box_size), random.randint(0, box_size)]
        particles.append(particle)
    return particles

def random_offset(particles):
    particles_copy = copy.deepcopy(particles)
    for particle in particles_copy:
        #print(particle, "before")
        particle[0] = abs(particle[0] + random.randint(-offset_limit, offset_limit)) if particle[0] < box_size-offset_limit else abs(particle[0]-offset_limit)
        particle[1] = abs(particle[1] + random.randint(-offset_limit, offset_limit)) if particle[1] < box_size-offset_limit else abs(particle[1]-offset_limit)
        particle[2] = abs(particle[2] + random.randint(-offset_limit, offset_limit)) if particle[2] < box_size-offset_limit else abs(particle[2]-offset_limit)
        #print(particle, "after")
    return particles_copy

def dist_pot(particles):
    pot_table = []
    for particle1 in particles:
        temp_table = []
        for particle2 in particles:
            r = math.sqrt((particle2[0]-particle1[0])**2 + (particle2[1]-particle1[1])**2+ (particle2[2]-particle1[2])**2)
            pottential = 0 if r == 0 else 4*ep*(((sig/r)**12) - ((sig/r)**6))
            temp_table.append(pottential)
        pot_table.append(temp_table)
    return pot_table

def compute(potts):
    sum = 0
    for i in potts:
        for j in i:
            sum+=j
    return sum/2


particles = spawn_particles(5)
iteration = 0
min_coords = []
min_pott  = 0

while True:
    potts = dist_pot(particles)
    pott = compute(potts)

    offset_particles = random_offset(particles)
    potts_o = dist_pot(offset_particles)
    pott_o = compute(potts_o)
    
    #Send to GLOBAL minima 
    ratio = pott_o/pott if pott != 0 else 0.5 #Try using less simple algorithm cause jumps too often
    ratio_simple = pott_o < pott
    accept = np.random.random() > 0.02
    if ratio_simple or accept: 
        particles = offset_particles
    
    #Store the lowest pottential value with coordinates
    if min_pott > pott_o: 
       min_coords = offset_particles
       min_pott = pott_o
       print("yeah")

    #Write data to CSV
    data = [pott, pott_o, min_pott]
    file_name = "global_minima.csv"
    if iteration == 0:
        with open(file_name, 'w', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(data)
    else:
        with open(file_name, 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(data)
    
    if iteration >= 20000:
        break

    print(iteration)
    iteration+=1

print(min_coords, min_pott)
show(min_coords, save=True)    
