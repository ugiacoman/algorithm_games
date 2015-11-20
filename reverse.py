def reverse(a_list):
	low = 0
	high = len(a_list) - 1
	while low < high:
		a_list[low], a_list[high] = a_list[high], a_list[low]
		low += 1
		high -= 1

	return(a_list)
	


def main():
	print("")
	original_list = raw_input("Please input strings separated by spaces: ")
	a_list = original_list.split()
	print(a_list)
	reverse(a_list)
	print(a_list)
	print("")


main()