import matplotlib.pyplot as plt

def show(particles, save=False):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    for particle in particles:
        ax.scatter(particle[0], particle[1],particle[2])
    if save is True: plt.savefig("locaL_minima_particles.jpg") 
    plt.show()

coords7 = [[-0.9523699364,0.0159052548,-0.0840802250],
[-0.2528949024,0.8598484003,-0.3332183372],
[-0.3357005052,-0.8500181306,0.2812584200],
[0.7960710440,0.5155096551,-0.1218613860],
[0.7448954577,-0.5412454414,0.2579017563],
[-0.0442130155,0.1953980103,0.5377653956],
[0.0442118576,-0.1953977484,-0.5377656238]]
print(coords7)
show(coords7)
