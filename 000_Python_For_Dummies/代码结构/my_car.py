from car import Car 
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# 修改属性的值
# 1. 直接改，不安全
my_new_car.odometer_reading = 1000 
my_new_car.read_odometer()

# 2. 通过class的方法改
my_new_car.update_odometer(200)
my_new_car.read_odometer()