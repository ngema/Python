                    #Regular Expressions
#the re.match function can be used to determine whether it matches at the beginning of a string.
'''
To avoid any confusion while working with regular expressions, we would use raw
strings as r"expression".
'''

import re

pattern=r"spam"

if re.match(pattern,"spamspamspam"):
    print("Match")

else:
    print("No Match")

#The function re.search finds a match of a pattern anywhere in the string.
#The function re.findall returns a list of all substrings that match a pattern.
if re.search(pattern,"eggspamsausagespam"):
    print("Match")
else:
    print("No Match")

print(re.findall(pattern,"eggspamsausagespam"))
'''
This method replaces all occurrences of the pattern in string with repl,
substituting all occurrences, unless max provided
'''

str="My name is David .Hi David"
pattern=r"David"
newstr=re.sub(pattern,"Amy",str)
print(newstr)

'''
The pattern "^gr.y$" means that the string should start with gr, then follow with any character, except a newline, and end with y.
'''

                #character classes
'''
Character classes provide a way to match only one of a specific set of characters.
A character class is created by putting the characters it matches inside square brackets.
'''

import re

pattern=r"[aeiou]"

if re.search(pattern,"gery"):
    print("Match 1")

if re.search(pattern,"qwertyuiop"):
    print("Match 2")

if re.search(pattern,"rythm"):
    print("Match 3")


patterns=r"[A-Z][0-9]"

if re.search(patterns,"LS8"):
    print("Match 1")

if re.search(patterns,"E3"):
    print("Match 2")

if re.search(patterns,"1ab"):
    print("Natch 3")

#Place a ^ at the start of a character class to invert it.
#This causes it to match any character other than the ones included.

pat=r"[^A-Z]"

if re.search(pat,"this is all quiet"):
    print("Match 1")

if re.search(pat, "AbCdEfG123"):
   print("Match 2")

if re.search(pat, "THISISALLSHOUTING"):
   print("Match 3")

           #Metacharacters
# metacharacters are *, +, ?, { and }.
#The metacharacter ? means "zero or one repetitions

patt=r"ice(-)?cream"

if re.match(patt,"ice-cream"):
    print("Match 1")

if re.match(patt,"icecream"):
    print("match 2")

'''
Curly braces can be used to represent the number of repetitions between two numbers.
The regex {x,y} means "between x and y repetitions of something". 
'''

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")

if re.match(pattern, "9999"):
   print("Match 3")


            #Groups
'''
Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content.
They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
Non-capturing groups have the format (?:...). They are not accessible by the group method,
so they can be added to an existing regular expression without breaking the numbering.
'''
import re
'''
test = re.compile('(a)(b(?:c)(d)(?:e))') 
match = test.search('abcde') 
match.groups() ('a', 'bcde', 'd') 
len(match.groups())'''


                #The Zen of Python
import this


a, b, c, d, *e, f, g = range(20)
print(len(e))
                #__main__

'''
To do this, place script code inside if __name__ == "__main__". 
This ensures that it won't be run if the file is imported.
'''
'''
if __name__=="__main__":
   print("This is a script")




def func(**kwargs):
    print(kwargs["zero"])

func(a=0,zero=8)


for i in range(10):
    try:
        if 10/i ==2.0:
            break
    except ZeroDivisionError:
            print(1)
    else:
            print(2)

'''



        #Metacharacters (Need to be escaped): .[{()\^$]?*+
        #allow us to search for a specific of text.
'''
. -Any character Except New Line
\d-Digit (0-9)
\D-Not a Digit (0-9)
\w-Word Character (a-z,A-Z,0-9, _)
\W-Not a Word character
\s-Whitespace(space,tab,newline)
\S-Not whitespace (space,tab,newline)

\b-Word Boundary
\B-Not a word boundary
^-Beginning of a string
$-End of a String

[]-Matches characters in brackets
[^ ]-Matches characters NOT in brackets
|-Either or
()-Group

Quantifiers:
* -0 or more
+-1 or more
?-0 or one
{3}-exact number
{3,4}- Range of NUmbers (Minimum,Maximum)

#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]
'''
        

import re

text_to_search='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

Metacharacters :
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
458*854*9647
800-555-4321
900.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
pat
bat
'''


sentence='Start a sentence and then bring it to an end'

print(r'\tTAB') #it is called the raw string
#pattern=re.compile(r'.')
#pattern=re.compile(r'[89]00[-.]\d{3}[-.]\d{4}')
#pattern=re.compile(r'\bHa')
#pattern=re.compile(r'coreyms\.com')
#pattern=re.compile(r'^Start')
#pattern=re.compile(r'end$')
#matches=pattern.finditer(sentence)
#pattern=re.compile(r'[^b]at')
pattern=re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches=pattern.finditer(text_to_search)


for match in matches:
    print(match)

'''
with open('phiwa.txt','r') as f:
    contents=f.read()

    matches=pattern.finditer(contents)

    for match in matches:
        print(match)

print(text_to_search[1:4])
'''


import re
emails='''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
#pattern=re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
#pattern=re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')
pattern=re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
matches=pattern.finditer(emails)

for match in matches:
    print(match)

urls='''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

patterns=re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subb_urls=patterns.sub(r'\2\3',urls)
print(subb_urls)
matches=patterns.finditer(urls)

for match in matches:
    print(match.group(1))












