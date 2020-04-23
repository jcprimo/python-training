from hanoi import hanoi_solver
# THIS SHIT DOESNT BELONG TO ME, IT IS A PURE COPY AND PASTE FOR EDUCATION PURPOSES!
# ORIGINAL DOOD: https://github.com/Chuxclub/Pylearn/blob/master/hanoi/hanoi_ascii.py
#


# This is the fukcing animation
				#size=2 max_size =4
def create_ring(size, max_size):
	res_ring = []
	# What the fuck are we doing here?
	middle = max_size #4
	first_bracket = max_size - size #2
	last_bracket = max_size + size #6

	# When the size is 0 then loop thru the range
	# of 2*max +1m and append to the ring
	if size == 0:
		for i in range(2 * max_size + 1): #PEMDAS
			res_ring.append(" ")

	else:
		for i in range(2 * max_size + 1):
			if i == first_bracket:
				res_ring.append("<")

			# If we are in the middle of the disc
			# then write the number to indicate the level
			elif i == middle and size > 1:
				res_ring.append(str(size))
			elif first_bracket < i < last_bracket:
				res_ring.append("-")
			elif i == last_bracket:
				res_ring.append(">")
			else:
				res_ring.append(" ")
	return res_ring


# All towers must have the same size for this function to work
# which means that if there's no ring, then 0 has been chosen
def print_floor(max_size):
	res_floor = []

	# Why 3 and 2?
	for i in range((2*max_size+1) * 3 + 2):
		if i == max_size:
			res_floor.append("A")

		elif i ==(2*max_size+1)+1+max_size:
			res_floor.append("B")

		elif i == (2*max_size+1)*2+2+max_size:
			res_floor.append("C")
		
		else:
			res_floor.append("=")
	return res_floor


def print_towers(towers):
	total_towers = len(towers)
	max_ring = len(towers[0])
	res_ring_line = []

	for j in range(0, max_ring):
		for i in range(0, total_towers):
			res_ring_line.extend(create_ring(towers[i][j], max_ring))
			res_ring_line.append(" ")
		print("".join(res_ring_line))
		res_ring_line = []
	print("".join(print_floor(max_ring)))
