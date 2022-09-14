#Importing classes module
import classes
import functions as f
import os

#counter for key in dict and creating empty dict that will be id(int): contact(object)
contact_id = 1
contacts_dict = {}

#variable for user menu choice used to match case
menu_choice = None

# while user input is not 'EX' (ex is to escape from program)
#show menu a and get user's menu choice
while menu_choice != 'EX':
    f.menu_prompt()
    #assign input for menu and clear screen
    menu_choice = input('Enter a choice: A, E, D, SA or EX >>')
    os.system('cls||clear')

    # match case user input with upper for A, E, D, S, SA
    match menu_choice.upper():
        case 'A':
            #new while loop and match case to choose what type of contact to enter
            add_choice = None
            while add_choice != 'EX':
                f.add_contact_prompt()
                add_choice = input('Enter a choice: C, CC, FC, WC or EX >>')
                os.system('cls||clear')

                # Creating a new instance of whatever clss is being entere, Contact, CloseContact, FamilyContact or WorkContact
                # using the class method set_details() to get user input for contact
                #incremendting contact ID each time a contact is created
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
                print("====================================Editing a contact ==================================")
                print("Enter the contacts name or EX to exit to main menu.")
                print('\n====================================================================================')
                edit_choice = input('Enter a contact name to edit >> ')

                # match edit_choice.upper():
                #     case 'EX':
                #         break

                #     case other:
                #         for v in contacts_dict.values():
                #             if v.f_name == edit_choice:
                #                 print(v.get_details())
                #                 print('Edit details')
                #                 match v.class_type:
                #                     case 'c':
                #                         f_name, l_name, phone = classes.Contact.set_details()
                #                         v.update_contact(f_name, l_name, phone)
                #                         break
                #                     case 'cc':
                #                         f_name, l_name, phone, address = classes.CloseContact.set_details()
                #                         v.update_contact(f_name, l_name, phone, address)
                #                         break
                #                     case 'fc':
                #                         f_name, l_name, phone, address, pet, drink = classes.FamilyContact.set_details()
                #                         v.update_contact(f_name, l_name, phone, address, pet, drink)
                #                         break
                #                     case 'wc':
                #                         f_name, l_name, phone, address, w_address, w_phone, skills = classes.WorkContact.set_details()
                #                         v.update_contact(f_name, l_name, phone, address, w_address, w_phone, skills)
                #                         break
                #         else:
                #             print("that contaxt doesnt exist")
        case 'D':
            print('Deleting a contact')
            del_choice = None
            while del_choice != 'EX':
                print("====================================Deleting a contact ==================================")
                print("Enter the contacts name to delete or EX to exit to main menu.")
                print('\n====================================================================================')
                del_choice = input('Enter a contact name to delete >> ')

                match del_choice.upper():
                    case 'EX':
                        break

                    case other:
                        for k, v in contacts_dict.items():
                            if v.f_name == del_choice:
                                print(v.get_details())
                                del contacts_dict[k]
                                break
                        else:
                            print("that contaxt doesnt exist")
        case 'S':
            show_choice = None
            while show_choice != 'EX':
                print("====================================Displaying a contact ==================================")
                print("Enter the contacts name to display or EX to exit to main menu.")
                print('\n====================================================================================')
                show_choice = input('Enter a contact name to display >> ')

                match show_choice.upper():
                    case 'EX':
                        break

                    case other:
                        for v in contacts_dict.values():
                            if v.f_name == show_choice:
                                print(v.get_details())
                                break
                        else:
                            print("that contaxt doesnt exist")
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






