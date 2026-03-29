'''
PART 1 – Basic For Loop Questions 
Q1. Print Numbers 
Use a for loop to print numbers from 1 to 10.

for i in range(1,11):
    print(i)
    
Q2. Print Even Numbers 
Print all even numbers between 1 and 20.

for i in range(1,21):
    if i%2==0:
        print(i)
        
Q3. Find Sum 
Print the sum of numbers from 1 to 10 using a for loop.
sum = 0
for i in range(1, 11):
    sum += i
print("The sum is:", sum)

Q4. Multiplication Table 
Take a number from the user and print its multiplication table up to 10.
n=int(input("Enter a number:"))
for i in range(1,11):
    print(i*n)

Q5. Count Characters 
Take a string and count the total number of characters using a for loop.

st = "HELLOWORLD"
count = 0
for i in st:
    count +=1
print("Total Characters :",count)

PART 2 – Break Related Questions

Q6. Stop at 5 
Print numbers from 1 to 10. 
Stop the loop when the number becomes 5.
for i in range(1,11):
    if i ==5:
        break
    print(i)

Q7. Search in List 
Search for number 25 in a list. 
If found, print "Found" and stop the loop.
list = [10, 20, 25, 30, 35, 40]
for i in list:
    if i == 25:
        print(i,"Found")
        break

Q8. First Negative Number 
Given a list of numbers, print the first negative number and stop the loop.
list = [10, 20, 25, -30, -35, -40]
for i in list:
    if i<0:
        print("first negative no. is:", i)
        break

PART 3 – Continue Related Questions

Q9. Skip 5 
Print numbers from 1 to 10. 
Skip number 5.

for i in range(1,11):
    if i ==5:
        continue
    print(i)
    
Q10. Skip Even Numbers 
Print numbers from 1 to 20. 
Skip all even numbers.

for i in range(1,21):
    if i%2==0:
        continue
    print(i)

Q11. Skip Letter 
Print each character of the string "PYTHON". 
Skip the letter "O".

str = "PYTHON"
for i in str:
    if i=="O":
        continue
    print(i)

Q12. Empty Loop 
Run a loop from 1 to 5 but do nothing inside the loop using pass.

for i in range(1,6):
    pass
    
Q13. Skip Using Pass 
Loop from 1 to 10. 
If number is 6, just use pass.

for i in range(1,11):
    if i ==6:
        pass
    else:
        print(i)
 
PART 5 – For-Else Questions 
(Remember: else runs only if the loop is not stopped by break.) 
 
Q14. Search Number Using for-else 
Search for number 100 in a list. 
If found, print "Found". 
If not found, print "Not Found".

list = [50,40,100,200,300]
for i in list:
    if i ==100:
        print("Found")
        break
else:
    print("Not found")
 
Q15. Prime Number Check 
Take a number from the user and check whether it is prime using for-else.

count=0
n=int(input("enter a no: "))
for i in range(1,n+1):
    if n % i==0:
        count= count+1
if count ==2:
    print("Prime no. ")
else:
    print("not a prime no.")


Q16. Star Pattern 
Print: 
* 
** 
*** 
**** 
***** 
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end = "")
    print()
 
Q17. Reverse Star Pattern 
Print: 
***** 
**** 
*** 
** 
* 
for i in range(5,0,-1):
    for j in range(1, i + 1):
        print("*", end = "")
    print()
    
Q18. Number Pattern 
Print: 
1 
12 
123 
1234 
12345

for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end = "")
    print() 
 
Q19. Same Number Pattern 
Print: 
1 
22 
333 
4444 
55555

for i in range(1,6):
    for j in range(1, i + 1):
        print(i, end = "")
    print()
 
Q20. Pyramid Pattern 
Print: 
        * 
      *** 
    ***** 
  ******* 
*********
k = 4                          
for i in range(1, 10, 2):     
    print(" " * k, end="")     
    k -= 1                     
    for j in range(1, i + 1): 
        print("*", end="")
    print() 

 
Q21. Inverted Pyramid 
Print: 
********* 
  ******* 
    ***** 
      *** 
        * 
k = 0
for i in range(9,0,-2):
    print(" "*k,end="")
    k+=1
    for i in range(1,i+1):
        print("*",end="")
    print()
    
Q22. Break in Pattern 
Print a star pattern. 
Stop printing when the row number reaches 4.

for i in range(1,10):
    if i>4:
        break
    for j in range(1,i+1):
        print("*",end="")
    print()

'''





        
