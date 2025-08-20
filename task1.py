name = input("enter name ")

notes = input("enter notes ")

with open("file.txt", "w") as f:
    f.write("name: " + name + "\n")
    f.write("notes: " + notes + "\n")

with open("file.txt", "r") as f:
    content = f.read()
    print(content)
