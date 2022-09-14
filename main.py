#Importing classes module
import classes
import os

#counter for key in dict and creating empty dict that will be id(int): contact(object)
contact_id = 0
contacts_dict = {}

user_choice = None

while user_choice != 'EX':
    print('======================================================================================\n')
    print('Contacts database. What would you like to do?')
    print('Add Contact - A')
    print('Edit Contact - E')
    print('Del Contact - D')
    print('Show Contact - S')
    print('Show all Contact - SA')
    print('Exit Program - EX')
    print('\n====================================================================================')
    menu_choice = input('Enter a choice: A, E, D, SA or EX >>')
    os.system('cls||clear')
    match menu_choice.upper():
        case 'A':
            add_choice = None
            while add_choice != 'EX':
                print('======================================================================================\n')
                print("====================================Adding a contact ==================================")
                print("Enter a contact, close contact, work contact or family contacy?")
                print('Contact - C')
                print('Close ontact - CC')
                print('Family Contact - FC')
                print('Work Contact - WC')
                print('Exit Back to main menu - EX')
                print('\n====================================================================================')
                add_choice = input('Enter a choice: C, CC, FC, WC or EX >>')
                os.system('cls||clear')
                match add_choice.upper():
                    case 'C':
                        print('Adding a contact')
                        f_name, l_name, phone = classes.Contact.set_details()
                        contacts_dict[contact_id] = classes.Contact(contact_id, f_name, l_name, phone)
                        contact_id += 1
                    case 'CC':
                        print('Adding a Close contact')
                        f_name, l_name, phone, address = classes.CloseContact.set_details()
                        contacts_dict[contact_id] = classes.CloseContact(contact_id, f_name, l_name, phone, address)
                        contact_id += 1
                    case 'FC':
                        print('Adding a Family contact')
                        f_name, l_name, phone, address, pet_name, fav_drink = classes.FamilyContact.set_details()
                        contacts_dict[contact_id] = classes.FamilyContact(contact_id, f_name, l_name, phone, address, pet_name, fav_drink)
                        contact_id += 1
                    case 'WC':
                        print('Adding a Work contact')
                        f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
                        contacts_dict[contact_id] = classes.WorkContact(contact_id, f_name, l_name, phone, address, w_address, w_phone, skills)
                        contact_id += 1
                    case 'EX':
                        break
                    case other:
                        print('that is not a valid choice')
        case 'E':
            edit_choice = None
            while edit_choice != 'EX':
                print('Editing a contact')
                print("====================================Editing a contact ==================================")
                print("Enter the contacts name or EX to exit to main menu.")
                print('\n====================================================================================')
                edit_choice = input('Enter a contact name to edit >> ')

                match edit_choice.upper():
                    case 'EX':
                        break

                    case other:
                        for k, v in contacts_dict.items():
                            if v.f_name == edit_choice:
                                print(v.get_details())
                                print('Edit details')
                                match v.class_type:
                                    case 'c':
                                        f_name, l_name, phone = classes.Contact.set_details()
                                        v.update_contact(f_name, l_name, phone)
                                        break
                                    case 'cc':
                                        f_name, l_name, phone, address = classes.CloseContact.set_details()
                                        v.update_contact(f_name, l_name, phone, address)
                                        break
                        else:
                            print("that contaxt doesnt exist")
        case 'D':
            print('Deleting a contact')
        case 'S':
            print('Showing a contact')
        case 'SA':
            print('Showing all contacts')
            for k, v in contacts_dict.items():
            #     if v.f_name == find:
                print('==========================================')
                print(v.get_details())
                print('\n==========================================')
        case 'EX':
            break
        case other:
            print('that is not a valid choice')






