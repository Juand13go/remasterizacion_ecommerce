from order_item import OrderItem
from persistence import Persistence
from product import Product
from store import Store
from user import Customer, Administrator
from order import Order
from exceptions import  CanNotFindUserError, CanNotFindOrderError

# 1. Main system initialization (Store)
vortex = Store("Vortex")


# 2. Actors definition (Users)
customer = Customer("Juan Diego", "1035975741", "ramirezrendonjuandiego@gmail.com", "J1d2r3r4", "Calle 38#58 B79")
admin = Administrator("Natalia", "1040571701", "natys5424@gmail.com", "N1r2r3")

# 3. User registration in the Store
vortex.create_user(customer)
vortex.create_user(admin)

# 4. Product catalog creation
automation_with_n8n = Product("1", "Automation with n8n", 80, 4500000)
usb = Product("2", "USB Memory", 150, 100000)
iphone13 = Product("3", "Iphone 13", 10, 3000000)

# 5. Product registration in the Store (Requires Administrator verification)
vortex.create_product(admin, automation_with_n8n)
vortex.create_product(admin, usb)
vortex.create_product(admin, iphone13)

# 6. Order workflow and Item selection
order_item = OrderItem("1", automation_with_n8n, 2)
order = Order("1", customer)
order.add_order_item(order_item)

order_item_2 = OrderItem("2", usb, 43)
order_item_3 = OrderItem("3", iphone13, 1)
order_2 = Order("2", customer)
order_2.add_order_item(order_item_2)


# 8. Testing Search Methods (find_user_by_id, find_order_by_id)

print("\nFind User By ID TEST: ")
try:
    user_found = vortex.find_user_by_id("1035975741")
    print(f"Success Case: {user_found}")
    
    vortex.find_user_by_id("9999999999")
except CanNotFindUserError as e:
    print(f"Expected Error Case: {e}")


print("\nFind Order By ID TEST: ")
try:
    order_found = vortex.find_order_by_id("2")
    print(f"Success Case: {order_found}")
    
    vortex.find_order_by_id("404")
except CanNotFindOrderError as e:
    print(f"Expected Error Case: {e}")

# 9. Global Store state rendering
print(vortex)


persistence = Persistence()

persistence.save_file(vortex)
persistence.load_file()