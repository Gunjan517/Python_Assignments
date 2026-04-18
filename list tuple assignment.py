'''
Python Programming Questions – LIST
------------------------------------------------------------
Basic Level 
1. Write a Python program to create a list of integers and print its elements.

li = [10, 20, 30, 40, 50]
print(li)
for i in li:
    print(i)
    
2. Write a program to find the sum and average of all elements in a list.

li = [10, 20, 30, 40, 50]
print("List:", li)

sum = 0
average = sum / len(li)
for i in li:
    sum += i
print("Sum =", sum)
print("Average =", average)

3. Write a program to find the largest and smallest element in a list.

list=[10, 20, 30, 40, 50]
largest = max(list)
smallest = min(list)
print("list",list)
print("largest no. is", largest)
print("smallest no. is", smallest)

4. Write a Python program to count the number of elements in a list without using len().

list=[1,2,3,4,5,6,15,5]
count=0
for i in list:
    count += 1
print("No. of elements:",count)

5. Write a program to reverse a list without using built-in functions.
li = [10, 20, 30, 40, 50, 60, 70]
print("list",li)
rev_list = []

for i in range(len(li) - 1, -1, -1):
    rev_list.append(li[i])

print("reversed list",rev_list)

6. Write a program to check if an element exists in a list

li = [1, 2, 3, 4, 5, 6, 20]

ele = 20
if ele in li:
    print(f"{ele} exists in the list")
else:
    print(f"{ele} does not exist in the list")
 
7. Write a Python program to remove duplicate elements from a list.
li = [10, 20, 30, 40, 50, 30, 50, 60]
new_list = []
for i in li:
    if i not in new_list:
        new_list.append(i)
print(li)
print(new_list)

8. Write a program to sort a list in ascending and descending order.
li = [20, 30, 10, 40, 60, 50]
li.sort()
print(li)
li.sort(reverse=True)
print(li)

Intermediate Level
9. Write a program to merge two lists and remove duplicates.

li1 = [1,2,3,4]
li2 = [3,4,5,6]
merge= li1 + li2   
new_list = []               

for i in merge:
    if i not in new_list:
        new_list.append(i)

print("Merged list:", merge)
print("No duplicates:", new_list)

10. Write a program to find common elements between two lists.
li1 = [1, 2, 3, 4, 5, 6]
li2 = [4, 5, 6, 7, 8]

com_ele = []
for i in li1:
    if i in li2 and i not in com_ele:  
        com_ele.append(i)
print("List 1:", li1)
print("List 2:", li2)
print("Common elements:", com_ele)

11. Write a program to split a list into even and odd numbers.
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even=[]
odd=[]

for i in li:
    if i %2==0:
        even.append(i)
    else:
        odd.append(i)
 
print("Even nos:", even)
print("Odd nos:", odd)

12. Write a program to rotate a list by n positions.
li = [1,2,3,4,5,6,7,8,9,10]
print( li )
n = int(input("No of Right Rotation : "))
for i in range(n):
    val = li.pop(len(li)-1)
    li.insert(0,val)
print(li)

13. Write a Python program to find the second largest number in a list.
li = [10, 20, 40, 30, 50, 60, 70]
largest = li[0]
sec_largest = li[0]

for i in li:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest and i != largest:
        sec_largest = i

print("Second largest no. :", sec_largest)

14. Write a program to flatten a nested list.

li = [[10,30,40],[7,8,9],[5,8,7]]
f_li = []
print("Nested List :",li)
for x in li:
    for i in x:
        f_li.append(i)
print("Flatten List :",f_li)

15. Write a program to count frequency of each element in a list.

li = [10, 20, 10, 30, 20, 40, 10, 30, 20]

frequency = {}

for i in li:
    if i in frequency:
        frequency[i] += 1   
    else:
        frequency[i] = 1    

print("Original list:", li)
print("Frequency of elements:", frequency)

16. Write a program to replace all negative numbers with zero in a list.
li = [1, -2, 3, -4, -5, -6, 8]

for i in range(len(li)):
    if li[i] < 0:      
        li[i] = 0      

print("Updated list:", li)

Advanced Level:--
17. Write a program to remove all occurrences of a given element from a list.
list=[10, 20, 30, 40, 50,10, 10]
element = 10
new_list=[]
for i in list:
    if i != element:
        new_list.append(i)
print("New list=", new_list)

18. Write a program to check if a list is a palindrome.
li = [1, 2, 3, 2, 1]

if li == li[::-1]:  
    print("list is a palindrome")
else:
    print("list is not a palindrome")

19. Write a Python program to find missing numbers in a given list of consecutive integers.
li = [2,4,6,8,10,12,14,18]
diff = li[1]-li[0]
print(li)
flag = 0
for i in range(0,len(li)-1):
    if li[i]+diff != li[i+1]:
        print(f"{i+2} place Missing Element :",li[i]+diff)
        flag = 1
if flag==0:
    print("No Missing Value")

20. Write a program to perform element-wise addition of two lists.
li1 = [1, 2, 3, 4,5]
li2 = [5, 6, 7, 8, 9]

addition = []
for i in range(len(li1)):
    addition.append(li1[i] + li2[i])

print("addition:", addition)

21. Write a Python program to find the longest increasing subsequence in a list.
li = [21,78,89,765,23,23,35,39,45,667,8,9,635,58]
longest_sub_seq = []
temp = []
for i in range(0,len(li)-1):
    if li[i]<li[i+1]:
        temp.append(li[i])
    else:
        temp.append(li[i])
        if len(temp)>len(longest_sub_seq):
            longest_sub_seq = temp
        temp = []
print(longest_sub_seq)

22. Write a program to group elements based on frequency.

li = [1,4,6,54,3,1,3,4,6,5,3,2,1,3,4,6,54,3,1,4]
group_list = []
selected = []
for x in li:
    if x not in selected:
        selected.append(x)
        for j in li:
            if x==j:
                group_list.append(j)
print(group_list)




Python Programming Questions – TUPLE
---------------------------------------------------------------------
Basic Level 
23. Write a Python program to create a tuple and print its elements.
t = (10, 20, 30, 40, 50)
print(t)

24. Write a program to find the length of a tuple.
t = (10, 20, 30, 40, 50)
print(len(t))

25. Write a program to find the maximum and minimum element in a tuple.
t = (10, 20, 30, 40, 50)
print('maximum', max(t))
print('minimum',min(t))

26. Write a program to convert a tuple into a list.
t = (10, 20, 30, 40, 50)

li = list(t)
print("Tuple:", t)
print("List:", li)


27. Write a program to check if an element exists in a tuple.
t = (10, 20, 30, 40, 50)
ele=50
if ele in t:
    print("Element exists in tuple")
else:
    print("Element not exists in tuple")


28. Write a program to count occurrences of an element in a tuple.
t = (10, 20, 30, 40, 50,20,10,30,10,10,20,10)
count=0
ele = 10
for i in range(len(t)):
    if t[i]== ele:
        count=count+1
print("Occurrences of a element",count)

or
t = (10, 20, 30, 40, 50,20,10,30,10,10,20,10)
print(t.count(10))


Intermediate Level :-
29. Write a program to slice a tuple and display the result.
t = (10, 20, 30, 40, 50,20,10,30,10)
result=t[1:7]
print("tuple= ", t)
print("sliced tuple = ", result) 

30. Write a program to find repeated elements in a tuple.
t = (10, 20, 30, 40, 50, 20, 10, 30, 10, 10, 20, 10)

new_list = []   
for i in range(len(t)):
    for j in range(i+1, len(t)):
        if t[i] == t[j] and t[i] not in new_list:
            new_list.append(t[i])

print("Repeated elements:", new_list)

31. Write a program to merge two tuples.
t1 =(1, 2 ,3 , 4, 5)
t2 = (6, 7, 8, 9, 10)
t = t1+t2
print(t)

32. Write a program to unpack elements of a tuple into variables.
t = (1,2,3,4,5)
a,b,c,d,e = t

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)

33. Write a Python program to sort a tuple.

t = (2, 4, 3, 5, 1)
new = list(t)      
new.sort()         
new_t = tuple(new) 
print(t)         
print(new_t)  

34. Write a program to convert a list of tuples into a dictionary.
list1 = [('a', 10), ('b', 20), ('c', 30), ('d', 40)]

result = dict(list1)
print("list=", list1)
print("coverted to dictionary =" , result)

Advanced Level :--
35. Write a program to find the index of an element in a tuple.
t=(10,20,30,40,50,60,70)
for i in range(len(t)):
    print(t.index(t[i]),"is index of ",t[i])

36. Write a program to remove an element from a tuple (without directly modifying it).
t1 = (23,45,67,8,90,253)
num = 67
li = []
for x in t1:
    if num!=x:
        li.append(x)
print( tuple(li) )

37. Write a program to find common elements between two tuples.
t1 = [1, 2, 3, 4, 5, 6]
t2 = [4, 5, 6, 7, 8]

com_ele = []
for i in t1:
    if i in t2 and i not in com_ele:  
        com_ele.append(i)

print("Tuple 1:", t1)
print("Tuple2:", t2)
print("Common elements:", tuple(com_ele))

38. Write a Python program to check if a tuple is a palindrome.
t = (1, 2, 3, 2, 1)

if t == t[::-1]:  
    print("tuple is a palindrome")
else:
    print("tuple is not a palindrome")


39. Write a program to find the element with maximum frequency in a tuple.

t = (1,5,5,78,9,4,653,2,4,6,78,6,4,4,5,3,45,6,7,56,4,4)
maxx = t.count(t[0])
element = t[0]
for m in t:
    if maxx<t.count(m):
        maxx = t.count(m)
        element = m
print( element, maxx )

40. Write a program to create a nested tuple and access its elements
t=((1,2,3),6,(2,3))
print("First element :" ,t[0])
print("1st element of nested tuple",t[0][0])
print("2nd element of nested tuple",t[0][1])
print("3rd element of nested tuple",t[0][2])
print("second element : " ,t[1])
print("third element : " , t[2])
print("1st element of nested tuple",t[2][0])
print("2nd element of nested tuple",t[2][1])


or

nested_tuple=((1,2,3),6,(2,3))

for item in nested_tuple:
    if type(item) == tuple:
        print("Nested tuple found:", item)
        for sub_item in item:
            print("Element inside nested tuple:", sub_item)
    else:
        print("Normal element:", item)
'''




       
        



