class Gadjet:
    def __init__(self, brand, color, gb, year):
        self.__brand = brand
        self.__color = color
        self.__gb = gb
        self.__year = year

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_gb(self):
        return self.__gb

    def set_gb(self, gb):
        self.__gb = gb

    def get_info(self):
        print(f"brand: {self.get_brand()}\n"
              f"color: {self.get_color()}\n"
              f"gb: {self.get_gb()}\n"
              f"year: {self.get_year()}")

#
#
# class Laptop(Gadjet):
#     def __init__(self, brand, color, gb, year):
#
#         self.__brand = brand
#         self.__color = color
#         self.__gb = gb
#         self.__year = year
#
#     def get_brand(self):
#         return self.__brand
#
#     def set_brand(self, brand):
#         self.__brand = brand
#
#     def get_color(self):
#         return self.__color
#
#     def set_color(self, color):
#         self.__color = color
#
#     def get_year(self):
#         return self.__year
#
#     def set_year(self, year):
#         self.__year = year
#
#     def get_gb(self):
#         return self.__gb
#
#     def set_gb(self, gb):
#         self.__gb = gb
#
#     def get_info(self):
#         print(f"brand: {self.get_brand()}\n"
#               f"color: {self.get_color()}\n"
#               f"gb: {self.get_gb()}\n"
#               f"year: {self.get_year()}")
#
# class Mapcase(Gadjet):
#     def __init__(self, brand, color, gb, year):
#         self.__brand = brand
#         self.__color = color
#         self.__gb = gb
#         self.__year = year
#
#     def get_brand(self):
#         return self.__brand
#
#     def set_brand(self, brand):
#         self.__brand = brand
#
#     def get_color(self):
#         return self.__color
#
#     def set_color(self, color):
#         self.__color = color
#
#     def get_year(self):
#         return self.__year
#
#     def set_year(self, year):
#         self.__year = year
#
#     def get_gb(self):
#         return self.__gb
#
#     def set_gb(self, gb):
#         self.__gb = gb
#
#     def get_info(self):
#         print(f"brand: {self.get_brand()}\n"
#               f"color: {self.get_color()}\n"
#               f"gd: {self.get_gb()}\n"
#               f"year: {self.get_year()}")
#
redmi = Gadjet("Redmi", "Blue", "32", "2016")
# laptop = Laptop("lenovo", "grey", "128", "2014")
# plansh = Mapcase("iphone", "white", "64", "2018")