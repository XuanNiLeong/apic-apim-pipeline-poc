from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_order_item_request_builder import WithOrderItemRequestBuilder

class OrdersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /orders
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OrdersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/orders", path_parameters)
    
    def by_order_id(self,order_id: str) -> WithOrderItemRequestBuilder:
        """
        Gets an item from the test.orders.item collection
        param order_id: Unique identifier of the order to retrieve
        Returns: WithOrderItemRequestBuilder
        """
        if order_id is None:
            raise TypeError("order_id cannot be null.")
        from .item.with_order_item_request_builder import WithOrderItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["orderId"] = order_id
        return WithOrderItemRequestBuilder(self.request_adapter, url_tpl_params)
    

