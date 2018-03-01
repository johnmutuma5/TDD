import unittest

from app.phonebook import Phonebook, Contact

class PhonebookTestCase (unittest.TestCase):

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phonebook = Phonebook()



    def test_add_contact (self):

        contact = Contact ('Lazuli', 'Muthoni', '0728655088')
        first_name = self.phonebook.add_contact (contact)
        self.assertEqual (first_name, 'Lazuli')

    def test_update_contact (self):

        contact = Contact ('Lazuli', 'Muthoni', '0728655088')
        self.phonebook.add_contact (contact)

        # test update first_name alone
        updated_contact = self.phonebook.update_contact("Lazuli", "Muthoni", new_first = "Lazuli Olive")
        self.assertEqual(updated_contact.first_name, 'Lazuli Olive')

        # test update last_name alone
        updated_contact = self.phonebook.update_contact("Lazuli Olive", "Muthoni", new_last = "Murimi")
        self.assertEqual (updated_contact.last_name, 'Murimi')

        # test update mobile number alone
        updated_contact = self.phonebook.update_contact("Lazuli Olive", "Murimi", new_mobile = "0725280260")
        self.assertEqual (updated_contact.mobile, '0725280260')

        # test update All
        updated_contact = self.phonebook.update_contact("Lazuli Olive", "Murimi", new_mobile = "0728655088",
                                                            new_last = 'Muthoni',
                                                            new_first = 'Lazuli')
        self.assertEqual (updated_contact.mobile, '0728655088')
        self.assertEqual (updated_contact.first_name, 'Lazuli')
        self.assertEqual (updated_contact.last_name, 'Muthoni')


    def test_delete_contact (self):

        contact = Contact ('Lazuli', 'Muthoni', '0728655088')
        self.phonebook.add_contact (contact)

        # add a second contact
        contact = Contact ('Sheelah', 'B', '0725280260')
        self.phonebook.add_contact (contact)

        # delete second contact
        self.phonebook.delete_contact ('Sheelah', 'B')

        # check if the contact still exists
        contact = None
        for contact in self.phonebook.contacts:
            if contact.first_name == 'Sheelah' and contact.last_name == 'B':
                contact = contact
                break
        #if contact is not None, then it was not deleted successfully
        self.assertNotEqual(contact, None)


    def test_view_contact(self):

            contact = Contact ('Lazuli', 'Muthoni', '0728655088')
            self.phonebook.add_contact (contact)

            mobile = self.phonebook.view_contact('Lazuli', 'Muthoni')            
            self.assertEqual(mobile, '0728655088')






if __name__ == "__main__":
    unittest.main ()
