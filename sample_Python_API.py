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

def viewUser(id):
    return query(["id"], [id])

def viewAllUsers():
    return users if users else None

def viewUsersByFirstName(firstName):
    return query(["firstName"], [firstName])

def deleteUser(id):
    index = next((i for i, user in enumerate(users) if user.id == id), None)
    return users.pop(index) if index is not None else None

def deleteAllusers():
    users.clear()
    global ID
    ID = 1
    return True

def query(keys, values):
    keyValues = createDictionary(keys, values)
    res = []
    for key, value in keyValues.items():
        res = [user for user in users if getattr(user, key) == value]
    return res if res else None

def createDictionary(keys, values):
    return dict(zip(keys, values))