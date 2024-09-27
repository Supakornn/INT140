# 041 Supakorn Ieamgomol
# 043 Somchai Wantaeng
# 050 Sirinda Charoenwai
# 051 Siriyakon Sangkaew

"""write a function to convert kms to miles
- allow only int or float as input parameter
- raise TypeError("Only int or float") if input parameter is a wrong type
- raise ValueError("Only Non-Negative Value") if input parameter is less than 0
- convert km to miles and return float"""
def km_to_miles(km):
    if not isinstance(km, (int, float)): 
        raise TypeError("Only int or float")
    if km < 0:
        raise ValueError("Only Non-Negative Value")
    
    return km * 0.621371192


"""write a function to check if a string 
has duplicate characters next to each other
- allow only str as input parameter
- raise TypeError if input validation fails
- return bool: True/False
- use while/for loop"""
def consecutive_char(string):
    if not isinstance(string, str):
        raise TypeError("Only string")
    
    for i in range(len(string) -1 ):
        if string[i] == string[i+1]:
            return True
    return False


"""write a function to check if a string 
has duplicate characters
- allow only str as input parameter
- raise TypeError if input validation fails
- return bool: True/False
- use nested while/for loop"""
def duplicate(string):
    if not isinstance(string, str):
        raise TypeError("Only string")
    
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return True
    return False

"""write a function to find the maximum value of the three int parameters
- allow only int as input parameter
- raise TypeError if input validation fails
- return the maximum value of the three values
- use only comparison: <, >, <=, >=, !=, ==
- not allow the use of lists or any function
- multiple parameters with the same value has no effect to the return value"""
def max_value(x,y,z):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
        raise TypeError("Only int")
    
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z