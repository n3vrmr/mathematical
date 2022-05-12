# -*- coding: utf-8 -*-
"""
Created on Thu May 12 08:17:09 2022

@author: Nevermore
"""
from decimal import Decimal

def golden(x):
    x >= 2
    values = [0,1]
    for i in range(2,x):
        values.append(values[i-1] + values[i-2])
        reason = max(values)/values[i-1]
    print(Decimal(reason))
    return reason

def main():
    print("Au,79")

if __name__ == '__main__':
    main()
    golden(10000)