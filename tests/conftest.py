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


@pytest.fixture
def calculate_value_response():
    return {
        "withReturn": {
            "id": 6,
            "destination_table_id": 1,
            "range_start": 3000,
            "range_end": 4499,
            "minimum_value": 6.5,
            "suggested_value": 6.5,
            "type": 0,
            "vehicle_type": 1,
            "back": 1,
            "created_at": "2016-11-09 11:11:11",
            "updated_at": "2018-01-02 11:17:50",
            "deleted_at": None,
            "city": None,
            "uf": None,
            "tax": 1.5,
        },
        "withoutReturn": {
            "id": 5,
            "destination_table_id": 1,
            "range_start": 3000,
            "range_end": 4499,
            "minimum_value": 6.5,
            "suggested_value": 6.5,
            "type": 0,
            "vehicle_type": 1,
            "back": 0,
            "created_at": "2016-11-09 11:11:11",
            "updated_at": "2018-01-02 11:17:39",
            "deleted_at": None,
            "city": None,
            "uf": None,
            "tax": 1.5,
        },
    }
