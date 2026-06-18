from exceptions import (
    CanNotCreateProductError, 
    CanNotCreateUserError, 
    CanNotCreateOrderError, 
    CanNotFindOrderError, 
    CanNotFindProductError, 
    CanNotFindUserError
)
from product import Product
from user import Administrator, Customer, User
from order import Order

class Store:
    def __init__(self, name: str):
        self.name = name
        self.products_list = []
        self.users_list = []
        self.orders_list = []

    def create_product(self, user: User, product: Product):
        if not isinstance(user, Administrator):
            raise CanNotCreateProductError (f"User '{user.name}' cannot create products because he's not an administrator.")
        
        if product in self.products_list:
            raise CanNotCreateProductError (f"The product {product.name} already exists in the products list.")

        self.products_list.append(product)
        return f"Product '{product.name}' successfully created by administrator {user.name}."
        
    def create_user(self, user: User):
        if user in self.users_list:
            raise CanNotCreateUserError(f"User '{user.name}' already exists.")

        self.users_list.append(user)
        return f"User '{user.name}' was successfully created."

    def create_order(self, order: Order):
        if not isinstance(order.customer, Customer):
            raise CanNotCreateOrderError (
                f"Order with ID {order.id} is invalid. Orders can only belong to Customers, "
                f"but this order belongs to a {type(order.customer).__name__}."
            )

        if order in self.orders_list:
            raise CanNotCreateOrderError(f"Order with ID {order.id} could not be created. Please verify the parameters.")

        self.orders_list.append(order)
        order.customer.add_order_history(order)
        return f"Order with ID {order.id} was successfully created."

    def find_product_by_id(self, id: str):
        for product in self.products_list:
            if product.id == id:
                return (product)
        
        raise CanNotFindProductError(f"Product with'{id}' does not exist in our catalog.")

    def find_user_by_id(self, user_id: str):
        for user in self.users_list:
            if user.id == user_id:
                return (user)
        
        raise CanNotFindUserError(f"User with ID {user_id} does not exist in our records.")

    def find_order_by_id(self, order_id: str):
        for order in self.orders_list:
            if order.id == order_id:
                return (order)
        
        raise CanNotFindOrderError(f"Order with ID {order_id} does not exist in our records.")

    def __str__(self):
        products = "\n" + ", ".join([f"Product name: {p.name}, Price: {p.price}" for p in self.products_list]) + "\n"
        users = ", ".join([str(user).strip() for user in self.users_list]) + "\n"
        orders = ", ".join([str(order).strip() for order in self.orders_list])
        return f"Store Name: {self.name}{products}{users}{orders}\n"