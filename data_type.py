def data_type(n):
    if type(n)==str:
        return len(n)
    elif n ==None:
        return 'no value'
    elif type(n)== bool:
        return n
    elif isinstance(n,list):
        if len(n)<2:
            return None
        elif len(n)>2:
            return n[2]
    elif type(n)==int:
        if n>100:
            return 'more than 100'
        elif n<100:
            return 'less than 100'
        elif n==100:
            return 'equal to 100'


"""
Define a function called data_type, to take one argument.
Compare and return results, based on the argument supplied
to the function. Complete the test to produce the perfect
function that accounts for all expectations.

For strings, return its length.
For None return string 'no value'
For booleans return the boolean
For integers return a string showing how it compares to hundred e.g.
For 67 return 'less than 100'
for 4034 return 'more than 100' or equal to 100 as the case may be
For lists return the 3rd item, or None if it doesn't exist
"""

