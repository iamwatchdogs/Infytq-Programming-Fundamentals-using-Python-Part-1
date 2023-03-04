'''
Problem Statement
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 

Assume that the sentence would begin with a word and there will be only a single space between the words.

Perform case sensitive string operations wherever necessary.

Sample Input

the sun rises in the east

Expected Output

eht snu sesir ni eht stea
'''

#lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    #start writing your code here
    res=''
    count=0
    for i in sentence.split():
        if count%2 == 0:
            res += i[::-1]+' '
        else:
            vowels=''
            consonts=''
            for j in i:
                if j.lower() in ['a','e','i','o','u']:
                    vowels+=j
                else:
                    consonts+=j
            res += consonts+vowels+' '
        count += 1
    return res.strip()

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
