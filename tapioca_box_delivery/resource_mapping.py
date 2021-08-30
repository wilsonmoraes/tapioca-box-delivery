# coding: utf-8

RESOURCE_MAPPING = {
    "calculate_value": {
        "resource": "orders/calculate-value/{vehicle_type}/{destination_lat}/{destination_lng}",
        "docs": "https://dev.api.boxdelivery.com.br/doc/index.html#api-Order-PostOrders",
        "methods": ["GET"],
    },
    "create_order": {
        "resource": "orders",
        "docs": "https://dev.api.boxdelivery.com.br/doc/index.html#api-Order-PostOrders",
        "methods": ["POST"],
    },
    "cancel_order": {
        "resource": "orders/{id}/cancel",
        "docs": "https://dev.api.boxdelivery.com.br/doc/index.html#api-Order-PutOrdersIdCancel",
        "methods": ["PUT"],
    },
    "detail_order": {
        "resource": "orders/{id}",
        "docs": "https://dev.api.boxdelivery.com.br/doc/index.html#api-Order-GetOrdersId",
        "methods": ["GET"],
    },
    "end_order": {
        "resource": "orders/{id}/finish",
        "docs": "https://dev.api.boxdelivery.com.br/doc/index.html#api-Order-PutOrdersIdFinish",
        "methods": ["PUT"],
    },
}
