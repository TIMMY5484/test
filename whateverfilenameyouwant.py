active = "true"
fileExists = "false"
print("Welcome to py terminal")
print("Commands")
print("file, make a file")
print("In file, add text to file")
print("Recall, print file")
while active == "true":
    enter=input("")
    if enter == ("file"):
        filename = input("What is the filename")
        print(filename, "Has been stored")
    elif enter == ("in file"):
        fileExists = "true"
        add=input("What do you want to add to the file")
    elif enter == ("recall"):
        if fileExists == "true":
            print(add)
    else:
        print("The file you are looking for doesn't exist")
