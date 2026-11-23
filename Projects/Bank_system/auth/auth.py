from utils.file_handler import read_json, write_json

class Auth:

    def register(self, username, password):
        users = read_json("Bank_system/auth/users.json")

        if username in users:
            return "User already exists"

        users[username] = {
            "password": password,
            "balance": 0
        }

        write_json("Bank_system/auth/users.json", users)

        return "Account created"

    def login(self, username, password):
        users = read_json("Bank_system/auth/users.json")

        if username in users and users[username]["password"] == password:
            return True

        return False