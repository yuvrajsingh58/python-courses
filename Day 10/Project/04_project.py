with open("notes.txt","a") as file:
    note = input("Write a note: ")
    file.write(note + "\n")

print("Note saved!")

with open("notes.txt","r") as file:
    print("\nAll Notes:")
    print(file.read())