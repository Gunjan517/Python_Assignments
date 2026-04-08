'''
Python While Loop Exercise
************************************
Part 1 – Basic Level
--------------------------------
1. Print numbers from 1 to 10 using a while loop.
a = 1
while a<=10:
    print(a)
    a = a+1

2. Print even numbers from 1 to 20.
a=1
while a<=20:
    if a%2==0:
        print(a)
    a = a+1

3. Print odd numbers from 1 to 20.
a=1
while a<=20:
    if a%2!=0:
        print(a)
    a = a+1

4. Print numbers from 10 to 1 (reverse order).
a = 10
while a >= 1:          
    print(a)
    a = a - 1         

5. Print multiplication table of 5 using while loop.
a = 1
while a <= 10:          
    print(5*a)
    a = a +1   

Part 2 – Intermediate Level
---------------------------------------
6. Find the sum of first 10 natural numbers using while loop.

num = 0
a = 1
while a <= 10:
    num = num + a   
    a = a + 1
print("Sum =", num) 
    
7. Find factorial of a number entered by user.

num = int(input("Enter a number: "))
fact = 1
while num>1:
    fact=fact*num
    num = num-1
print("Factorial :",fact)

8. Count number of digits in a given number.
num = int(input("Enter a no."))
count = 0
while num > 0:
    num = num // 10   
    count = count + 1 
print("Number of digits:", count)

9. Reverse a number using while loop.
num=int(input("Enter a no."))
add = 0
while num>0:
    rem = num%10
    add = add*10 +rem
    num = num//10
print("Reverse number:",add)

10. Check whether a number is palindrome or not using while loop.
num = int(input("Enter a number: "))
originalnum = num
reversed = 0

while num > 0:
    rem = num % 10          
    reversed = reversed * 10 + rem 
    num = num // 10           

if originalnum == reversed:
    print("Palindrome number")
else:
    print("Not a palindrome number")

Part 3 – Pattern Based
--------------------------------
11. Print pattern: 
* 
** 
*** 
**** 
*****

a=1
while a<6:
    print("*" *a)
    a=a+1

    
12. Print pattern: 
1 
12 
123 
1234 
12345

i = 1
while i <= 5:          
    j = 1
    while j <= i:      
        print(j, end="")   
        j = j + 1
    print()            
    i = i + 1

Part 4 – Logical / Real Scenario
--------------------------------------------

13. Ask user to enter password until correct password is entered.

correct_password = "admin1234"

while True:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access Granted")
        break
    else:
        print("Wrong password")

14. Create a number guessing game:
• Generate a random number (1–10) 
• Keep asking user until they guess correctly

import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number (1-10): "))
    
    if guess == number:
        print("Correct! You guessed it .")
        break
    else:
        print("Wrong guess, try again")

15. Keep taking input numbers until user enters 0, then print total sum.
add = 0
while True:
    num = int(input("Enter A Number(0 for Exit) : "))
    add = add + num
    if num==0:
        break
print("Total :",add)

Bonus Challenge (Interview Level)
---------------------------------------------------

16. Print Fibonacci series up to N terms using while loop.
a = 0
b = 1
terms =int(input("enter a no."))
i = 1
while i<=terms:
    c = a+b
    print(c)
    a = b
    b = c
    i+=1

17. Check whether a number is Armstrong number.
num = 153
copy = num
add = 0
while num>0:
    rem = num%10
    add = add+rem**3
    num = num//10
print("New Number : ",add)
if copy==add:
    print("Armstrong")
else:
    print("Not Armstrong")
    
18. Print prime numbers between 1 to 50 using while loop.

print("Prime numbers between 1 and 50 are:")

n = 2
while n <= 50:
    count = 0
    i = 1
    
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    
    if count == 2:   
        print(n, end=" ")
    
    n += 1
'''









