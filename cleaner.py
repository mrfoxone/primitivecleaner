import os
destination = input("Enter the folder path:")

os.chdir(destination)
# print(os.getcwd())

if os.listdir(destination) == []:
    print("Folder is Empty")
else:
    for temp in os.listdir():
        # print("Folder is cleaning.....")
        os.remove(temp)
        if os.listdir(destination) == []:
            print("Folder is cleaned")