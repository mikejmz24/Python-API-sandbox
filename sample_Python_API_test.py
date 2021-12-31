import sample_Python_API
from sample_Python_API import UserMatcher

def test_createUser_creates_and_returns_user_Jack_Daniels():
    JackDaniels = sample_Python_API.createUser("Jack", "Daniels", 33)
    assert JackDaniels == UserMatcher(JackDaniels)
    assert JackDaniels.id == 1
    assert JackDaniels.firstName == "Jack"
    assert JackDaniels.lastName == "Daniels"
    assert JackDaniels.age == 33

def test_viewAllUsers_returns_null_when_no_users_exist():
    sample_Python_API.deleteAllusers()
    assert sample_Python_API.viewAllUsers() is None

def test_viewAllUsers_returns_user_Jack_Daniels_and_user_Jim_Bean_object_data():
    sample_Python_API.deleteAllusers()
    sample_Python_API.createUser("Jack", "Daniels", 33)
    sample_Python_API.createUser("Jim", "Bean", 32)
    users1 = sample_Python_API.viewAllUsers()
    assert users1[0].id == 1
    assert users1[0].firstName == "Jack"
    assert users1[0].lastName == "Daniels"
    assert users1[0].age == 33
    assert users1[1].id == 2
    assert users1[1].firstName == "Jim"
    assert users1[1].lastName == "Bean"
    assert users1[1].age == 32
