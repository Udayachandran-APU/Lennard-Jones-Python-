import random, math, copy, csv, os
import matplotlib.pyplot as plt

box_size = 150 #volume
ep = 1 #minimum pottential in u-units (uday-units)
sig = 100 #distance in u-units where pottential is zero
offset_limit = 1 #step size

def spawn_particles(n):
    particles = []
    for i in range(n):
        particle = [random.randint(0, box_size), random.randint(0, box_size), random.randint(0, box_size)]
        particles.append(particle)
    return particles

def random_offset(particles):
    particles_copy = copy.deepcopy(particles)
    for particle in particles_copy:
        particle[0] = abs(particle[0] + random.randint(-offset_limit, offset_limit)) if particle[0] < box_size-offset_limit else abs(particle[0]-offset_limit)
        particle[1] = abs(particle[1] + random.randint(-offset_limit, offset_limit)) if particle[1] < box_size-offset_limit else abs(particle[1]-offset_limit)
        particle[2] = abs(particle[2] + random.randint(-offset_limit, offset_limit)) if particle[2] < box_size-offset_limit else abs(particle[2]-offset_limit)
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

def show(particles, save):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    save_path = "./images"
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    for particle in particles:
        ax.scatter(particle[0], particle[1],particle[2])
    if save is True: plt.savefig(os.path.join(save_path, "no_numpy.jpg")) 
    plt.show()

def write_to_csv(pott, pott_o, min_pott, file_name="./csv_files/no_numpy.csv"):
    if not os.path.exists:
        os.mkdir("./csv_files")
    data = [pott, pott_o, min_pott]
    with open(file_name, 'a', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(data)

def monte_carlo_minimize(n: int, max_iter = 20000, local = False, save_csv = False, show_plot = True):
    particles = spawn_particles(n)
    iteration = 0
    min_coords = []
    min_pott  = 0

    while iteration <= max_iter:
        potts = dist_pot(particles)
        pott = compute(potts)

        offset_particles = random_offset(particles)
        potts_o = dist_pot(offset_particles)
        pott_o = compute(potts_o)
        
        if local is False: #Send to GLOBAL minima
            del_E = pott_o-pott
            if del_E < 0 or random.random() < math.exp(-del_E/0.2): 
                #acceptance is e^{delG/T} note: delE = delG cause I can't do stuff with entropy and enthalpy
                particles = offset_particles
                print(f"lowered: {pott} -> {pott_o}")
        else: #Send to LOCAL minima
            if pott_o < pott: 
                particles = offset_particles
                print("lowered") 
        
        #Store the lowest pottential value with coordinates
        if min_pott > pott_o: 
            min_coords = offset_particles
            min_pott = pott_o
            print("yeah")

        if save_csv is True: write_to_csv(pott, pott_o, min_pott)   
        print(iteration)
        iteration+=1

    if show_plot is True:
        print(min_coords, min_pott)
        show(min_coords, save=True)    

if __name__ == "__main__":
    monte_carlo_minimize(6, save_csv=True, local=False)

