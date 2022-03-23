""" 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
"""

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda num: (num % 2 == 0), original_list))
odd_list = list(filter(lambda num: (num % 2 == 1), original_list))

print(even_list)
print(odd_list)

""" 2)
find which days of the week have exactly 6 characters.
"""

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
sixdays_list = list(filter(lambda num: (len(num) == 6), weekdays))

print(sixdays_list)

""" 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

"""
Original_list2 = ["orange", "red", "green", "blue", "white", "black"]
Bad_Colors = ["orange", "black"]

colors_list = list(filter(lambda num: (num not in Bad_Colors), Original_list2))

print(colors_list)


""" 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 """
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

new_list = list(filter(lambda num: (num not in list2), list1))
print(new_list)

""" 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

"""
Original_list3 = ["red", "black", "white", "green", "orange"]
word_list = list(filter(lambda num: ("ack" in num), Original_list3))
word_list2 = list(filter(lambda num: ("abc" in num), Original_list3))

print(word_list)
print(word_list2)


""" 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
"""
Pass1 = "password"
Pass2 = "PASSWORD1"
Pass3 = "Password"
Pass4 = "pass1"
Pass5 = "Password1"

Password_key = lambda x: (any(islower(), isupper(), isdigit(), len(x) >= 8)), Pass2
print(Password_key)


""" 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
