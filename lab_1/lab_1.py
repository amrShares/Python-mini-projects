# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#2

# text = input('enter a phrase : ')
# count=0


# for character in text :
#     if character == 'a' or character == 'i' or character == 'o' or character == 'e' or character == 'u':
#         count += 1
        
# print("number of vowels is", count)


#3

# num_iterations = 5
# inputs = []

# for i in range(num_iterations):
    
#     element = input("please enter a word : ")
    
#     inputs.append(element)
    
# print(sorted(inputs))

#3 one-line input

# num_iterations = 5

# inputs = input("please enter any number of words, separated by commas : ").split(",")
    
# print(sorted(inputs))

#4 

# phrase = "hello, I am a student in iti. the iti program duration is 9 month"
# print(phrase.count("iti"))

#5

# phrase = "hello, this phrase contains vowels"
# print(phrase.replace('a', '').replace('e','').replace('i','').replace('o','').replace('u',''))

#5 solution 2.0

# vowels = ['a', 'e', 'i', 'o', 'u']
# phrase = "hello, this phrase contains vowels"

# phrase = ''.join([char  for char in phrase if char not in vowels])
# print(phrase)


#6
 
# phrase = "this is a phrase that contains multiple occurences of the letter i"
# positions = []
# i=0
# for character in phrase:
#     if character == 'i' :
#         positions.append(i)
#     i+=1
# print(positions)

#7
# table_length = int(input("write multiplication table size : "))
# table = []
# for i in range(1,table_length+1):
#     table.append([])
#     for j in range(1,i+1):
#         table[i-1].append(i*j)
# print(table)

#8

# pyramid_length = int(input("enter pyramid height : "))
# for i in range(0,pyramid_length+1):
#     for j in range(1,i+1):
#         print('*', end = '')
#     print()
    
#8 again because she doesn't like my solutions  
    
pyramid_length = int(input("enter pyramid height : "))
for i in range(0,pyramid_length+1):
    for j in range(pyramid_length-i):
        print(' ', end = '')
    for k in range(1,i+1):
        print('*', end = '')
    print()