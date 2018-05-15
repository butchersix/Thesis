# Random Selector python program for Thesis Data Gathering

'''
	References:
		1. https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
		2. https://unix.stackexchange.com/questions/238180/execute-shell-commands-in-python
		3. https://stackoverflow.com/questions/3397752/copy-multiple-files-in-python
		4. https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
		5. https://developers.google.com/edu/python/lists
		6. https://docs.python.org/3/library/random.html
		7. https://stackoverflow.com/questions/7118276/how-to-remove-specific-element-in-an-array-using-python
		8. https://stackoverflow.com/questions/1712227/how-to-get-the-number-of-elements-in-a-list-in-python
		9. https://stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists
		10. https://www.guru99.com/reading-and-writing-files-in-python.html#3
'''
# Packages here
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
import random
import shutil
import time

print("===== RANDOM SELECTOR PROGRAM || THESIS DATA GATHERING =====\n\n")
print("Note: For custom paths, edit path.txt\n\n")

'''
	Inputs needed:
		1. Path of Dataset
		2. Number of samples needed to be randomly selected

'''

# Initialization of variables
path = ""
i = 0 # index counter
x = 0
new_dataset = []
new_dataset_directory = "new_dataset"

# functions

def generate_number(size):
	return random.randint(1, size)

def delayPrint(string, seconds): # n seconds delay printing
	time.sleep(seconds)
	print(string)

# Main process
delayPrint("Checking file cache...", 1)
if isfile("path.txt"):
	delayPrint("Path file has been verified", 1)
	f = open("path.txt", "r")
	path = f.read();
	f.close()
else:
	path = input("Path of Dataset: ")
	f = open("path.txt", "w+")
	f.write(path)
	f.close()

samples = input("Number of samples: ")
delayPrint("List of chosen paintings:", 1)

paintings = [f for f in listdir(path) if isfile(join(path, f))]
SIZE_OF_DATASET = len(paintings)
while i < int(samples):
	x = generate_number(SIZE_OF_DATASET+1) - 1
	delayPrint(paintings[x], 0.2)
	new_dataset.append(paintings[x])
	paintings.remove(paintings[x])
	SIZE_OF_DATASET = len(paintings)
	i += 1
delayPrint("Paintings successfully chosen!", 1)

# Make a new directory for the new dataset
if not os.path.exists(new_dataset_directory):
	os.makedirs(new_dataset_directory)
	delayPrint("Directory created!", 1)
else:
	delayPrint("Directory exists!", 1)
	delayPrint("Deleting directory...", 1)
	shutil.rmtree(new_dataset_directory)
	delayPrint("Delete successful!", 1)
	delayPrint("Creating directory...", 1)
	os.makedirs(new_dataset_directory)
	delayPrint("Successfully created!", 1)

# copy the chosen files from source to destination
delayPrint("Copying the files...", 1)
chosen_files = os.listdir(path)
for file_name in chosen_files:
	full_file_name = os.path.join(path, file_name)
	if (os.path.isfile(full_file_name)):
		full_fn = full_file_name.split("/")[3]
		for i in new_dataset:
			if i == full_fn: # file name only, do not include path
				delayPrint("Copying " + full_fn, 0.2)
				shutil.copy(full_file_name, new_dataset_directory)
delayPrint("Copied successfully!", 1)

