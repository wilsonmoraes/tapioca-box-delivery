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
