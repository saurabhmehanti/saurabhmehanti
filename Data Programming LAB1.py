#!/usr/bin/env python
# coding: utf-8

# # Question 1
# ### What data type is each of the following (evaluate where necessary)?

# In[1]:


import math


# In[2]:


a=5
b=5.0
c=5 > 1
d='5'
e=5 * 2
f='5' * 2
g='5' + '2'
h=5 / 2
i=5%2
j= {5,2,1}
k=5== 3
l=math.pi


# In[3]:


print(f'The datatype of {a} is:', type(a))
print(f'The datatype of {b} is:', type(b))
print('The datatype of 5 > 1 is:', type(c))
print(f'The datatype of {d} is:', type(d))
print(f'The datatype of {e} is:', type(e))
print(f'The datatype of {f} is:', type(f))
print(f'The datatype of {g} is:', type(g))
print(f'The datatype of {h} is:', type(h))
print(f'The datatype of {i} is:', type(i))
print('The datatype of',j, 'is:', type(j))
print('The datatype of 5 == 3 is:', type(k))
print('The datatype of pi(the number)is:', type(l))


# # Question 2
# ### Write (and evaluate) python expressions that answer these questions:
# ### a. How many letters are there in 'Supercalifragilisticexpialidocious'?

# In[4]:


W = 'Supercalifragilisticexpialidocious'
letters = len(W)
print(f"There are {letters} letters in the word '{W}'.")


# ### b. Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring?

# In[5]:


substring = 'ice'
if substring in W:
    print(f'Yes, {substring} is the substring of {W}')
else:
    print(f'No, {substring} is not the substring of {W}')


# ### c. Which of the following words is the longest: Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or Bababadalgharaghtakamminarronnkonn?

# In[6]:


words = ['Supercalifragilisticexpialidocious','Honorificabilitudinitatibus','Bababadalgharaghtakamminarronnkonn']

longest = max(words, key=len)

print(f"The longest word is: {longest}")


# ### d. Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?

# In[7]:


composers = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
composers.sort()  # This will sort the list of words alphabatically

first = composers[0]

print("The composer that comes first is:", first)


# # Question 3
# ### Implement function triangleArea(a,b,c) that takes as input the lengths of the 3 sides of a triangle and returns the area of the triangle. By Heron's formula, the area of a triangle with side lengths a, b, and c is s(s - a)(s -b)(s -c), where s = (a +b + c) /2.

# In[8]:


def triangleArea(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))**0.5 
    return area

a = int(input('First Side: '))
b = int(input('Second Side: '))
c = int(input('Third Side: '))
area = triangleArea(a, b, c)
print("The area of the triangle with sides", a, b, "and", c, "is",area)


# # Question 4
# ### Write a program in python to separate odd and even integers in separate arrays. Go to the editor Test Data : Input the number of elements to be stored in the array :5 Input 5 elements in the array :
# ### element - 0 : 25
# ### element - 1 : 47
# ### element - 2 : 42
# ### element - 3 : 56
# ### element - 4 : 32
# ### Expected Output:
# ### The Even elements are:
# ### 42 56 32
# ### The Odd elements are :
# ### 25 47

# In[9]:


elements = [25, 47, 42, 56, 32]

# Creating empty list of even and odd numbers.
even = []
odd = []

for i in elements:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

# Print the even and odd elements
print("The Even elements are:")
print(" ".join(map(str, even)))

print("The Odd elements are:")
print(" ".join(map(str, odd)))


# # Question 5
# ### a. Write a function inside(x,y,x1,y1,x2,y2) that returns True or False depending on whether the point (x,y) lies in the rectangle with lower left corner (x1,y1) and upper right corner (x2,y2).

# In[10]:


############################
## When x = 1 and y = 1. ###
############################

def inside(x, y, x1, y1, x2, y2):
    if x1 <= x <= x2 and y1 <= y <= y2:
        return True
    else:
        return False

x = 1
y = 1
x1 = 0
y1 = 0
x2 = 2
y2 = 3

result = inside(x, y, x1, y1, x2, y2)
print(result)

#############################
## When x = -1 and y = -1. ##
#############################
def inside_2(X, Y, X1, Y1, X2, Y2):
    if X1 <= X <= X2 and Y1 <= Y <= Y2:
        return True
    else:
        return False
X = -1
Y = -1
X1 = 0
Y1 = 0
X2 = 2
Y2 = 3

result_2 = inside_2(X, Y, X1, Y1, X2, Y2)
print(result_2)


# ### b. Use function inside() from part a. to write an expression that tests whether the point (1,1) lies in both of the following rectangles: one with lower left corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower left corner (0.5, 0.2) and upper right corner (1.1, 2).

# In[11]:


# Let the points be x and y
x = 1
y = 1

# Rectangle 1 
x1_r1 = 0.3
y1_r1 = 0.5
x2_r1 = 1.1
y2_r1 = 0.7

# Rectangle 2
x1_r2 = 0.5
y1_r2 = 0.2
x2_r2 = 1.1
y2_r2 = 2.0

# Test if (x, y) is inside both rectangles
rect1 = inside(x, y, x1_r1, y1_r1, x2_r1, y2_r1)
rect2 = inside(x, y, x1_r2, y1_r2, x2_r2, y2_r2)

# Check the result
if rect1 and rect2:
    print(f"The point ({x}, {y}) is inside both rectangles.")
else:
    print(f"The point ({x}, {y}) is not inside both rectangles.")


# # Question 6
# ### 16. You can turn a word into pig-Latin using the following two rules (simplified):
# ### • If the word starts with a consonant, move that letter to the end and append 'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'.
# ### • If the word starts with a vowel, simply append 'way' to the end of the word. For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant).
# ### Write a function pig() that takes a word (i.e., a string) as input and returns its pig-Latin form. Your function should still work if the input word contains upper case characters. Your output should always be lower case however

# In[12]:


def pig(word):
    word = word.lower()  # We will convert the word into lower case everytime
    
    # if the word starts with a vowel
    vowels = ['a','e','i','o','u']
    if word[0] in vowels:
        return word + 'way'
    else:
        index = 0
        while index < len(word) and word[index] not in vowels:
            index += 1
        
        # Rearrange the word and append 'ay'
        return word[index:] + word[:index] + 'ay'


word1 = 'happy'
word2 = 'pencil'
word3 = 'enter'
word4 = 'other'

print(pig(word1))
print(pig(word2))
print(pig(word3))
print(pig(word4))


# # Question 7
# ### File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic. Write a function bldcount() that reads the file with name name and reports (i.e., prints) how many patients there are in each bloodtype.

# In[13]:


def bldcount(filename):
    file = open(filename, 'r')
    data = file.readline()
    word_list = []
    blood_type = ['A', 'B', 'AB', 'O', 'OO']
    word_list.append(data.split(" "))
    for btype in blood_type:
        count = word_list[0].count(btype)
        print("There are {} patients of blood type {}.".format(count, btype))

bldcount('bloodtype1.txt')


# # Question 8
# ### Write a function curconv() that takes as input:
# ### 1. a currency represented using a string (e.g., 'JPY' for the Japanese Yen or 'EUR' for the Euro)
# ### 2. an amount and then converts and returns the amount in US dollars.

# In[ ]:





# In[14]:


def curconv (target_currency, amount):
    currency_data = {}
    currency_file = open ('currencies.txt')
    file_lines = currency_file.readlines ()
    
    for line in file_lines:
        code = line[:3].strip() 
        values = line[4:].split("\t")
        currency_data[code] = (values[0].strip(), values [1].strip ())

    conversion_rate = float (currency_data[target_currency][0])
    converted_amount = amount * conversion_rate
    print(converted_amount)

curconv ('EUR', 100)
curconv('JPY', 100)


# # Question 9
# ### Each of the following will cause an exception (an error). Identify what type of exception each will cause.
# ### Trying to add incompatible variables, as in adding 6 + ‘a’. Referring to the 12th item of a list that has only 10 items. Using a value that is out of range for a functi on’s input, such as calling math.sqrt( 1.0). Using an undeclared variable, such as p rint(x) when x has not been defined. Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory.

# In[15]:


try:
    trying = 6 + 'a'
    print(trying)
except Exception as e:
    print('Exception Occured',e)
    
# It is a type error because we are trying to add a integer and a string.


# In[16]:


# Refering to the 12th item of a list that has only 10 items.

List = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ']

try:
    item = List[11]
    print("Item:", item)
except Exception as e:
    print("Error:", e)
    
# This is an index error because there are only 10 items in the element but we are trying to access 12th item.


# In[17]:


try:
    math.sqrt(-1.0)
except Exception as e:
    print('Error', e)
    
# This is a value Error becasue square root of a negative number is not defined in the real number system.


# In[18]:


try:
    print(Undeclared)
except Exception as e:
    print("Error:",e)
    
    
#This is a name error because the variable "Undeclared" is not defined.


# In[19]:


try:
    name_of_file = "bloodtypee3.txt"
    file = open(name_of_file, 'r')
    for line in file:
        print(line.strip())
except Exception as e:
    print(f"An error occurred: {e}")

    
    
# This is a example of a file we used above which was "bloodtype1.txt", but when we miss-spelled the file name
# it will give FileNotFound Error.


# In[ ]:




