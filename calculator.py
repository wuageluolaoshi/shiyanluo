#!/usr/bin/env python3

import sys

lst = []
dict1 = {}
try:
    before_tax_salarys = sys.argv[1:]
    for before_tax_salary in before_tax_salarys:
        lst.append(tuple(before_tax_salary.split(":")))
    dict1 = dict(lst)
    for id, before_tax_salary in dict1.items():
        take_tax = int(before_tax_salary) - 3500 - 0.165 * int(before_tax_salary)
        if take_tax < 0:
            after_tax_salary = int(before_tax_salary) - 0.165 * int(before_tax_salary) 
            print("{}:{:.2f}".format(id,after_tax_salary))
        if 0<take_tax <= 1500:

             after_tax_salary = int(before_tax_salary) - 0.165 * int(before_tax_salary) - take_tax * 0.03
             print("{}:{:.2f}".format(id,after_tax_salary))

        if 1500 < take_tax <= 4500:
        
             after_tax_salary = int(before_tax_salary) - 0.165 * int(before_tax_salary) - take_tax * 0.1 + 105

             print("{}:{:.2f}".format(id,after_tax_salary))
        
        if 4500 < take_tax <= 9000:
        
             after_tax_salary = int(before_tax_salary) - 0.165 * int(before_tax_salary) - take_tax * 0.2 + 555

             print("{}:{:.2f}".format(id,after_tax_salary))

        if 9000 < take_tax <= 35000:
        
             after_tax_salary = int(before_tax_salary) - 0.165 * int(before_tax_salary) - take_tax * 0.25 + 1005
             print("{}:{:.2f}".format(id,after_tax_salary))

        if 35000 < take_tax <= 55000:

             after_tax_salary = int(before_tax_salary) - 0.165 * int(before_tax_salary) - take_tax * 0.3 + 2755

             print("{}:{:.2f}".format(id,after_tax_salary))

        if 55000 < take_tax <= 80000:

             after_tax_salary = int(before_tax_salary) - 0.165 * int(before_tax_salary) - take_tax * 0.35 + 5505

             print("{}:{:.2f}".format(id,after_tax_salary))


        if 80000 < take_tax:
             after_tax_salary = int(before_tax_salary) - 0.165 * int(before_tax_salary) - take_tax * 0.45 + 13505

             print("{}:{:.2f}".format(id,after_tax_salary))
   
    
except:
    print("Parameter Error")

