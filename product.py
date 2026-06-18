class Product:
    def __init__(self, id: str, name: str, stock: int, price: float):
        self.id = id
        self.name = name
        self.stock = stock
        self.price = price

    def __eq__(self, product_comparison):
        if not isinstance(product_comparison, Product):
            return NotImplemented
        return self.id == product_comparison.id 

    def __hash__(self):
        return hash(self.id)

    @property
    def is_available(self) -> bool:
        return self.stock > 0

    def __str__(self):
        return f"Product ID: {self.id}, Product Name: {self.name}, Price: {self.price}"