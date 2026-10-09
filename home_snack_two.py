def largest_element_in_list(list):

	largest = list[0]
	
	for number in list:
		if number > largest:
			largest = number
	return largest
	
def smallest_element_in_list(list):

	smallest = list[0]
	
	for number in list:
		if number < smallest:
			smallest  = number
	return smallest
	
	
	
print(largest_element_in_list([2,4,6,8,10,12,14,16,18,20]))
print(smallest_element_in_list([2,4,6,8,10,12,14,16,18,20]))
	
	

