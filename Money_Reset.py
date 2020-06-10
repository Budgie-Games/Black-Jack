import os
cwd = os.getcwd()

s = input("Are you sure you want to reset your money to $1000? y/n > ")
if s == "y":

    with open(cwd + "\\data\\bjdata.txt", "w")as file:
        file.truncate()
        file.seek(0)
        file.write("1000")

    print("Process Done!")

else:
    print("Process Denied!")