
# Import the necessary libraries
import os, argparse
from utilities.preprocessor import read_csv_file
from utilities.parser import variables_parcing

# Define the main function
def main():
	
	# Call the function that parses the different variables
	args = variables_parcing()

	# Specify the path to the CSV file relative to the script's directory
	file_path = os.path.join(os.path.dirname(__file__), args.data_dir, args.dataset)

	# call the function read_csv_file that is defined in a different file named preprocessing.py
	dataset = read_csv_file(file_path)
	print(dataset.head())

# Call the main function
if __name__ == '__main__':
	main()

