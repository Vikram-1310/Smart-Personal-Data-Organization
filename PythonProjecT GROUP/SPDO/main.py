from models.person import Person
from utils.validators import *
from utils.file_ops import *
from analysis.analyzer import analyze_data
from analysis.visualizer import show_charts

data = read_json()

def add_record():
    id  = input("Enter ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    gender = input("Enter gender: ")
    city = input("Enter city: ")
    interests = input("Enter interests (comma): ").split(",")
    if not validate_age(age):
        print("Invalid age")
        return
    if not validate_email(email):
        print("Invalid email")
        return
    if not validate_phone(phone):
        print("Invalid phone")
        return

    p = Person(id,name, int(age), phone, email, gender, city, interests)
    data.append(p.to_dict())
    write_json(data)

def display_all():
    for d in data:
        print(d)

def search():
    key = input("Search by name: ")
    for d in data:
        if key.lower() in d["name"].lower():
            print(d)

def menu():
    while True:
        print("\n1.Add \n2.Display \n3.Search \n4.Export CSV \n5.Analyze \n6.Visualize \n7.Exit")
        ch = input("Choice: ")

        if ch == "1":
            add_record()
        elif ch == "2":
            display_all()
        elif ch == "3":
            search()
        elif ch == "4":
            write_csv(data)
        elif ch == "5":
            analyze_data(data)
        elif ch == "6":
            show_charts(data)
        elif ch == "7":
             break
             exit("Terminated")


if __name__ == "__main__":
    menu()