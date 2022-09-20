# **Coder Academy - Assignment T1A3 - Terminal Application: Submitted by Mario Lisbona**

## **Table of contents**

[**Coder Academy - Assignment T1A3 - Terminal Application: Submitted by Mario Lisbona**](#coder-academy---assignment-t1a3---terminal-application-submitted-by-mario-lisbona)
[**Table of contents**](#table-of-contents)
- [**Coder Academy - Assignment T1A3 - Terminal Application: Submitted by Mario Lisbona**](#coder-academy---assignment-t1a3---terminal-application-submitted-by-mario-lisbona)
  - [**Table of contents**](#table-of-contents)
  - [**R3 - Attributions**](#r3---attributions)
  - [**R4 - Links**](#r4---links)
  - [**R5 - Styling Conventions**](#r5---styling-conventions)
  - [**R6 - Features**](#r6---features)
    - [**Feature 1 - Create / Add a contact**](#feature-1---create--add-a-contact)
    - [**Feature 2 - Edit a contact**](#feature-2---edit-a-contact)
    - [**Feature 3 - Delete a contact**](#feature-3---delete-a-contact)
    - [**Feature 4 - Display contacts**](#feature-4---display-contacts)
      - [**Display a contact**](#display-a-contact)
      - [**Display all contacts**](#display-all-contacts)
    - [**Feature 5 - Creating a new Contact Book or Accessing an existing one**](#feature-5---creating-a-new-contact-book-or-accessing-an-existing-one)
    - [**Feature 6 - Match cases for main program menu and Add Contact Menu**](#feature-6---match-cases-for-main-program-menu-and-add-contact-menu)
  - [**R7 - Implementation Plan**](#r7---implementation-plan)
  - [**R8 - Help Documentation**](#r8---help-documentation)




## **R3 - Attributions**
- [^1 - Template]() - Erika Varagouli (2021) [*What Each Markup Language Is Used For*](https://www.semrush.com/blog/markup-language/), Semrush website, accessed 25 August 2022.




- [Generator Expressions]() - [*Generator Expressions*](https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search), Stack Overflow website, accessed 19 Sept 2022.
- [Packaging Python Projects]() - [*Packaging Python Projects*](https://packaging.python.org/en/latest/tutorials/packaging-projects/), Python org website, accessed 20 Sept 2022.
- 

## **R4 - Links**

- [Github Repo]()
- [Slide Deck Presentation link - Youtube]()

## **R5 - Styling Conventions**

 - style guide: PEP8 style guide

## **R6 - Features**

### **Feature 1 - Create / Add a contact**

The Contacts Book will need to be able to add a contact. The user will be able to select between 4 types of contacts to add to their contact book.
- Contact
- Close Contact
- Family Contact
- Work Contact

The contacts will share some commonalities with their input fields. All contacts will contain the base fields of first name, last name and phone number. Below is a list of the input fields for each contact type and the fields they share. I will use classes and classes to implement this functionality and inheritance. All contact variables will be of String Type.

| Contact      | Close Contact                          | Family Contact                               | Work Contact                                 |   |
|--------------|----------------------------------------|----------------------------------------------|----------------------------------------------|---|
| ID           | ID                                     | ID                                           | ID                                           |   |
| Contact Type | Contact Type                           | Contact Type                                 | Contact Type                                 |   |
| First name   | First name  (inherited from Contact)   | First name  (inherited from Close Contact)   | First name  (inherited from Close Contact)   |   |
| Last name    | Last name  (inherited from Contact)    | Last name  (inherited from Close Contact)    | Last name  (inherited from Close Contact)    |   |
| Phone number | Phone number  (inherited from Contact) | Phone number  (inherited from Close Contact) | Phone number  (inherited from Close Contact) |   |
|              | Address                                | Address  (inherited from Close Contact)      | Address  (inherited from Close Contact)      |   |
|              |                                        | Pet name                                     | Work Address                                 |   |
|              |                                        | Favourite Drink                              | Work Phone                                   |   |
|              |                                        |                                              | Skills                                       |   |

<br>

<img src="./docs/T1A3%20class%20inheritance.drawio.png" alt="Class inheritance">

<br>

Variables will be assigned depending on which type of contact is being created. Once this has been done, those variables will become key/pair values in a dictionary. That dictionary will be inserted into json file with a unique ID

The TinyDB module will be used to manage the database CRUD, Create, Read, Update and Delete functions. Every time a contact is created the user ID will need to be incremented. Deeper Error checking will need to be performed on 3 of the fields:
- first name
  - remove leading or trailing white spaces
  - prompt user to enter valid data if the field is completly empty
  - prompt user to enter valid data if the field is made up of only white space
- last name
  - remove leading or trailing white spaces
  - prompt user to enter valid data if the field is completly empty
  - prompt user to enter valid data if the field is made up of only white space
- phone number
  - remove leading or trailing white spaces
  - have the data be only numeric
  - allow white space inbetween numbers
- work phone number
  - remove leading or trailing white spaces
  - have the data be only numeric
  - allow white space inbetween numbers

  
### **Feature 2 - Edit a contact**

The user will be able to edit an existing contact. They will be able to search the contacts book for a first name. The application will then use TinDB’s search and get methods to retrieve the contact if it exists in the database. If there is only a single contact with that name, the contact will be displayed and the user will be prompted to confirm whether they want to edit that contact. If they select no is selected then they are taken back to the Home Menu. If they confirm that they want to edit the contact then they will be asked to fill in the particular fields that are valid for that contact type.

If multiple results return from the name search then all the contacts with their unique ID will be displayed in a table. The user will be prompted to choose an ID to edit. Error checking here will be vital so that they don't edit a different contact to the ones that are displayed.

Once a valid ID has been selected, the user will be asked to confirm they want to edit this contact. If they choose no, they’ll be returned to the home menu, otherwise they will be asked to fill in the particular fields that are valid for that contact type. 

Each contact dict will have a key/value pair of ```type: contact_type```. The edit feature will access this type from the selected contact to edit and use it in a match case structure so that the correct type of contact input fields are called for the type of contact that has been returned by the search.

If no results are found, display a message to the user and prompt them to search for another user or go back to the home menu.

The edit feature will use the same code as the create contact, so will utilise the same error checking functionality.


  
### **Feature 3 - Delete a contact**

The delete feature will be similar to the edit feature in that it will search the database for a name entered by the user. A message will be displayed if the name cannot be found and they’ll be prompted to search again or be taken back to the home menu. Results, singular and multiple will be displayed to the user. They will need to select and ID to delete with multiple results.
Once a contact has been selected then they are prompted to confirm the delete. If they select yes the contact will be deleted and returned to the home menu.


### **Feature 4 - Display contacts**

This feature will be implemented in two ways, searching for a contact to be displayed and displaying the entire contact book.

#### **Display a contact**

The user will search for a contact. The same search functionality that is shared with the edit and delete features will be used. Multiple and single results will be displayed in a table. The user will be prompted to search again or return home. If a result is not found, the user will be prompted to search again or be returned to the home menu.

#### **Display all contacts**

The whole database will be displayed in a table if the user selects this option. The table is created using the Rich module. First the table is created and headings assigned to columns. Then a for loop is used to iterate over the database and create a new row for each contact. If statements are used to access the right amount of elements for each contact type

### **Feature 5 - Creating a new Contact Book or Accessing an existing one**

The application will start on a menu prompting the user to make a choice between creating a new contacts book or creating a new one. They can also quit the application at this stage as well.

I am including this feature because I wanted the user (Educator) to have some mock data to play around with rather than having to enter information to test the features.

If the user wants to access an existing contacts book then firstly an instance of the TinyDB class will need to be created along with the path to the contacts.json file. Once this is done, we can assign the contents of the json file to a variable. We need to find the next available ID so that we aren't creating ID’s that clash with the existing contacts. This will be done by accessing TinyDB’s .doc_id method. This will return the ID that is assigned to each document (contact) in the json file. The application will need to iterate over the entire json file to find the last ID that is used. This will be incremented by 1 and used for the next contact that is created.

If the user chooses to create a new database then the user ID will need to be initialised to zero and then the new database will be iterated over.



### **Feature 6 - Match cases for main program menu and Add Contact Menu**

A match case, combined with while loops will be used for the home menu and the add contact menu so that the application will run continually until the user chooses to quit.

<br>

<img src="./docs/T1A3%20Match%20case.drawio.png" alt="Class inheritance">

<br>

There will also be another match cased used by the application only (not accessible by the user) that will facilitate the editing of contacts. It will access use the documens returned by the search of the json file. The ```type: contact_type``` of that document will be accessed and a match case will be used to determin which type of contact needs to be edited.


## **R7 - Implementation Plan**

- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item
- Utilise a suitable project management platform to track this implementation plan.
- Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan. 
- Your checklists for each feature should have at least 5 items.

## **R8 - Help Documentation**

- Design help documentation which includes a set of instructions which accurately describe how to use and install the application.
  - steps to install the application
  - any dependencies required by the application to operate
  - any system/hardware requirements
  - how to use any command line arguments made for the application


















3 features included - describe each feature

trello for implementation plan

https://www.asciiart.eu/

packaging termial app as pypi package
