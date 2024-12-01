import csv, os
import numpy as np
import matplotlib.pyplot as plt


box_size = 450 #volume  <- You might have to reduce to like 250 for smaller number of particles so they converge faster
ep = 1 #minimum pottential in u-units (uday-units)
sig = 100 #distance in u-units where pottential is zero
offset_limit = 5 #step size

def spawn_particles(n):
    particles = np.random.uniform(0,box_size, size=(n,3)) #I'm using uniform here cause it supposidly spawns then unfiromly 
    particles = particles.astype(np.float64)
    return particles


def random_offset(particles, iteration, total_iterations):
    particles_copy = np.copy(particles)
    shape = particles.shape
    offset_amt = max(0.5, offset_limit * np.exp(- iteration / (0.2* total_iterations)))
    offset_particles =  particles_copy + np.random.uniform(-offset_amt, offset_amt, size=shape)
    offset_particles = offset_particles.clip(0, box_size) 
    return offset_particles


def dist_pot(particles):
    #We are taking a 2d array, taking only the first row and making a nxn array where the rows are repeating. By doing this we can perform operations with it such as finding distance and pottential and shit
    difference = particles[:, np.newaxis] - particles #broadcasted array 
    distances = np.sqrt(np.sum(difference ** 2, axis=-1)) #credits: https://stackoverflow.com/a/78032444
    np.fill_diagonal(distances, np.inf)
    pots = 4* ep * ((sig/distances)**12 - (sig/distances)**6)
    np.fill_diagonal(distances, 0)
    pot = np.sum(pots)/2
    return pots, pot


def show(particles, pot_min, save):
    file_name = "./images/lj_numpy.jpg"
    if not os.path.exists("./images"):
        os.mkdir("./images")

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.set_title(f"Mininima: {pot_min}")
    ax.scatter(particles[:,0], particles[:,1],particles[:, 2])
    if save is True: plt.savefig(file_name) 
    plt.show()


def write_to_csv(pot, pot_o, min_pot):
    data = [pot, pot_o, min_pot]
    file_name = "./csv_files/lj_numpy.csv"
    if not os.path.exists("./csv_files"):
        os.mkdir("./csv_files")
    with open(file_name, 'a', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(data)


if __name__ == "__main__":
    particles = spawn_particles(20) # <- change number of particles here
    total_iterations = 70000 # <- change total iterations here
    T = 2
    min_temp = 0.005
    Cooling_rate = 0.9995
    
    min_pot  = np.inf
    iteration = 0
    min_coords = []
    energies = np.array([])
    accepts = np.array([])
    while iteration <= total_iterations:
        pots, pot = dist_pot(particles)
        offset_particles = random_offset(particles, iteration, total_iterations)
        pots_o, pot_o = dist_pot(offset_particles)

        #Send to GLOBAL minima 
        del_E = pot_o - pot
        if del_E < 0 or np.random.random() < np.exp(-del_E / T):  # It's accepting too many wrong accepts during later stages doesn't work well
            particles = offset_particles     

        #Store the lowest pottential value with coordinates
        if min_pot > pot_o: 
            print(f"Updating min_pot: {min_pot} -> {pot_o}")
            min_coords = np.copy(offset_particles)
            min_pot = pot_o
        energies = np.append(energies, pot_o)
        
        print(iteration)
        T*=Cooling_rate #Annealling stuff
        T = max(T, min_temp) #Making minimum temps so the annealing code doesn't cool it to very small number
        iteration+=1
    
    show(min_coords, min_pot, save=True) # <- Remove if you have issues with matplotlib and directories
    print(min_pot)
    plt.plot(energies)
    plt.ylim(min_pot, min_pot + 0.2)
    plt.show()
