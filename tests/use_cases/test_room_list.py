import pytest
import uuid
from unittest import mock

from rentomatic.domain.room import Room
from rentomatic.use_cases.room_list import room_list_use_case, calculate_total_interest


@pytest.fixture
def domain_rooms():
    room_1 = Room(
        code=uuid.uuid4(),
        size=2,
        price=10,
        longitude=-0.5,
        latitude=5.1
    )

    room_2 = Room(
        code=uuid.uuid4(),
        size=4,
        price=50,
        longitude=-0.5,
        latitude=5.1
    )

    room_3 = Room(
        code=uuid.uuid4(),
        size=6,
        price=60,
        longitude=-0.5,
        latitude=5.1
    )

    room_4 = Room(
        code=uuid.uuid4(),
        size=10,
        price=100,
        longitude=-0.5,
        latitude=5.1
    )

    return [room_1, room_2, room_3, room_4]

def test_room_list_without_parameters(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms
    result = room_list_use_case(repo)
    repo.list.assert_called_with()
    assert result == domain_rooms

def test_calculate_total_interest():
    total_amount = 1000
    percent = 5
    expected_result = 50
    result = calculate_total_interest(total_amount, percent)
    assert result == expected_result

    total_amount = 5000
    percent = 0
    expected_result = 0
    result = calculate_total_interest(total_amount, percent)
    assert result == expected_result

    total_amount = 2000
    percent = 3
    expected_result = 60
    result = calculate_total_interest(total_amount, percent)
    assert result == expected_result

