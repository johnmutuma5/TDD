def main ():
    contact = Contact ('Lazuli', 'Muthoni', '0728655088')
    phonebook = Phonebook()

    last_name = phonebook.add_contact (contact)
    print (last_name)



class Contact ():
    def __init__ (self, first_name, last_name, mobile):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile

    def __str__ (self):
        contact_string = '''First Name: {}\nSecond Name: {}\nMobile: {}'''.format(self.first_name,
                                    self.last_name,
                                    self.mobile)
        return contact_string




class Phonebook():
    def __init__(self):
        self.contacts = []

    def add_contact (self, contact):
        self.contacts.append(contact)
        pushed_contact = self.contacts[-1]
        return pushed_contact.first_name



#call main

if __name__ == "__main__":
    main ()
