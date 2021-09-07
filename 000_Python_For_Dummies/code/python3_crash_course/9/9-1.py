# -*- coding: UTF-8 -*-
class Restaurant:
  """餐馆"""

  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
  
  def describe(self):
    print(f"Restaurant name is {self.restaurant_name}")
    print(f"\nRestaurant type is {self.cuisine_type}")

  def open(self):
    print("Restaurunt is opening now!")

my_restaurant = Restaurant("ManYunXuan", "Chinese")

my_restaurant.describe()
my_restaurant.open()