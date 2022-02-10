import sys

#print(sys.argv)
args = sys.argv[1:]
print(args)

"""
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

새로운 크로스 플랫폼 PowerShell 사용 https://aka.ms/pscore6

PS C:\pyworks> cd day26
PS C:\pyworks\day26> python sys_ex.py
['sys_ex.py']
PS C:\pyworks\day26> python sys_ex.py dog cat
['sys_ex.py', 'dog', 'cat']
PS C:\pyworks\day26> python sys_ex.py dog cat
['dog', 'cat']
PS C:\pyworks\day26>

"""