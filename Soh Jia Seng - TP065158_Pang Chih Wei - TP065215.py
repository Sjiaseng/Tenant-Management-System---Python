#Pang Chih Wei - TP065215
#Soh Jia Seng - Tp065158

import datetime

def start():
    print("     Welcome to Tenant management system     ")
    print("\n \n             ......... Loading System ........       ")
    # Check if the 6 text file is available, if yes continue to login, if no shut down
    try:
        file1 = open("user.txt", "r")
        file2 = open("tenant.txt", "r")
        file3 = open("property.txt", "r")
        file4 = open("userlog.txt", "r")
        file5 = open("historytenant.txt","r")
        file6 = open("historyproperty.txt","r")
    except:
        print('\n Error: Missing file user.txt, tenant.txt, property.txt, userlog.txt, historytenant.txt, historyproperty.txt\n \n System shut down\n')
        exit()

    file1.close()
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    file6.close()

    start_time = datetime.datetime.now()
    print("\n \nSystem start at: ", start_time.strftime("%c"))
    print("\n \nAdmin Login")


def login():
    success = False
    userfile = open("user.txt", "r")
    Username = input("\nEnter Username: \n")
    Password = input("\nEnter Password: \n")

    # split the text (Username and password) by "|"
    for i in userfile:
        a, b = i.split("|")
        b = b.strip()
        # Check if the username and password same or not, if yes pass and append date at log file, else
        if (a == Username and b == Password):
            success = True
            break
    userfile.close()
    if (success):
        print("\nDone Login\n")
        with open("userlog.txt", "a") as file:
            file.write("Username:")
            file.write(Username)
            file.write("\n")
            file.write("Start Execution Time: ")
            file.write(str(datetime.datetime.now()))
            file.write("\n")
    else:
        print("\nUsername or Password incorrect, Please try again\n")
        login()



##################################################     Settings Start     ##################################################
def delete_user():
    try:
        # open property file as read mode
        with open("user.txt", "r") as file1:
            count = 0
            # showing data in multiple arrays
            for lines in file1:
                # numbering of data after each loop
                count += 1
                print(count, ".", [lines.split("|")[0]])

        with open("user.txt", "r") as file2:
            line = file2.readlines()
            # getting line numbers from users to delete
            try:
                choose = int(input("Enter line to delete:"))
                index = choose - 1
                # deleting a line based on an index
                del line[index]

            except Exception:
                print("Only integers are accepted!")
                settings()

        # rewriting the data which are not deleted
        with open("user.txt", "w") as file3:
            for attribute in line:
                file3.write(attribute)
        print("\n Admin has be deleted successfully\n")
        settings()
    except Exception:
        print("Something went wrong! Please try again!")
        settings()


# Settings Change Password
def Change_Password():
    username = []
    password = []

    try:
        with open("user.txt", "r") as file:
            for i in file:
                a, b = i.split('|')
                username.append(a.strip())
                password.append(b.strip())

            old_password = input("Enter your old password: ")
            if old_password not in password:
                print("Password incorrect!")
                print("Do you want to continue?")
                print("1. Yes")
                print("2. No")
                option = input("Enter your option: ")
                if option == "1":
                    Change_Password()
                elif option == "2":
                    menu()
                else:
                    print("\nInvalid input please try again!\n")
                    Change_Password()

            new_password = input("Enter your new password: ")
            if len(new_password) <= 6:
                print("\nPassword too short, try again\n")
                Change_Password()
            elif (new_password.isalnum()):
                print("\nMust contain data !@%^&*+=-_\/?<>,. \n")
                return Change_Password()
            elif (new_password.isupper()):
                print("\nMust contain upper and lower\n")
                return Change_Password()
            elif (new_password.islower()):
                print("\nMust contain upper and lower\n")
                return Change_Password()
            elif new_password in password:
                print("\nPassword already exist, try again\n")
                Change_Password()

            confirm_password = input("\nReenter your password: ")

            if new_password != confirm_password:
                print("\nPassword incorrect!\n")
                Change_Password()

            index = password.index(old_password)
            password[index] = new_password

            with open("user.txt", "w") as file2:
                for index in range(len(username)):
                    file2.write(str(username[index]) + "|" + str(password[index]) + "\n")
                print("\nProcess Success!\n")
            modifyadminuser()

    except Exception:
        print("\nSomething wrong! Please try again!\n")
        Change_Password()


# Settings Change Username
def Change_Username():
    username = []
    password = []
    try:
        with open("user.txt", "r") as file:
            for i in file:
                a, b = i.split('|')
                username.append(a)
                password.append(b)

            old_username = input("Enter your old username: ")
            if old_username not in username:
                print("\nUsername Name not Found!\n")
                print("\nDo you want to continue?\n")
                print("1. Yes\n", "2. No")

                option = input("Enter your option: ")
                if option == "1":
                    Change_Username()
                elif option == "2":
                    menu()
                else:
                    print("\nInvalid input please try again!\n")
                    Change_Username()

            new_username = input("Enter your new username: ")
            if new_username in username:
                print("\nUsername is taken by another user! Please try again!\n")
                Change_Username()

            index = username.index(old_username)

            username[index] = new_username

        with open("user.txt", "w") as file2:
            for index in range(len(username)):
                file2.write(str(username[index]) + "|" + str(password[index]))
        print("\nUsername change success\n")
        modifyadminuser()
    except Exception:
        print("\nSomething wrong! Please try again!\n")
        Change_Username()

# Settings Register
def register():
    userfile = open("user.txt", "r")
    u = []  # Empty variable to store username
    p = []  # Empty variable to store password
    # match up the username and password
    for i in userfile:
        # split the text (Username and password) by "|"
        a, b = i.split("|")
        b = b.strip()
        # append username
        u.append(a)
        # append password
        p.append(b)

    Username = input("\nCreate Username: \n")
    # check if username exists
    if Username in u:
        print("\nError: Username exists\n")
        register()
    # check if username has data or not
    elif len(Username) < 2:
        print("\nError: Username too short\n")
        register()

    Password = input("\nCreate Password: \n")
    PasswordC = input("\nConfirm password: \n")

    # double check the password is match to above or not, confirm password again
    if Password != PasswordC:
        print("\nPassword don't match, try again\n")
        register()
    # Make sure password is not lower than 6, must more than 6
    elif len(Password) <= 6:
        print("\nPassword too short, try again\n")
        register()
    # Make sure password has alphabet and numeric in the password
    elif (Password.isalnum()):
        print("Must contain (!@%^&*+=-_\/?<>,.) in password ")
        register()
    # Make sure password has lower
    elif (Password.isupper()):
        print("Must contain upper and lower")
        register()
    # Make sure password has upper
    elif (Password.islower()):
        print("Musto\ contain upper and lower")
        register()
    elif Password in p:
        print("\nError: Password already exists\n")
        register()

    # if all condition is okay, then open the text file and append the data into it, split by "|" and make it next row
    else:
        userfile = open("user.txt", "a")
        userfile.write(Username + "|" + Password + "\n")
        userfile.close()
        print("\nUser added successfully, Changes will be make at next start !\n")

    option = input("Add more (a), Exit (e):, End Process and restart (end): \n\n")
    if option == "a":
        register()
    elif option == "e":
        settings()
    elif option == "end":
        print("\n \nSystem Process to ShutDown.... Please Wait")
        print("\n \nDone Shutdown, Bye~\n \n")
    else:
        print("\nInvalid Option\n")
        return True


# Settings Modify menu
def modifyadminuser():
    print("\n \n[1]. Change Admin Username")
    print("[2]. Change Admin Password")
    print("[3]. Back\n \n")

    option = input("Enter your option: ")

    if option == "1":
        Change_Username()
    elif option == "2":
        Change_Password()
    elif option == "3":
        settings()
    else:
        print("\n \nInvalid Option")
        modifyadminuser()


# View user log
def userlog():
    # open userlog file and print it
    f = open("userlog.txt", "r")
    print(f.read())
    settings()


###Settings Function###
def settings():
    print("\n \n[1]. Add Admin")
    print("[2]. Modify Admin")
    print("[3]. Delete Admin")
    print("[4]. View User log")
    print("[5]. Back\n \n")

    option = input("Enter your option: ")
    if option == "1":
        register()
    elif option == "2":
        modifyadminuser()
    elif option == "3":
        delete_user()
    elif option == "4":
        userlog()
    elif option == "5":
        menu()
    else:
        print("\n \nInvalid Option")
        settings()


##################################################     Settings End     ##################################################


##################################################     Search Start     ##################################################


# getting input from user for further action after searching
def search_menu():
    print("Do you want to continue?")
    print("a. Continue searching data in tenant.txt.")
    print("b. Continue searching data in property.txt.")
    print("c. Continue searching on both files.")
    print("d. Exit")
    # making decision based on user's input
    options = input("Enter your option:")
    if options == "a":
        search_tenant()
        search_menu()
    elif options == "b":
        search_property()
        search_menu()
    elif options == "c":
        search_both()
        search_menu()
    elif options == "d":
        print("Heading back to searching menu...")
        search_data_menu()
    else:
        print("Invalid Input")
        search_menu()


# function of searching tenant.txt only
def search_tenant():
    # array contains elements to be used as numbering on data
    info_of_data = ["Name", "Age", "Email", "Phone", "IC Number", "Birthday", "City", "Address", "Postcode",
                    "Nationality", "Job",
                    "Employer Name", "Salary", "Property Assigned", "Property Rent Amount (Paid)", "Check in Date"]
    # array to detect if the information exist in tenant.txt file
    searched_data = []
    # index used to input numbering to data
    index = -1

    try:
        with open("tenant.txt", "r") as file:
            keyword = input("Enter searching keyword:" + "\n")
            for line in file:
                # determine is the keyword to search in the line of tenant.txt or not
                if keyword.lower() in line.lower():
                    # separate data into elements
                    seperate = line.replace("|", ",")
                    print("---------------------------------------------")
                    for i in seperate.split(","):
                        index += 1
                        # making numbering of elements compatible to the data output
                        if index > 14:
                            index = -1
                        print(info_of_data[index], ":", i)
                        # append data into a list to determine is data in output
                        searched_data.append(i)
                        continue
            # searching if the list is empty, then no data is found and vice versa
            if searched_data == []:
                print("Data Not Found!")

    except Exception:
        print("Something wrong!")


# function for searching data in property.txt
def search_property():
    # array contains elements to be used as numbering on data
    info_of_data = ["Property Name", "Property City", "Property Address", "Property Postcode",
                    "Property Acquisition Date", "Property Acquisition Price(RM)",
                    "Property Suggested Rent Amount", "Property Square Foot"]
    # array to detect if the information exist in tenant.txt file
    searched_data = []
    # index used to input numbering to data
    index = -1

    try:
        with open("property.txt", "r") as file:
            keyword = input("Enter searching keyword:")

            for line in file:
                # determine is the keyword to search in the line of property.txt or not
                if keyword.lower() in line.lower():
                    # separate data into elements
                    seperate = line.replace("|", ",")
                    print("---------------------------------------------")
                    for i in seperate.split(","):
                        index += 1
                        # making numbering of elements compatible to the data output
                        if index > 6:
                            index = -1
                        print(info_of_data[index], ":", i)
                        searched_data.append(i)
                        continue
            # searching if the list is empty, then no data is found and vice versa
            if searched_data == []:
                print("Data Not Found!")

    except Exception:
        print("Something wrong!")


# searching data on both tenant.txt and property.txt
# combination of both function in searching data in tenant.txt and property.txt
def search_both():
    info_of_data1 = ["Name", "Age", "Email", "Phone", "IC Number", "Birthday", "City", "Address", "Postcode",
                     "Nationality", "Job",
                     "Employer Name", "Salary", "Property Assigned", "Property Rent Amount (Paid)", "Check in Date"]
    searched_data1 = []

    index = -1
    try:
        with open("tenant.txt", "r") as file:
            keyword = input("Enter searching keyword:" + "\n")
            for line in file:
                if keyword.lower() in line.lower():
                    seperate = line.replace("|", ",")
                    print("From tenant.txt:")
                    print("---------------------------------------------")
                    for i in seperate.split(","):
                        index += 1
                        if index > 14:
                            index = -1
                        print(info_of_data1[index], ":", i)
                        searched_data1.append(i)
                        continue

            if searched_data1 == []:
                print("\nData not found in tenant.txt!\n")

        info_of_data2 = ["Property Name", "Property City", "Property Address", "Property Postcode",
                         "Property Acquisition Date", "Property Acquisition Price(RM)",
                         "Property Suggested Rent Amount", "Property Square Foot"]
        searched_data2 = []
        index = -1
        with open("property.txt", "r") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    seperate = line.replace("|", ",")
                    print("From property.txt")
                    print("---------------------------------------------")
                    for i in seperate.split(","):
                        index += 1
                        if index > 6:
                            index = -1
                        print(info_of_data2[index], ":", i)
                        searched_data2.append(i)
                        continue

            if searched_data2 == []:
                print("\nData not found in property.txt!\n")

    except Exception:
        print("Something went wrong! Please try again.")
        search_both()


# menu of searching data
def search_data_menu():
    print("\nSearching data in files.")
    print("1. Tenant")
    print("2. Property")
    print("3. Both")
    print("4. Back\n")
    # getting input from users
    choice = input("Enter your choice:")
    # making decision based on user input
    if choice == "1":
        search_tenant()
        search_menu()
    elif choice == "2":
        search_property()
        search_menu()
    elif choice == "3":
        search_both()
        search_menu()
    elif choice == "4":
        menu()
    else:
        print("Invalid Input! Try again.")
        search_data_menu()


##################################################     Search End     ##################################################


##################################################     Tenant Start     ##################################################

# Tenant name valid function
def tenant_name_valid():
    name = input("Enter name: ")
    # Valid name that contain character A to Z or a to z or space. Others cannot be accepted
    if not (("A" <= name and name <= "Z") or ("a" <= name and name <= "z") or (name == " ")):
        print("\nError : Name cannot contain integer or other symbol\n")
        tenant_name_valid()
    # Valid the name must more than two character
    elif len(name) < 3:
        print("\nError: Name too short\n")
        tenant_name_valid()
        # If all accept, append data
    else:
        with open("tenant.txt", "a") as file:
            file.write(name + "|")
            file.close()


# Tenant age valid function
def tenant_age_valid():
    age = input("Enter age: ")
    # Only numeric is accepted
    if not age.isnumeric():
        print("\nError: Only accept numeric data\n")
        tenant_age_valid()
    elif int(age) < 17:
        print("\nError: Tenant illegal age\n")
        tenant_age_valid()
    elif len(age) > 2:
        print("\n Error: Invalid Age\n")
        tenant_age_valid()
    else:
        with open("tenant.txt", "a") as file:
            file.write(age + "|")
            file.close()

# Tenant Email valid function
def tenant_email_valid():
    email = input("Enter Email (example@domain.com): ")
    # Valid if the input contain @
    if not "@" in email:
        print("\nError: Must include @ in data\n")
        tenant_email_valid()
    # Valid if the input contain .
    elif not "." in email:
        print("\nError: Must include . in data\n")
        tenant_email_valid()
    elif len(email) < 5:
        print("\n Error: Email to short\n")
        tenant_email_valid()
    else:
        with open("tenant.txt", "a") as file:
            file.write(email + "|")
            file.close()


# Tenant phone valid function
def tenant_phone_valid():
    phone = input("Enter Phone (60123456678): ")
    # Must contain numeric
    if not phone.isnumeric():
        print("\nError: Only accept numeric data\n")
        tenant_phone_valid()
    # Must not less than 11 character
    elif len(str(phone)) < 11:
        print("\nError: Phone Number too short\n")
        tenant_phone_valid()
    # Must not more than 11 character
    elif len(str(phone)) > 11:
        print("\nError: Phone number too long\n")
        tenant_phone_valid()
    else:
        with open("tenant.txt", "a") as file:
            file.write(phone + "|")
            file.close()


# Tenant ic number valid function (ICN)= Identity card number
def tenant_icn_valid():
    icn = input("Enter Identity Card Number (xxxxxxxxxxxx)12: ")
    tenantfile = open("tenant.txt", "r")
    lines = tenantfile.readlines()
    result = []
    # get data from column nub 4 and check if the input is duplicated or not
    for x in lines:
        result.append(x.split("|")[4])
        # Must contain numeric
    if not icn.isnumeric():
        print("\nError: Only accept numeric data\n")
        tenant_icn_valid()
        # Must not less than 12 character
    elif len(str(icn)) < 12:
        print("\nError: IC Number too short\n")
        tenant_icn_valid()
        # Must not more than 12 character
    elif len(str(icn)) > 12:
        print("\nError: IC Number too long\n")
        tenant_icn_valid()
        # if no ducplicate with data from input, then append it
    elif not icn in result:
        with open("tenant.txt", "a") as file:
            file.write(icn + "|")
            file.close()
    else:
        print("Error: The IC Number is duplicated")
        tenant_icn_valid()


# Tenant birth day valid function
def tenant_b_date_valid():
    b_date = input("Enter Birth Day Date (dd/mm/yyyy): ")
    # Check if the date is valid or not
    try:
        day, month, year = b_date.split('/')
        datetime.datetime(int(year), int(month), int(day))
        with open("tenant.txt", "a") as file:
            file.write(b_date + "|")
            file.close()
    except Exception as e:
        print("\nError: Invalid date format, it should be 'dd/mm/yy. Please try again\n")
        tenant_b_date_valid()


# Tenant birth city valid function
def tenant_b_city_valid():
    b_city = input("Enter Birth City: ")
    # Valid name that contain character A to Z or a to z or space. Others cannot be accepted

    if not (("A" <= b_city and b_city <= "Z") or ("a" <= b_city and b_city <= "z") or (b_city == " ")):
        print("\nError : City name cannot contain integer or others sysmbol\n")
        tenant_b_city_valid()
        # make sure city is more than 2 character
    elif len(b_city) < 2:
        print("\nError: City Name too short\n")
        tenant_b_city_valid()
    else:
        with open("tenant.txt", "a") as file:
            file.write(b_city + "|")
            file.close()


# Tenant birth address valid function
def tenant_b_address_valid():
    b_address = input("Enter Birth Address: ")
    # make sure address is more than 5 character
    if "," in b_address:
        print("\nError : Address does not correct, do not include (,) \n")
        tenant_b_address_valid()
    elif len(b_address) < 5:
        print("\nError: Address Name too short\n")
        tenant_b_address_valid()
    else:
        with open("tenant.txt", "a") as file:
            file.write(b_address + "|")
            file.close()


# Tenant birth postcode valid function
def tenant_b_postcode_valid():
    b_postcode = input("Enter Birth Postcode (xxxxx): ")
    # Make sure postcode is numeric
    if not b_postcode.isnumeric():
        print("\nError: Only accept numeric data\n")
        tenant_b_postcode_valid()
    # Lenght not less than 5
    elif len(str(b_postcode)) < 5:
        print("\nError: Postcode too short\n")
        tenant_b_postcode_valid()
    # Lenght not more than 5
    elif len(str(b_postcode)) > 5:
        print("\nError: Postcode too long\n")
        tenant_b_postcode_valid()
    else:
        with open("tenant.txt", "a") as file:
            file.write(b_postcode + "|")
            file.close()


# Tenant birth nationality valid function
def tenant_b_nation_valid():
    b_nation = input("Enter Nationality: ")
    # Valid name that contain character A to Z or a to z or space. Others cannot be accepted
    if not (("A" <= b_nation and b_nation <= "Z") or ("a" <= b_nation and b_nation <= "z") or (b_nation == " ")):
        print("\nError : Nationality cannot contain integer or others symbol\n")
        tenant_b_nation_valid()
            # length must more than 2
    elif len(b_nation) < 2:
        print("\nError: Nation Name too short\n")
        tenant_b_nation_valid()
    else:
        with open("tenant.txt", "a") as file:
            file.write(b_nation + "|")
            file.close()


# Tenant jobs valid function
def tenant_jobs_valid():
    jobs = input("Enter Tenant Jobs: ")
    # Valid name that contain character A to Z or a to z or space. Others cannot be accepted
    if not (("A" <= jobs and jobs <= "Z") or ("a" <= jobs and jobs <= "z") or (jobs == " ")):
        print("\nError : Jobs name cannot contain integer or others symbol\n")
        tenant_jobs_valid()
        # length must more than 2
    elif len(jobs) < 3:
        print("\nError: Jobs Name too short\n")
        tenant_jobs_valid()
    else:
        with open("tenant.txt", "a") as file:
            file.write(jobs + "|")
            file.close()


# Tenant employer valid function
def tenant_employer_valid():
    employer = input("Enter Tenant Employer Name: ")
    # Valid name that contain character A to Z or a to z or space. Others cannot be accepted
    if not (("A" <= employer and employer <= "Z") or ("a" <= employer and employer <= "z") or (employer == " ")):
        print("\nError : Employer name cannot contain integer or others symbol\n")
        tenant_employer_valid()
        # length must more than 2
    elif len(employer) < 3:
        print("\nError: Name too short\n")
        tenant_employer_valid()
    else:
        with open("tenant.txt", "a") as file:
            file.write(employer + "|")
            file.close()


# Tenant salary valid function
def tenant_salary_valid():
    salary = input("Enter Tenant Salary Amount/month RM (xxx): ")
    # Only numeric is acceptable
    if not salary.isnumeric():
        print("\nError: Only accept numeric data\n")
        tenant_salary_valid()
    # Length must more than 1, which need to be 10 and above
    elif len(str(salary)) < 3:
        print("\nAlert: This tenant too poor, not suggest to rent\n")
        tenant_salary_valid()
    else:
        with open("tenant.txt", "a") as file:
            file.write(salary + "|")
            file.close()


# Tenant property assign to tenant valid function
def tenant_property_assign_valid():
    propertyfile = open("property.txt", "r")
    # Open property text file, read all 0 column
    lines = propertyfile.readlines()
    result = []
    result2 = []
    for x in lines:
        result.append(x.split("|")[0])
        result2.append(x.split("|")[6])
        # print all data at 0 column and column 6
    print("All Property Name: ", result)
    print("Suggested rent amount: ", result2)
    propertyname = input("\nEnter Property: ")
    # check if data in 0 column same with input or no, if same append data, else get error and return
    if propertyname in result:
        with open("tenant.txt", "a") as file:
            file.write(propertyname + "|")
            file.close()
    else:
        print("\nError: Property name is not found, please choose the list below\n")
        tenant_property_assign_valid()


# Tenant rent amount, total price that tenant paid
# rntamt = Rent amount
def tenant_property_rent_amount_valid():
    rntamt = input("Enter Tenant rent amount/month (Paid): ")
    if not rntamt.isnumeric():
        print("\nError: Only accept numeric data\n")
        tenant_property_rent_amount_valid()
    # Length must more than 1, which need to be 10 and above
    elif len(str(rntamt)) < 3:
        print("\nAlert: Invalid rent amount\n")
        tenant_property_rent_amount_valid()
    else:
        with open("tenant.txt", "a") as file:
            file.write(rntamt + "|")
            file.close()


# Tenant check in date valid function
def tenant_checkin_date_valid():
    checkin_date = input("Enter Check-in Date (dd/mm/yyyy): ")
    # Check if the date is valid or not
    try:
        day, month, year = checkin_date.split('/')  # input split by /
        datetime.datetime(int(year), int(month), int(day))  # input must be int and according day month year
        # if data valid, append data, else get error and return
        with open("tenant.txt", "a") as file:
            file.write(checkin_date + "\n")
            file.close()
    except Exception as e:
        print("\nError: Invalid date format, it should be dd/mm/yy. Please try again\n")
        tenant_checkin_date_valid()


# Add Tenant Function
def add_new_tenant():
    file = open("property.txt", "r")
    read = file.readline(1)
    if read == "":
        print("\nError: Empty data in property\n")
        option = input("(a)Add property data. (e)To exit: ")
        if option == "a":
            add_new_property()
        elif option == "e":
            tenant()
        else:
            print("\nInvalid Option\n")
            add_new_tenant()
    else:
        tenant_name_valid()
        tenant_age_valid()
        tenant_email_valid()
        tenant_phone_valid()
        tenant_icn_valid()
        tenant_b_date_valid()
        tenant_b_city_valid()
        tenant_b_address_valid()
        tenant_b_postcode_valid()
        tenant_b_nation_valid()
        tenant_jobs_valid()
        tenant_employer_valid()
        tenant_salary_valid()
        tenant_property_assign_valid()
        tenant_property_rent_amount_valid()
        tenant_checkin_date_valid()
        print("\nTenant Added Successfully\n")
        option = input("(a)Add more or (e)Exit: ")
        if option == "a":
            add_new_tenant()
        elif option == "e":
            tenant()
        else:
            print("\nOption Invalid\n")
            tenant()


# function of reading tenant.txt
def read_tenant():
    # numbering for data in tenant.txt
    numbering = ["Name", "Age", "Email", "Phone", "IC Number", "Birthday", "City", "Address", "Postcode",
                 "Nationality", "Job",
                 "Employer Name", "Salary", "Property Assigned", "Property Rent Amount (Paid)", "Check in Date"]
    index = -1
    try:
        with open("tenant.txt", "r") as file:
            for line in file:
                # changing "|" symbol into ","
                seperate = line.replace("|", ",")
                print("---------------------------------------------")
                # spliting the data into an element
                for i in seperate.split(","):
                    # counting of numbering
                    index += 1
                    # return as -1 to match up with numbering on a new line
                    if index > 14:
                        index = -1
                    # printing all data with numbering
                    print(numbering[index], ":", i)
        tenant()
    except Exception:
        print("Something went wrong please try again!")
        read_tenant()

# reading history file
def read_history_tenant():
    # numbering for data in tenant.txt
    numbering = ["Name", "Age", "Email", "Phone", "IC Number", "Birthday", "City", "Address", "Postcode",
                 "Nationality", "Job",
                 "Employer Name", "Salary", "Property Assigned", "Property Rent Amount (Paid)", "Check in Date"]
    index = -1
    try:
        with open("historytenant.txt", "r") as file:
            for line in file:
                # changing "|" symbol into ","
                seperate = line.replace("|", ",")
                print("---------------------------------------------")
                # spliting the data into an element
                for i in seperate.split(","):
                    # counting of numbering
                    index += 1
                    # return as -1 to match up with numbering on a new line
                    if index > 14:
                        index = -1
                    # printing all data with numbering
                    print(numbering[index], ":", i)
        tenant()
    except Exception:
        print("Something went wrong please try again!")
        read_history_tenant()

# Modify Tenant
def modify_tenant():
    print("Modifying tenant.txt")
    print("1. Replacing all info with a keyword")
    print("2. Updating whole line")
    print("3. Back")
    # getting input from user
    opt1 = input("Enter an option: ")
    # making decision based on input
    if opt1 == "1":
        try:
            # reading tenant.txt
            with open("tenant.txt", "r") as file:
                count = 0
                # printing every line in tenant.txt in list with numbering
                for lines in file:
                    count += 1
                    print(count, ".", [lines.rstrip()])

            with open("tenant.txt", "r") as file:
                data = file.read()
                # getting input from user
                oldtext = input("Text to change: ")
                newtext = input("Text to insert: ")
                # replacing the data provide by user
                data = data.replace(oldtext, newtext)

            with open("tenant.txt", "w") as file:
                # rewriting the data after modify
                file.write(data)
            # alert users after the update is done
            print("\nDone update!")
            modify_tenant()

        except Exception:
            print("Something went wrong! Please try again!")
            modify_tenant()

    elif opt1 == "2":
        delete_tenant_modify()
        add_new_tenant()

    # back to modify data menu
    elif opt1 == "3":
        tenant()
    # reload program if errors are detected
    else:
        print("Invalid input please try again!")
        modify_tenant()

def delete_tenant_modify():
    try:
        # open tenant file as read mode
        with open("tenant.txt", "r") as file1:
            count=0
            # showing the data in multiple arrays
            for lines in file1:
                # numbering of data after each loop
                count += 1
                print(count,".",[lines.rstrip()])
        # open tenant file in lines
        with open("tenant.txt", "r") as file2:
            line = file2.readlines()
            # getting line numbers from users to delete
            try:
                choose = int(input("Enter line to execute:"))
                index = choose - 1
                # deleting a line based on an index
                del line[index]

            except Exception:
                print("Only integers are accepted!")
                modify_tenant()

        # rewriting the data which are not deleted
        with open("tenant.txt", "w") as file3:
            for attribute in line:
                file3.write(attribute)

    except Exception:
        print("Something went wrong! Please try again!")
        modify_tenant()


# Tenant Delete function
def delete_tenant():
    try:
        # open tenant file as read mode
        with open("tenant.txt", "r") as file1:
            count=0
            # showing the data in multiple arrays
            for lines in file1:
                # numbering of data after each loop
                count += 1
                print(count,".",[lines.rstrip()])
        # open tenant file in lines
        with open("tenant.txt", "r") as file2:
            line = file2.readlines()
            # getting line numbers from users to delete
            try:
                choose = int(input("Enter line to delete:"))
                index = choose - 1
                # inserting deleted info into history file
                with open("historytenant.txt", "a") as historyfile:
                    historyfile.write(line[index])
                # deleting a line based on an index
                del line[index]

            except Exception:
                print("Only integers are accepted!")
                tenant()

        # rewriting the data which are not deleted
        with open("tenant.txt", "w") as file3:
            for attribute in line:
                file3.write(attribute)
        print("Success")
        tenant()
    except Exception:
        print("Something went wrong! Please try again!")
        tenant()

def request():
    print("Do you want to continue?")
    print("a. Continue deleting data")
    print("b. Exit")
    option1 = input("Enter your option:")
    if option1 == "a":
        delete_tenant()
    elif option1 == "b":
        tenant()
    else:
        print("\nInvalid Input\n")
        request()


# Tenant Menu
def tenant():
    print("\n \n[1]. View All Tenant")
    print("[2]. Add New Tenant")
    print("[3]. Modify Tenant")
    print("[4]. Delete Tenant")
    print("[5]. View History Tenant")
    print("[6]. Back\n \n")

    option = input("Enter your option: ")
    if option == "1":
        read_tenant()
    elif option == "2":
        add_new_tenant()
    elif option == "3":
        modify_tenant()
    elif option == "4":
        delete_tenant()
    elif option == "5":
        read_history_tenant()
    elif option =="6":
        menu()
    else:
        print("\nInvalid Option\n")
        tenant()


##################################################     Tenant End     ##################################################


##################################################     Property Start     ##################################################


# Property Name valid function
def property_name_valid():
    # Open property file
    propertyfile = open("property.txt", "r")
    lines = propertyfile.readlines()
    # Read data from column 0
    result = []
    for x in lines:
        result.append(x.split("|")[0])
    # Print all data from column 0 to let user know the data is exsit
    print("All Property Name: ", result)
    propertyname = input("\nEnter Property Name: ")
    # if data input not same with data in column 0, append data, else get error and return
    if len(propertyname) < 3:
        print("\nError: Name too short\n")
        add_new_property()
    elif not propertyname in result:
        with open("property.txt", "a") as file:
            file.write(propertyname + "|")
            file.close()
    else:
        print("\nError: Property name is duplicated")
        print(result)
        add_new_property()


# Property city valid function
def property_city_valid():
    p_city = input("Enter City: ")
    # Valid name that contain character A to Z or a to z or space. Others cannot be accepted
    if not (("A" <= p_city and p_city <= "Z") or ("a" <= p_city and p_city <= "z") or (p_city == " ")):
        print("\nError : Name cannot contain integer or others symbol\n")
        property_city_valid()
        # check if the input is more than 2 character or not
    elif len(p_city) < 2:
        print("\nError: City Name too short\n")
        property_city_valid()
    else:
        with open("property.txt", "a") as file:
            file.write(p_city + "|")
            file.close()


# Property Address valid function
def property_address_valid():
    p_address = input("Enter Address: ")
    # check if the input is more than 5 character
    if "," in p_address:
        print("\nError : Address does not correct, do not include (,) \n")
        property_address_valid()
    elif len(p_address) < 5:
        print("\nError: Address Name too short\n")
        property_address_valid()
    else:
        with open("property.txt", "a") as file:
            file.write(p_address + "|")
            file.close()


# Property postcode valid function
def property_postcode_valid():
    p_postcode = input("Enter Postcode (xxxxx): ")
    # Check if input is numeric, get error if no
    if not p_postcode.isnumeric():
        print("\nError: Only can contain numeric\n")
        property_postcode_valid()
    # Check if input less than 5
    elif len(str(p_postcode)) < 5:
        print("\nError: Postcode too short\n")
        property_postcode_valid()
        # Check if input more than 5
    elif len(str(p_postcode)) > 5:
        print("\nError: Postcode too long\n")
        property_postcode_valid()
    else:
        with open("property.txt", "a") as file:
            file.write(p_postcode + "|")
            file.close()


# Property acquisition date valid function
def property_acquisition_date_valid():
    p_date = input("Enter Acquisition Date(dd/mm/yyyy): ")
    # Check if the date is valid or not
    try:
        day, month, year = p_date.split('/')
        datetime.datetime(int(year), int(month), int(day))
        with open("property.txt", "a") as file:
            file.write(p_date + "|")
            file.close()
    except Exception as e:
        print("\nError: Invalid date format, it should be 'dd/mm/yy. Please try again\n")
        property_acquisition_date_valid()


def property_acquisition_price_valid():
    p_price = input("Enter Acquisition Price(RM xxxx): ")
    # length must be more than 1
    if len(str(p_price)) < 4:
        print("\nAlert: impossible amount\n")
        property_acquisition_price_valid()
    # Only numeric is acceptable
    elif not p_price.isnumeric():
        print("\nError: Only accept numeric data\n")
        property_acquisition_price_valid()
    else:
        with open("property.txt", "a") as file:
            file.write(p_price + "|")
            file.close()


def property_sqft_valid():
    sqft = input("Enter Square Foot (xxx sqft): ")
    # Only numeric is acceptable
    if not sqft.isnumeric():
        print("\nError: Only accept numeric data\n")
        property_sqft_valid()
    elif len(str(sqft)) < 1:
        print("\nError: Invalid Square Foot\n")
        property_sqft_valid()
    else:
        with open("property.txt", "a") as file:
            file.write(sqft + "\n")
            file.close()


def property_rntamt_valid():
    rntamt = input("Enter Suggested Rent Amount/month(RM xxx): ")
    # length must be more than 1
    if len(str(rntamt)) < 3:
        print("\nAlert: This tenant too poor, not suggest to rent\n")
        property_rntamt_valid()
    # Only numeric is acceptable
    elif not rntamt.isnumeric():
        print("\nError: Only accept numeric data\n")
        property_rntamt_valid()
    else:
        with open("property.txt", "a") as file:
            file.write(rntamt + "|")
            file.close()


# Add property function
def add_new_property():
    property_name_valid()
    property_city_valid()
    property_address_valid()
    property_postcode_valid()
    property_acquisition_date_valid()
    property_acquisition_price_valid()
    property_rntamt_valid()
    property_sqft_valid()
    print("\nProperty Added Successfully\n")
    option = input("(a)Add more or (e)Exit: ")
    if option == "a":
        add_new_property()
    elif option == "e":
        property()
    else:
        print("\nOption Invalid\n")
        property()


def read_property():
    # numbering for data in property.txt
    numbering2 = ["Property Name", "Property City", "Property Address", "Property Postcode",
                  "Property Acquisition Date", "Property Acquisition Price(RM)",
                  "Property Suggested Rent Amount", "Property Square Foot"]
    index = -1
    try:
        with open("property.txt", "r") as file:
            for line in file:
                # replacing "|" in between data to ","
                seperate = line.replace("|", ",")
                print("---------------------------------------------")
                # spliting all data into an element
                for i in seperate.split(","):
                    # counter of numbering
                    index += 1
                    # return back to first numbering in new data
                    if index > 6:
                        index = -1
                    # printing required info
                    print(numbering2[index], ":", i)
        property()
    except Exception:
        print("Something went wrong, please try again!")
        read_property()

def read_history_property():
    # numbering for data in property.txt
    numbering2 = ["Property Name", "Property City", "Property Address", "Property Postcode",
                  "Property Acquisition Date", "Property Acquisition Price(RM)",
                  "Property Suggested Rent Amount", "Property Square Foot"]
    index = -1
    try:
        with open("historyproperty.txt", "r") as file:
            for line in file:
                # replacing "|" in between data to ","
                seperate = line.replace("|", ",")
                print("---------------------------------------------")
                # spliting all data into an element
                for i in seperate.split(","):
                    # counter of numbering
                    index += 1
                    # return back to first numbering in new data
                    if index > 6:
                        index = -1
                    # printing required info
                    print(numbering2[index], ":", i)
        property()
    except Exception:
        print("Something went wrong, please try again!")
        read_history_property()


def modify_property():
    print("Modifying property.txt")
    print("1. Replacing all info with a keyword")
    print("2. Updating whole line")
    print("3. Exit")
    # getting input from user
    opt2 = input("Enter an option:")
    # making decision based on input
    if opt2 == "1":
        try:
            # reading property.txt
            with open("property.txt", "r") as file:
                count = 0
                # printing every line in property.txt in list with numbering
                for lines in file:
                    count += 1
                    print(count, ".", [lines.rstrip()])

            with open("property.txt", "r") as file:
                data = file.read()
                # getting input from user
                oldtext = input("Text to change:")
                newtext = input("Text to insert:")
                # replacing the data provide by user
                data = data.replace(oldtext, newtext)

            with open("property.txt", "w") as file:
                # rewriting the data after modify
                file.write(data)
            # alert users after done update
            print("Done update!")
            modify_property()

        except Exception:
            print("Something went wrong! Please try again!")
            modify_property()

    elif opt2 == "2":
        delete_property_modify()
        add_new_property()

    # back to property menu
    elif opt2 == "3":
        property()
    else:
        print("Invalid input. Please try again!")
        modify_property()

def delete_property_modify():
    try:
        # open property file as read mode
        with open("property.txt", "r") as file1:
            count = 0
            # showing data in multiple arrays
            for lines in file1:
                # numbering of data after each loop
                count += 1
                print(count, ".", [lines.rstrip()])

        with open("property.txt", "r") as file2:
            line = file2.readlines()
            # getting line numbers from users to delete
            try:
                choose = int(input("Enter line to execute:"))
                index = choose - 1
                # deleting a line based on an index
                del line[index]

            except Exception:
                print("Only integers are accepted!")
                modify_property()

        # rewriting the data which are not deleted
        with open("property.txt", "w") as file3:
            for attribute in line:
                file3.write(attribute)

    except Exception:
        print("Something went wrong! Please try again!")
        modify_property()

def delete_property():
    try:
        # open property file as read mode
        with open("property.txt", "r") as file1:
            count = 0
            # showing data in multiple arrays
            for lines in file1:
                # numbering of data after each loop
                count += 1
                print(count, ".", [lines.rstrip()])

        with open("property.txt", "r") as file2:
            line = file2.readlines()
            # getting line numbers from users to delete
            try:
                choose = int(input("Enter line to delete:"))
                index = choose - 1
                # inserting deleted info into history fill
                with open("historyproperty.txt", "a") as historyfile:
                    historyfile.write(line[index])
                # deleting a line based on an index
                del line[index]
               
            except Exception:
                print("Only integers are accepted!")
                property()

        # rewriting the data which are not deleted
        with open("property.txt", "w") as file3:
            for attribute in line:
                file3.write(attribute)

        print("\nProperty delete success\n")
        property()

    except Exception:
        print("Something went wrong! Please try again!")
        property()

# Property Menu
def property():
    print("\n \n[1]. View All Property")
    print("[2]. Add New Property")
    print("[3]. Modify Property")
    print("[4]. Delete Property")
    print("[5]. View History Property")
    print("[6]. Back\n \n")

    option = input("Enter your option: ")
    if option == "1":
        read_property()
    elif option == "2":
        add_new_property()
    elif option == "3":
        modify_property()
    elif option == "4":
        delete_property()
    elif option == "5":
        read_history_property()
    elif option == "6":
        menu()
    else:
        print("\nInvalid Option\n")
        property()


##################################################     Property End     ##################################################

##################################################     Dashboard Start     ##################################################
def dash_total_tenant():
    # open tenant file as read
    file = open("tenant.txt", "r")
    # loop the line in file to check if line is empty or not. if line is not empty increase line count by 1 each time line
    total = 0
    for line in file:
        if line != "\n":
            total += 1
    file.close()
    print("Total tenant: ", total)


def dash_total_property():
    # open property file as read
    file = open("property.txt", "r")
    # loop the line in file to check if line is empty or not. if line is not empty increase line count by 1 each time line
    total = 0
    for line in file:
        if line != "\n":
            total += 1
    file.close()
    print("Total property: ", total)


def dash_total_admin():
    # open user file as read
    file = open("user.txt", "r")
    # loop the line in file to check if line is empty or not. if line is not empty increase line count by 1 each time line
    total = 0
    for line in file:
        if line != "\n":
            total += 1
    file.close()
    print("Total Admin: ", total)


def total_expenditure():
    file = open("property.txt", "r")
    # open property file as read
    lines = file.readlines()
    sum = 0
    result = []
    for line in lines:
        result.append(line.split("|")[5])
        # if the data at column number 5 is digit, loop back and add together
    for i in result:
        if i.isdigit() == True:
            sum += int(i)
    file.close()
    print("Total expenditure: RM", sum)


def total_earning():
    file = open("tenant.txt", "r")
    # open property file as read
    lines = file.readlines()
    sum = 0
    result = []
    for line in lines:
        result.append(line.split("|")[14])
        # if the data at column number 14 is digit, loop back and add together
    for i in result:
        if i.isdigit() == True:
            sum += int(i)
    file.close()
    print("Monthly Income: RM", sum)


def dashboard():
    print("\n ===== System Information =====\n")
    dash_total_tenant()
    dash_total_property()
    dash_total_admin()
    total_expenditure()
    total_earning()
    option = input("\nPress any key to exit: ")
    if option == "e":
        menu()
    else:
        menu()


##################################################     Dashboard End    ##################################################

# Main Menu
def menu():
    exit_time = datetime.datetime.now()
    print("\n[1]. Dashboard")
    print("[2]. Tenant")
    print("[3]. Property")
    print("[4]. Search")
    print("[5]. Settings")
    print("[6]. Logout\n \n")

    option = input("Enter your option: ")
    if option == "1":
        dashboard()
    elif option == "2":
        tenant()
    elif option == "3":
        property()
    elif option == "4":
        search_data_menu()
    elif option == "5":
        settings()
    elif option == "6":
        print("\n \n.........Processing to Logout.........")
        print("\n \nUser logout at: ", exit_time.strftime("%c"))
        print("\n \nDo you want Login or Shutdown ?")
        ####sl_option mean shut login
        print("\n 1. Shut Down\n 2. Login \n")
        sl_option = input("Select your option:")
        if sl_option == "1":
            print("\n \nSystem Process to ShutDown.... Please Wait")
            print("\n \nDone Shutdown, Bye~\n \n")
            with open("userlog.txt", "a") as file:
                file.write("Stop Execution Time: ")
                file.write(str(datetime.datetime.now()))
                file.write("\n")
        elif sl_option == "2":
            all()
        else:
            print("\n \nInvalid Option")
            menu()
    else:
        print("\n \nInvalid Option")
        menu()

def all():
    start()
    login()
    menu()
all()


