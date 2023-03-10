 c = a.copy()
>>> c
[10, 12, 23, 43, 2222, 11110, [2, 100], 22222, 1000]
>>> a.append(2000)
>>> a
[10, 12, 23, 43, 2222, 11110, [2, 100], 22222, 1000, 2000]
>>> c
[10, 12, 23, 43, 2222, 11110, [2, 100], 22222, 1000]
>>> a[-4]
[2, 100]
>>> a[-4][-1]
100
>>> a[-4][-1] = 1111111
>>> c
[10, 12, 23, 43, 2222, 11110, [2, 1111111], 22222, 1000]
>>> c=a[::]
>>> a[-4][-1] = 1
>>> c
[10, 12, 23, 43, 2222, 11110, [2, 1], 22222, 1000, 2000]
>>> a[0] = 1
>>> c
[10, 12, 23, 43, 2222, 11110, [2, 1], 22222, 1000, 2000]
>>> import deepcopy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'deepcopy'
>>> import copy
>>> copy.deepcopy(a)
[1, 12, 23, 43, 2222, 11110, [2, 1], 22222, 1000, 2000]
>>> c = copy.deepcopy(a)
>>> a
[1, 12, 23, 43, 2222, 11110, [2, 1], 22222, 1000, 2000]
>>> c
[1, 12, 23, 43, 2222, 11110, [2, 1], 22222, 1000, 2000]
>>> a[0] = 100
>>> c
[1, 12, 23, 43, 2222, 11110, [2, 1], 22222, 1000, 2000]
>>> a[-4][-1] = 100000
>>> c
[1, 12, 23, 43, 2222, 11110, [2, 1], 22222, 1000, 2000]






>> a
[1, 2, 3, 4]
>>> a
[1, 2, 3, 4]
>>> b
[1, 2, 3, 4]
>>> a.append(566)
>>> a
[1, 2, 3, 4, 566]
>>> b
[1, 2, 3, 4, 566]
>>> c = a.copy()
>>> c
[1, 2, 3, 4, 566]
>>> a.append(5669)
>>>
>>> a
[1, 2, 3, 4, 566, 5669]
>>> c
[1, 2, 3, 4, 566]
>>> a.append([1111,12222])
>>> a
[1, 2, 3, 4, 566, 5669, [1111, 12222]]
>>> c
[1, 2, 3, 4, 566]
>>> c =a.copy()
>>> c
[1, 2, 3, 4, 566, 5669, [1111, 12222]]
>>> a.append([1,8])
>>> a
[1, 2, 3, 4, 566, 5669, [1111, 12222], [1, 8]]
>>> c
[1, 2, 3, 4, 566, 5669, [1111, 12222]]
>>> a[-2][-1]=7
>>> a
[1, 2, 3, 4, 566, 5669, [1111, 7], [1, 8]]
>>> c
[1, 2, 3, 4, 566, 5669, [1111, 7]]
>>> d=a[::]
>>> d
[1, 2, 3, 4, 566, 5669, [1111, 7], [1, 8]]
>>> d
[1, 2, 3, 4, 566, 5669, [1111, 7], [1, 8]]
>>> a
[1, 2, 3, 4, 566, 5669, [1111, 7], [1, 8]]
>>> a.append([999])
>>> d
[1, 2, 3, 4, 566, 5669, [1111, 7], [1, 8]]