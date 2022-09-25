import functions as f


class Contact:
    """
    Base class for all the contact classes
    Contains a class m,ethod set_details which provides the correct
    fields for that type of contact.
    Error checking is done by calling the validate_name
    and validate phoen methods.
    """    
    def __init__(self, id, f_name, l_name, phone, class_type='c'):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.class_type = class_type
    
    #this method allows user input to be gathered before the object is created
    @classmethod
    def set_details(cls):
        """
            class method returns user input for  first name, last name and phone

        Returns:
            strings: input fields for the contact
        """        
        #calling functions to validate user input
        first_name = f.validate_name('First')
        last_name = f.validate_name('Last')
        phone = f.validate_phone()

        #user input is returned
        return first_name, last_name, phone

class CloseContact(Contact):
    """
        Inherits's the set_details method from Contact class and add
        an input for address

    Args:
        Contact (object): Contact class
    """    
    def __init__(self, id, f_name, l_name, phone, address, class_type='cc'):
        super().__init__(id, f_name, l_name, phone)
        self.address = address
        self.class_type = class_type

    #class method inherits all input from from derived set_details method
    #adds extra input for address
    @classmethod
    def set_details(cls):
        first_name, last_name, phone = super().set_details()
        address = input('Enter Address >> ')

        #user input is returned
        return first_name, last_name, phone, address.strip()


class FamilyContact(CloseContact):
    """
        inherits the inputs from the Closecontact class
        Adds 2 more fields, pet name and favourite drink
    Args:
        CloseContact (object): CLoseContact object
    """    
    def __init__(self, id, f_name, l_name, phone, address, pet_name, fav_drink, class_type='fc'):
        super().__init__(id, f_name, l_name, phone, address)
        self.pet_name = pet_name
        self.fav_drink = fav_drink
        self.class_type = class_type

    #class method inherits all input from from derived set_details method
    #adds extra input for pet name and fav_drink
    @classmethod
    def set_details(cls):
        first_name, last_name, phone, address = super().set_details()
        pet_name = input('Enter Pet\'s Name >> ').strip()
        fav_drink = input('Enter Favourite Drink >> ').strip()

        #user input is returned
        return first_name, last_name, phone, address, pet_name, fav_drink

class WorkContact(CloseContact):
    """
        inherits all the user inputs from the CloseContact calss
    Args:
        CloseContact (Object): CloseContact
    """    
    def __init__(self, id, f_name, l_name, phone, address, work_address, work_phone, skills, class_type='wc'):
        super().__init__(id, f_name, l_name, phone, address)
        self.work_address = work_address
        self.work_phone = work_phone
        self.skills = skills
        self.class_type = class_type


    #class method inherits all input from from derived set_details method
    #adds extra input for work address, work phone and skills
    @classmethod
    def set_details(cls):
        first_name, last_name, phone, address = super().set_details()
        work_address = input('Enter Work Address >> ').strip()
        
        #validate user input for phone number
        work_phone = f.validate_phone()
        
        skills = input('Enter Skills >> ').strip()

        #user input is returned
        return first_name, last_name, phone, address, work_address, work_phone, skills
