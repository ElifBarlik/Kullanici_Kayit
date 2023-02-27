import json
import os


class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email


class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedin=False
        self.currentUser={}

        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                users=json.load(file)
                for user in users:
                    user=json.loads(user)
                    newUser=User(user['username'], user['password'], user['email'])
                    self.users.append(newUser)
                
    def register(self, user:User):
        self.users.append(user)
        self.savetoFile()
        print('Kullanici olusturuldu.')
        
    def login(self,username,password):
        for user in self.users:
            if user.username==username and user.password==password:
                self.isLoggedin=True
                self.currentUser=user
                print('Giris Basarili.')
                break
            else:
                print('Giris Basarisiz.')
    def logout(self):
        self.isLoggedin=False
        self.currentUser={}
        print('Cikis Basarili.')
        
    def identity(self):
        if self.isLoggedin:
            print(f'Username: {self.currentUser.username}')
        else:
            print('Giris Basarisiz.')
    def savetoFile(self):
        list=[]
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open('users.json','w') as file:
            json.dump(list, file)

repository=UserRepository()



while True:
    print('Menu'.center(50,'-'))
    secim=input('1-Register\n2-Login\n3-Logout\n4-Indentity\n5-Exit\nSeciminiz: ')
    if secim=='1':
        username=input('Username: ')
        password=input('Password: ')
        email=input('Email: ')

        user=User(username,password,email)
        repository.register(user)

    elif secim=='2':
        username=input('Username: ')
        password=input('Password: ')
        repository.login(username,password)
    elif secim=='3':
        repository.logout()
    elif secim=='4':
        repository.identity()
    elif secim=='5':
        break
    else:
        print('Gecersiz Secim')