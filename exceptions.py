class StoreError(Exception):
    pass

class CanNotCreateProductError(StoreError):
    pass

class CanNotCreateUserError(StoreError):
    pass

class CanNotCreateOrderError(StoreError):
    pass

class CanNotAddOrderItemError(StoreError):
    pass

class CanNotFindProductError(StoreError):
    pass

class CanNotFindUserError(StoreError):
    pass

class CanNotFindOrderError(StoreError):
    pass