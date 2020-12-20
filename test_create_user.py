from account import Account
from book import Book
import string
import random
import testdata
import pytest

class TestCreateUser:

    BASE_URL = "https://demoqa.com"


    # def randomString(self, stringLength=10):
    #     """Generate a random string of fixed length """
    #     letters = string.ascii_lowercase
    #     name = ''.join(random.choice(letters) for i in range(stringLength))
    #     return name

    def test_add_new_book_in_collection(self):
        '''
        create new user
        get books by ISBN
        add book to the collection by ISBN
        '''
    def test_create_newuser(self):

        global user_id
        global token
        global username
        global password

        username = "Fox123"
        password = "User!2345"
        self.auth = (username, password)
        account = Account(self.BASE_URL, username, password)
        response = account.create_user()
        user_id = response.json().get("userID")
        res = account.generate_token()
        token=res.json().get("token")



    def test_get_all_books(self):
        book = Book(self.BASE_URL)
        return book.get_books()

    def test_getbook_by_isbn(self):
        isbn = Book(self.BASE_URL)
        response= isbn.get_book_by_isbn(testdata.current_isbn)
        assert response.json()['title'] == "Eloquent JavaScript, Second Edition"

    def test_create_book(self):
        '''
        This will add book to the users collection using ISBN number
        '''
        payload = {
            "userId": user_id,
            "collectionOfIsbns": [
                {
                    "isbn": testdata.current_isbn
                }
            ]
        }
        newbook = Book(self.BASE_URL)
        response = newbook.create_book(payload, token)

        assert response.json()['books'][0]['isbn'] == testdata.current_isbn





    def test_update_book_isbn(self):
        payload = {
             "userId": user_id,
             "isbn": testdata.new_isbn
        }

        updatebook = Book(self.BASE_URL)
        response = updatebook.update_book(payload, token, testdata.current_isbn)
        assert response.json()['books'][0]['isbn'] == testdata.new_isbn



    def test_delete_book_by_isbn(self):
        payload = {
             "userId": user_id,
             "isbn": testdata.new_isbn
        }
        deletebook = Book(self.BASE_URL)
        response = deletebook.delete_book_by_isbn(payload, token)

        '''
        The below decorator is used to mark the scenario's for expected failures
        '''
    @pytest.mark.xfail
    def test_delete_book_by_invalid_isbn(self):
        payload = {
             "userId": user_id,
             "isbn": testdata.invalid_isbn
        }
        deletebook = Book(self.BASE_URL)
        response = deletebook.delete_book_by_isbn(payload, token)
        print(response.json())
    #
    #
    #
    def test_delete_all_books(self):

        delbook = Book(self.BASE_URL)
        response = delbook.delete_books(user_id, token)
    #

    def test_delete_user(self):
         account = Account(self.BASE_URL,username,password)
         account.delete_user(user_id,token)

