'''
Problem Statement
Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence. 

Rules are as follows: 
a. Spaces are to be retained as is 
b. Each word should be encoded separately

If a word has only vowels then retain the word as is

If a word has a consonant (at least 1) then retain only those consonants

Note: Assume that the sentence would begin with a word and there will be only a single space between the words.

Sample Input

I love Python
MSD says I love cricket and tennis too
I will not repeat mistakes

Expected Output

I lv Pythn
MSD sys I lv crckt nd tnns t
I wll nt rpt mstks
'''

#lex_auth_01269444961482342489

def sms_encoding(data):
    #start writing your code here
    word=data.split()
    vowels="aeiouAEIOU"
    st=""
    for i in word:
        if(len(i)==1):
            st=st+i
        else:
            for j in i:
                if j not in set(vowels): #consonant
                    st=st+j
        st=st+" "
    return st[0:-1]

data="I love Python"
print(sms_encoding(data))
