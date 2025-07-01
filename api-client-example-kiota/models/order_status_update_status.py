from enum import Enum

class OrderStatusUpdate_status(str, Enum):
    Pending = "pending",
    Processing = "processing",
    Shipped = "shipped",
    Delivered = "delivered",
    Cancelled = "cancelled",

