# Tapioca Box Delivery

Wrapper for Box Delivery API services.
## Installation
```
pip install tapioca-box-delivery
```

## Quickstart

All mapped services are wrapped in the `Box Delivery` client.

``` python
from tapioca_box_delivery import BoxDeliveryClient


api = BoxDeliveryClient(sandbox=True,access_token='000000-000000-000000-000000')

response = box_delivery_client.calculate_value(
            vehicle_type=4, destination_lat="-16.731470", destination_lng="-49.283660"
        ).get()

onboarding_data = response().data

```
> You can also use `BoxDeliveryClient(sandbox=True, access_token=...)` to work with the sandbox environment.

The following resources are available:

|             Endpoint             |           Resource            |
| :------------------------------: | :---------------------------: |
|   `/orders/calculate-value/{vehicleType}/{destination_lat}/{destination_lng}`   | `calculate_value()` |
|    `/orders`    |  `create_order()`  |

---

To learn more about how Tapioca works, check the [documentation](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html).
'+
