# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 15:37:10 2022

@author: amrsh
"""


'''
 Write a function that accepts two arguments (length, start) to 
generate an array of a specific length filled with integer numbers 
increased by one from start
'''

# def two_args(length, start):
#     return [start+1]*length

# print(two_args(5, 2))

# def two_args(length, start):
#     return [(start + i + 1) for i in range(length)]

# print(two_args(5,2))

'''
 write a function that takes a number as an argument and if the 
number divisible by 3 return "Fizz" and if it is divisible by 5 return 
"buzz" and if is is divisible by both return "FizzBuzz"
'''
# def is_fizz_buzz(num):
#     if (num % 3 == 0 and num % 5 == 0):
#         return "FizzBuzz"
#     if (num % 3 == 0):
#         return "Fizz"
#     elif (num % 5 == 0):
#         return "Buzz"
    
# print(is_fizz_buzz(15))
# print(is_fizz_buzz(10))
# print(is_fizz_buzz(9))
# print(is_fizz_buzz(16))


'''
 Write a function which has an input of a string from user then it 
will return the same string reversed.
'''

# def reverse_string():
#     text = input("enter a string : ")
#     return text[::-1]
# print(reverse_string())


'''
Ask the user for his name then confirm that he has entered his 
name(not an empty string/integers). then proceed to ask him for 
his email and print all this data (Bonus) check if it is a valid email 
or not
'''
# import re
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# def user_interface():
#     text = input("please enter your name : ")
#     while (not text.isalpha()):
#         print("wrong input")
#         text = input("please enter your name : ")
#     print(f"hello, {text}")
#     text = input("what's your e-mail ? ")
#     if (re.search(regex, text)):
#         print("valid email")
#     else :
#         print("invalid e-mail")
    
# user_interface()


'''
Write a function that takes a string and prints the 
longest alphabetical ordered substring occurred For example, if 
the string is 'abdulrahman' then the output is: Longest substring in 
alphabetical order is: abdu
'''    
# def longest_ordered_0(text):
#     i = 0
#     longest = [1]
#     while (i < len(text)-1):
#         if (text[i] < text[i+1]):
#             longest[-1] += 1
#         else:
#             longest.append(1)
#         i+=1
#     return max(longest)

# def longest_ordered(text):
#     i = 0
#     longest = [[text[0]]]
#     while (i < len(text)-1):
#         if (text[i] < text[i+1]):
#             longest[-1].append(text[i+1])
#         else:
#             longest.append([text[i+1]])
#         i+=1
#     return ''.join(sorted(longest, key = len)[-1])
    
# print(longest_ordered("abcdefgalb"))

'''
Write a program which repeatedly reads numbers until the user 
enters “done”.
○ Once “done” is entered, print out the total, count, and 
average of the numbers.
○ If the user enters anything other than a number, detect their 
mistake, print an error message and skip to the next number.

'''

# text = input("please enter a number or if your're done enter 'done' : ")
# count = 0
# total = 0
# while(text != "done"):
#     if text.isdigit():
#         count +=1
#         total += int(text)
#     else :
#         print("wrong input")
#     text = input("please enter a number or if your're done enter 'done' : ")
        
# print(f"you entered {count} numbers")
# print(f"the sum of the numbers is {total}")
# print(f"the average of the numbers is {total / count}")    
    

'''
Word guessing game (hangman)
○ A list of words will be hardcoded in your program, out of 
which the interpreter will
○ choose 1 random word.
○ The user first must input their names
○ Ask the user to guess any alphabet. If the random word 
contains that alphabet, it
○ will be shown as the output(with correct placement)
○ Else the program will ask you to guess another alphabet.
○ Give 7 turns maximum to guess the complete word.
'''

# import random

# words = ['hello', 'noha', 'eat', 'sleep', 'play', 'work', 'giraffe', 'banana']


# def show_partial_guessed(word, parts):
#     partial = []
#     for character in word :
#         if character in parts:
#             partial.append(character)
#         else :
#             partial.append(" _ ")
#     print(''.join(partial))
    

# def check_complete(word, parts):
#     partial = []
#     for character in word :
#         if character in parts:
#             partial.append(character)
#         else :
#             partial.append(" _ ")
#     if ''.join(partial) == word:
#         return 1
#     else:
#         return 0
    
# def welcome_interface():
#     print("let's start a game")
#     print("I have a word in mind, can you gueess what it is?")
#     print("you have 7 attempts")
#     print("good luck!")
    
# def input_interface(word, parts):
#     character = input("enter a single character : ")
#     parts.append(character)
#     if character in word:
#         print("good choice!")
#     else :
#         print("bad luck. Try again!")
    
# def game_engine():
    
#     welcome_interface()
#     word = random.choice(words)
    
#     parts = []
#     attempts = 0
#     complete = False
    
#     while(attempts < 7 and not complete):
#         input_interface(word, parts)
#         show_partial_guessed(word, parts)
#         if (check_complete(word, parts)):
#             complete = True
#         attempts += 1
#     if complete :
#         print("good job, user! you found my word")
#     else :
#         print("nice try, user. Better luck next time!")
    
# game_engine()