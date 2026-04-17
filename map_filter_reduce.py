'''

Beginner Level
------------------------
1. Lambda Basics  
o Write a lambda function to add two numbers.

add=lambda a,b : a+b
print(add(5,10))

o Write a lambda function to check if a number is even or odd.

check_even=lambda num : 'Even' if num%2==0 else 'odd'
print(check_even(12))

2. Using map()  
o Given a list of integers, use map() to create a new list with each number squared.

li = [1, 2, 3, 4, 5, 6]
squared_list = list(map(lambda val :  val**2, li))
print(squared_list)

o Convert a list of strings to uppercase using map().

li = ['ab', 'bc', 'cd', 'ef']
upper_list= list(map(lambda val : val.upper(), li))
print(upper_list)

3. Using filter()  
o Given a list of numbers, filter out only even numbers.

num=[1,2,3,4,5,6,7]
evens=list(filter(lambda x: x%2==0, num))
print(evens)

o Filter words that have length greater than 5 from a list of strings.

string = ['aman', 'rajeev', 'rohit', 'rajesh', 'mahesh']
str_len = list(filter(lambda x: len(x) > 5, string))
print(str_len)

4. Using reduce()  
o Find the sum of all elements in a list using reduce().

from functools import reduce
numbers=[10,20,30,40,50]
total = reduce(lambda x,y: x+y, numbers)
print(total)

o Find the product of all numbers in a list.

from functools import reduce
numbers=[10,20,30,40]
product = reduce(lambda x,y: x*y, numbers)
print(product)

Intermediate Level
------------------------------
5. Combination of lambda + map  
o Given a list of numbers, return a list where each number is multiplied by 10.

li = [1, 2, 3, 4, 5, 6]
new_list = list(map(lambda val :  val*10, li))
print(new_list)

6. Combination of lambda + filter  
o From a list of numbers, filter out all numbers divisible by 3.

li = [12, 2, 3, 9, 5, 6, 21,10, 15]
new_list = list(filter(lambda x :  x%3==0, li))
print('numbers divisible by 3: ', new_list)

7. Using reduce() for maximum  
o Find the maximum number in a list using reduce().

from functools import reduce
num=[10,20,30,40,50,60]
maximum = reduce(lambda a,b  : a if a> b else b, num)
print(maximum)

8. String Manipulation  
o Given a list of names, use map() to return names with their first letter capitalized.

string = ['aman', 'rajeev', 'rohit', 'rajesh', 'mahesh']
capital_text = list (map (lambda x:  x.capitalize(), string))
print(capital_text)

9. Filter Palindromes  
o Given a list of strings, filter out only palindrome words using filter().

strings = ["madam", "apple", "racecar", "banana", "level", "python", "aman"]
palindromes = list(filter(lambda w: w == w[::-1], strings))
print(palindromes)

'''














