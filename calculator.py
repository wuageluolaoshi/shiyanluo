#!/usr/bin/env python3

import sys

try:
    salary = int(sys.argv[1])
    if 3500 <= salary <= 5000:
        tax = (salary - 3500) * 0.03
        print('{:.2f}'.format(tax,))

    elif 5000 < salary <= 8000:
        tax = (salary - 3500) * 0.1 - 105
        print('{:.2f}'.format(tax))
   
    elif 8000 < salary <= 12500:
        tax = (salary - 3500) * 0.2 - 555
        print('{:.2f}'.format(tax))
    elif 12500 < salary <= 38500:
        tax = (salary - 3500) * 0.25 - 1005
        print('{:.2f}'.format(tax))
    elif 38500 < salary <= 58500:
        tax = (salary - 3500) * 0.3 -2755
        print("{:.2f}".format(tax))
    elif 58500 < salary <= 83500:
        tax = (salary - 3500) * 0.35 - 5505
        print('{:.2f}'.format(tax))
    elif 83500 < salary:
        tax = (salary - 3500) * 0.45 -13505
        print("{:.2f}".format(tax))
    else:
        raise ValueError()
except:
    print("Parameter Error")

