import random, math, time, copy
#import numpy as np
import matplotlib.pyplot as plt

box_size = 2500 #volume
ep = 1
sig = 11 #u-distance units
offset_limit = 4 #temp

def show(particles):
    fig = plt.figure()
    ax = fig.add_subplot()#projection="3d")
    for particle in particles:
        ax.scatter(particle[0], particle[1]) #,particle[2])
    plt.show()

def spawn_particles(n):
    
    particles = []
    for i in range(n):
        particle = [random.randint(0, box_size), random.randint(0, box_size)] #, random.randint(0, box_size)]
        particles.append(particle)
    return particles

def random_offset(particles):
    particles_copy = copy.deepcopy(particles)
    for particle in particles_copy:
        #print(particle, "before")
        particle[0] = abs(particle[0] + random.randint(-offset_limit, offset_limit)) if particle[0] < box_size-offset_limit else abs(particle[0]-offset_limit)
        particle[1] = abs(particle[1] + random.randint(-offset_limit, offset_limit)) if particle[1] < box_size-offset_limit else abs(particle[1]-offset_limit)
        #particle[2] = abs(particle[2] + random.randint(-offset_limit, offset_limit)) if particle[2] < box_size-offset_limit else abs(particle[2]-offset_limit)
        #print(particle, "after")
    return particles_copy

def distance(particles):
    distance_table = []
    for particle1 in particles:
        temp_table = []
        for particle2 in particles:
            distance = math.sqrt((particle2[0]-particle1[0])**2 + (particle2[1]-particle1[1])**2) #+ (particle2[2]-particle1[2])**2)
            temp_table.append(distance)
        distance_table.append(temp_table)
    return distance_table

def pottential(distances):
    pot_table = []
    for distance_x in distances:
        temp_table = []
        for distance in distance_x:
            r = distance
            pottential = 0 if distance == 0 else 4*ep*(((sig/r)**12) - ((sig/r)**6))
            temp_table.append(pottential)
        pot_table.append(temp_table)
    return pot_table    

def compute(potts):
    sum = 0
    for i in potts:
        for j in i:
            sum+=j
    return sum/2


particles = spawn_particles(2)
iteration = 0
info = []
#write switch case for particles = offset_particles
while True:
    distance_ = distance(particles)
    potts = pottential(distance_)
    pott = compute(potts)
#debug point
    offset_particles = random_offset(particles)
    distance_o = distance(offset_particles)
    potts_o = pottential(offset_particles)
    pott_o = compute(potts_o)

    print(float(pott), float(pott_o))
    if float(pott) < float(pott_o): #Without using ratio and shit so doesn't account for local minima
        particles = offset_particles
        #print(f'del distance: {distance_o[0][1]-distance_[0][1]}, del pot: {pott_o-pott}')
        print(f"{distance_[0][1]} {distance_o[0][1]} {pott} {pott_o}")
        print("yeah bitch")
        time.sleep(2)
    else:
        print("no bitch")
        print(f"{distance_[0][1]} {distance_o[0][1]} {pott} {pott_o}")
        
print(convergance_l)

