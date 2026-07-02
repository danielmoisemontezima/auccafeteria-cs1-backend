'''
======================================================
                   STAFF ENTITIE HERE
======================================================
'''
"""
HOMEWORK GROUP:
                EDMOND Dorhys H. Kelly
                CORNEt Ezna
                BOUZY Worlder
"""
from dataclasses import dataclass,field
from enum import Enum
import uuid

class StaffRole(Enum):
    MANAGER = "manager"
    CHEF = "chef"

@dataclass
class Staff:
    name: str
    role: StaffRole
    id: str= field(default_factory=lambda: str(uuid.uuid4()))
    in_service : bool = True
    products: list = field(default_factory=list)

    def __post_init__(self)->None:
        self.validate()

    def validate(self)->None:
        if not self.name or self.name.strip()== "" :
           raise ValueError("[error] Your name cannot be empty.")
    
    def is_allowed_in_kitchen(self)->bool:
        if self.role in [StaffRole.MANAGER, StaffRole.CHEF]:
            return True
        else:
            return False
            
    def add_product(self, product: str)->None:
        product = product.lower()
        if product not in self.products:
            self.products.append(product)
        else:
            raise ValueError("This product has already been added.")    
    
    def remove_product(self, product: str)->None:
        product = product.lower()
        if product not in self.products:
            raise ValueError("Product not found.")
    
        self.products.remove(product)
        
    def set_product(self, old_product: str, new_product: str)-> None:
        old_product = old_product.lower()
        new_product = new_product.lower()
        
        if old_product not in self.products:
            raise ValueError("Product not found.")
        
        if new_product in self.products:
            raise ValueError("This product has already been added.")
        
        old_product_position = self.products.index(old_product)
        self.products[old_product_position]= new_product


