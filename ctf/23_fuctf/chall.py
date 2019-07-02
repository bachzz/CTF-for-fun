import os 
def menu():
	print("*************************")
	print("******** FIND ME ********")
	print("*************************")
	print("")
	print("1. List Dir")
	print("2. Read File")
	print("3. Exit")

def main():
	menu()

	print("Enter choice: ")
	try:
		choice=int(input())
		if (choice ==1):
			print("Enter path: ")
			path=input()
			print(os.listdir(path))
		elif (choice==2):
			print("Enter path: ")
			path=input()
			with open(path, 'r') as f:
				print(f.read())
		else:
			print("Invalid choice")
			exit(0)
	except ValueError:
		print("Invalid choice")
		exit(0)
	except FileNotFoundError:
		print("File is not exist")
		exit(0)
	except NotADirectoryError:
		print("This is a file")
		exit(0)
	exit(0)
if __name__== "__main__":
	main()

