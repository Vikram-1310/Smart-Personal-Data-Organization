import uuid
class Person:
    def __init__(self,id,name, age, phone, email, gender, city, interests):
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.gender = gender
        self.city = city
        self.interests = interests

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Phone: {self.phone}, Email: {self.email}")
        print(f"Gender: {self.gender}, City: {self.city}")
        print(f"Interests: {', '.join(self.interests)}")
        print("-" * 40)

    def update(self, field, value):
        if hasattr(self, field):
            setattr(self, field, value)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "phone": self.phone,
            "email": self.email,
            "gender": self.gender,
            "city": self.city,
            "interests": self.interests
        }