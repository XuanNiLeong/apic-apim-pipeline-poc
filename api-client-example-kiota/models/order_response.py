from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .order_item import OrderItem
    from .order_response_customer_info import OrderResponse_customerInfo
    from .order_response_status import OrderResponse_status

@dataclass
class OrderResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The createdAt property
    created_at: Optional[datetime.datetime] = None
    # The currency property
    currency: Optional[str] = None
    # The customerInfo property
    customer_info: Optional[OrderResponse_customerInfo] = None
    # The items property
    items: Optional[list[OrderItem]] = None
    # The orderId property
    order_id: Optional[str] = None
    # The status property
    status: Optional[OrderResponse_status] = None
    # The totalAmount property
    total_amount: Optional[float] = None
    # The updatedAt property
    updated_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrderResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrderResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrderResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .order_item import OrderItem
        from .order_response_customer_info import OrderResponse_customerInfo
        from .order_response_status import OrderResponse_status

        from .order_item import OrderItem
        from .order_response_customer_info import OrderResponse_customerInfo
        from .order_response_status import OrderResponse_status

        fields: dict[str, Callable[[Any], None]] = {
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "customerInfo": lambda n : setattr(self, 'customer_info', n.get_object_value(OrderResponse_customerInfo)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(OrderItem)),
            "orderId": lambda n : setattr(self, 'order_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(OrderResponse_status)),
            "totalAmount": lambda n : setattr(self, 'total_amount', n.get_float_value()),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("currency", self.currency)
        writer.write_object_value("customerInfo", self.customer_info)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("orderId", self.order_id)
        writer.write_enum_value("status", self.status)
        writer.write_float_value("totalAmount", self.total_amount)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_additional_data_value(self.additional_data)
    

