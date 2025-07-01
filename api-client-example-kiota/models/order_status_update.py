from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .order_status_update_status import OrderStatusUpdate_status

@dataclass
class OrderStatusUpdate(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Optional reason for status change
    reason: Optional[str] = None
    # The status property
    status: Optional[OrderStatusUpdate_status] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrderStatusUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrderStatusUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrderStatusUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .order_status_update_status import OrderStatusUpdate_status

        from .order_status_update_status import OrderStatusUpdate_status

        fields: dict[str, Callable[[Any], None]] = {
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(OrderStatusUpdate_status)),
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
        writer.write_str_value("reason", self.reason)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

