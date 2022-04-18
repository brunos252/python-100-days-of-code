# Errors, JSON

# FileNotFound - opening non-existent file
# KeyError - key does not exist
# IndexError - [i] where it doesnt exist
# TypeError - cant do that with that data type

# catching exceptions - we decide what happens
# try - except - else - finally
# try - code that might cause exception
# except - when exception occurs
# else - if there were no exceptions
# finally - no matter what happens
try:
    file = open("file.txt")
except FileNotFoundError:
    file = open("file.txt", "w")
except KeyError as error_message:   # use generated error message
    print("no key")
else:
    # no exceptions
    content = file.read()
    print(content)
finally:
    # not often used
    file.close()

# PEP 8 - should avoid bare "except:"
# can have multiple except

# finally use cases: if except has a return statement, finally is
# called before return
#      - if there is an exception inside the except block
#      - if another error is thrown in try
#      - continue and break statements
#      - make sure that files are closed, even if we dont catch exception

# raise - your own exception
raise TypeError("This is an error I made up")


# JSON - similar to dict, has key-value data structure
# in-built JSON library:
# json.dump(), json.load(), json.update()
# load reads it into a dictionary

# usually shoud have try outside of opening file

