from variable import Variable
from function import Function
from constants import *

class Memory:
    def __init__(self):
        # Global variable addresses
        self.global_int = 5000
        self.global_double = 6000
        self.global_bool = 7000

        # Local variable addresses
        self.local_int = 9000
        self.local_double = 10000
        self.local_bool = 11000

        # Temporal variable addresses
        self.temp_int = 43000
        self.temp_double = 44000
        self.temp_bool = 45000

        # Constant variable addresses
        self.cte_int = 20000
        self.cte_double = 21000
        self.cte_bool = 22000

        # Variable counters
        self.global_int_counter = 0
        self.global_double_counter = 0
        self.global_bool_counter = 0

        self.local_int_counter = 0
        self.local_double_counter = 0
        self.local_bool_counter = 0

        self.temp_int_counter = 0
        self.temp_double_counter = 0
        self.temp_bool_counter = 0

        self.cte_int_counter = 0
        self.cte_double_counter = 0
        self.cte_bool_counter = 0
    

    def set_cte_address(self, variable):
        # Assign address for int var
        if (variable.var_type == Types.INT.value):
            address = self.cte_int + self.cte_int_counter
            self.cte_int_counter+=1
            return address
            # Assign address for double var
        elif (variable.var_type == Types.DOUBLE.value):
            address = self.cte_double + self.cte_double_counter
            self.cte_double_counter+=1
            return address
            # Assign address for bool var
        elif (variable.var_type == Types.BOOL.value):
            address = self.cte_bool + self.cte_bool_counter
            self.cte_bool_counter+=1
            return address
        
    def set_temp_address(self, variable):
        # Assign address for int var
            if (variable.var_type == Types.INT.value):
                address = self.temp_int + self.temp_int_counter
                self.temp_int_counter+=1
                return address
            # Assign address for double var
            elif (variable.var_type == Types.DOUBLE.value):
                address = self.temp_double + self.temp_double_counter
                self.temp_double_counter+=1
                return address
            # Assign address for bool var
            elif (variable.var_type == Types.BOOL.value):
                address = self.temp_bool + self.temp_bool_counter
                self.temp_bool_counter+=1
                return address

    def set_address(self, variable, function_id):
        address = -1

        # Set address for global variables
        if (function_id == "Mathrix"):
            # Assign address for int var
            if (variable.var_type == Types.INT.value):
                address = self.global_int + self.global_int_counter
                self.global_int_counter+=1
                return address
            # Assign address for double var
            elif (variable.var_type == Types.DOUBLE.value):
                address = self.global_double + self.global_double_counter
                self.global_double_counter+=1
                return address
            # Assign address for bool var
            elif (variable.var_type == Types.BOOL.value):
                address = self.global_bool + self.global_bool_counter
                self.global_bool_counter+=1
                return address
        # Set address for local variables
        else:
            # Assign address for int var
            if (variable.var_type == Types.INT.value):
                address = self.local_int + self.local_int_counter
                self.local_int_counter+=1
                return address
            # Assign address for double var
            elif (variable.var_type == Types.DOUBLE.value):
                address = self.local_double + self.local_double_counter
                self.local_double_counter+=1
                return address
            # Assign address for bool var
            elif (variable.var_type == Types.BOOL.value):
                address = self.local_bool + self.local_bool_counter
                self.local_bool_counter+=1
                return address

    # Reset local variable addresses after done reading function
    def clear_local_temp_addresses(self):
        self.local_int_counter = 0
        self.local_double_counter = 0
        self.local_bool_counter = 0

        self.temp_int_counter = 0
        self.temp_double_counter = 0
        self.temp_bool_counter = 0



    
