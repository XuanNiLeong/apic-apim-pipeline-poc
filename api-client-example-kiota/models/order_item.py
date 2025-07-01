from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class OrderItem(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The itemId property
    item_id: Optional[str] = None
    # The productId property
    product_id: Optional[str] = None
    # The productName property
    product_name: Optional[str] = None
    # The quantity property
    quantity: Optional[int] = None
    # The totalPrice property
    total_price: Optional[float] = None
    # The unitPrice property
    unit_price: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrderItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrderItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrderItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "itemId": lambda n : setattr(self, 'item_id', n.get_str_value()),
            "productId": lambda n : setattr(self, 'product_id', n.get_str_value()),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "quantity": lambda n : setattr(self, 'quantity', n.get_int_value()),
            "totalPrice": lambda n : setattr(self, 'total_price', n.get_float_value()),
            "unitPrice": lambda n : setattr(self, 'unit_price', n.get_float_value()),
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
        writer.write_str_value("itemId", self.item_id)
        writer.write_str_value("productId", self.product_id)
        writer.write_str_value("productName", self.product_name)
        writer.write_int_value("quantity", self.quantity)
        writer.write_float_value("totalPrice", self.total_price)
        writer.write_float_value("unitPrice", self.unit_price)
        writer.write_additional_data_value(self.additional_data)
    

