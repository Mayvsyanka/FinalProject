from AddressBook import *


class Bot:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        if action == 'add':
            name = Name(input(SystemPresent().present("Name: "))).value.strip()
            phones = Phone().value
            birth = Birthday().value
            email = Email().value.strip()
            status = Status().value.strip()
            note = Note(input(SystemPresent().present("Note: "))).value
            record = Record(name, phones, birth, email, status, note)
            return self.book.add(record)
        elif action == 'search':
            print(
                "There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
            category = input(SystemPresent().present('Search category: '))
            pattern = input(SystemPresent().present('Search pattern: '))
            result = (self.book.search(pattern, category))
            for account in result:
                if account['birthday']:
                    birth = account['birthday'].strftime("%d/%m/%Y")
                    result = "_" * 50 + "\n" + \
                        f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                    print(result)
        elif action == 'edit':
            contact_name = input(SystemPresent().present('Contact name: '))
            parameter = input(SystemPresent().present(
                'Which parameter to edit(name, phones, birthday, status, email, note): ')).strip()
            new_value = input("New Value: ")
            return self.book.edit(contact_name, parameter, new_value)
        elif action == 'remove':
            pattern = input(SystemPresent().present(
                "Remove (contact name or phone): "))
            return self.book.remove(pattern)
        elif action == 'save':
            file_name = input(SystemPresent().present("File name: "))
            return self.book.save(file_name)
        elif action == 'load':
            file_name = input(SystemPresent().present("File name: "))
            return self.book.load(file_name)
        elif action == 'congratulate':
            print(self.book.congratulate())
        elif action == 'view':
            print(self.book)
        elif action == 'exit':
            pass
        else:
            PresentErrors().present("There is no such command!")
