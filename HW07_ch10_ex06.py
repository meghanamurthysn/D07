# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(lst):
	return lst == sorted(lst)

def main():
	print(is_sorted([3, 2, 1]))
	print(is_sorted([1, 2, 2]))

if __name__ == '__main__'	:
	main()