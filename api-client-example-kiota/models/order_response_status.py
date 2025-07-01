from enum import Enum

class OrderResponse_status(str, Enum):
    Pending = "pending",
    Processing = "processing",
    Shipped = "shipped",
    Delivered = "delivered",
    Cancelled = "cancelled",

