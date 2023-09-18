file_path = "/Users/divijdoshi/Desktop/COMP219_Git_sample/sample_data1.txt"

with open(file_path, 'r') as file:
	for line in file:
		print(line.strip())
