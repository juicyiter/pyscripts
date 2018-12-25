# coding: utf-8

#
#  io_input.py
#  IO
#
#  Created by jit on 21 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved.
#

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

s = input("Enter a string:")

punctuation = ".?!:;- —()（）[] '\"/,"

""" ignoring the punctuation and case """
s = s.lower()

## removing punctuations
for cha in s:
    if punctuation.find(cha) != -1:
        """ Found and remove """
        s = s.replace(cha, "")

print(s)
if is_palindrome(s):
    print("Yes, it's a palindrome text.")

else:
    print("No, it's not a palindrome text.")
