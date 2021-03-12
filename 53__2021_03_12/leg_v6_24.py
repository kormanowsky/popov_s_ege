file = open("24.txt", "r")

cur_1 = file.read(1)
cur_2 = file.read(1)
diff_1 = diff_2 = same = ""
count = 0
max_count = 0

while cur_2 != "":

    if diff_1 != "" and diff_2 != "":
        if cur_1 == cur_2 and cur_2 == same:
            count += 1
        else:
            if same == "":
                if cur_2 != diff_1 and cur_2 != diff_2:
                    same = cur_2
                    count = 1
            elif cur_1 != cur_2 and diff_1 != same \
                    and diff_2 != same and cur_1 != same and cur_2 != same:

                if count > max_count:
                    print("now max sequence is",
                          diff_1 + diff_2 + same * count + cur_1 + cur_2)
                    max_count = count
                count = 0
                same = ""
                diff_1 = cur_1
                diff_2 = cur_2
    elif cur_1 != cur_2:
        diff_1, diff_2 = cur_1, cur_2

    cur_1 = cur_2
    cur_2 = file.read(1)
file.close()
print(max_count)
