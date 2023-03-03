#lex_auth_01269441913243238467

def create_largest_number(number_list):
    #remove pass and write your logic here
    return int(''.join(sorted(map(str,number_list),reverse=True)))

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
