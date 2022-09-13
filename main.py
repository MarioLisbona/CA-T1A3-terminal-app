import classes
counter = 0
id = {}
while counter < 1:
    first_name = input('Enter your first name >> ')
    last_name = input('Enter your last name >> ')
    phone = input('Enter your phone >> ')
    contact_type = input("close contact or Work Conact, Family Contact **C W f** (N for Neither)>> ").lower()
    if contact_type == 'c':
        address = input('Enter your address >> ')
        id[counter] = classes.CloseContact(first_name, last_name, phone, address)
        counter += 1
    elif contact_type == 'w':
        address = input('Enter your address >> ')
        work_address = input('Enter your work address >> ')
        work_phone = input('Enter your work phone >> ')
        skills = input('Enter your skills >> ')
        id[counter] = classes.WorkContact(first_name, last_name, phone, address, work_address, work_phone, skills)
        counter += 1
    elif contact_type == 'f':
        address = input('Enter your address >> ')
        pet_name = input('Enter your pet name >> ')
        fav_drink = input('Enter your fav_drink >> ')
        id[counter] = classes.FamilyContact(first_name, last_name, phone, address, pet_name, fav_drink)
        counter += 1
    else:
        id[counter] = classes.Contact(first_name, last_name, phone)
        counter += 1

find = input("Who's contact details do you need? ")

for k, v in id.items():
    if v.f_name == find:
        print('==========================================')
        print(v.get_details())
        print('\n==========================================')
