file = open("file.txt", "r")

content = file.read()
print(content)
file.close()

file = open("file.txt", "a")
file.write("\nHello World")
file.close()