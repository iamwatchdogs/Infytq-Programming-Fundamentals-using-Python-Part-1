#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    intermediate_result=(no_of_adults*37550.0)+(no_of_children*(37550/3))
    service_tax=(7/100)*intermediate_result
    intermediate_result=intermediate_result+service_tax
    discount=(10/100)*intermediate_result
    total_ticket_cost=intermediate_result-discount
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(3,1)
print("Total Ticket Cost:",total_ticket_cost)
