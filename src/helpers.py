
# utils.py
import random
import re

def validate_employee_id(role, employee_id):
    prefix = {
        'chef': '2',
        'delivery': '3',
        'food_importer': '4',
        'manager': '5'
    }
    print(f"Validating ID: {employee_id} for role: {role}")  # Debug print
    if role in prefix:
        if str(employee_id).startswith(prefix[role]):
            print("ID is valid.")  # Debug print
            return True
        else:
            print("ID does not start with the correct prefix.")  # Debug print
            return False
    else:
        print("Role is not recognized.")  # Debug print
        return False
