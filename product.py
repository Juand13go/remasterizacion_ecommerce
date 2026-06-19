class Product:
    def __init__(self, id: str, name: str, stock: int, price: float):
        self.id = id
        self.name = name
        self.stock = stock
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.id == other.id 

    def __hash__(self):
        return hash(self.id)

    def to_dict(self):
        return {
            "id" : self.id, 
            "name" : self.name,
            "stock" : self.stock,
            "price" : self.price
        }

    @property
    def is_available(self) -> bool:
        return self.stock > 0

    def __str__(self):
        return f"Product ID: {self.id}, Product Name: {self.name}, Price: {self.price}"