users = []
ID = 1

class User:
    id: int
    firstName: str
    lastName: str
    age: int

    def __init__(self, firstName, lastName, age):
        self.id = ID
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __repr__(self):
        return f"User(id={repr(self.id)}, firstName={repr(self.firstName)}, lastName={repr(self.lastName)}, age={repr(self.age)})"

class UserMatcher:
    expected: User

    def __init__(self, expected):
        self.expected = expected

    def __eq__(self, other):
        return self.expected.id == other.id and \
            self.expected.firstName == other.firstName and \
            self.expected.lastName == other.lastName and \
            self.expected.age == other.age

def createUser(firstName, lastName, age):
    createdUser = User(firstName, lastName, age)
    users.append(createdUser)
    global ID
    ID += 1
    return createdUser
    # users.append(User(firstName, lastName, age))
    # print("User", firstName, lastName, "was added successfully!")

def viewUser(id):
    foundUsers = [x for x in users if x.id == id]
    if len(foundUsers) == 0:
        print("User does not exist :(")
    else:
        i = id - 1
        print(foundUsers[0].id, foundUsers[0].firstName,
              foundUsers[0].lastName, foundUsers[0].age)

def viewAllUsers():
    if len(users) > 0:
        return users
    else:
        return None

def deleteUser(id):
    if id == 0 or id > len(users):
        print("User does not exist :(")
    else:
        i = id - 1
        print("User", users[i].firstName,
              users[i].lastName, "will be deleted!")
        users.pop(i)

def deleteAllusers():
    users.clear()
    global ID
    ID = 1
    return True

# createUser("Jack", "Daniels", 30)
# createUser("Jim", "Bean", 40)
# createUser("Don Julio", "Cristalino", 70)
# deleteUser(2)
# createUser("Jim", "Bean II", 44)
# createUser("Elijah", "Craig", 55)
