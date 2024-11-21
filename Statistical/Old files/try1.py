# This is first attempt at simulating lenoard jones pottential
#Use pygame/matplotlib to visualize (2D)


#Spawn n particles with random (x, y) coordinate within boundary
	#make coordinate system
	#LJ function
#Give random velocity
#Calculate LJ pottential by calcualting distance with (x, y) per t time
#keep calculating until pottential reaches minimum
#Graph LJ to show global mimina
#Show the configuration for different n number of particles

#make random velocity proportional to lenoard pottential V
stable = False
particles_radius = [
	[0,2,3,4],
	[2,0,3,4],
	[3,2,0,4]
]
particles_pot = [
	[0,2,3,4],
	[2,0,3,4],
	[3,2,0,4]
]
list[m][n] = list[n][m]
list[m][m] = 0

particles = [
	[x1, y1, v1],
	[x2, y2, v2]
]

def random_offset(particles):
	for coords in particles:
		x = coords[0] += coords
		y = coords[1]
		x += random offset
		y += random offset 

def compute(particles)
	for coords in particles:
		r = distance(particles)
		v = pottential(particles)
		update v
	
	sum of all v
	compare old sum and new sum
	if old sum > new sum:
		old sum = new sum
		set new x y for all

	if old sum <= threshold
		stable = True
