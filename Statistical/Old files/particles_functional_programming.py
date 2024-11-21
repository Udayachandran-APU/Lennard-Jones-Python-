import random, math, time
import numpy as np

def spawn_particles(n):
    box_size = 1
    particles = []
    for i in range(n):
        particles.append([random.randint(0, box_size), random.randint(0, box_size), random.randint(0, box_size)])
    return particles

def random_offset(particles):
    offset_limit = 1
    for particle in particles:
        particle[0] += random.randint(-offset_limit, offset_limit)
        particle[1] += random.randint(-offset_limit, offset_limit)
        particle[2] += random.randint(-offset_limit, offset_limit)
    return particles

def distance(particles):
    distance_table = []
    for particle1 in particles:
        temp_table = []
        for particle2 in particles:
            distance = math.sqrt((particle2[0]-particle1[0])**2 + (particle2[1]-particle1[1])**2 + (particle2[2]-particle1[2])**2)
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
            pottential = 0 if distance == 0 else 4*ep*(((sig/r)**12) - ((sig/r)**6))#.as_integer_ratio() #This won't work cause of see later
            temp_table.append(pottential)
        pot_table.append(temp_table)
    return pot_table

def compute(potts):
    sum = 0
    potts_np = np.asarray(potts)
    print(potts_np)
    sum = np.trace(potts_np)
    return sum


particles = spawn_particles(2)
threshold = 0.01e-10
sum_potts = threshold + 100 
while True:#not sum_potts <= threshold:
    random_offset(particles)
    distances = distance(particles)
    print(distances)
    potts = pottential(distances)
    print(potts)
    sum_potts = compute(potts) #late => becuase in order to add the numbers in this shit, we need numbers to add
    print(sum_potts)
    time.sleep(0.2)



particles_r = [[]]
particles_v = [[]]


'''
def spawn_particles(n):
    particles = []
    for i in range(n):
        [particles] += [random.randint(box_size), random.randint(box_size), random.randint(box_size)]
    return particles

def random_offset(particles):
    for index, particle in enumerate:
        return(index, particle)
'''
