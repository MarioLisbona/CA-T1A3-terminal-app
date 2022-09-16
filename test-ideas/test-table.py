from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Id", justify="right", style="cyan", no_wrap=True)
table.add_column("First name", style="magenta")
table.add_column("Last name", style="magenta")
table.add_column("Phone", justify="right", style="green")
table.add_column("Address", justify="right", style="green")

list = [('1', 'Mario', 'Lisbona', '0412 450 719')]
dict = [
    {"id": '1', "type": "Contact", "first_name": "Mario", "last_name": "Lisbona", "phone": "0412 450 719"},
    {"id": '2', "type": "Contact", "first_name": "Ali", "last_name": "Taubner", "phone": "0481 468 068"},
    {"id": '3', "type": "Contact", "first_name": "Coda", "last_name": "Cat", "phone": "111 222 333"},
    {"id": '3', "type": "Close Contact", "first_name": "Bob", "last_name": "Smith", "phone": "000 220002 300", "address": "49 Broome Street"},
    {"id": '1', "type": "Contact", "first_name": "Mario", "last_name": "Lisbona", "phone": "0412 450 719"},
    {"id": '2', "type": "Contact", "first_name": "Ali", "last_name": "Taubner", "phone": "0481 468 068"},
    {"id": '3', "type": "Contact", "first_name": "Coda", "last_name": "Cat", "phone": "111 222 333"},
    {"id": '3', "type": "Close Contact", "first_name": "Bob", "last_name": "Smith", "phone": "000 220002 300", "address": "49 Broome Street"},
    {"id": '1', "type": "Contact", "first_name": "Mario", "last_name": "Lisbona", "phone": "0412 450 719"},
    {"id": '2', "type": "Contact", "first_name": "Ali", "last_name": "Taubner", "phone": "0481 468 068"},
    {"id": '3', "type": "Contact", "first_name": "Coda", "last_name": "Cat", "phone": "111 222 333"},
    {"id": '3', "type": "Close Contact", "first_name": "Bob", "last_name": "Smith", "phone": "000 220002 300", "address": "49 Broome Street"}
]

print(dict)
print(len(dict))
print(dict[0]['first_name'])

# for x in range(len(dict)):
#     print(dict[x]['first_name'], dict[x]['last_name'])
# user_tuple = tuple(dict)

# print(user_tuple)
# print(dict)


# list_of_tuple = [tuple(val) for val in dict.values()]

# print(list_of_tuple)

# out = [tuple(v) for  v in dict.items()]


# new_list = []

# for x in out:
#     print(x[-1])
#     new_list.append(x[-1])

# print(new_list)

for idx, val in enumerate(dict):
    print(len(val))


console = Console()

# for x in range(len(dict)):
#     table.add_row(dict[x]['id'], dict[x]['first_name'], dict[x]['last_name'], dict[x]['phone'])

for idx, val in enumerate(dict):
    if len(val) == 6:
        table.add_row(dict[idx]['id'], dict[idx]['first_name'], dict[idx]['last_name'], dict[idx]['phone'],  dict[idx]['address'])
    elif len(val) == 5:
        table.add_row(dict[idx]['id'], dict[idx]['first_name'], dict[idx]['last_name'], dict[idx]['phone'])
# print(dict['id'])  
# table.add_row(dict[0]['id'], dict[0]['first_name'], dict[0]['last_name'], dict[0]['phone'])

console.print(table)




# =================================================================================================================================================================

            dict = [
                {"id": '1', "type": "Contact", "first_name": "Mario", "last_name": "Lisbona", "phone": "0412 450 719"},
                {"id": '2', "type": "Contact", "first_name": "Ali", "last_name": "Taubner", "phone": "0481 468 068"},
                {"id": '3', "type": "Contact", "first_name": "Coda", "last_name": "Cat", "phone": "111 222 333"},
                {"id": '3', "type": "Close Contact", "first_name": "Bob", "last_name": "Smith", "phone": "000 220002 300", "address": "49 Broome Street"},
                {"id": '1', "type": "Contact", "first_name": "Mario", "last_name": "Lisbona", "phone": "0412 450 719"},
                {"id": '2', "type": "Contact", "first_name": "Ali", "last_name": "Taubner", "phone": "0481 468 068"},
                {"id": '3', "type": "Contact", "first_name": "Coda", "last_name": "Cat", "phone": "111 222 333"},
                {"id": '3', "type": "Close Contact", "first_name": "Bob", "last_name": "Smith", "phone": "000 220002 300", "address": "49 Broome Street", 'work_address': 'myself', 'work_phone': 'Beer', 'skills': 'Beer drinking'},
                {"id": '1', "type": "Contact", "first_name": "Mario", "last_name": "Lisbona", "phone": "0412 450 719"},
                {"id": '2', "type": "Contact", "first_name": "Ali", "last_name": "Taubner", "phone": "0481 468 068"},
                {"id": '5', "type": "Contact", "first_name": "Coda", "last_name": "Cat", "phone": "111 222 333", "address": "49 Broome Street", 'pet': 'myself', 'fav_drink': 'Beer'},
                {"id": '3', "type": "Close Contact", "first_name": "Bob", "last_name": "Smith", "phone": "000 220002 300", "address": "49 Broome Street"}
            ]
            table = Table(title="Star Wars Movies")

            table.add_column("Id", justify="right", style="cyan", no_wrap=True)
            table.add_column("First name", style="magenta")
            table.add_column("Last name", style="magenta")
            table.add_column("Phone", justify="right", style="green")
            table.add_column("Address", justify="right", style="green")

            # #user tinyDB all method to iterate through entire database and print results
            whole_db = ContactsDb.all()
            for idx, val in enumerate(dict):
                if len(val) == 5:
                    table.add_row(dict[idx]['id'], dict[idx]['first_name'], dict[idx]['last_name'], dict[idx]['phone'])
                elif len(val) == 6:
                    table.add_row(dict[idx]['id'], dict[idx]['first_name'], dict[idx]['last_name'], dict[idx]['phone'],  dict[idx]['address'])
                elif len(val) == 8:
                    table.add_row(dict[idx]['id'], dict[idx]['first_name'], dict[idx]['last_name'], dict[idx]['phone'],  dict[idx]['address'], dict[idx]['pet'], dict[idx]['fav_drink'])
                elif len(val) == 9:
                    table.add_row(dict[idx]['id'], dict[idx]['first_name'], dict[idx]['last_name'], dict[idx]['phone'],  dict[idx]['address'], dict[idx]['work_address'], dict[idx]['work_phone'], dict[idx]['skills'])
