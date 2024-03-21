import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    date: str
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
    gender='Male',
    number='1234567890',
    date='03 April,2000',
    subjects='Math',
    hobbies='Sport',
    photo='photo.jpg',
    current_address='Street 123',
    state='NCR',
    city='Delhi'
)
