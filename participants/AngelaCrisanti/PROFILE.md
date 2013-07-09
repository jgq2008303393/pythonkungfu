# Create an object variable
x = object()
y = object()

# Create an array which contains 10 times of it's object
x_list = [x] * 10
y_list = [y] * 10

# Big list containing x_list and y_list
big_list = (x_list + y_list)

# Check them out
print "x_list contains %d objects" % len(x_list)
print "y_list contains %d objects" % len(y_list)
print "big_list contains %d of x objects" % big_list.count(x)
print "big_list contains %d of y objects" % big_list.count(y)
print "big_list contains %d total objects" % len(big_list)