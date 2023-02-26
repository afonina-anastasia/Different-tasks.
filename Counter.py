from collections import Counter

first_list = []
work_list = []
second_list = []
work_list_1 = []
with open("rooms.txt", "r") as f:
    for line in f:
        for i in line.split():
            if i.isdigit():
                work_list.append(int(i))
    first_list.append(int(work_list[0]))
    # print(first_list)

    for i in work_list[1:]:
        second_list.append(int(i))
    else:
        work_list_1.append(i)

r = Counter(second_list)
for i in second_list:
    if r[i] == 1:
        print(f"Captain's room number is {i}")
        break
else:
    print("Not found")
