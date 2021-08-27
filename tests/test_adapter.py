def test_adapter_as_sandbox(box_delivery_adapter):
    api_params = {"sandbox": True}
    api_root = box_delivery_adapter.get_api_root(api_params)
    assert api_root == box_delivery_adapter.sandbox_url


def test_adapter(box_delivery_adapter):
    api_params = {"sandbox": False}
    api_root = box_delivery_adapter.get_api_root(api_params)
    assert api_root == box_delivery_adapter.production_url
