#Python Programming Projects 
#COSC 1315 Intro To Programming
------------------------------------------------------------------------------------------------------------------------------------

/// Write a program that determines the loan payment amount, given the loan amount, interest rate, and the number of payments. 
#user information

n = input("Please enter your fullname: ")
o = input("What is your occupation?: ")

#user iputs amount they want, interest rate and for how long to pay
loan_amt = float(input("Enter the loan amount: "))
rate = float(input("Enter the annual interest rate percentage: "))
years = int(input("How long will it take to repay this loan? " ))


#This computes the interest rate per pay period and # of payments
period_rate = rate / 12 / 100
num_payments = years * 12

#This formula computes the payment amount
payment_amt = period_rate * loan_amt / (1-(1 + period_rate) ** -num_payments)

#This formula computes the total cost of borrowing
total_cost = num_payments * payment_amt - loan_amt


#This prints the results for the user
print(n + "" + o)
print("The payment amount will be $ " , payment_amt, "per month." )
print("The total cost of borrowing will be $", total_cost,".")
------------------------------------------------------------------------------------------------------------------------------------
///If the user enters data that is "out of bounds" (loan amount/number of payments below or above minimum/maximum in the table), display an error message explaining the situation to the user and ask for the loan amount or number of payments (whichever one was out of bounds) again. Message Example: "We do not finance loans below $500."

def input_amount():
    while True:
        loan_amount = int(input("Enter loan amount: $"))
        if loan_amount < 500:
            print("We do not finance loans below $500")
            continue

        return loan_amount

        
def input_payments():
    while True:
        num_payments = int(input("Enter number of payments: "))
        if num_payments < 6 or num_payments > 48:
            print("Number of payments must be between 6 and 48")
            continue

        return num_payments


    
def calc_interest(loan_amount, num_payments):
    if loan_amount >= 500 and loan_amount <= 2500:
        if num_payments >= 6 and num_payments <=12:
            return 0.08
        if num_payments >= 13 and num_payments <= 36:
            return 0.10
        if num_payments >= 37 and num_payments <= 48:
            return 0.12
    elif loan_amount >= 2501 and loan_amount <= 10000:
        if num_payments >= 6 and num_payments <=12:
            return 0.07 # This is what table states
        if num_payments >= 13 and num_payments <= 36:
            return 0.08 # This is what table states
        if num_payments >= 37 and num_payments <= 48:
            return 0.06 # This is what table states
    elif loan_amount >= 10001:
        if num_payments >= 6 and num_payments <=12:
            return 0.05
        if num_payments >= 13 and num_payments <= 36:
            return 0.06
        if num_payments >= 37 and num_payments <= 48:
            return 0.07
        
def calc_payments(loan_amount, num_payments, interest_rate):
    return loan_amount / num_payments * (1.0 + interest_rate)


def main():
    while True:
        loan_amount = input_amount()
        num_payments = input_payments()
        interest_rate = calc_interest(loan_amount, num_payments)
        monthly_payments = calc_payments(loan_amount, num_payments,
                                         interest_rate)

        print()
        print("Amount of loan:", loan_amount)
        print("Number of payments:", num_payments)

        print("Monthly payments:", round(monthly_payments, 2))
        print("Interest rate: ", int(interest_rate*100), '%', sep='')
        print()

        print("Would you like enter another set of data?")
        choice = input()
        while True:
            if choice == 'y' or choice == 'Y': break
            elif choice =='n' or choice == 'N': return

if __name__ == "__main__": main()
------------------------------------------------------------------------------------------------------------------------------------
/// This program reads an input file and counts the words in it and performs various operations
#Return a list of words from file
def fileToList(file):
    #Declare a list object
wordList=[]
  
with open(file,'r') as f:
    #Read file
    data=f.read().split('\n')
    #For every line
    for line in data:
        if not len(line)==0:
            #Exclude empty lines
            #Split words that are separated by , or . or ? etc.,
            wordList=wordList+(line.replace(',',' ').replace('.',' ').replace('?',' ').replace('--',' ').split())
  
return wordList


#This function returns the average characters per word in the file
def averageCharsPerWord(wordList):
    countList=[]
    count=0
    i=0
    avg=0
#For every word in list
for word in wordList:
    count=len(word)
    #Get length of word
    countList.append(count)
    i+=1

    #Calculate average
    avg=sum(countList)/i
return avg


#Returns a dictionary with key as length of word and value as count of each length number
def wordLengthCount(wordList):
    wordDict={}
    count=0
    for word in wordList:
        count=len(word)
        #If length count is present in dict, increment value by 1
        if count in wordDict:
            # append the new number to the existing array at this slot
            wordDict[count]=wordDict[count]+1
        else:
            # create a new array in this slot
            wordDict[count]=1
    return wordDict


#Returns count of vowels in the word list
def countVowels(wordList):
    vowels=['a','e','i','o','u']
    vowelCount=0
    for word in wordList:
        for i in word:
            if i in vowels:
                vowelCount+=1

    return vowelCount
  

#Driver program
#Write to file results.txt
f = open("results.txt", "w")
#Call the function and get word list
wordList=fileToList("GBA.txt")
#Get average
avg=averageCharsPerWord(wordList)
#Write into file
f.write("Average characters per word: ")
f.write(str(avg))
f.write("\n")

wordDict=wordLengthCount(wordList)


#Iterate dict and print each word length count
for key,value in sorted(wordDict.items()):
    f.write(str(value))
    f.write(" words of length ")
    f.write(str(key))
    f.write("\n")

f.write("\nTotal number of words in input file: ")
f.write(str(len(wordList)))
f.write("\Total number of vowels in input file: ")
f.write(str(countVowels(wordList)))
f.close()


#Write to lowercase.txt
f = open("lowercase.txt", "w")
for word in wordList:
    f.write(word.lower())
    f.write(" ")
    f.close()


#Write to uppercase.txt
f = open("uppercase.txt", "w")
for word in wordList:
    f.write(word.upper())
    f.write(" ")
    f.close()
  


print("results.txt, lowercase.txt and uppercase.txt files written successfully!")
------------------------------------------------------------------------------------------------------------------------------------