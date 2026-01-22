class GM:
    """Gm mashinalarining ma'lumoti"""
    count=0

    @staticmethod
    def change_price_sum(dollar,narx):
        data=dollar*narx
        return data

    def __new__(cls,*args,**kwargs):
        # print(cls)
        # print(args)
        # print(kwargs)
        instanse=super().__new__(cls)
        # print(type(instanse))
        return instanse

    def __init__(self, model, color, price, year):
        self.model = model
        self.color = color
        self.price = price
        self.year = year

    def get_model(self):
        return self.model

    def get_info(self):
        return f"Model {self.model}, color: {self.color}, price: {self.price}, year: {self.year}"

    def update_price(self,new_price):
        if new_price<0:
            print("Narx manfiy bo'lmaydi!!!")
        else:
            self.price = new_price

    def update_year(self):
        self.year += 1


obj=GM("cobalt",'white',14000,2026)
# print(obj.get_model() )
obj.update_price(-18000)
obj.update_year()

print(obj.get_info())