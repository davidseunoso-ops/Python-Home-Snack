def sequential_list_from_1_to_15():
	sequential_list = []
	for numbers in range(1,16):
		sequential_list.append(numbers)
	return sequential_list
	
	
def add_third_element(list):
	sum_of_numbers = 0
	for numbers in list[2: :3]:
		sum_of_numbers = sum_of_numbers + numbers 
	return sum_of_numbers	
		
print(add_third_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print (sequential_list_from_1_to_15())

