# Bloodlink
# This program is an blood donation management system.
# Users can store, retrive, search and match donors and blood requests data. Data can be saved and loaded form the filesystem.
#


# We're storing all our Donors and Blood requests in list called donors and request.
# An individual donor is stored as a dictonary.
# The structure an donor is:
# donor = {
# 'name': 'Name of the donor',
#         'blood_group': 'Blood group',
#         'phone': 'Phone number',
#         'location': 'Donors location'
#     }
# 
# The structure of an blood request is:
# request = {
#         'name': name,
#         'blood_group': blood_group,
#         'phone': phone,
#         'date': date,
#         'location': location
#     }


from pathlib import Path
from difflib import SequenceMatcher


donors = []
requests = []

# This funciton prints all the donors as a table.
def view_donors():

    if not donors:
        print("There are no donors. Add donors first")
    else:
        print('-'*65)
        print(f"{'Name':20} {'BG':^5} {'Phone':15} {'Location'}")
        print('-'*65)

        for donor in donors:
            print(f"{donor.get('name'):20} {donor.get('blood_group'):^5} {donor.get('phone'):15} {donor.get('location')}")

# This function takes two word/stirng and checks similarity between them and returns a ratio
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# This is an implimentation of basic fuzzy search, finds approximate result.
def fuzzy_search(query, *fields):

    query = query.lower()

    for field in fields:
        text = str(field).lower()

        if query in text:
            return True
        
        for word in text.split():
            if similarity(query, word) >= 0.75:
                return True
        
    return False


# This functions checks if the input is empty, and won't let user continue unitl they've entered a non empty text. We'll use this one instead of input() function
def required_input(prompt):
    while True:
        value = input(prompt).strip()
        
        if value:
            return value
        print("This field is required")

# Checks if blood group is valid
def blood_group_input(prompt):
    BLOOD_GROUP = {'O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-'}

    while True:
        value = input(prompt).strip().upper()

        if value in BLOOD_GROUP:
            return value
        
        print("Invalid blood group, enter a valid one")

# Checks if phone number is valid Bangladeshi number
def phone_input():
    while True:
        value = input('Phone: ').strip()

        if value.isdigit() and len(value) == 11 and value.startswith('01'):
            return value
        
        print("Enter a valid 11 digit Bangladeshi phone number (01XXXXXXXXX)")


def search_donor():
    query = required_input("Search donor: ")
    results = []
    for donor in donors:
        if fuzzy_search(query, *donor.values()):
            results.append(donor)

    if not results:
        print("No donors found.")
        return
    else:
        print('-'*65)
        print(f"{'Name':20} {'BG':^5} {'Phone':15} {'Location'}")
        print('-'*65)
        for donor in results:
            print(f"{donor.get('name'):20} {donor.get('blood_group'):^5} {donor.get('phone'):15} {donor.get('location')}")

        
def add_donor():
    print("Enter donor details")
    name = required_input("Name: ")
    blood_group = blood_group_input("Blood Group(O+, O-, A+, A-, B+, B-, AB+, AB-): ")
    phone = phone_input()
    location = required_input("Location: ")
    
    donor = {
        'name': name,
        'blood_group': blood_group,
        'phone': phone,
        'location': location
    }
    donors.append(donor)

def view_requests():
    if not requests:
        print("There are no blood requests.")
    else:
        print('-'*65)
        print(f"{'Name':20} {'BG':^5} {'Phone':15} {'Date':20} {'Location'}")
        print('-'*65)
        for request in requests:
            print(f"{request.get('name'):20} {request.get('blood_group'):^5} {request.get('phone'):15} {request.get('date'):20} {request.get('location')}")

def search_requests():
    query = required_input("Search requests: ")
    results = []
    for request in requests:
        if fuzzy_search(query, *request.values()):
            results.append(request)

    if not results:
        print("No request found.")
        return
    else:
        print('-'*65)
        print(f"{'Name':20} {'BG':^5} {'Phone':15} {'Date':20} {'Location'}")
        print('-'*65)
        for donor in results:
            print(f"{donor.get('name'):20} {donor.get('blood_group'):^5} {donor.get('phone'):15} {donor.get('date'):20} {donor.get('location')}")

def add_request():
    print("Enter Patient details")
    name = required_input("Name: ")
    blood_group = blood_group_input("Blood Group(O+, O-, A+, A-, B+, B-, AB+, AB-): ")
    phone = phone_input()
    date = required_input("Date, When is blood needed?: ")
    location = required_input("Location, Where is the blood needed?: ")
    request = {
        'name': name,
        'blood_group': blood_group,
        'phone': phone,
        'date': date,
        'location': location
    }
    requests.append(request)


def match_donors():
    if not requests:
        print("No blood requests available.")
        return

    print("\nAvailable Requests:")
    for i, r in enumerate(requests, 1):
        print(f"{i}. {r.get('name')} | {r.get('blood_group')} | {r.get('location')}")

    try:
        choice = int(input("\nSelect request number: ")) - 1
        request = requests[choice] 
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    req_bg = request.get('blood_group')
    req_location = request.get('location')

    matches = []

    for donor in donors:
        if donor.get("blood_group") == req_bg: 
            if fuzzy_search(req_location, donor.get('location')):
                matches.append(donor)

    if not matches:
        print("No matching donors found.")
        return

    print("\nMatched Donors:")
    print('-'*65)
    print(f"{'Name':20} {'BG':^5} {'Phone':15} {'Location'}")
    print('-'*65)

    for d in matches:
        print(f"{d.get('name'):20} {d.get('blood_group'):^5} {d.get('phone'):15} {d.get('location')}")

def save_data():
    data = {'donors': donors, 'requests': requests}

    with open('donors.txt', 'w') as f:
        for d in donors:
            line = f"{d.get('name')}|{d.get('blood_group')}|{d.get('phone')}|{d.get('location')}\n"
            f.write(line)
    with open('requests.txt', 'w') as f:
        for r in requests:
            line = f"{r.get('name')}|{r.get('blood_group')}|{r.get('phone')}|{r.get('date')}|{r.get('location')}\n"
            f.write(line)

    print("Data saved")


def load_data():
    global donors, requests

    donors = []
    requests = []
    

    try:
        with open('donors.txt') as f:
            for line in f:
                name, bg, phone, location = line.strip().split('|')

                donor = {
                    'name': name,
                    'blood_group': bg,
                    'phone': phone,
                    'location': location
                }
                
                donors.append(donor)

        with open('requests.txt') as f:
            for line in f:
                name, bg, phone, date, location = line.strip().split('|')

                request = {
                    'name': name,
                    'blood_group': bg,
                    'phone': phone,
                    'date': date,
                    'location': location
                }

                requests.append(request)

        print(f"Data loaded")

    except FileNotFoundError:
        print("No previous data found. Please add and save records first.")



load_data()
    

while True:
    print("""
1. View Donors
2. Search Donor
3. Add Donor
4. View Requests
5. Search Requests
6. Add blood request
7. Match Donors
8. Save data
9. Load Data
0. Exit""")

    try:
        choice = int(input("Enter your choice:  "))
    except ValueError:
        print("Invalid choice, enter a valid option")
        continue

    if choice == 1:
        view_donors()
    elif choice == 2:
        search_donor()
    elif choice == 3:
        add_donor()
    elif choice == 4:
        view_requests()
    elif choice == 5:
        search_requests()
    elif choice == 6:
        add_request()
    elif choice == 7:
        match_donors()
    elif choice == 8:
        save_data()
    elif choice == 9:
        load_data()
    elif choice == 0:
        break


