
#This function test if the number entered is a isbn10 number
def isbn10(number):

    tot=0
    mult = 0 ;

    #Loop from 10 down to 1 
    #Add the multiplied number to the total
    for i in range(10,0,-1):
        tot+=1
        mult += i* int(number[tot-1])
        
    #If the total is divisible by 11 , Return true . Else return False
    if (mult%11==0):
        return True
    else:
        return False



#This function test if the number entered is a isbn10 number
def isbn13(number):
    tot = 0
    mult =0

    ##Loop from 1 to 13 (Amount of numbers)
    for i in range(1,14):
        tot+=1
        
        #If it is a even number , multiply by 3 and append to the Total
        #If number is uneven append to the Total
        if i%2==0:
            mult+= int(number[i-1]) * 3
        else:
            mult+= int(number[i-1]) 
    
    #If the total is divisible by 10 , Return True . Else return False.
    if (mult%10==0):
        return True
    else:
        return False



##Function that tests an inputted number
def Testnum(number):
    
    #If the length of the number is 10(isbn10 number)
    #Test if it is a valid isbn10 number
    #If isbn10 is valid , initiate a newnumber with 978 as the first digits
    if len(number)==10:

        if isbn10(number)==True:
            newnum = "978" + number 
            
            #Loop from 1 to 9 and test what last digit is valid for a isbn13 number
            #If new isbn13 number is valid ,Print it to the user.
            for i in range(0,10):
                tester = newnum[:-1] + str(i)
                if isbn13(tester)==True:
                    print(f"Your new isbn13 number is : {tester}")

        #print isbn10 invalid if number is not valid
        else:
            print("Your isbn10 is invalid !")

    #If the length of inputted number is 13 , Test if its a valid isbn13 number
    #If isbn13 is true , print valid number .Else print invalid number
    elif len(number)==13:
        if isbn13(number)==True:
            print("Your isbn13 number is valid !")
        else:
            print("Your isbn13 number is invalid")
    
    ##If length is not 10 or 13 , print to user
    else:
        print("Number entered is not 10 or 13 digits")



#Try
#Ask the user to enter a 10 or 13 digit number
#If the entered number is not digits then raise Exception
#Call the Testnum function to test number
try:
    num = str(input("Please enter a 10 or 13 digit isbn number : \n"))

    if (num.isdigit()==False):
        print("Your value should contain numbers only\n")
        raise Exception
    
    Testnum(num)
    

except(Exception):
    print("There was an error with your input")




    