from .person_creator_validator import person_creator_validator

class MockRequest():
    def __init__(self, body) -> None:
        self.body = body

def test_person_creator_validator():
    request = MockRequest({
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 1
    })    

    person_creator_validator(request)
    