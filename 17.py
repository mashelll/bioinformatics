weights = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def calc_varinats(total_mass):

	number_list = [0] * (total_mass + 1)
	number_list[total_mass] = 1
	
	counter = total_mass
	while (counter > 0):

		for weight in weights:
			number_list[counter - weight] += number_list[counter]

		counter -= 1

		while (number_list[counter] == 0):
			counter -= 1

	return(number_list[0]) 

def main():

	with open('/home/masha/Загрузки/rosalind_ba4d.txt', 'r') as f:
		total_mass = int(f.readline())
	output = calc_varinats(total_mass)

	with open('/home/masha/Загрузки/output.txt', 'w') as f: 
    		f.write(str(output))


if __name__ == "__main__":
	main()

