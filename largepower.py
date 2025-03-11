def large_power(base,exponent):
    result=base**exponent

    if (result>500):
        return True
    else:
        return False
print(large_power(2,4))