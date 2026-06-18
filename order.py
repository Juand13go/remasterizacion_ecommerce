from exceptions import CanNotAddOrderItemError
from order_item import OrderItem
from user import Customer

class Order:
    def __init__(self, id: str, customer: Customer):
        self.id = id
        self.customer = customer
        self.order_items_list = []

    def __eq__(self, order_comparison):
        if not isinstance(order_comparison, Order):
            return NotImplemented
        return self.id == order_comparison.id 

    def __hash__(self):
        return hash(self.id)

    def add_order_item(self, order_item: OrderItem):
        if order_item not in self.order_items_list:
            order_item.substract_stock(order_item.product)
            self.order_items_list.append(order_item)
            return f"Order item with ID {order_item.id} was successfully added to the order."
        else:
            raise CanNotAddOrderItemError(
                f"Order item with ID {order_item.id} could not be added because it already exists in this order."
            )

    @property
    def total(self) -> float:
        return sum([item.product_cost for item in self.order_items_list])

    def __str__(self):
        order_items_str = ", ".join(
            f"[Item ID: {item.id}, Product: {item.product.name}, Quantity: {item.quantity}]" 
            for item in self.order_items_list
        )
        return f"Order ID: {self.id}, Customer: {self.customer.name}, Items: {order_items_str}, Total: {self.total}"