#Importing classes module
import classes

#counter for key in dict and creating empty dict that will be id(int): contact(object)
counter = 0
contacts_dict = {}

#just one loop for one to create one contact
#if / elif statements for normal contact, close contact, family contact and work contact

#each contidional will call the specific classmethod set_details method to enter contact details
#set_details will return the user input and that user input is used to create a new isntance of that class.
#counter is incremented for the key in the dict ------may not be needed
while counter < 1:
    contact_type = input("close contact or Work Conact, Family Contact **C W f** (N for Neither)>> ").lower()
    if contact_type == 'c':
        f_name, l_name, phone, address = classes.CloseContact.set_details()
        contacts_dict[counter] = classes.CloseContact(f_name, l_name, phone, address)
        counter += 1
    elif contact_type == 'w':
        f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
        contacts_dict[counter] = classes.WorkContact(f_name, l_name, phone, address, w_address, w_phone, skills)
        counter += 1
    elif contact_type == 'f':
        f_name, l_name, phone, address, pet_name, fav_drink = classes.FamilyContact.set_details()
        contacts_dict[counter] = classes.FamilyContact(f_name, l_name, phone, address, pet_name, fav_drink)
        counter += 1
    else:
        f_name, l_name, phone = classes.Contact.set_details()
        contacts_dict[counter] = classes.Contact(f_name, l_name, phone)
        counter += 1


#testing out  seach and edit contact functionionality...
find = input("Who's contact details do you need? ")

#search dict for contact. if found in value, call the get_dtails method on that object

for k, v in contacts_dict.items():
    if v.f_name == find:
        print('==========================================')
        print(v.get_details())
        print('\n==========================================')

        #testing update here on just the phone number
        #update_phone method is only declared in base class and inherited to all its derived classes
        find = input(f"Would you like to update {v.f_name} {l_name}'s details> Y or N >> ").lower()
        if find ==  'y':
            phone = input('Enter your phone >> ')
            v.update_phone(phone)
        
        print('==========================================')
        print(v.get_details())
        print('\n==========================================')





