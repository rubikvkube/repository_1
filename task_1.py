from datetime import datetime
import os

path = str(input("Enter path to directory: "))
file_extension = str(input("Enter file extension (e.g. .txt): "))
list_of_files = []
for file in os.listdir(path):
    if file.endswith(file_extension):
        list_of_files.append(os.path.join(path, file))

latest_file = max(list_of_files, key=os.path.getctime)

for file in list_of_files:
	if os.path.getmtime(latest_file)-os.path.getmtime(file)<=10:
		print (file)
#my first comment
