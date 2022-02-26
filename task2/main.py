from flask import Flask
from data import db_session
from data.users import Users
from data.jobs import Jobs
import datetime

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


def add_job(team_leader, job, work_size, collaborators, start_date, is_finished):
    jobs = Jobs()
    jobs.team_leader = team_leader
    jobs.job = job
    jobs.work_size = work_size
    jobs.collaborators = collaborators
    jobs.start_date = start_date
    jobs.is_finished = is_finished
    db_sess = db_session.create_session()
    db_sess.add(jobs)
    db_sess.commit()


def main():
    now = datetime.datetime.now()
    db_session.global_init("db/mars_explorer.db")
    add_job(1, "deployment of residential modules 1 and 2", 15, "2, 3", now, False)

    # app.run()


if __name__ == '__main__':
    main()
