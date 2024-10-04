import datetime
print(datetime.date.today())
import application.salary as salary
import db.people as people

if __name__ == '__main__':

    salary.calculate_salary()
    people.get_employees("Jimmi")


