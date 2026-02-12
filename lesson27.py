# class Category:
#     """Category class"""
#     def __init__(self,category_name:str,):
#         self.category_name = category_name
#
#
#
# class Product(Category):
#     """Product class"""
#     def __init__(self ,category_name,product_name,product_price,product_count):
#         super().__init__(category_name)
#         self.product_name = product_name
#         self.product_price = product_price
#         self.product_count=product_count
#
#     def get_product_count(self):
#         return self.product_count
#
# obj1=Product('smartphones','apple',1000,20)
#
#
# class User(Product):
#     """User class"""
#     def __init__(self,category_name,product_name,product_price,product_count):
#         super().__init__(category_name,product_name,product_price,product_count)
#
#
#
