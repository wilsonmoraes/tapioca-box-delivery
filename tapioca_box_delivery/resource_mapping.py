# coding: utf-8

RESOURCE_MAPPING = {
    "calculate_value": {
        "resource": "orders/calculate-value/{vehicleType}/{destinationLat}/{destinationLng}",
        "docs": "https://dev.api.boxdelivery.com.br/doc/index.html#api-Order-PostOrders",
        "methods": ["GET"]
    },
    "create_order": {
        "resource": "orders",
        "docs": "https://dev.api.boxdelivery.com.br/doc/index.html#api-Order-PostOrders",
        "methods": ["POST"]
    },
}
