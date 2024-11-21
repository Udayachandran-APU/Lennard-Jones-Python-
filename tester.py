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