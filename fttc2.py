import accessible_output2.outputs.auto
import sys
out = accessible_output2.outputs.auto.Auto()
out.output("Welcome to File Transfer Time Calculator. This tool allows you to estimate how long it will take for data to transfer from one location to another based on data size and transfer speed.")
def calculate_file_transfer_time():
	out=accessible_output2.outputs.auto.Auto()
	out.output("Please type the size of the file you're trying to transfer in megabytes")
	file_size = float(input("Please type the size of the file you're trying to transfer in megabytes"))
	out.output("Please type your data    transfer speed in megabits")
	transfer_speed = float(input("Please type your data transfer speed in megabits"))
	speed_in_megabytes = transfer_speed / 8
	transfer_time = round(file_size / speed_in_megabytes,2)
	if transfer_time > 86399.99:
		out.output("your file will take"+ str(round(transfer_time / 86400,2)) +"days to transfer")
	elif transfer_time > 3599.99:
		out.output("Your file will take"+ str(round(transfer_time / 3600,2)) +"hours to transfer")
	elif transfer_time > 59.99:
		out.output("Your file will take"+ str(round(transfer_time / 60,2)) +"minutes to transfer")
	else:
		out.output("Your file will take"+ str(transfer_time) +"seconds to transfer")
	try_again = input("Would you like to try another file?\n")
	if try_again == "y":
		calculate_file_transfer_time()
	elif try_again == "n":
		out.output("Thanks for using this tool. For more of my software, please visit https://houseoffireseed.ml/programs")
		sys.exit("Thanks for using this tool. For more of my software, please visit https://houseoffireseed.ml/programs")
calculate_file_transfer_time()