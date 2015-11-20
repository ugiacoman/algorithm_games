def Palindrome(number):
	number = str(number)
	number = number.lstrip("0")
	rev_number = number[::-1]
	le_sum = int(number) + int(rev_number)

	if (str(number) == str(rev_number)):
		print(number)
	elif ((str(le_sum) == str(le_sum)[::-1])):
		print(le_sum)
	elif (le_sum >= 1000000000):
		print(-1)
	else:
		Palindrome(le_sum)



def main():
	user_input = input("Please input a number: ")
	Palindrome(user_input)
	


if __name__ == '__main__':
     main()