from tapioca import JSONAdapterMixin, TapiocaAdapter, generate_wrapper_from_adapter
from .resource_mapping import RESOURCE_MAPPING


class BoxDeliveryClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    production_url = "https://api.boxdelivery.com.br/v2/"
    sandbox_url = "https://dev.api.boxdelivery.com.br/v2/"
    access_token = None
    resource_mapping = RESOURCE_MAPPING

    def refresh_authentication(self, api_params, *args, **kwargs):
        # here can be created a routine like:
        # response = requests.post(f"{self.api_root}", json=payload)
        # self.access_token = response.json()["data"]["userAuthentication"]["token"]
        pass

    def get_request_kwargs(self, api_params, *args, **kwargs):
        if not self.access_token:
            self.refresh_authentication(api_params, args, kwargs)
        api_params["headers"]["authorization"] = self.access_token
        params = super().get_request_kwargs(api_params, *args, **kwargs)
        return params

    def get_api_root(self, api_params, **kwargs):
        url = api_params.get("url", self.production_url)
        if api_params.get("sandbox"):
            url = self.sandbox_url
        return url


BoxDeliveryClient = generate_wrapper_from_adapter(BoxDeliveryClientAdapter)
