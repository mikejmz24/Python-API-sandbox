users = []
ID = 1

class User:
    id: int
    firstName: str
    lastName: str
    age: int

    def __init__(self, firstName: str, lastName: str, age: int) -> None:
        self.id = ID
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __repr__(self) -> str:
        return f"User(id={repr(self.id)}, firstName={repr(self.firstName)}, lastName={repr(self.lastName)}, age={repr(self.age)})"

class UserMatcher:
    expected: User

    def __init__(self, expected) -> None:
        self.expected = expected

    def __eq__(self, other):
        return self.expected.id == other.id and \
            self.expected.firstName == other.firstName and \
            self.expected.lastName == other.lastName and \
            self.expected.age == other.age

def createUser(firstName: str, lastName: str, age: int) -> User:
    createdUser = User(firstName, lastName, age)
    users.append(createdUser)
    global ID
    ID += 1
    return createdUser

def viewUser(id: int) -> list:
    return query(["id"], [id])

def viewAllUsers() -> list:
    return users if users else None

def viewUsersByFirstName(firstName: str) -> list:
    return query(["firstName"], [firstName])

def deleteUser(id: int) -> list:
    index = next((i for i, user in enumerate(users) if user.id == id), None)
    return users.pop(index) if index is not None else None

def deleteAllusers() -> bool:
    users.clear()
    global ID
    ID = 1
    return True

def query(keys, values) -> list:
    keyValues = createDictionary(keys, values)
    index = 1
    queryRes = []
    res = "user for user in users if "
    for key, value in keyValues.items():
        value = value if type(value) is int else f'\"{value}\"'
        if (index == 1):
            res += f"getattr(user, \"{key}\") == {value}"
        else:
            res += f" and getattr(user, \"{key}\") == {value}"
        index += 1
    res = "queryRes = [" + res + "]"
    lcls = locals()
    exec(res, globals(), lcls )
    queryRes = lcls["queryRes"]
    return queryRes if queryRes else None

def createDictionary(keys, values) -> dict:
    return dict(zip(keys, values))