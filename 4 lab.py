import random
from tkinter import filedialog
file1 = open("file1.txt", "w+")
Listok1 = [random.randint(0, 100) for i in range(10)]
file1.write(' '.join(map(str, Listok1)))
file1.close()
file2 = open("file2.txt", "w+")
Listok2 = [random.randint(0, 100) for i in range(10)]
file2.write(' '.join(map(str, Listok2)))
file2.close()
my_file_path = filedialog.askopenfilename()
my_file = open(my_file_path, "r")
fileContent = my_file.read()
print(fileContent)
fileContentInt = list(map(int, fileContent.split()))
average = sum(fileContentInt) / len(fileContentInt)
print(average)
