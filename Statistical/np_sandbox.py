import numpy as np
import copy
def spawn_particles(n):
    particles = np.random.randint(0,10, size=(3,3)) 
    particles = particles.astype(np.double)
    return particles

def random_offset(particles): #The mask part hasn't been accounted for
    offset_limit = 1
    particles_copy = copy.deepcopy(particles)
    shape = particles.shape
    offset_arr = np.random.randint(-offset_limit, offset_limit, size=shape)
    return particles + offset_arr

def random_offset_gpt(particles, box_size=box_size, offset_limit=offset_limit):
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

def dist_pot(particles):
    '''
    We are taking a 2d array, taking only the first row and making a nxn array where the rows are repeating. By doing this we can perform operations with it such as finding distance and pottential and shit
    '''
    barr = particles[:, np.newaxis] - particles #barr = broadcasted array 
    barr = barr**2
#    barr = np.sqrt(np.sum(barr[np.newaxis, :])) # IDK IF THIS WORKS CHECK
    print(barr) 
    print(barr[np.newaxis, :])

def compute_potentials_gpt(particles, ep=1, sig=1):
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

particles = spawn_particles(4)
offset_particles = random_offset_gpt(particles)
print(offset_particles) 
dist_pot(offset_particles)
