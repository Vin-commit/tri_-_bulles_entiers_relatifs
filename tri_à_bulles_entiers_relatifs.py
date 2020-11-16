#!/usr/bin/python3
# coding: utf-8
 
def triBulles(lst):
  for i in range(len(lst)):
    k = i
    while (k > 0 and lst[k-1] > lst[k]):
      lst[k-1], lst[k] = lst[k], lst[k-1]
      k = k - 1
      return lst
      
lst = [1, -7, 10, 4, 2, 3, -5, 9, 6, 8, 6, 0]
print (“Liste d’entiers relatifs avant le tri :”, lst)
print (“Liste d’entiers relatifs après le tri :”, triBulles(lst))


-------------------------------------------------------------------------------- Résultat --------------------------------------------------------------------------------------