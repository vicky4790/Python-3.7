#My First interactive Python Code


# Greetings section
firstName = input('Please enter your first Name:')
lastName = input('Please enter your last Name:')
lastName = lastName.upper()

print('\nHey there,' + firstName + ' ' + lastName)
print('\tWelcome to Python programming!!')

def main():

    import datetime
    import turtle

    print("\nChoose any one of the below!")
    print("\n \t\t1. Area of a Triangle \n \t\t2. Loan Calculator \n \t\t3. Draw a 2D line")

    #Interative section starts
    userChoice = input("\n \tPlease enter your choice (eg. 1,2,3 etc..): ")

    userChoice = int(userChoice)
    if userChoice == 1:
        print("\t\t\t\t ------------# \t ---------------------------- \t #------------ \t\t\t\t")
        print("\t\t\t\t ############# \t Welcome to Area Calculator!! \t ############# \t\t\t\t")
        print("\t\t\t\t ------------# \t ---------------------------- \t #------------ \t\t\t\t")
        widthTriangle = input('Enter the width (in cm): ')
        heightTriangle = input('Enter the height (in cm): ')

        #Calculator logic
        try:
            areaTriangle = float(widthTriangle) * float(heightTriangle) / 2
            print("\n-----------------------------------------")
            print("Area of your Triangle is %.2f sq.cm" % areaTriangle)

        except ZeroDivisionError:
            print("The answer is infinity!")

        except:
            print('\n \t\tOops! you have entered incorrect value')

    elif userChoice == 2:
        print("\t\t\t\t ------------# \t ---------------------------- \t #------------ \t\t\t\t")
        print("\t\t\t\t ############# \t Welcome to Loan Calculator!! \t ############# \t\t\t\t")
        print("\t\t\t\t ------------# \t ---------------------------- \t #------------ \t\t\t\t")
        print("\nPlease enter the following requested details!")

        #Calculator logic
        loanAmount = input("How much do you want to borrow? : ")
        interestRate = 0.088
        print("Interest rate for this loan is %.3f" % interestRate)
        numberOfPayments = input("Please provide the number of months for repayment: ")

        try:
            monthlyPayment = float(loanAmount) * (interestRate * (1 + interestRate) * int(numberOfPayments)) / ((1 + interestRate) * int(numberOfPayments) - 1)
            print("\n-----------------------------------------")
            print('\tMonthly EMI to be paid is %.2f' % monthlyPayment)
            print("-----------------------------------------")

        except ZeroDivisionError:
            print("The answer is infinity!")

        except:
            print('\n \t\tOops! you have entered incorrect value')

    elif userChoice == 3:
        counter = input("Enter the start value: ")
        counter = int(counter)
        upperLimit = input("Enter the upper limit: ")
        upperLimit = int(upperLimit)
        try:
            while counter < upperLimit:
                turtle.forward(1)
                turtle.right(1)
                counter = counter + 1
        except:
            print('\n \t\tOops! you have entered incorrect value')

    else:
        print('\n \tPlease enter a valid choice!')

    print('\n\n\n')
    print(datetime.date.today())

    rerun = input("Do you want to continue? (yes/no):")
    if rerun.upper() == "YES":
        main()
    else:
        print("Thank you for using this software " + firstName + ' ' + lastName)
        exit()


main()


