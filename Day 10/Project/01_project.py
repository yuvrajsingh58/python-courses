file = open("student.txt","w")

name = input("Enter your name: ")

file.write(name)

file.close()

print("Data saved successfully!")