#base class - minimum information stored in this class
class Contact:
    def __init__(self, f_name, l_name, phone):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
    
    #this method allows user input to be gathered before the object is created
    @classmethod
    def set_details(cls):
        first_name = input('Enter contact\'s first name >> ')
        last_name = input('Enter contact\'s last name >> ')
        phone = input('Enter contact\'s phone >> ')
        #user input is returned
        return first_name, last_name, phone

    #return contacts details
    def get_details(self):
        return f'\ncontact:\t\t{self.f_name} {self.l_name}\nPhone:\t\t\t{self.phone}'
    
    #update phone details method - this will be inherited in derived classes
    def update_phone(self, new_phone):
        self.phone = new_phone


#new class with more detailed information
class CloseContact(Contact):
    def __init__(self, f_name, l_name, phone, address):
        super().__init__(f_name, l_name, phone)
        self.address = address

    #class method inherits all input from from derived set_details method
    #adds extra input for address
    @classmethod
    def set_details(cls):
        first_name, last_name, phone = super().set_details()
        address = input('Enter contact\'s address >> ')

        #user input is returned
        return first_name, last_name, phone, address

    #return contacts details
    def get_details(self):
        return f'\ncontact:\t\t{self.f_name} {self.l_name}\nPhone:\t\t\t{self.phone}\nAddress:\t\t{self.address}'

class FamilyContact(CloseContact):
    def __init__(self, f_name, l_name, phone, address, pet_name, fav_drink):
        super().__init__(f_name, l_name, phone, address)
        self.pet_name = pet_name
        self.fav_drink = fav_drink

    #class method inherits all input from from derived set_details method
    #adds extra input for pet name and fav_drink
    @classmethod
    def set_details(cls):
        first_name, last_name, phone, address = super().set_details()
        pet_name = input('Enter contact\'s pet name >> ')
        fav_drink = input('Enter contact\'s fav_drink >> ')

        #user input is returned
        return first_name, last_name, phone, address, pet_name, fav_drink

    #return contacts details
    def get_details(self):
        return f'\ncontact:\t\t{self.f_name} {self.l_name}\nPhone:\t\t\t{self.phone}\nAddress:\t\t{self.address}\nPet name:\t\t{self.pet_name}\nFavourite Drink:\t{self.fav_drink}'

class WorkContact(CloseContact):
    def __init__(self, f_name, l_name, phone, address, work_address, work_phone, skills):
        super().__init__(f_name, l_name, phone, address)
        self.work_address = work_address
        self.work_phone = work_phone
        self.skills = skills


    #class method inherits all input from from derived set_details method
    #adds extra input for work address, work phone and skills
    @classmethod
    def set_details(cls):
        first_name, last_name, phone, address = super().set_details()
        work_address = input('Enter contact\'s work address >> ')
        work_phone = input('Enter contact\'s work phone >> ')
        skills = input('Enter contact\'s skills >> ')

        #user input is returned
        return first_name, last_name, phone, address, work_address, work_phone, skills

    #return contacts details
    def get_details(self):
        return f'\ncontact:\t{self.f_name} {self.l_name}\nPhone:\t\t{self.phone}\nAddress:\t{self.address}\nWork Address:\t{self.work_address}\nWork Phone:\t{self.work_phone}\nSkills:\t\t{self.skills}'
