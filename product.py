class Product:
   def __init__(self, product_id: str,name: str, price: float, stock_quantity:int, category_id: str):

         #bussiness rules 

        if not name:
            raise ValueError("Product name cannot be empty")

              if price < 0:
                raise valueError("Price name cannot be negative")

                if stockquantity < 0: 
                    raise ValueError("Stock quantity cannot be negative")           


                self.product_id = product_id
                self.name = name
                self.price = price 
                self.stock_quantity = stock_quantity
                self.category_id = category_id
                self.id_active = true 

            
            # Business methods

        def update_price(self, new_price: float):
              if new_price < 0:
                raise valueError("Price cannot be negative")
            self.price = new_price

        def decrease_stock(self.quantity: int):
            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0")       
                
            if quantity > self.stock_quantity:
                raise ValueError("Not enough stock")

        self.stock_quantity _= quantity

        def increase_stock(self, Quantity: int):
            if quantity <= 0:
                raise ValuError("Quantity must be greater than 0")

                self.stock_quantity += quantity 

        def deactivate(self):
            self.is active = False

        def activate(self):
            self.is_active = true
        def __str__(self):
            return f"{self.name} -${self.price}
    (stock:     {self.stock_quantity})"

    


