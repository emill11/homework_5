import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    subjects: str
    hobbies: str
    photo: str
    current_address: str
    state: str
    city: str


user_1 = User(
    first_name='Ivan',
    last_name='Ivanov',
    email='test@test.test',
    gender='male',
    number='1234567890',
    subjects='ma',
    hobbies='sport',
    photo='photo.jpg',
    current_address='Street 123',
    state='NC',
    city='De'
)

user_2 = User(
    first_name='Admin',
    last_name='Admin',
    email='admin@test.test',
    gender='male',
    number='1234567890',
    subjects='ma',
    hobbies='sport',
    photo='photo.jpg',
    current_address='Street 123',
    state='NC',
    city='De'
)
