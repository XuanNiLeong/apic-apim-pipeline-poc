from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .orders.orders_request_builder import OrdersRequestBuilder

class Test(BaseRequestBuilder):
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new Test and sets the default values.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if request_adapter is None:
            raise TypeError("request_adapter cannot be null.")
        super().__init__(request_adapter, "{+baseurl}", None)
        if not self.request_adapter.base_url:
            self.request_adapter.base_url = "https://api.order-service.com/v1"
        self.path_parameters["base_url"] = self.request_adapter.base_url
    
    @property
    def orders(self) -> OrdersRequestBuilder:
        """
        The orders property
        """
        from .orders.orders_request_builder import OrdersRequestBuilder

        return OrdersRequestBuilder(self.request_adapter, self.path_parameters)
    

