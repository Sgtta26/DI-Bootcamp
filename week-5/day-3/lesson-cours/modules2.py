from faker import Faker
from cls_attribute2 import Human

fake = Faker()
for _ in range(1000):
    fake_name = fake.name()
    Human(name=fake_name)

print(Human.people)