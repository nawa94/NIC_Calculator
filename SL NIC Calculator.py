#from datetime import datetime
import datetime

# Function for validating user input
def validate(nic : str) -> bool :
    nic_lenght = len(nic)
    if nic_lenght == 12 and nic.isdigit() :
        nic_validated = True
    elif nic_lenght == 10 and nic[0:9].isdigit() and (nic[-1] == 'v' or nic[-1] == 'V'):
        nic_validated = True
    else :
        nic_validated = False
    return nic_validated

# Function to convert old nic to new nic format
def change_nic_type(nic :str) -> str:
    return '19'+nic[0:5]+'0'+nic[5:9]

# Identify born year
def get_born_year(nic : str) -> int :
    return int(nic[0:4])

# Function to find the gender
def get_gender(nic : str) -> str :
    if int(nic[4:7]) < 500 :
        return "Male"
    else :
        return "Female"

# Function to get born date
def get_born_date(nic : str) -> datetime.date :
    born_year = get_born_year(nic)
    born_day = int(nic[4:7])
    if born_day > 500 :
        born_day -= 500
    date_calculator = datetime.date(2000,1,1) + datetime.timedelta(days=born_day-1)
    born_date = date_calculator.replace(year=born_year)
    return born_date


# Get user input
nic_number = input("Please enter your NIC number : ")
old_nic = False

# validate the nic number
validate_nic = validate(nic_number)

if validate_nic == False :
    print("Please enter a valid NIC number")
else :
    if len(nic_number) == 10 :
        nic_number = change_nic_type(nic_number)
        print(f'Your new NIC number is : {nic_number}')

    gender = get_gender(nic_number)
    birthday = get_born_date(nic_number)
    born_day = birthday.strftime('%A')

    print(f'Your gender is : {gender}')
    print(f'your birthday is : {birthday}')
    print(f'Your born date is : {born_day}')