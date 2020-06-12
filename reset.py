import os
cwd = os.getcwd()

s = input("Are you sure you want to reset your progress? y/n > ")
if s == "y":
    with open(cwd + "\\data\\bjdata.txt", "w")as file:
        file.truncate()
        file.seek(0)
        file.write("1000")
    with open(cwd + "\\data\\eqski.txt", "w")as file:
        file.truncate()
        file.seek(0)
        file.write("11")
    with open(cwd + "\\data\\skidata.txt", "w")as file:
        file.truncate()
        file.seek(0)
        file.write("1000")
    with open(cwd + "\\data\\skidata_.txt", "w")as file:
        file.truncate()
        file.seek(0)
        file.write("1000")

    print("Process Done!")

else:
    print("Process Denied!")