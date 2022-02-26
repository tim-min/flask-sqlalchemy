from flask import Flask
from data import db_session
from data.users import Users

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def add_users(name, surname, age, position, speciality, address, email):
    users = Users()
    users.name = name
    users.surname = surname
    users.age = age
    users.position = position
    users.speciality = speciality
    users.address = address
    users.email = email
    db_sess = db_session.create_session()
    db_sess.add(users)
    db_sess.commit()


def main():
    db_session.global_init("db/mars_explorer.db")
    add_users("Ridley", "Scott", 21, "captain", "research engineer", "module_1", "scott_chief@mars.org")
    add_users("Andrey", "Ivanov", 25, "notcaptain", "pilot", "module_2", "andrey_ivanov@mars.org")
    add_users("Ivan", "Andreev", 23, "notnotcaptain", "navigator", "module_3", "ivan_andreev@mars.org")
    add_users("Evgeniy", "Ivanov", 35, "notnotnotcaptain", "inspector", "module_4", "evgeniy_ivanov@mars.org")
    add_users("Ivan", "Ivanov", 21, "notnotnotnotcaptain", "navigator", "module_5", "ivan_ivanov@mars.org")
    
    # app.run()


if __name__ == '__main__':
    main()
