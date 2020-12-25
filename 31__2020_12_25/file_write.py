# Если файла нет, то он будет создан
f = open("text.txt", "w")
# Содержимое перезаписывается
f.write("this is my text")
f.write("this is another text")