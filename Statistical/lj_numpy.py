import numpy as np
import copy, csv
import matplotlib.pyplot as plt

box_size = 350 #volume
ep = 1 #minimum pottential in u-units (uday-units)
sig = 100 #distance in u-units where pottential is zero
offset_limit = 5 #step size

def spawn_particles(n):
    particles = np.random.uniform(0,box_size, size=(n,3)) 
    particles = particles.astype(np.float64)
    return particles

def random_offset(particles, iteration, total_iterations): #The mask part hasn't been accounted for
    particles_copy = copy.deepcopy(particles)
    shape = particles.shape
    offset_amt = max(0.5, offset_limit * np.exp(- iteration / (0.2* total_iterations)))
    offset_particles =  particles_copy + np.random.uniform(-offset_amt, offset_amt, size=shape)
    offset_particles = offset_particles.clip(0, box_size) # no bounce back as hard to code
    return offset_particles

def dist_pot(particles):
    #We are taking a 2d array, taking only the first row and making a nxn array where the rows are repeating. By doing this we can perform operations with it such as finding distance and pottential and shit
    difference = particles[:, np.newaxis] - particles #broadcasted array 
    difference_squared = difference**2
    distances = np.sqrt(np.sum(difference ** 2, axis=-1))
    np.fill_diagonal(distances, np.inf)
    if np.min(distances) < 1e-2:
        print("Particles are too close!")
        input("press any key")

    pots = 4* ep * ((sig/distances)**12 - (sig/distances)**6)
    np.fill_diagonal(distances, 0)
    pot = np.sum(np.triu(pots))
    return pots, pot

def show(particles, save):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.scatter(particles[:,0], particles[:,1],particles[:, 2])
    ax.plot3D(particles[:,0], particles[:,1],particles[:, 2])
    if save is True: plt.savefig("np_sandbox.jpg") 
    plt.show()

particles = spawn_particles(11)
iteration = 0
total_iterations = 50000
T = 2
Cooling_rate = 0.995
min_coords = []
min_pot  = np.inf
energies = np.array([])

while True:
    pots, pot = dist_pot(particles)

    offset_particles = random_offset(particles, iteration, total_iterations)
    pots_o, pot_o = dist_pot(offset_particles)
    '''
    #Send to LOCAL minima
    if pot_o < pot: 
        particles = offset_particles
        print("lowered") 
    '''
    #Send to GLOBAL minima 
    del_E = pot_o - pot
    if del_E < 0 or np.random.random() < np.exp(-del_E / T):  # Accept lower or probabilistically higher
        particles = offset_particles  # Accept new configuration
    
    #Store the lowest pottential value with coordinates
    if min_pot > pot_o: 
       print(f"Updating min_pot: {min_pot} -> {pot_o}")
       min_coords = np.copy(offset_particles)
       min_pot = pot_o
    
    energies = np.append(energies, pot_o)
    '''
    #Write data to CSV
    data = [pot, pot_o, min_pot]
    file_name = "np_sandbox.csv"
    if iteration == 0:
        with open(file_name, 'w', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(data)
    else:
        with open(file_name, 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(data)
    '''
    
    if iteration >= total_iterations:
        break
    
    
    print(iteration)
    T*=Cooling_rate
    iteration+=1


print(min_coords, min_pot)
show(min_coords, save=False)    
plt.plot(energies)
plt.ylim(min_pot, min_pot + 0.2)
plt.show()