#lex_auth_012693763253788672132

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    for i in range(no_of_passengers):
        ticket_number_list.append(airline+':'+source[:3]+':'+destination[:3]+':'+str(101+i))
        if len(ticket_number_list) > 5:
            ticket_number_list.pop(0)

    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))
