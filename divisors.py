
divisor_num = int(input("Enter a number to find divisors\n"))
divisor_list = []

#Intake user's number, establish range to test, and add to list of divisors.
def find_divisors(num):
    #Establish range
    num_list = range(1,divisor_num)
    #Test num_list against divisor_num.
    for i in num_list:
        #If i in num_list is a divisor of divisor_num, add it to the divisor_list.
        if num % i == 0:
            divisor_list.append(i)
        else:
            continue

#Run function with user input as divisor_num
find_divisors(divisor_num)

#Print the list of divisors.
print(divisor_list)