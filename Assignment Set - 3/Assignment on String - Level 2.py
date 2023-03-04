#lex_auth_012693816331657216161

def encode(message):
    #Remove pass and write your logic here
    if len(message) == 1:
        return '1'+message
    result=''
    count = 0
    for i in range(1,len(message)):
        if message[i-1] == message[i]:
            count+=1
        else:
            result+=str(count+1)+message[i-1]
            count=0
    if message[len(message)-2] == message[len(message)-1]:
        result+=str(count)+message[len(message)-1]
    else:
        result+='1'+message[len(message)-1]
    return result

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
