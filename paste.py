Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=input('something:')
something:10 #entered data is treated as number
>>> x
10
>>> x=input('something:')
something:'10' #eentered data is treated as string
1. Python 3 – What is New? 
Python 3
3
>>> x
'10'
>>> x=raw_input("something:")
something:10 #entered data is treated as string even without ''
>>> x
'10'
>>> x=raw_input("something:")
something:'10' #entered data treated as string including ''
something:5
>>> 
>>> 4
4
>>> ti

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ti
NameError: name 'ti' is not defined
>>> 
