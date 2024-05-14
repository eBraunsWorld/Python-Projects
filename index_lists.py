#Gather word to test from user.
word = input("Enter one-word to determine if it's a palindrome:\n")

#Function to take input word, reverse it, and determine its equality. 
#If true, print that the input word is a palidrome.
#If false, print that the input word is not a palindrome. 
def find_palindrome(string):
    #Reverse the input string.
    reverse = string[::-1]
    #If reverse is the same as input string, print that it is a palindrome.
    if reverse == string:
        print(string + " is a palindrome.")
    #If not, print that the input word IS NOT a palindrome. 
    else:
        print(string + " IS NOT a palindrome.")

#Runs the function.
find_palindrome(word)