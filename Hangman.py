#Code for Hangman:)
import numpy

    return True
def input_answer(answer):
    if len(answer) == 1:
        answer= answer.lower()
        exit= False
        return answer
    else:
        print "Try again, only one letter at a time"
        exit= True

word_list=["bomb","jelly","desktop","mangosteen"]#Later
#raw_input ("Hangman Time :) Press any key to begin.")
word= (numpy.random.choice(word_list))
ino=0
letters=word_list[ino]
#code for ACSII art
Artwork=[
"------\n"
"|    |\n"
"|\n"
"|\n"
"|\n"
"|\n"
"|______\n"
,
"------\n"
"|    |\n"
"|    O\n"
"|\n"
"|\n"
"|\n"
"|______\n"
,

"------\n"
"|    |\n"
"|    O\n"
"|   /|\\\n"
"|\n"
"|\n"
"|______\n"
,
"------\n"
"|    |\n"
"|    O\n"
"|   /|\\\n"
"|    |\n"
"|   / \\\n"
"|______\n"

]



print Artwork[0]
print "_ "*len(word)
number_attempts= (len(Artwork)-1)

right=0
input_answer(answer)
if exit==False:
    for x in letters:
        if x==answer :
            print ("  "*word.index(x)) + answer
            print "_ " * len(word)
            y=False
            right=1
    y =True
    if y!=False and right==0:
        print Artwork[1]
if exit==True:


