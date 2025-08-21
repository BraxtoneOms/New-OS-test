# file = open("new_file.pdf", "w")
# file.write("This is a new file created in write mode\n")

file = open("new_file.pdf", "r")
data = file.read()
print(data)

try:
    file = open("new_file.pdf", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found. Please check the file path.")
