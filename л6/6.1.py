class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    
    def set_password(self, new_password):
        self.__password = new_password
    
    def check_password(self, password):
        return self.__password == password


# Пример использования
user = UserAccount("ivan_petrov", "ivan@mail.ru", "mypass123")

print(f"Пользователь: {user.username}")
print(f"Email: {user.email}")
print(f"Проверка пароля 'mypass123': {user.check_password('mypass123')}")
print(f"Проверка пароля 'wrong': {user.check_password('wrong')}")

user.set_password("newpass456")
print(f"Проверка старого пароля: {user.check_password('mypass123')}")
print(f"Проверка нового пароля: {user.check_password('newpass456')}")