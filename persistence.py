from order import Order
from order_item import OrderItem
from product import Product
from store import Store
from datetime import datetime
import json
from user import Customer, Administrator

class Persistence:
    def __init__(self, file = "file.json"):
        self.file = file

    def save_file(self, store: Store):
        data = {
            "name" : store.name,
            "products_list" : [products.to_dict() for products in store.products_list],
            "users_list" : [users.to_dict() for users in store.users_list],
            "orders_list" : [orders.to_dict() for orders in store.orders_list],
            "save_date" : datetime.now().isoformat(),
        }
        with open(self.file,"w",encoding="utf-8") as f:
            json.dump(data, f,indent=4, ensure_ascii=False)

    def load_file(self):
        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f)
        store = Store(data["name"])
        for products_data in (data["products_list"]):
            product = Product(
                id = (products_data['id']),
                name = (products_data['name']),
                stock = (products_data['stock']),
                price = (products_data['price']),
            )
            store.products_list.append(product)

        for users_data in (data["users_list"]):
            if users_data["role"] == "Customer":
                customer = Customer(
                    name = (users_data['name']),
                    id = (users_data['id']),
                    email = (users_data['email']),
                    password = (users_data['password']),
                    address = (users_data['address']),
                )
                store.users_list.append(customer)
            elif users_data["role"] == "Administrator": 
                administrator = Administrator(
                    name = (users_data['name']),
                    id = (users_data['id']),
                    email = (users_data['email']),
                    password = (users_data['password']),
                )
                store.users_list.append(administrator)        

        for orders_data in data["orders_list"]:
            order = Order(
                id = orders_data['id'],
                customer = store.find_user_by_id(orders_data['customer_id'])
            )  

            for items in orders_data["items"]:
                order_items_list = OrderItem(
                    id = items['item_id'],
                    product = store.find_product_by_id(items['product_id']),
                    quantity = items['quantity']
                )
                order.order_items_list.append(order_items_list)

            store.create_order(order)
        return store
    

        