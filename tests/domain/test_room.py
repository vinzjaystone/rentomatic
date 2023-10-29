import uuid
from rentomatic.domain.room import Room

def test_room_model():
    code = uuid.uuid4()
    room = Room(
        code,
        size=200,
        price=10,
        longitude=-0.01755,
        latitude=51.21231,
    )

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.01755
    assert room.latitude == 51.21231

def test_room_model_from_dict():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "size" : 200,
        "price": 10,
        "longitude": -0.01755,
        "latitude": 51.21231,
    }

    room = Room.from_dict(init_dict)

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.01755
    assert room.latitude == 51.21231

def test_room_model_to_dict():
    init_dict = {
        "code": uuid.uuid4(),
        "size" : 200,
        "price": 10,
        "longitude": -0.01755,
        "latitude": 51.21231,
    }

    room = Room.from_dict(init_dict)
    assert room.to_dict() == init_dict

def test_room_model_comparison():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "size" : 200,
        "price": 10,
        "longitude": -0.01755,
        "latitude": 51.21231,
    }

    room1 = Room.from_dict(init_dict)
    room2 = Room.from_dict(init_dict)

    assert room1 == room2

