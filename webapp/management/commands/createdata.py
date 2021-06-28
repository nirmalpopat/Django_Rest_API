from django.core.management.base import BaseCommand
from faker import Faker
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        education = ['Computer', 'Electrical', 'Machanical', 'Automobile', 'Civil', 'Aranotical', 'Diploma']
        sr = random.SystemRandom()
        fake = Faker()
        print(fake.first_name())
        print(fake.last_name())
        print(fake.email())
        print(fake.phone_number()[:10])
        print(fake.phone_number()[-2:])
        print(sr.choice(education) + ' Engineering')
        print(fake.city_suffix())

        '''def __init__(self):
            education = ['Computer', 'Electrical', 'Machanical', 'Automobile', 'Civil', 'Aranotical', 'Diploma']
        sr = random.SystemRandom()
        fake = Faker()
        for i in range(20):
            data = employee(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), mobile_number=fake.phone_number()[:10], age=fake.phone_number()[-2:],education=sr.choice(education) + ' Engineering',city=fake.city_suffix())
            data.save()'''