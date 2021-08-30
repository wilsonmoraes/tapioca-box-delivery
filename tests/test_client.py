import uuid

import pytest
import responses
from tapioca.exceptions import ClientError, ServerError


@responses.activate
def test_invalid_token_client(box_delivery_url, box_delivery_client):
    endpoint = f"{box_delivery_url}orders/calculate-value/4/-16.731470/-49.283660"
    responses.add(responses.GET, endpoint, status=401)
    with pytest.raises(ClientError) as client_error:
        box_delivery_client.calculate_value(
            vehicle_type=4, destination_lat="-16.731470", destination_lng="-49.283660"
        ).get()
    assert "401" in str(client_error.value)


@responses.activate
def test_server_error(box_delivery_url, box_delivery_client):
    endpoint = f"{box_delivery_url}orders/calculate-value/4/-16.731470/-49.283660"
    responses.add(responses.GET, endpoint, status=500)
    with pytest.raises(ServerError) as server_error:
        box_delivery_client.calculate_value(
            vehicle_type=4, destination_lat="-16.731470", destination_lng="-49.283660"
        ).get()
    assert "500" in str(server_error.value)


@responses.activate
def test_calculate_value(box_delivery_url, box_delivery_client, calculate_value_response):
    endpoint = f"{box_delivery_url}orders/calculate-value/4/-16.731470/-49.283660"
    responses.add(responses.GET, endpoint, status=200, json=calculate_value_response)
    response = box_delivery_client.calculate_value(
        vehicle_type=4, destination_lat="-16.731470", destination_lng="-49.283660"
    ).get()
    response_data = response().data
    assert isinstance(response_data, dict)
    assert isinstance(response_data["withReturn"], dict)
    assert isinstance(response_data["withoutReturn"], dict)


@responses.activate
def test_create_order(box_delivery_url, box_delivery_client):
    endpoint = f"{box_delivery_url}orders"
    responses.add(responses.POST, endpoint, status=200, json={"data": {"id": "12345"}})
    response = box_delivery_client.create_order().post({})
    response_data = response().data
    assert isinstance(response_data, dict)
    assert isinstance(response_data["data"], dict)
    assert isinstance(response_data["data"]["id"], str)


@responses.activate
def test_cancel_order(box_delivery_url, box_delivery_client):
    endpoint = f"{box_delivery_url}orders/1/cancel"
    responses.add(responses.PUT, endpoint, status=200, json={"id": str(uuid.uuid4())})
    response = box_delivery_client.cancel_order(id=1).put()
    response_data = response().data
    assert response().status_code == 200
    assert isinstance(response_data["id"], str)


@responses.activate
def test_try_to_cancel_order_on_delivery(box_delivery_url, box_delivery_client):
    endpoint = f"{box_delivery_url}orders/1/cancel"
    responses.add(
        responses.PUT,
        endpoint,
        status=400,
        json={"delivery-10000": "O pedido já foi aceito por um entregador e não pode ser cancelado"},
    )
    with pytest.raises(ClientError) as client_error:
        box_delivery_client.cancel_order(id=1).put()
    assert "400" in str(client_error.value)
    assert "delivery-10000" in client_error.value.client


@responses.activate
def test_try_to_cancel_order_not_found(box_delivery_url, box_delivery_client):
    endpoint = f"{box_delivery_url}orders/1/cancel"
    responses.add(responses.PUT, endpoint, status=404, json={"error": "Pedido não encontrado"})
    with pytest.raises(ClientError) as client_error:
        box_delivery_client.cancel_order(id=1).put()
    assert "404" in str(client_error.value)
