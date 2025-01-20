product_name, product_code = input().split()
product_code = int(product_code)

# Write your code here!

class Product:
    def __init__(self, product_name="codetree", product_code=50):
        self.product_name = product_name
        self.product_code = product_code
    
    def set_product(self, product_name, product_code):
        self.product_name = product_name
        self.product_code = product_code

    def print(self):
        print(f"product {self.product_code} is {self.product_name}")
    
product = Product()

product.print()

product.set_product(product_name, product_code)

product.print()