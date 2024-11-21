import random, math, time
#import numpy as np
import matplotlib.pyplot as plt
box_size = 1000

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
    offset_limit = 1
    for particle in particles:
        #print(particle, "before")
        particle[0] = abs(particle[0] + random.randint(-offset_limit, offset_limit)) if particle[0] < box_size-offset_limit else abs(particle[0]-offset_limit)
        particle[1] = abs(particle[1] + random.randint(-offset_limit, offset_limit)) if particle[1] < box_size-offset_limit else abs(particle[1]-offset_limit)
        #particle[2] = abs(particle[2] + random.randint(-offset_limit, offset_limit)) if particle[2] < box_size-offset_limit else abs(particle[2]-offset_limit)
        #print(particle, "after")
    return particles

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
    ep = 1
    sig = 1
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


og_particles = spawn_particles(3)
threshold = 0.46e-9
sum_potts = threshold +0.01
convergance = threshold + 0.01 
switch = 0
iteration = 0
convergance_l = []
#write switch case for og_particles = offset_particles
while True: #convergance > threshold: #sum_potts > threshold: 
    
    offset_particles = random_offset(og_particles)
    distances = distance(offset_particles)
    potts = pottential(distances)
    sum_potts_new = compute(potts) 
    convergance = abs(sum_potts-sum_potts_new)
    print(convergance, "convergance")
    #print(f"sum plots new {sum_potts_new} \nsum plots {sum_potts}")
    if sum_potts_new < sum_potts:
        sum_potts = sum_potts_new
        offset_particles = og_particles
    convergance_l.append(convergance)
    iteration +=1
    if iteration >= 10:
        break
    show(offset_particles)
plt.plot(convergance_l)
plt.show()
print(sum_potts)
show(offset_particles)
    
