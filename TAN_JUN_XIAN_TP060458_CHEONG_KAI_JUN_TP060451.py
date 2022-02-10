#TAN JUN XIAN TP060458
#CHEONG KAI JUN TP060451

variables = []      #to retrieve variables inside function
                    #list is outside function so that value isnt erased

def mainPage():
    print("=" * 50)         #display options
    print("1. Login")
    print("2. Register")
    print("3. View all cars available for rent")
    print("4. Exit")
    print()
    print("=" * 50)
    try:
        loginOption = int(input("Select your option: "))    #select option
                                                            #different option calls different functions
        if (loginOption == 1):      #1 = login      
            loginSystem()
        elif (loginOption == 2):    #2 = register
            registerOption()
        elif (loginOption == 3):    #3 = view all cars available for rent
            displayCars(0)
            mainPage()
        elif (loginOption == 4):    #4 = exit
            print("Thank you for using our car rental services!")
            pass
        else:
            print("Invalid input!")     #show error if integer input, but not within 1-4
            pause = input("Press <Enter> to continue.")
            mainPage()
    except:
        print("Invalid input!")     #show error if non-integer input is given
        pause = input("Press <Enter> to continue.")
        mainPage()
        
def loginSystem(): 
    
    memberLoginLists = []   #read member login details, put them into a list
    with open("LoginDataMember.txt") as memberLogin:
        for memberLoginDetails in memberLogin:
            memberLoginLists.append(memberLoginDetails.strip("\n").split("|")) #split list

    adminLoginLists = []    #read admin login details, put them into a list
    with open("LoginDataAdmin.txt") as adminLogin:
        for adminLoginDetails in adminLogin:
            adminLoginLists.append(adminLoginDetails.strip("\n").split("|")) #split list

    memberLoginID = [i[0] for i in memberLoginLists]    #(member) split list into ID and PW
    memberLoginPW = [i[1] for i in memberLoginLists]

    adminLoginID = [i[0] for i in adminLoginLists]      #(admin) split list into ID and PW
    adminLoginPW = [i[1] for i in adminLoginLists]
    print("=" * 50)
    print()
    print("Login Page.")
    print("Note! ID and Password are case sensitive!")
    print("=" * 50)
    loginDetailsID = str(input("Enter ID: "))
    loginDetailsIDStrip = loginDetailsID.strip()    #take out spaces between

    if loginDetailsIDStrip in adminLoginID:     #check if ID is in admin list
        loginIndex = adminLoginID.index(loginDetailsIDStrip)    #checks with position of ID to get PW
        tempLoginPW = (adminLoginPW[loginIndex])  
        loginDetailsPW = input("Enter Password: ")
        
        if loginDetailsPW == tempLoginPW:  #check if PW matches 
            variables.append(loginIndex)
            adminPage()     #goes to admin page
        else:
            print("Wrong Password!")
            pause = input("Press <Enter> to continue. ")
            loginSystem()  #wrong password recalls the function

    elif loginDetailsIDStrip in memberLoginID:  #check if ID is in member list
        loginIndex = memberLoginID.index(loginDetailsIDStrip)   #checks with position of ID to get PW
        tempLoginPW = (memberLoginPW[loginIndex])      
        loginDetailsPW = input("Enter Password: ")
        
        if loginDetailsPW == tempLoginPW:   #check if PW matches
            variables.append(loginIndex)    #gets position to display correct member details
            memberDetailsPage()
        else:
            print("Wrong Password!")
            pause = input("Press <Enter> to continue. ")
            loginSystem()  #wrong password recalls the function
    
    else:       #if it is not in admin or member, it is considered invalid
        print("Invalid ID!")
        pause = input("Press <Enter> to continue. ")
        mainPage()  #goes back to main page
   
    memberLogin.close()
    adminLogin.close()

def adminPage():

    print()
    print("=" * 50)                     #display options
    print("1. Add Cars")
    print("2. Modify car details")
    print("3. (Cars) Display all records of:")
    print("4. (Customer) Display all/specific records of: ")
    print("5. Return a rented car")
    print("6. Exit (Return to login page)")
    print("=" * 50)

    try:
        while True:
            adminOption = int(input("\nSelect your option: "))  #asking for input
            if (adminOption == 1):  #1 = add cars
                addCars()

            elif (adminOption == 2):    #2 = modify existing car details
                modifyCars(0)

            elif (adminOption == 3):    #3 = display record for cars...
                print()
                print("1. Cars rented out")     #display options (2nd)
                print("2. Cars available for rent")
                print()
                adminOption2 = int(input("Select your option: "))   #asking for 2nd input
                print("=" * 50)

                if (adminOption2 == 1):     #3.1 = ...rented out
                    displayCars(1)
                elif (adminOption2 == 2):   #3.2 = ...available for rent
                    displayCars(0)
                else:
                    print("Invalid Input")

            elif (adminOption == 4):    #4 = search for specific record of customer
                print()
                print("1. All Customer Bookings")     
                print("2. Search for specific customer bookings")
                print("3. All payment for a specific month")        
                print("4. Search for specific customer payment records")
                print()
                print("=" * 50)
                adminOption3 = int(input("Select your option: "))
                if (adminOption3 == 1):     #4.1 = ...all customer bookings
                    displayBookings(1)
                elif (adminOption3 == 2):   #4.2 = ...specific customer bookings
                    displayBookings(2)
                elif (adminOption3 == 3):   #4.3 = ...all customer payments for a specific month
                    displayPayment(1)
                elif (adminOption3 == 4):   #4.4 = ...specific customer payment records
                    displayPayment(2)
                else:
                    print("Invalid Input")
                    
            elif (adminOption == 5):    #5 = return a rented car (change status)
                modifyCars(1)

            elif (adminOption == 6):    #6 return to login page
                mainPage()
                break

            else: 
                print("Invalid input!") #show error if integer but not within 1-6
                pause = input("Press <Enter> to continue.")
    except:
        print("Invalid input!")     #show error if non-integer input is given
        pause = input("Press <Enter> to continue.")
        adminPage()



def memberDetailsPage():
    while True:
        
        memberDetailsLists = []     #read member details file
        with open('MemberDetails.txt') as memberDetailsRead:
            for memberDetailsDisplay in memberDetailsRead:
                memberDetailsLists.append(memberDetailsDisplay.strip("\n").split("|"))

        memberDetailsCount = variables[len(variables)-1]   #take variable from previous functions to determine which 'position' of data to display
        selectedMemberDetails = (memberDetailsLists[memberDetailsCount])
 
        print()
        print("Name       : ", selectedMemberDetails[0])   #display details
        print("Age        : ", selectedMemberDetails[1])
        print("Contact No.: ", selectedMemberDetails[2])
        print()
        print("=" * 50)
        print("Options: ")
        print("1. Modify details")
        print("2. View rental history")
        print("3. View available car list")
        print("4. Rental booking and payment")
        print("5. Exit (Return to login screen)")
        print()
        print("=" * 50)

        try:
            cont = int(input("Your choice: "))  #asking for input
            
            if (cont == 1):     #1 = modify details
                memberDetailsEdit()
                break
            elif (cont == 2):   #2 = view rental history
                viewRentalHistory()
            elif (cont == 3):   #3 = display car list / booking
                displayCars(0)
            elif (cont == 4):
                bookCars()
            elif (cont == 5):   #5 = go back to login screen
                mainPage()
                break
            else:
                print("Invalid input!") #show error if integer but not within 1-4
                pause = input("Press <Enter> to continue.")
                memberDetailsPage()

        except:
            print("Invalid input!")     #show error if non-integer input is given
            pause = input("Press <Enter> to continue.")
            memberDetailsPage()
            
def memberDetailsEdit():
    
    print("=" * 50)
    print("1: Name")        #display options
    print("2: Age")
    print("3: Contact No.")
    print("4: Exit")
    print("=" * 50)
    print()
    try:
        number = int(input("Select an option :"))    #asking for input

        if (number == 1):   #1 = edit name
            memberDetailsEdit2(1)
        elif (number == 2): #2 = edit age
            memberDetailsEdit2(2)
        elif (number == 3): #3 = edit contact no.
            memberDetailsEdit2(3)
        elif (number == 4): #4 = return to member details page
            memberDetailsPage()
        else:
            print("Invalid input!") #show error if integer but not within 1-4
            pause = input("Press <Enter> to continue.")
            memberDetailsEdit()
    except:
        print("Invalid input!")     #show error if non-integer input is given
        pause = input("Press <Enter> to continue.")
        memberDetailsEdit()

def memberDetailsEdit2(number):
    print("=" * 50)
    memberDetailsLists = []     #read member details file
    with open('MemberDetails.txt') as memberDetailsRead:
        for memberDetailsDisplay in memberDetailsRead:
            memberDetailsLists.append(memberDetailsDisplay.strip("\n").split("|")) #split into list

 
    memberDetailsCount = variables[len(variables)-1]   #take variable from previous function to show position
    selectedMemberDetails = (memberDetailsLists[memberDetailsCount])

    fileRead = open("MemberDetails.txt", "rt")  #open text file for reading
    memberDetails = fileRead.read()
    if (number == 1):                           #1 = edit name
            inputChange = input("New Name: ")
            memberDetails = memberDetails.replace(selectedMemberDetails[0], inputChange)    #change value within variable in python
            fileRead.close()
            fileRead = open("MemberDetails.txt", "wt")
            fileRead.write(memberDetails)                                                   #replace value within text file within variable
            fileRead.close()
            fileRead2 = open("RentalDetails.txt", "wt")
            fileRead2.write(memberDetails)
            fileRead2.close()
            print ("Your name has been changed to", inputChange)
            memberDetailsEdit()                 

    elif (number == 2):                         #2 = edit age
            inputChange = input("New Age: ")
            memberDetails = memberDetails.replace(selectedMemberDetails[1], inputChange)    #change value within variable in python
            fileRead.close()
            fileRead = open("MemberDetails.txt", "wt")
            fileRead.write(memberDetails)                                                   #replace value within text file within variable
            fileRead.close()
            print ("Your age has been changed to", inputChange)
            memberDetailsEdit()

    elif (number == 3):                           #3 = edit contact no
            inputChange = input("New Contact No.: ")
            memberDetails = memberDetails.replace(selectedMemberDetails[2], inputChange)    #change value within variable in python
            fileRead.close()
            fileRead = open("MemberDetails.txt", "wt")
            fileRead.write(memberDetails)                                                   #replace value within text file within variable
            fileRead.close()
            print ("Your contact no. has been changed to", inputChange)
            memberDetailsEdit()            
            
def viewRentalHistory():
    data = []   #read rental details file
    with open("RentalDetails.txt","r") as rentalHistory:
        for rec in rentalHistory:
            data.append(rec.strip("\n").split("|"))
    
    memberDetailsCount = variables[len(variables)-1]   #take variable from previous function to show position
    selectedMemberDetails = (data[memberDetailsCount])

    
    print("=" * 50)            
    In = (len(selectedMemberDetails) - 1)
    print("Name: ", selectedMemberDetails[0])
    print("Amount of cars rented: ", In)
    print()

    for carsRented in selectedMemberDetails:
        if (In < 1):
            print("No rental history.")
        elif (carsRented != selectedMemberDetails[0]):
            print(carsRented)

    print("=" * 50)
    
def registerOption():
    print("=" * 50)
    print("Registration page.")
    print("Note! ID and Password are case sensitive!")
    print("=" * 50)
    
    print()     #get input to be added into login data file
    insertID = input("Enter new ID: ")
    insertPW = input("Enter new Password: ")
    newLogin = ("\n" + str(insertID) + "|" + str(insertPW))     #\n for new line, | as a form of splitting data

    with open ("LoginDataMember.txt", "a") as newRegister:      #add into text file
        newRegister.write(newLogin)
    print("=" * 50)
    print()     #get input to be added into member details file
    print("Now enter your personal information. ")  
    insertName = input("Enter name: ")
    insertAge = input("Enter age: ")
    insertContact = input("Enter contact number: ")
    newDetails = ("\n" + insertName + "|" + insertAge + "|" + insertContact)    #\n for new line, | as a form of splitting data
    with open ("RentalDetails.txt", "a+") as rental:
        rental.write(str(insertName)+ "\n")

    with open ("MemberDetails.txt", "a") as newMemberDetails:   #add into text file
        newMemberDetails.write(newDetails)
        newMemberDetails.close()
    
    print("\nNew user has been added!")
    print()
    mainPage()  #go back to main page
    
def bookCars():
    print("=" * 50)
    displayCars(0)
    modifyCars(2)
    print("=" * 50)
    
def addCars():

    try:
        cd = open("carDetails.txt","a+")
        while True:
            print("=" * 50)
            model = input("Enter car model: ")                                  #take in data
            make = input("Enter car make: ")
            modelYear = int(input("Enter car model year: "))
            plateNumber = input("Enter car plate number: ")
            flag = "0"                                                          #new cars will always be available until it is rented out for the first time
            cd.write(str(model.upper())+"|"+(str(make.upper()))+"|"+(str(modelYear))+"|"+(str(plateNumber.upper()))+"|"+flag+"\n")

            cont = input("[Press <enter> to continue add another car or 'X' to exit]")
            if ((cont == "x") or (cont == "X")):                                #choose to add or exit
                break
            
        cd.close()
        adminPage()
    except:
        print("\nERROR. PLEASE MAKE SURE DATA ENTERED IS APPROPRIATE. TRY AGAIN.")
        print("="*50)
        addCars()

def modifyCars(mode):                                                                                   #mode 0 = modify car details
    if int(mode) == 0:
        print("TO MODIFY CAR DETAILS:")                                                                 #mode 1 = return cars
    elif int(mode) == 1:
        print("TO RETURN A CAR:")                                                                       #mode 2 = rent out cars
    elif int(mode) == 2:
        print("TO RENT A CAR:")
    print("-"*50)                                                                                       
    keyword = input("Enter car model: ")
    plateNumber = input("Enter plate number of the car: ")
    print("-"*50)

    check = 0
    
    memberDetailsLists = []     #read member details file
    with open('MemberDetails.txt') as memberDetailsRead:
        for memberDetailsDisplay in memberDetailsRead:
            memberDetailsLists.append(memberDetailsDisplay.strip("\n").split("|")) #split into list

    memberDetailsCount = variables[len(variables)-1]   #take variable from previous function to show position
    selectedMemberDetails = (memberDetailsLists[memberDetailsCount])

    try:
        with open("carDetails.txt", "r") as file:
            records = file.readlines()
            for record in records:
                check = check + 1
                
        with open("carDetails.txt", "w") as file:
            count = 0
            for record in records:
                field = record.split("|")
                if len(record) > 0:
                    if (plateNumber.upper() == field[3]) and (keyword.upper() == field[0]):
                        print("Car model   : ", str(field[0]))                                             #show latest version of the record
                        print("Car make    : ", str(field[1]))
                        print("Model year  : ", str(int(field[2])))
                        print("Plate number: ", str(field[3]))
                        print("-"*50)
                        if int(mode) == 0:                                                              #modify
                            newModel = input("Enter new car model: ")                                   #take in new details
                            newMake = input("Enter new car make: ")
                            newModelYear = input("Enter new model year: ")
                            newPlateNumber = input("Enter new plate number: ")
                            file.write(str(newModel.upper())+"|"+(str(newMake.upper()))+"|"+(str(newModelYear))+"|"+(str(newPlateNumber.upper()))+"|"+str(field[4]))
                            print("\nCAR DETAILS MODIFIED.")
                            print("-"*50)
                        elif int(mode) == 1:                                                            #return cars
                            if int(field[4]) == 0:                                                      #check if its returned previously
                                print("THIS CAR IS RETURNED PREVIOUSLY. YOU CAN'T RETURN IT AGAIN.")
                                print("-"*50)
                                file.write(record)
                            elif int(field[4]) == 1:                                                    #check if its rented out previously
                                cont = input("[Press <enter> to return car or 'X' to cancel]")          #confirmation
                                if ((cont == "x") or (cont == "X")):                                    #canceled
                                    file.write(record)
                                    print("\nCAR RETURNING CANCELED.")
                                    print("-"*50)
                                else:                                                                   #confirmed
                                    flag = "0"
                                    file.write((str(field[0]))+"|"+(str(field[1]))+"|"+(str(field[2]))+"|"+(str(field[3]))+"|"+str(flag)+"\n")
                                    print("\nCAR RETURNED SUCCESSFULLY.")
                                    print("-"*50)
                        elif int(mode) == 2:                                                            #rent out cars
                            if int(field[4]) == 1:                                                      #check if its rented out previously
                                print("THIS CAR IS NOT RETURNED YET. YOU CAN'T RENT IT NOW.")
                                print("-"*50)
                                file.write(record)
                            elif int(field[4]) == 0:                                                    #check if its returned previously
                                cont = input("[Press <enter> to rent car or 'X' to cancel]")            #confirmation
                                if ((cont == "x") or (cont == "X")):                                    #canceled
                                    file.write(record)
                                    print("\nCAR RENTING CANCELED.")
                                    print("-"*50)
                                else:                                                                   #confirmed
                                    import datetime as dt
                                    rentDate = input("Start Date of renting (dd/mm/yyyy): ")
                                    duration = int(input("Rent for how many days: "))
                                    startDate = dt.datetime.strptime(rentDate, "%d/%m/%Y")
                                    day = dt.timedelta(duration)
                                    endDate = startDate + day
                                    price = duration * 300
                                    pay = input("[Press <enter> to pay and confirm booking, or 'X' to cancel]")            #confirmation
                                    if ((pay == "x") or (pay == "X")):
                                        file.write(record)
                                        print("\nFAILED TO PAY, BOOKING CANCELED.")
                                        print("-"*50)
                                    else:
                                        with open("Booking.txt", "a+") as booking:
                                            booking.write((str(selectedMemberDetails[0]))+"|"+(str(field[0]))+"|"+(str(field[3]))+"|"+(str(startDate))+"|"+(str(endDate))+"\n")
                                        with open("Payment.txt", "a+") as payment:
                                            payment.write((str(selectedMemberDetails[0]))+"|"+(str(price))+"|"+(str(startDate))+"\n")
                                        with open("RentalDetails.txt", "r") as rental:
                                            r = rental.readlines()
                                        with open("RentalDetails.txt", "w") as rental:
                                            for rec in r:
                                                data = rec.split("|")
                                                if data[0] == selectedMemberDetails[0]:
                                                    rental.write((rec.strip("\n"))+"|"+(str(field[1]))+" "+(str(field[0]))+"\n")
                                                else: 
                                                    rental.write(rec)
                                        flag = "1"
                                        file.write((str(field[0]))+"|"+(str(field[1]))+"|"+(str(field[2]))+"|"+(str(field[3]))+"|"+str(flag)+"\n")
                                        print("\nCAR RENTED OUT SUCCESSFULLY.")
                                        print("-"*50)
                    else:
                        count = count + 1
                        file.write(record)
        if count == check:                                                                              #check if the record is being found in the text file or not.
            print("CAR NOT FOUND. PLEASE TRY AGAIN.")
            print("\n")
            print("="*50)
            modifyCars(mode)
    except:
        print("SOMETHING WENT WRONG, TRY AGAIN.")
        print("\n")
        print("="*50)
        modifyCars(mode)

def displayCars(availability):                          # 0 for available
                                                        # 1 for rented out
    try:                                            
        records = open("carDetails.txt","r")
        
        if (availability == 0):
            print("-"*50)
            print("CARS AVAILABLE FOR RENT")
        elif (availability == 1):
            print("-"*50)
            print("CARS RENTED OUT")
                    
        print("-"*50)
        
        for record in records:
            field = record.split("|")
            if int(field[4]) == availability:       # check for availability
                print("Car model   : ", str(field[0]))
                print("Car make    : ", str(field[1]))
                print("Model year  : ", str(int(field[2])))
                print("Plate number: ", str(field[3]))
                print()

        records.close()
    except:
        print("="*50)
        print("ERROR OCCURED. PLEASE ASK FOR TECHNICAL SUPPORT.")
        print("="*50)

def displayBookings(mode):
    try:
        records = open("Booking.txt", "r")
        import datetime as dt
        if mode == 1:       #display all booking records
            print("=" * 50)
            print("ALL BOOKINGS RECORDED: ")
            print("=" * 50)
            for record in records:  #loop through all records and print them out
                field = record.strip("\n").split("|")
                print("Member ID    : ", str(field[0]))
                print("Booked car   : ", str(field[1]) + ", " + str(field[2]))
                start = dt.datetime.strptime(field[3], "%Y-%m-%d %H:%M:%S")
                startDate = '{:%d-%m-%Y}'.format(start)
                print("Rent Out Date: ", startDate)
                end = dt.datetime.strptime(field[4], "%Y-%m-%d %H:%M:%S")
                endDate = '{:%d-%m-%Y}'.format(end)
                print("Return Date  : ", endDate)
                print()

        elif mode == 2:     #display specific booking records
            print("=" * 50)
            print("SPECIFIC CUSTOMER'S BOOKINGS: ")
            memberID = input("Enter Member ID (CASE SENSITIVE): ") #get input
            print("=" * 50)
            count = 0
            for record in records:  #loop through all records and search for records that matches with input
                field = record.strip("\n").split("|")
                if field[0] == memberID:
                    count = count + 1
                    print("Member ID    : ", str(field[0]))
                    print("Booked car   : ", str(field[1]) + ", " + str(field[2]))
                    start = dt.datetime.strptime(field[3], "%Y-%m-%d %H:%M:%S")
                    startDate = '{:%d-%m-%Y}'.format(start)
                    print("Rent Out Date: ", startDate)
                    end = dt.datetime.strptime(field[4], "%Y-%m-%d %H:%M:%S")
                    endDate = '{:%d-%m-%Y}'.format(end)
                    print("Return Date  : ", endDate)
                    print()
            if count == 0:
                print("The customer that you're looking for does not have any booking records.\nCheck again if you've entered the correct ID")
        print("=" * 50)
    except:
        print("ERROR OCCURED. PLEASE ASK FOR TECHNICAL SUPPORT.")
        print("="*50)

def displayPayment(mode):
    try:
        records = open("Payment.txt", "r")
        import datetime as dt
        if mode == 1:   #display all payment records in specific month
            try:
                month = int(input("Enter month to check for payment records (Integer in the format of XX): ")) #get input
            except:
                print("The value you entered is not according to the format or the data type required.")
            try:
                print("=" * 50)
                print("CUSTOMER PAYMENT RECORDS FOR: ", month)
                print("=" * 50)
                count = 0
                for record in records: #loop through and find records with date that matches with the input month
                    field = record.strip("\n").split("|")
                    date = field[2]
                    paydate = date.strip(" ").split("-")
                    if month == int(paydate[1]):
                        count = count + 1
                        print("Member ID    : ", str(field[0]))
                        print("Amount Paid  : " + " RM" + (str(field[1])))
                        pay = dt.datetime.strptime(field[2], "%Y-%m-%d %H:%M:%S")
                        payD = '{:%d-%m-%Y}'.format(pay)
                        print("Payment Date : ", payD)
                        print()
                if count == 0:     
                    print("No payment done on the MONTH entered.")
            except:
                print("SOMETHING WENT WRONG. TRY AGAIN.")
                
        elif mode == 2: #specifc customer's payments
            print("=" * 50)
            print("SPECIFIC CUSTOMER'S PAYMENTS: ")
            memberID = input("Enter Member ID (CASE SENSITIVE): ") #get input
            print("=" * 50)
            count = 0
            for record in records:  #loop through and find records that matches with input
                field = record.strip("\n").split("|")
                if field[0] == memberID:
                    count = count + 1
                    print("Member ID    : ", str(field[0]))
                    print("Amount Paid  : " + " RM" + (str(field[1])))
                    pay = dt.datetime.strptime(field[2], "%Y-%m-%d %H:%M:%S")
                    payD = '{:%d-%m-%Y}'.format(pay)
                    print("Payment Date : ", payD)
                    print()
            if count == 0:
                print("The customer that you're looking for does not have any payment records.\nCheck again if you've entered the correct ID")
        print("=" * 50)
    except:
        print("ERROR OCCURED. PLEASE ASK FOR TECHNICAL SUPPORT.")
        print("="*50)


mainPage()



