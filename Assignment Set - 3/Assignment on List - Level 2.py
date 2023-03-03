#lex_auth_012693795044450304151

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    for i in reqd_gems:
        if i not in gems_list:
            bill_amount=-1
            return bill_amount
    for i in range(len(reqd_gems)):
        k = gems_list.index(reqd_gems[i])
        
        bill_amount+= price_list[k]*reqd_quantity[i]
    if bill_amount>30000:
        bill_amount= bill_amount-(5/100)*bill_amount    #Write your logic here
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
