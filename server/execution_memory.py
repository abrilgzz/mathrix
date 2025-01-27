# coding=utf-8
from fastnumbers import fast_real
from functions_table import Variable
from constants import Types

class ExecutionMemory(object):
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

        # Storing variables in memory dictionary, for global and local variables
        self.memory = {}
        self.memory['global'] = {}

        self.memory['global']['var'] = {}
        self.memory['global']['temp'] = {}
        self.memory['global']['cte'] = {}  

        self.memory['global']['var']['int'] = {}
        self.memory['global']['var']['double'] = {}
        self.memory['global']['var']['bool'] = {}

        self.memory['global']['temp']['int'] = {}
        self.memory['global']['temp']['double'] = {}
        self.memory['global']['temp']['bool'] = {}

        self.memory['global']['cte']['int'] = {}
        self.memory['global']['cte']['double'] = {}
        self.memory['global']['cte']['bool'] = {}

        self.memory['local'] = {}

    # Function that retrieves the value for an address by checking the address for the memory location
    def get_variable_value(self, address, current_function):
        # DEBUGGING
        # print("address: ", address)
        #print("current_function: ", current_function)
        # Check if address given is a constant to return this as value
        if self.is_constant(address):
            address = self.convert_constant(address)
            return int(address)

        # Check if address is a reference to another address
        if self.is_address_reference(address):
            address = int(self.dereference(address, current_function))
            
        # Global variables
        if (5000 <= address <= 8999):
            if(5000 <= address <= 5999):
                return int(self.memory['global']['var']['int'][address])
            elif(6000 <= address <= 6999):
                return float(self.memory['global']['var']['double'][address])
            elif(7000 <= address <= 7999):
                return self.memory['global']['var']['bool'][address]
        # Global Constant variables
        if (20000 <= address <= 22999):
            if(20000 <= address <= 20999):
                return int(self.convert_constant(self.memory['global']['cte']['int'][address]))
            elif(21000 <= address <= 21999):
                return float(self.convert_constant(self.memory['global']['cte']['double'][address]))
            elif(22000 <= address <= 22999):
                return self.convert_constant(self.memory['global']['cte']['bool'][address])   
        elif(current_function == 'Mathrix'):
            # Global Temp variables
            if (43000 <= address <= 45999):
                if(43000 <= address <= 43999):
                    return int(self.memory['global']['temp']['int'][address])
                elif(44000 <= address <= 44999):
                    return float(self.memory['global']['temp']['double'][address])
                elif(45000 <= address <= 45999):
                    return self.memory['global']['temp']['bool'][address]
        else:
            # Local variables
            if (9000 <= address <= 11999):
                if(9000 <= address <= 9999):
                    return int(self.memory['local'][current_function]['var']['int'][address])
                elif(10000 <= address <= 10999):
                    return float(self.memory['local'][current_function]['var']['double'][address])
                elif(11000 <= address <= 11999):
                    return self.memory['local'][current_function]['var']['bool'][address]
            # Temp variables
            if (43000 <= address <= 45999):
                if(43000 <= address <= 43999):
                    return int(self.memory['local'][current_function]['temp']['int'][address])
                elif(44000 <= address <= 44999):
                    return float(self.memory['local'][current_function]['temp']['double'][address])
                elif(45000 <= address <= 45999):
                    return self.memory['local'][current_function]['temp']['bool'][address]


    # Function that writes into memory map, with address as key and result as value
    def write_to_memory(self, address, result, current_function):
        # DEBUGGING
        # print("****writing to memory****")
        # print("address: ", address)
        # print("result: ", result)
        # print("result type: ", type(result))
        # print("current_function: ", current_function)
        # print("memory: ", self.memory)

        if self.is_address_reference(address):
            address = address[:-1]
            address = address[1:]
            address = int(address)
            address = self.get_variable_value(address, current_function)
            # print("real_address: ", address, "result: ", result)
        
        # Global variables
        if (5000 <= address <= 8999):
                if(5000 <= address <= 5999):
                    if isinstance(result, (int, float)):
                        result = int(result)
                    self.memory['global']['var']['int'][address] = result
                elif(6000 <= address <= 6999):
                    self.memory['global']['var']['double'][address] = result
                elif(7000 <= address <= 7999):
                    self.memory['global']['var']['bool'][address] = result
        # Global Constant variables
        elif (20000 <= address <= 22999):
                if(20000 <= address <= 20999):
                    if isinstance(result, (int, float)):
                        result = int(result)
                    self.memory['global']['cte']['int'][address] = result
                elif(21000 <= address <= 21999):
                    self.memory['global']['cte']['double'][address] = result
                elif(22000 <= address <= 22999):
                    self.memory['global']['cte']['bool'][address] = result
        elif(current_function == 'Mathrix'):
            # Global Temp variables
            if (43000 <= address <= 45999):
                if(43000 <= address <= 43999):
                    if isinstance(result, (int, float)):
                        result = int(result)
                    self.memory['global']['temp']['int'][address] = result
                elif(44000 <= address <= 44999):
                    self.memory['global']['temp']['double'][address] = result
                elif(45000 <= address <= 45999):
                    self.memory['global']['temp']['bool'][address] = result
        else:
            # Local variables
            if (9000 <= address <= 11999):
                if(9000 <= address <= 9999):
                    if isinstance(result, (int, float)):
                        result = int(result)
                    self.memory['local'][str(current_function)]['var']['int'][address] = result 
                elif(10000 <= address <= 10999):
                    self.memory['local'][str(current_function)]['var']['double'][address] = result
                elif(11000 <= address <= 11999):
                    self.memory['local'][str(current_function)]['var']['bool'][address] = result
            # Local Temp variables
            elif (43000 <= address <= 45999):
                if(43000 <= address <= 43999):
                    if isinstance(result, (int, float)):
                        result = int(result)
                    self.memory['local'][str(current_function)]['temp']['int'][address] = result 
                elif(44000 <= address <= 44999):
                    self.memory['local'][str(current_function)]['temp']['double'][address] = result
                elif(45000 <= address <= 45999):
                    self.memory['local'][str(current_function)]['temp']['bool'][address] = result

    # Function that writes parameters to memory as local variables for a given function
    def write_param_to_memory(self, param_type, param_number, param, function_counter):
        address = int(param_number) + 9000

        if param_type == Types.INT.value:
            var_type = 'int'
            param = int(param)
        elif param_type == Types.DOUBLE.value:
            var_type = 'double'
            param = int(param)
        if param_type == Types.BOOL.value:
            var_type = 'bool'

        # DEBUGGING
        # print("function_counter: ", function_counter)
        # print(self.memory['local'][str(function_counter-1)]['var'])
        # print(self.memory['local'][str(function_counter-1)]['var'][var_type])
        #print(self.memory['local'][str(function_counter-1)]['var'][var_type][address])
        self.memory['local'][str(function_counter-1)]['var'][var_type][address] = param

    # Function that clears memory map for a local function
    def clear_memory(self, function):
        self.memory['local'][function].clear()

    # Function that clears entire memory map
    def end_program(self):
        self.memory.clear()
    
    # Function that creates local memory map for a given function
    def start_local_memory(self, local_vars_quad, temp_vars_quad, function_counter):
        self.memory['local'][str(function_counter)] = {}

        self.memory['local'][str(function_counter)]['var'] = {}
        self.memory['local'][str(function_counter)]['var']['int'] = {}
        self.memory['local'][str(function_counter)]['var']['double'] = {} 
        self.memory['local'][str(function_counter)]['var']['bool'] = {}

        self.memory['local'][str(function_counter)]['temp'] = {}
        self.memory['local'][str(function_counter)]['temp']['int'] = {}
        self.memory['local'][str(function_counter)]['temp']['double'] = {}
        self.memory['local'][str(function_counter)]['temp']['bool'] = {}

    # Function that writes Global variables to global memory map
    def start_global_memory(self, vars_directory):
        for v in vars_directory:
            variable = vars_directory[v]
            # DEBUGGING
            # print("adding ", variable, " to memory")
            if self.is_matrix(variable) and variable.var_type != Types.BOOL.value:
                self.create_matrix(variable, 'Mathrix')
            else:
            # Atomic variables
                # Global variables
                if(5000 <= variable.var_address <= 8999):
                    if(variable.var_type == Types.INT.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                    if(variable.var_type == Types.DOUBLE.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                    if(variable.var_type == Types.BOOL.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                # Constant variables
                elif (20000 <= variable.var_address <= 22999):
                    if(variable.var_type == Types.INT.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                    if(variable.var_type == Types.DOUBLE.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                    if(variable.var_type == Types.BOOL.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                # Temp variables
                elif (43000 <= variable.var_address <= 45999):
                    if(variable.var_type == Types.INT.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                    if(variable.var_type == Types.DOUBLE.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
                    if(variable.var_type == Types.BOOL.value):
                        self.write_to_memory(variable.var_address, variable.var_id, 'Mathrix')
            
    # Function that determines if a variable is a matrix
    # by checking if it has a dimension directory
    def is_matrix(self, variable):
        if variable.var_dim1_dict != 0:
            return True

    # Function that initializes the needed spaces in memory for a given matrix
    def create_matrix(self, variable, current_function):
        # print("variable address: ", variable.var_address)
        spaces_needed = self.calculate_m0(variable)
        counter = 0

        for x in range(0, spaces_needed):
            self.write_to_memory(variable.var_address + counter, 0, current_function)
            counter+=1

    # Function that calculates m0 = the amount of spaces needed to store the given matrix
    def calculate_m0(self, variable):
        # Formulas for 2 dimensional arrays
        r1 = 1 * (variable.var_dim1_dict.lim_s - 0 + 1)
        m0 = r1 * (variable.var_dim2_dict.lim_s - 0 + 1)
        return m0

    # Function that checks if value is constant
    # by checking if the value has a #
    def is_constant(self, value):
        value = str(value)
        if '#' in value:
            return True

    # Function that converts constants (int or float)
    def convert_constant(self, value):
        number = fast_real(value[1:])
        return number

    # Function that determines if an address is a reference to another address
    # by checking if the value has parenthesis
    def is_address_reference(self, value):
        value = str(value)
        if '(' in value:
            #print("is reference")
            return True

    # Function that de-references an address by removing parenthesis and 
    # checking in the memory map the value for this address key
    def dereference(self, address_ref, current_function):
        # print("address_ref: ", address_ref)
        address_ref = address_ref[:-1]
        address_ref = address_ref[1:]
        address_ref = int(address_ref)

        real_address = self.get_variable_value(address_ref, current_function)
        #print("real_address: ", real_address)
        return real_address


