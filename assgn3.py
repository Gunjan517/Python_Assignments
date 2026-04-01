'''
A. Python IF (Single Condition)
***************************************************************
1. Write a Python program to check if a number is positive.

num = int(input("Enter a number: "))
if num>0:
    print("The number is positive")
    
2. Print "Eligible to vote" if age is 18 or above.

age = int(input("Enter your age: "))
if age>=18:
    print("Eligible to vote")
    
3. Check if a number is divisible by 7.

num = int(input("Enter a number: "))
if num%7==0:
    print("the number is divisible by 7")

4. Print "Pass" if marks are greater than 40.

num = int(input("Enter your marks: "))
if num>=40:
    print("Pass")

5. Check if a number is greater than 100.

num = int(input("Enter a number: "))
if num>100:
    print("The number is greater than 100")

6. Display a message if temperature exceeds 45°C.

temp =int(input("Enter the Temperature: "))
if temp >= 45:
    print("Warning: Temperature exceeds 45°C!")
   
7. Check if a string length is more than 8 characters.

str=input("Enter a string:")
if len(str) > 8:
    print("The string length is more than 8 characters")
else:
    print("The string length is 8 or less than 8 characters")
    
8. Print "Logged In" if password matches "admin123".
pwd = input("Enter your password: ")

if pwd == "admin123":
    print("Logged in")
else:
    print("Invalid password")

9. Check if a number is a multiple of 10.
num = int(input("Enter a number: "))
if num%10==0:
    print("the number is a multiple of 10")
else:
    print("the number is not a multiple of 10")
    
10. Print a warning if balance is below minimum limit.
min_limit = 1000
balance = int(input("Enter your account balance"))
if balance <= min_limit:
    print("Warning! Balance is below the minimum limit")
else:
    print("Balance is Sufficient ")
'''

"""
B. Python IF–ELSE (Two Conditions)
*************************************************************************
11. Check whether a number is even or odd.
num = int(input("Enter a number"))

if num%2==0:
    print("Even no. ")
else:
    print("Odd no. ")
    
12. Find the largest of two numbers.
a= 45
b= 55

if a>b:
    print("a is the largest number")
else:
    print("b is the largest number")

13. Check whether a person is eligible for driving license.
age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible for driving license")
else:
    print("You are not eligible for driving license")

14. Print "Pass" or "Fail" based on marks.
num = int(input("Enter your marks: "))
if num>=30:
    print("Pass")
else:
    print("Fail")
    
15. Check whether a number is positive or negative.
num = int(input("Enter a number: "))
if num>0:
    print("positive no.")
else:
    print("negative no.")
    
16. Check whether a character is a vowel or consonant.
ch = input("Enter a character : ")
if ch in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")

17. Check if a year is leap or not.
year=int(input("Enter a year:"))
if year % 400 == 0:
    print(year, "is a leap year.")
elif year % 100 == 0:
    print(year, "is not a leap year.")
elif year % 4 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

18. Print "Valid Password" or "Invalid Password".
pwd = input("Enter your password: ")

if pwd == "admin123":
    print("Logged in")
else:
    print("Invalid password")

19. Determine whether salary is taxable or not.
salary = float(input("Enter your annual salary: "))
tax_limit = 250000

if salary >= tax_limit:
    print("Taxable Salary")
else:
    print("Not Taxable")
    
20. Check whether a number is greater than 50 or not.
num = int(input("Enter a number: "))

if num>50:
    print("The number is greater than 50")
elif num==50:
    print("The number is equal to 50")
else:
    print("The number is less than 50")

"""
'''
C. Python NESTED IF–ELSE
******************************************************
21. Find the largest of three numbers.
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))

if a >= b:
    if a >= c:
        print("a is the largest number")
    else:
        print("c is the largest number")
else:
    if b >= c:
        print("b is the largest number")
    else:
        print("c is the largest number")
    
22. Check whether a number is positive, negative, or zero.
num = int(input("Enter a number: "))

if num>0:
    print("positive no.")
else:
    if num < 0:
        print("negative no.") 
    else:
        print(" zero")

23. Assign grades: 
● A → marks ≥ 90 
● B → marks ≥ 75 
● C → marks ≥ 60 
● Fail → below 60

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
else:
    if marks >= 75:
        print("Grade: B")
    else:
        if marks >= 60:
            print("Grade: C")
        else:
            print("Fail")
            
24. Check whether a triangle is equilateral, isosceles, or scalene.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a == b:
    if b == c:
        print("The triangle is Equilateral")
    else:
        print("The triangle is Isosceles")
else:
    if b == c or a == c:
        print("The triangle is Isosceles")
    else:
        print("The triangle is Scalene")     

25. Check whether a character is uppercase, lowercase, digit, or special character.
ch = input("Enter A Character : ")
if ch>='0':
    if ch<='9':
        print("Digit")
    else:
        if ch<='Z':
            print("Upper Case")
        else:
            if ch<='z':
                print("Lower Case")
            else:
                print('Special Character')
else:
    print('Special Character')

26. Calculate electricity bill using slab-wise rates.
service_charge = 250
1-100 => 5/-
101-200 => 7/-
200+  => 10/-

service = 250
unit = int(input("Enter Unit Consumption : "))
if unit<=100:
    bill = unit*5
else:
    if unit<=200:
        bill = unit*7
    else:
        bill = unit*10
bill = bill+service
print("Bill :",bill)

27. Validate login using username and password.
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "admin123":
        print("Logged in")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")

28. Check student result using marks of 3 subjects.
m1 = int(input("enter marks 1: "))
m2 = int(input("enter marks 2: "))
m3 = int(input("enter marks 3: "))
num=m1+m2+m3
avg =num/3

if avg >= 90:
    print("Grade A")
else:
    if avg >= 70:
        print("Grade B")
    else:
        if avg >= 60:
            print("Grade C")
        else:
            if avg >= 50:
                print("Pass")
            else:
                print("Fail")


29. Find the second largest number among three numbers.
if a>b: 
    if a<c:
        print("Second Largest :",a)
    else:
        if b>c:
            print("Second Largest :",b)
        else:
            print("Second Largest :",c)
else:
    if b<c:
        print("Second Largest :",b)
    else:
        if a>c:
            print("Second Largest :",a)
        else:
            print("Second Largest :",c)

30. Check loan eligibility using age, salary, and credit score.
age = int(input("Enter your age:"))
salary = int(input("Enter your salary:"))
credit_score = int(input("Enter your credit score:"))
if age >=21:
    if salary>=20000:
        if credit_score >=500:
                   print("Loan approved")
        else:
            print(" Credit score is low")
    else:
        print("low salary")
else:
    print("you are not eligible")


D. Python ELIF (Multiple Conditions)
**********************************************
31. Print day name using day number (1–7).
day = int(input("enter day number (1-7): "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")

32. Print month name using month number.
month = int(input("Enter month number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid month number")

33. Display grade based on percentage.
per = int(input("Enter your percentage: "))

if per >= 90:
    print("Grade A")
elif per >= 75:
    print("Grade B")
elif per >= 60:
    print("Grade C")
elif per >= 50:
    print("Grade D")
else:
    print("Fail")

34. Display bonus percentage based on experience years.
experience = int(input("Enter your years of experience: "))

if experience >= 15:
    print("Bonus = 20%")
elif experience >= 8:
    print("Bonus = 10%")
elif experience >= 3:
    print("Bonus = 5%")
else:
    print("No Bonus")
    
35. Identify traffic signal meaning.
signal_color= input("Enter traffic signal color (red/yellow/green): ")

if signal_color == "red":
    print("STOP! do not proceed")
elif signal_color == "yellow":
    print("CAUTION! Prepare to stop or proceed carefully.")
elif signal_color == "green":
    print("GO! Vehicles can move ahead.")
else:
    print("Invalid input. Please enter red, yellow or green.")

36. Categorize temperature as Cold / Warm / Hot.
temperature = int(input("Enter the temperature in °C: "))

if temperature < 15:
    print("Cold")
elif temperature >= 15 and temperature <= 30:
    print("Warm")
else:
    print("Hot")

37. Categorize employee based on salary range.
num = int(input("Enter your salary:-"))

if num >= 100000:
    print("Executive Level")
elif num >= 60000:
    print("Senior Level")
elif num >= 30000:
    print("Mid Level")
else:
    print("Entry Level")

38. Print discount percentage based on purchase amount.
amount = int(input("Enter your purchase amount: "))

if amount >= 10000:
    discount = 20
elif amount >= 5000:
    discount = 15
elif amount >= 2000:
    discount = 10
else:
    discount = 5
print(f"You get a {discount}% discount on your purchase.")

39. Identify number type: single-digit / double-digit / multi-digit.
num = int(input("Enter A Number : "))
if num>=0 and num<=9:
    print("Single Digit")
elif num<100:
    print("Double Digit")
elif num<1000:
    print("Triple Digit")
else:
    print("Multi Digit")

40. Assign performance rating: Poor / Average / Good / Excellent.
num= int(input("Enter the performance marks (0-100): "))

if num < 40:
    rating = "Poor"
elif num < 60:
    rating = "Average"
elif num < 80:
    rating = "Good"
else:
    rating = "Excellent"

print("Performance Rating:", rating)

E. Python COMPLEX CONDITIONS (AND / OR / NOT)
******************************************************************
41. Check whether a number is divisible by 5 and 11.
num = int(input("Enter the number: "))

if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11")
else:
    print("The number is not divisible by both 5 and 11")

42. Check if a person is eligible for loan: 
● age ≥ 21 
● salary ≥ 25,000 
● credit score ≥ 700

age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))
credit_score = int(input("Enter credit score: "))

if age >= 21 and salary >= 25000 and credit_score >= 700:
    print("You are eligible for the loan")
else:
    print("You are not eligible for the loan")

43. Validate login using username AND password.
username = "aman"
password = "aman@123"

u_name = input("Enter your username: ")
p_wd = input("Enter your password: ")

if u_name == username and p_wd == password:
    print("Login successful!")
else:
    print("Invalid username or password.")

44. Check student pass condition: 
● All subjects ≥ 40 
● Average ≥ 50
s1=int(input("Enter marks for Subject 1: "))
s2= int(input("Enter marks for Subject 2: "))
s3 = int(input("Enter marks for Subject 3: "))
average=(s1+s2+s3)/3
if s1>=40 and s2>=40 and s3>=40 and average >=50:
    print("Student Passed")
else:
    print("Student Failed")

45. Check if a number lies between 10 and 100.
num = int(input("Enter a number: "))
if num >= 10 and num <= 100:
    print("number lies between 10 and 100")
else:
    print("number does not lie between 10 and 100")

46. Check exam eligibility: 
● attendance ≥ 75% OR 
● medical certificate available

att = float(input("Enter attendance percentage: "))
med_cert= input("Do you have a medical certificate? (yes/no): ")

if att >= 75 or med_cert.lower() == "yes":
    print("You are eligible for the exam")
else:
    print("You are not eligible for the exam")

47. Validate a date using conditions.
day = int(input("Enter Day : "))
month = int(input("Enter Month : "))
year = int(input("Enter Year : "))
if day>=1 and day<=31 and month>=1 and month<=12:
    print("Valid Date")
else:
    print("Invalid Date")

48. Check whether an email format is valid.
email = input("Enter An Email ID : ")
if '@' in email and '.' in email:
    print("valid email :",email)
else:
    print("Invalid Email")
    
(or)

email = input("Enter An Email ID : ")
if '@' in email and '.' in email and ( '0' in email or '1' in email or '2' in email):
    print("valid email :",email)
else:
    print("Invalid Email")

49. Determine insurance eligibility using age, health status, and income.
age = int(input("Enter your age: "))
health_sta = input("What's your health status? (excellent/poor): ")
income = int(input("Enter your income: "))

if age >= 18 and health_sta.lower() == "excellent" and income >= 50000:
    print("You are eligible for the insurance")
else:
    print("You are not eligible for the insurance")
    
50. Check leap year using complete leap year logic.
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year ")
else:
    print(f"{year} is NOT a Leap Year ")

'''

          




    





