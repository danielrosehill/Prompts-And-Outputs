import os

 
year = input("Please enter the last two digits of the year: ")

 
os.makedirs(year, exist_ok=True)

 
for i in range(1, 13):
    subfolder_name = os.path.join(year, str(i))
    os.makedirs(subfolder_name, exist_ok=True)

print(f"Folder '{year}' with subfolders from 1 to 12 created successfully.")
