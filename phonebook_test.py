import unittest

from app.phonebook import Phonebook, Contact

class PhonebookTestCase (unittest.TestCase):

    def test_add_contact (self):
        contact = Contact ('Lazuli', 'Muthoni', '0728655088')
        phonebook = Phonebook()
        first_name = phonebook.add_contact (contact)
        self.assertEqual (first_name, 'Lazuli')


if __name__ == "__main__":
    unittest.main ()
