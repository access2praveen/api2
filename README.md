#Book Store API Testing

A python3.9 framework to test Bookstore API functions 
This implementation extensively uses Python's `requests` 
for sending RestAPI requests and capture responses.

This script creates random users and extract user-id and token from response
and uses that information to create/update and Delete books

The following modules needs to be installed 




#### Example Response ####

The recommended way to execute this application is to first set up a Python 3.9 virtual environment, 
and use the requirements.txt file with pip to install correct versions of packages.

The Project directory contains below files
```
account.py - contains class methods related to user
book.py  - contains class methods related to Book 
test_book_functions - contains test scripts to test book api's 
report.html - Generates test report 
```

The command to Run the test suite

```
C:\Users\praveen\PycharmProjects\Fox>pytest -sv test_create_user.py --html=report.html
========================================= test session starts =========================================
platform win32 -- Python 3.9.0, pytest-6.2.1, py-1.10.0, pluggy-0.13.1 -- c:\users\praveen\appdata\local\programs\python\python39\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.9.0', 'Platform': 'Windows-10-10.0.18362-SP0', 'Packages': {'pytest': '6.2.1', 'py': '1.10.0', 'pluggy': '0.13.1'}, 'Plugins': {'html': '3.1.1', 'metadata': '1.11.0'}}
rootdir: C:\Users\praveen\PycharmProjects\Fox
plugins: html-3.1.1, metadata-1.11.0
collected 9 items

test_create_user.py::TestCreateUser::test_create_newuser username: tiqjmvczet
PASSED
test_create_user.py::TestCreateUser::test_get_all_books PASSED
test_create_user.py::TestCreateUser::test_getbook_by_isbn PASSED
test_create_user.py::TestCreateUser::test_create_book PASSED
test_create_user.py::TestCreateUser::test_update_book_isbn PASSED
test_create_user.py::TestCreateUser::test_delete_book_by_isbn PASSED
test_create_user.py::TestCreateUser::test_delete_book_by_invalid_isbn XFAIL
test_create_user.py::TestCreateUser::test_delete_all_books PASSED
test_create_user.py::TestCreateUser::test_delete_user PASSED
```

The XFAIL refers to Expected failure scenario   


###References ###

https://docs.pytest.org/en/stable/contents.html
https://requests.readthedocs.io/en/master/
