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
    if role in prefix:
        if str(employee_id).startswith(prefix[role]):
            return True
        else:
            return False
    else:
        return False
