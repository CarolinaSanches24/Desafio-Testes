#Convenções de nomenclatura
import unittest

class Account: 
    def create(self):                                    #criar uma conta:
       return True
    
    def delete(self):                                    # excluir conta
        return True

class TestAccounts(unittest.TestCase):
    def test_creation(self):
        account = Account()
        self.assertTrue(account.create())

    def test_deletion(self):
        account = Account()
        self.assertTrue(account.delete())

if __name__ == '__main__':
    unittest.main()

