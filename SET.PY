Q. Imagine you have a list of numbers. Write a Python code to create a set that contains only the unique numbers in the list.
A=[1,12,23,3,2,11,1,3,21,1,2,2,2,23,44,4,]
b=set(A)
print(b)

Q.You have a set of student names who have attended a workshop. Write a Python code to add a new student to the set.
set1={"we","are","people"}
set1.add("hello")
print(set1)

Q. Suppose you have two sets of numbers. Write a Python code to create a new set that contains only the numbers that are present in both sets.
set1={1,2,3,4,5,6,7,8}
set2={9,8,7,6,5,4,3}
print(set1 and set2)


Q.You have a set of words. Write a Python code to create a new set that contains only the words that start with the letter "a".
set1={"qwerty","you","are","mad"}
set2=set()
for i in set1:
  if i[0]=='a':
    set2.add(i)
print(set2)

Q. Imagine you have a set of customer IDs. Write a Python code to create a new set that contains only the IDs of customers who have made more than 5 purchases.
cus_id={(1,2),(3,34),(5,6),(89,6)}
set2=set()
for i in cus_id:
  if i[1]>5:
    set2.add(i[0])
print(set2)


Q. You have a set of employee IDs. Write a Python code to remove a specific employee from the set.
set1 = {11, 12, 13, 14, 15, 16, 17}
set2 = set1.copy()
n = int(input('Enter the element to be removed: '))
for n in set2:
  if i==n:
    set1.remove(n)
print(set1)

Q. Imagine you have two sets of words. Write a Python code to create a new set that contains only the words that are present in the first set but not in the second set.
set1={"hii","hello","who","where"}
set2={"hello","who","did","this"}
set3=set1-set2

print("words which are not present in the set1 are: ",set3)



Q. You have a set of email addresses. Write a Python code to create a new set that contains only the email addresses that end with ".edu"

set1={"akash@gmail.com","piyush@gamil.com","nilesh@gamil.edu","siddhi@gmail.com"}
set2=set()
for i in set1:
  if '.edu' in i:
    set2.add(i)
print(set2)


Q.Suppose you have a set of book titles. Write a Python code to create a new set that contains only the titles that contain the word "Python".

set1={"harry","python","the","secerts","of","chamber"}
set2=set()
for i in set1:
  if 'python'in i:
    set2.add(i)
print(set2)


Q. Imagine you have a list of strings representing company names. Write a Python code to create a set that contains only the unique first letters of the company names.
list1=["TCS","Capgimini","ACCENTURE","MICROSOFT"]
set1=set()
for i in list1:
  if i:
    set1.add(i[0])
print(set1)


Q. You have a set of names. Write a Python code to check if a specific name is present in the set.
set1={"abc","def","ghi","klm"}
search=input("enetr the word to be search: ")
if search in set1:
  print(search,"the word exits in the set")
else:
   print(search,"the word does not exits in the set")

Q. Suppose you have two sets of numbers. Write a Python code to create a new set that contains only the numbers that are present in one set but not in both sets.
set1={1,2,3,44,5,6,7,8}
set2={2,3,4,5,6,78,8}
set3=set1-set2
print(set3)

