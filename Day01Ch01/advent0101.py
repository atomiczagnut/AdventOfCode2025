# Advent of Code 2025 -- Day 1 -- Challenge 1

# Initialize global variables
pointer = 50
zero_times = 0

# Function to move the pointer
def turn_dial(instruction):
	value = 0
	direction = instruction[0]
	times = int(instruction[1:])
	
	if direction == "R":
		value = (value + times) % 100
	elif direction == "L":
		value = -((value + times) % 100)
	else:
		print("Error: Invalid direction")
		
	return value
	
# Read input file line by line
with open ("input.txt", "r") as f:
	for line in f:
		pointer = (pointer + (turn_dial(line.strip()))) % 100
		print(f"The dial is rotated {turn_dial(line.strip())} and ends pointing at {pointer}")	
		if (pointer == 0):
			zero_times = zero_times + 1
	
# The result
print(f"zero_times: {zero_times}")
