class Contact:
    def __init__(self, f_name, l_name, phone):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        
    def get_details(self):
        return f'\ncontact:\t\t{self.f_name} {self.l_name}\nPhone:\t\t\t{self.phone}'

class CloseContact(Contact):
    def __init__(self, f_name, l_name, phone, address):
        super().__init__(f_name, l_name, phone)
        self.address = address

    def get_details(self):
        return f'\ncontact:\t\t{self.f_name} {self.l_name}\nPhone:\t\t\t{self.phone}\nAddress:\t\t{self.address}'

class FamilyContact(CloseContact):
    def __init__(self, f_name, l_name, phone, address, pet_name, fav_drink):
        super().__init__(f_name, l_name, phone, address)
        self.pet_name = pet_name
        self.fav_drink = fav_drink

    def get_details(self):
        return f'\ncontact:\t\t{self.f_name} {self.l_name}\nPhone:\t\t\t{self.phone}\nAddress:\t\t{self.address}\nPet name:\t\t{self.pet_name}\nFavourite Drink:\t{self.fav_drink}'

class WorkContact(CloseContact):
    def __init__(self, f_name, l_name, phone, address, work_address, work_phone, skills):
        super().__init__(f_name, l_name, phone, address)
        self.work_address = work_address
        self.work_phone = work_phone
        self.skills = skills


    def get_details(self):
        return f'\ncontact:\t{self.f_name} {self.l_name}\nPhone:\t\t{self.phone}\nAddress:\t{self.address}\nWork Address:\t{self.work_address}\nWork Phone:\t{self.work_phone}\nSkills:\t\t{self.skills}'
