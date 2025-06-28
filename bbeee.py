#1
string = input('Enter a string: ')
letter = 0
digit = 0
for char in string:
   if char.isalpha():
       letter += 1
   elif char.isdigit():
       digit += 1
print('Number of letters:', letter)
print('number of digits:', digit)
#2
str1 = input("enter first string: ")
symb = input("enter symbol: ")

count = 0
for char in str1:
    if char == symb:
        count += 1

print(f"the symbol '{symb}' appears {count} times in the string '{str1}'.")

#3

str2 = input("eter a string: ")

print(str2[::-1])

#4

str3 = input("enter a string: ")
word = input("enter a word to search for: ")
count = 0
for w in str3.split():
    if w == word:
        count += 1
print(f"the word '{word}' appears {count} times in the string '{str3}'.")

#5

string1 = input("enter a string: ")
search_word = input("Enter the word to search for: ")
replace_word = input("Enter the word to replace it with: ")
words = string.split()
modified_words = []
for word in words:
   if word == search_word:
       modified_words.append(replace_word)
   else:

       modified_words.append(word)
mod_string = " ".join(modified_words)
print(mod_string)

#6

strr = input()
t=''
a=strr.split(" ")
for i in a:
        if len(i)>len(t):
            t=i
        else:
            continue
print(t)
