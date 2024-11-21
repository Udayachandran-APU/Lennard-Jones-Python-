import csv
import numpy as np

# Optimized potential and compute functions
def compute_potentials(particles, ep=1.0, sig=1.0):
    particles = np.array(particles)  # Ensure particles is a numpy array
    diffs = particles[:, np.newaxis, :] - particles[np.newaxis, :, :]
    distances = np.sqrt(np.sum(diffs ** 2, axis=-1))
    
    np.fill_diagonal(distances, np.inf)  # Prevent division by zero
    
    inv_distances = 1.0 / distances
    inv_distances6 = inv_distances ** 6
    potentials = 4 * ep * (sig ** 12 * inv_distances6 ** 2 - sig ** 6 * inv_distances6)
    
    total_potential_energy = np.sum(np.triu(potentials))
    return total_potential_energy, potentials

# Parameters
size = 200
distances = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Write results to a CSV file
with open("bacon3part.csv", "w", newline="\n") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["d_01", "d_02", "d_12", "Potential"])  # Header row

    for i in range(50, size):
        distances[0][1] = distances[1][0] = i
        for j in range(50, size):
            distances[0][2] = distances[2][0] = j
            for k in range(50, size):
                distances[1][2] = distances[2][1] = k

                # Convert distances into a 3D particle configuration
                particles = [
                    [0, 0, 0],  # Particle 0
                    [distances[0][1], 0, 0],  # Particle 1
                    [0, distances[0][2], distances[1][2]]  # Particle 2
                ]

                # Calculate potential
                total_potential, _ = compute_potentials(particles, ep=1.0, sig=1.0)

                # Write results
                writer.writerow([distances[0][1], distances[0][2], distances[1][2], total_potential])
