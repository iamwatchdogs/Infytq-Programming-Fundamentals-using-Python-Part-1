#lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    list1=list(range(num1,num2+1))
    list2=[]
    if num1<num2:
        for i in list1:
            temp = i
            temp1 =0
            while temp!=0:
                temp1+=temp%10
                temp=temp//10    
            if temp1%3==0 and i%5 ==0 and len(str(i)) == 2:
                    list2.append(i)
        if(len(list2)!=0):
            list2.sort()
            max_num = list2[-1]
        else:
            max_num=-1
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)
