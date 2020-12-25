f = open("text3.txt", "w")
# \n в конце строки
f.writelines([
    "this is my text\n",
    "this is another text\n"
])

f.write("this is line 3\n")
f.write("this is line 4\n")