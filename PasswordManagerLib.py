from passlib.hash import sha256_crypt
import ast
class PasswordManager:
    def __init__(self):
        pass

    def verifyPassword(self, username, password):
        fh = open(r'C:\Users\Phan\PycharmProjects\hellotiki\password.txt', 'r')
        read = ast.literal_eval(fh.read())
        if read['username'] == username:
            if sha256_crypt.verify(password, read['password']) :
                return True
        return False

    def validateUsername(self, username):
        if ' ' in username:
            return False
        return True

    def validatePassword(self, password):
        if ' ' in password:
            return False
        if len(password) < 6:
            return False
        if any(i.isdigit() for i in password) == False:
            return False
        if any(i.isupper() for i in password) == False:
            return False
        if any(i.islower() for i in password) == False:
            return False
        return True

    def encrypt(self, password):
        passwordEncrypted = sha256_crypt.encrypt(str(password))
        return passwordEncrypted

    def setNewPassword(self, username, passwordEncrypted):
        file = open(r'C:\Users\Phan\PycharmProjects\hellotiki\password.txt', 'w')
        content = {}
        content['username'] = username
        content['password'] = passwordEncrypted
        file.write(str(content))
        file.close()
        return True