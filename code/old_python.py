print "Hello, World!"

# Unicode string
unicode_string = u"Hello"
print unicode_string

# Byte string
byte_string = "Hello"
print byte_string

# xrange for efficient iteration
for i in xrange(5):
    print i

# Handling exceptions
# Python 2.7 code example with try block

try:
    # Attempt to open a file that does not exist
    with open('nonexistent_file.txt', 'r') as f:
        content = f.read()
    # Attempt to divide by zero
    result = 10 / 0
except IOError, e:  # Handling IOError
    print "Error: Could not read file -", e
except ZeroDivisionError, e:  # Handling ZeroDivisionError
    print "Error: Division by zero -", e
else:
    # If no exceptions were raised, execute this block
    print "File read successfully."
    print "Result of division:", result
finally:
    # Cleanup code that runs whether an exception occurred or not
    print "Cleaning up resources..."


# Dictionary methods returning lists
my_dict = {'a': 1, 'b': 2}
print my_dict.keys()
print my_dict.values()
print my_dict.items()
