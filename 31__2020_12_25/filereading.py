from random import randint


with open("test.txt", "w") as output_file:
    output_file.write(str(randint(10 ** 800, 10 ** 1000)))

with open("test.txt", "r") as input_file:
    while True:
        read = input_file.read(1)
        if not read:
            break
        print(read)
print('end')
