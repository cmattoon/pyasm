"""
An example of a high-level implementation for sum.asm
"""
test = [40.5, 26.7, 21.9, 1.5, -40.5, -23.4]

print("%20.7f" % sum(test))
print("%20.7f" % sum(test[:2]))
print("%20.7f" % sum([]))
print("%20.7f" % sum(test[:3]))
