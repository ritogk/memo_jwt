from flask_seeder import Seeder, Faker, generator
import sys
sys.path.append('../')
from db.models.all import User

class UserSeeder(Seeder):

    # Refer: https://pypi.org/project/Flask-Seeder/
    # Lower priority will be run first. All seeders with the same priority are then ordered by class name.
    # def __init__(self, db=None):
    #     super().__init__(db=db)
    #     self.priority = 1

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=User,
            init={
                "id": None,
                "name": generator.String('[a-z]\d{4}\c{3}'),
                "email": 'homing0321r4cfw@yahoo.co.jp',
                "created_at": None,
                "updated_at": None,
            }
        )

        # Create 1 users
        for user in faker.create(1):
            print("Adding user: %s" % user)
            # Flask-Seeder will by default commit all changes to the database.
            self.db.session.add(user)