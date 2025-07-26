from . import my_module2 as mm2
from .my_folder_sub import my_module_sub1, my_module_sub2

class my_module1:
    def __init__(self):
        pass

    def print_my_module1(self):
        print("print_my_module1")

    def print_my_module2(self):
        temp_instance = mm2.my_module2()
        temp_instance.print_my_module2()

    def print_my_module_sub1(self):
        temp_instance = my_module_sub1()
        temp_instance.print_sub1()

    def print_my_module_sub2(self):
        temp_instance = my_module_sub2()
        temp_instance.print_sub2()
