# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(list_str):
	count = 0
	for item in list_str:
		if isinstance(item, list):
			list_str[count] = capitalize_nested(item)
		else:
			list_str[count] = item.upper()
		count += 1
	return list_str

def main():
	list_str = ['apple', ['bear', 'python'], 'cat']
	print(capitalize_nested(list_str))

if __name__ == '__main__':
	main()
		
			