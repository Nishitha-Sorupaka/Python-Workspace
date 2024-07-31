#MultableDemo.py
from MulTable import table
from invalid import InvalidInputError,ZeroError

try:
    table()
except InvalidInputError:
    print("Do not enter Negative Number!")
except ZeroError:
	print("Do not enter Zero!")
except ValueError:
    print("Do not enter strs, symbols, alpha-numerics")



