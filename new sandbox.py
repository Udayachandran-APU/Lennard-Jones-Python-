import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Optimized positions
optimized_positions = [
    [0.0, 0.0, 0.0],
    [1.12246205, 0.0, 0.0],
    [0.56123102, 0.97194844, 0.0]
]

# Convert to arrays for plotting
x, y, z = zip(*optimized_positions)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot particles
ax.scatter(x, y, z, c='r', s=100, label="Particles")

# Annotate points
for i, (xi, yi, zi) in enumerate(zip(x, y, z)):
    ax.text(xi, yi, zi, f'P{i}', color='blue', fontsize=10)

# Set plot limits
ax.set_xlim([-0.5, 1.5])
ax.set_ylim([-0.5, 1.5])
ax.set_zlim([-0.5, 1.5])

# Labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Visualization of Optimized Particle Positions')

# Show legend and plot
ax.legend()
plt.show()
