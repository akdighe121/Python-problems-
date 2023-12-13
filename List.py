Q. Suppose you have a list of temperatures recorded every hour for a week. Write a Python code to find the highest temperature from the list.

temp = [72, 68, 75, 80, 77, 82, 79, 85, 73, 70]
temp.sort()
print("maximum temperature is " , temp[-1])

Q. You have a list of grocery items and their prices. Write a Python code to calculate the total cost of the groceries.

grocery=[("apple",90),("banana",40),("pineapple",30),("chiku",50),("orange",60)]
Tcost=0
for item in grocery:
  print(item)
for item,price in grocery:

  Tcost+=price

print("the total cost of the items is ", Tcost)

Q. You have a list of names and their ages. Write a Python code to
#     find the name of the oldest person in the list.

record=[("akash",22),("siddi",23),("piyush",24),("nilesh",26)]
oldage=0
for name,age in record:
  if age>oldage:
    oldage=age
print(oldage)

Q. You have a list of strings representing sentences. Write a Python code to count the number of words in each sentence and store them in a new list.
sentence=["my name is akash","i am from ahmednagar","i am engineer"]
counts=[]
for line in sentence:
  word=line.split()
  count=len(word)
  counts.append(count)
  print(line ,"Sentence contains the total no ",count)

Q. Imagine you have a list of email addresses.
#Write a Python code to create a new list that contains only the email addresses that end with ".com".
Eaddress=[
    "john.doe@example.com",
    "jane.smith@gmail.com",
    "user123@yahoo.com",
    "contact.me@hotmail.com",
    "test.user@outlook.com",
    "developer007@protonmail.com",
    "mary.johnson@aol.com",
    "sam.wilson@icloud.com",
    "webmaster@mywebsite.org",
    "info@company.net",
    "support@helpdesk.co",
    "marketing@startup.biz",]
com_mail=[]
for i in Eaddress:
  if i.endswith(".com"):
      com_mail.append(i)
for i in com_mail:
  print(i)

Q. You have a list of numbers. Write a Python code to create a new list that contains only the odd numbers from the original list.
alist=[22,25,62,56,65,85,91,23]
blist=[]
for i in alist:
  if i%2 != 0 :
    blist.append(i)
blist

Q. Suppose you have a list of dictionaries where each dictionary contains information about a person such as name, age, and address. Write a Python code to create a new list that contains only the names of the people in the list.
a = [{"Name": "Akash","address": "Agra","age": 23},
     {"Name": "Rucha","address": "Lucknow","age": 24},
     {"Name": "Rushi","address": "Agra","age": 28},
     {"Name": "Priti","address": "Shahdol","age": 26},
     {"Name": "piyush","address": "Bareilly","age": 27}]
f = []
for i in a :
    f.append(i["Name"])
print(f)

Q.You have a list of strings representing book titles. Write a Python code to create a new list that contains only the titles that contain the word "Python".
vlist = ["intro to python","wonderland of fairy","beginner editon for python","hello to the world of python"]
ylist = []
for i in vlist :
  if "python" in i :
    ylist.append(i)
print(ylist)

Q. Imagine you have a list of tuples where each tuple contains a name and a phone number. Write a Python code to create a new list that contains only the phone numbers.
alist = [("Akash",846985),("Priti",258596),("piyush",652856),("Nilesh",586245)]
blist = []
for name,num in alist :
    blist.append(num)
print(blist)

Q. You have a list of numbers. Write a Python code to create a new list that contains the squares of the numbers in the original list.
alist = [1,2,3,4,5,6,7,8,9]
blist = []
for i in alist :
  blist.append(i**2)
print(blist)

Q. Suppose you have a list of strings representing file names. Write a Python code to create a new list that contains only the file names that have the extension ".txt".
alist = ["1.txt","2.pdf","3.txt","4.txt","5.jpg"]
blist = []
for i in alist :
  if ".txt" in i :
    blist.append(i)
print(blist)


Q. Imagine you have a list of tuples where each tuple contains a name and a salary. Write a Python code to create a new list that contains only the names of the people who earn more than $50,000 per year.

alist = [("Ironman",50000),("Thor",60000),("Antman",90000),("Spiderman",40000),("Wonda",30000)]
blist = []
for name,salary in alist :
  if salary>50000 :
    blist.append(name)
print(blist)

Q. You have a list of strings representing sentences. Write a Python code to create a new list that contains only the sentences that contain the word "Python" and "programming".
alist = ["hello guys welcome",
         "today we are going to start python",
         "our new module is python language",
         "python programming is very important"]
blist = []
for i in alist :
  if "python" and "programming" in i :
    blist.append(i)
print(blist)


Q. Suppose you have a list of integers. Write a Python code to create a new list that contains only the integers that are divisible by 3.
alist = [234,3455,456,56,6,77,5,57,4644,45]
blist = []
for i in alist :
  if i%3 == 0 :
    blist.append(i)
print(blist)
