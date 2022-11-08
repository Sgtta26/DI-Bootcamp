# Local module
import property_module

# Python built-in module
from random import sample, randint
# Downloaded module/package
from faker import Faker

fake = Faker()

print(fake.name())