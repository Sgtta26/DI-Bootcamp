# Exception = Error

data = '&@$U%DHJ!#'

# ValueError, TypeError, AssertionError

# ValueError = correct type but incorrect value (got 10, expected 5)
# TypeError = incorrect type (got float, expected string)
# AssertionError = correct value, but incorrect result (got 100 (50+50), expected 99)

if '%' in data:
    raise AssertionError("Bug in the system!")