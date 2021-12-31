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

def test_viewUser_finds_and_returns_user_Jack_Daniels_data():
    sample_Python_API.deleteAllusers()
    sample_Python_API.createUser("Jack", "Daniels", 21)
    JackDaniels = sample_Python_API.viewUser(1)
    assert JackDaniels[0].id == 1
    assert JackDaniels[0].firstName == "Jack"
    assert JackDaniels[0].lastName == "Daniels"
    assert JackDaniels[0].age == 21

def test_viewUser_returns_None_when_no_user_matches_its_id():
    sample_Python_API.deleteAllusers()
    assert sample_Python_API.viewUser(0) is None

def test_deleteUser_removes_user_Jack_Daniels_from_users_list_and_returns_its_object_data():
    sample_Python_API.deleteAllusers()
    JackDaniels = sample_Python_API.createUser("Jack", "Daniels", 20)
    deletedUser = sample_Python_API.deleteUser(1)
    assert deletedUser == UserMatcher(JackDaniels)
    assert deletedUser.id == 1
    assert deletedUser.firstName == "Jack"
    assert deletedUser.lastName == "Daniels"
    assert deletedUser.age == 20

def test_deleteUser_returns_None_when_user_id_does_not_find_any_match():
    sample_Python_API.deleteAllusers()
    assert sample_Python_API.deleteUser(0) is None

def test_Users_are_created_with_an_auto_incremental_id_even_when_other_users_are_deleted():
    sample_Python_API.deleteAllusers()
    sample_Python_API.createUser("Jack", "Daniels", 33)
    sample_Python_API.createUser("Jim", "Bean", 32)
    sample_Python_API.deleteUser(2)
    sample_Python_API.createUser("Jim", "Bean II", 21)
    createdUsers = sample_Python_API.viewAllUsers()
    assert createdUsers[0].id == 1
    assert createdUsers[0].firstName == "Jack"
    assert createdUsers[0].lastName == "Daniels"
    assert createdUsers[0].age == 33
    assert createdUsers[1].id == 3
    assert createdUsers[1].firstName == "Jim"
    assert createdUsers[1].lastName == "Bean II"
    assert createdUsers[1].age == 21

def test_viewUsersByFirstName_returns_four_Users_named_Don_Julio():
    sample_Python_API.deleteAllusers()
    sample_Python_API.createUser("Don Julio", "Blanco", 1)
    sample_Python_API.createUser("Don Julio", "Reposado", 1)
    sample_Python_API.createUser("Don Julio", "Añejo", 3)
    sample_Python_API.createUser("Don Julio", "Cristalino", 70)
    donJulios = sample_Python_API.viewUsersByFirstName("Don Julio")
    assert donJulios[0].id == 1
    assert donJulios[0].firstName == "Don Julio"
    assert donJulios[0].lastName == "Blanco"
    assert donJulios[0].age == 1
    assert donJulios[1].id == 2
    assert donJulios[1].firstName == "Don Julio"
    assert donJulios[1].lastName == "Reposado"
    assert donJulios[1].age == 1
    assert donJulios[2].id == 3
    assert donJulios[2].firstName == "Don Julio"
    assert donJulios[2].lastName == "Añejo"
    assert donJulios[2].age == 3
    assert donJulios[3].id == 4
    assert donJulios[3].firstName == "Don Julio"
    assert donJulios[3].lastName == "Cristalino"
    assert donJulios[3].age == 70

def test_query_finds_and_returns_two_Users_with_firstName_Don_Julio_and_age_1():
    sample_Python_API.deleteAllusers()
    sample_Python_API.createUser("Don Julio", "Añejo", 3)
    sample_Python_API.createUser("Don Julio", "Blanco", 1)
    sample_Python_API.createUser("Don Julio", "Cristalino", 70)
    sample_Python_API.createUser("Don Julio", "Reposado", 1)
    filteredDonJulios = sample_Python_API.query(["firstName", "age"], ["Don Julio", 1])
    assert filteredDonJulios[0].id == 2
    assert filteredDonJulios[0].firstName == "Don Julio"
    assert filteredDonJulios[0].lastName == "Blanco"
    assert filteredDonJulios[0].age == 1
    assert filteredDonJulios[1].id == 4
    assert filteredDonJulios[1].firstName == "Don Julio"
    assert filteredDonJulios[1].lastName == "Reposado"
    assert filteredDonJulios[1].age == 1