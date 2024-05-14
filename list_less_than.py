a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
values_less_than = int(input("Enter a whole number:\n"))

def less_than_values(list):
    for i in list:
        if i < values_less_than:
            new_list.append(i)
        else:
            continue

less_than_values(a)

print(new_list)