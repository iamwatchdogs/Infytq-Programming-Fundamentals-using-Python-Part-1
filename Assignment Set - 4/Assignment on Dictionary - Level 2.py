'''
Problem Statement
Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
Assume that the words contain only uppercase letters and the maximum word length is 10.

Sample Input

{"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}

Expected Output

[2, 2, 1]
'''

#lex_auth_01269444890062848087

def find_correct(word_dict):
    #start writing your code here
    res=[0,0,0]
    for x,y in word_dict.items():
        if x == y:
            res[0] += 1
        elif len(x) == len(y):
            count=0
            for i in range(len(x)):
                if x[i] != y[i]:
                    count += 1
            if count <= 2:
                res[1] += 1
            else:
                res[2] += 1
        else:
            res[2] += 1
    return res
    

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
