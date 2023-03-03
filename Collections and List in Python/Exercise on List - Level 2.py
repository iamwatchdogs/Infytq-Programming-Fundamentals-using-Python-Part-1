#lex_auth_012693750719488000124

def get_count(num_list):
    count=0

    # Write your logic here
    for i in range(1,len(num_list)):
        if num_list[i-1] == num_list[i]:
            count+=1

    return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))
