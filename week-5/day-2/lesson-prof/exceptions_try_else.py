try:
    user_in = int(input("Provide a number: "))
    if user_in > 10:
        pass
    else:
        raise AssertionError("number is less than 10")

except ValueError:
    print("Invalid data flow")
    
except AssertionError:
    print("Invalid number")
    
finally:
    print("FINISHING PROGRAM")