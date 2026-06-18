class User:
    def __init__(self, name, id, email, password):
        self.name = name
        self.id = id
        self.email = email
        self.password = password

    def __eq__(self, user_comparison):
        if not isinstance(user_comparison, User):
            return NotImplemented
        return self.id == user_comparison.id 

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"Username: {self.name}, ID: {self.id}"

class Customer(User): 
    def __init__(self, name, id, email, password, address):
        super().__init__(name, id, email, password)
        self.address = address
        self.order_history = []

    def add_order_history(self, order):
        if order not in self.order_history:
            self.order_history.append(order)
            return f"The order with ID {order.id} was added to {self.name}'s order history."
        else: 
            return f"The order with ID {order.id} already exists in {self.name}'s order history."

    def __str__(self):
        orders_text = []
        for order in self.order_history:
            items_text = []
            for item in order.order_items_list:
                items_text.append(f"Item ID: {item.id}, Product: {item.product.name}, Quantity: {item.quantity}")    
            
            items_str = ", ".join(items_text)
            order_str = f"Order ID: {order.id} | Items: [{items_str}] | Total: {order.total}"
            orders_text.append(order_str) 
            
        formatted_orders = " | ".join(orders_text) if orders_text else "No orders yet"
        return f"Username: {self.name}, ID: {self.id}, Order History: {formatted_orders}"

    @property
    def role(self):
        return "Customer"

class Administrator(User):
    @property
    def role(self):
        return "Administrator"