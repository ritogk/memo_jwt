from flask_seeder import Seeder, Faker, generator
import sys
sys.path.append('../')
from db.models.all import UserAuthentication
import hashlib

class UserAuthenticationSeeder(Seeder):

    # Refer: https://pypi.org/project/Flask-Seeder/
    # Lower priority will be run first. All seeders with the same priority are then ordered by class name.
    # def __init__(self, db=None):
    #     super().__init__(db=db)
    #     self.priority = 1

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=UserAuthentication,
            init={
                "id": None,
                "username": 'test',
                "password": hashlib.sha256('test'.encode()).hexdigest(),
                "created_at": None,
                "updated_at": None,
            }
        )

        # Create 1
        for user_authentication in faker.create(1):
            print("Adding user_authentication: %s" % user_authentication)
            self.db.session.add(user_authentication)