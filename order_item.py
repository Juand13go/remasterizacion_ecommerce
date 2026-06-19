from product import Product

class OrderItem:
    def __init__(self, id: str, product: Product, quantity: int):
        self.id = id
        self.product = product
        self.quantity = quantity

    def to_dict(self):
        return{
            "item_id" : self.id,
            "product_id" : self.product.id,
            "quantity" : self.quantity
        }

    @property
    def product_cost(self) -> float:
        return self.product.price * self.quantity

    def substract_stock(self, product):
        product.stock = product.stock - self.quantity
        return f"Stock: {product.stock}"

    def __str__(self):
        return f"Item ID: {self.id} | Product: {self.product.name} | Quantity: {self.quantity} | Subtotal: {self.product_cost}"