# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:34:44 2023

@author: Nevermore
"""
from math import sqrt

class Divisors:
    def __init__(self,natural_int:int):
        self.natural_int = natural_int
        return
        

    def n_divisors(self):
        self.divisors = []
        for i in range(1, int(sqrt(self.natural_int))+1):
            if self.natural_int % i == 0:
                self.divisors.append(i)
                self.divisors.append(self.natural_int//i)
        self.divisors.sort()
        self.number_divisors = len(self.divisors)
        return self.number_divisors
    
n = Divisors(2048)