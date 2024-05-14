#Generate 2 random lists of unique numbers
import random
a = random.sample(range(1,10000),5000)
b = random.sample(range(1,10000),8000)

#Function to generate empty list and append common numbers that are in both provided lists.
def common_nums(list_a, list_b):
    #Generate empty list
    same_num_list = []
    #Find numbers that are in list_a and list_b.
    for num in list_a:
        #If numbers are in both lists, append it to the same_num_list.
        if num in list_b:
            same_num_list.append(num)
    #Return results in ascending order.
    return sorted(same_num_list)

same_num_list = common_nums(a,b)

print(same_num_list)
