import uuid

import pytest

from tapioca_box_delivery import BoxDelivery
from tapioca_box_delivery.tapioca_box_delivery import BoxDeliveryClientAdapter


@pytest.fixture
def box_delivery_url():
    return "https://dev.api.boxdelivery.com.br/v2/"


@pytest.fixture
def unique_id():
    return str(uuid.uuid4())


@pytest.fixture
def box_delivery_client(unique_id):
    return BoxDelivery(
        sandbox=True,
        access_key=unique_id,
    )


@pytest.fixture
def box_delivery_adapter():
    return BoxDeliveryClientAdapter()


@pytest.fixture
def payload_create_order(unique_id):
    return {
        "phone": "62982410475",
        "total_value": 200.00,
        "client_name": "Client test",
        "order_payment_type_id": 1,
        "courier_must_return": 1,
        "need_bag": 1,
        "vehicle_type": 1,
        "address": {
            "city": "São Paulo",
            "neighborhood": "Centro",
            "state": "SP",
            "zipcode": "68.379-200",
            "address": "Av. Principal",
            "number": 10,
            "complement": {"lat": 120, "lng": 12},
        },
        "multiple": [],
    }
