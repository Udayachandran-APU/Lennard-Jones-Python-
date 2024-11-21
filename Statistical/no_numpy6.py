#To-do:
#1 make random velocity proportional to pottential
    #to make it bounce off really fast when they are too close together
#2 low-priority: Convert to numpy to make more effectient

import random, math, time, copy, csv
import matplotlib.pyplot as plt

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


def spawn_particles(n):
    particles = []
    for i in range(n):
        particle = [random.randint(0, box_size), random.randint(0, box_size)]#, random.randint(0, box_size)]
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
            distance = math.sqrt((particle2[0]-particle1[0])**2 + (particle2[1]-particle1[1])**2)#+ (particle2[2]-particle1[2])**2)
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

#3x3 tester
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

particles = spawn_particles(3)
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
'''
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

    ratio = pott_o/pott if pott != 0 else 2
    print(ratio)
    if ratio < random.random()*10:
        comparisn = True
    else:
        comparisn = False
'''
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
    
    if iteration >= 1000:
        break
    iteration+=1
show(particles, save=True)    