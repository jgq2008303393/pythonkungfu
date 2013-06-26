#!/usr/bin/env python

from pymongo import Connection

databaseName = "sample_database"
connection = Connection()

db = connection[databaseName]
employees = db['employees']

person1 = {"name": "John Doe", "age": 25, "dept": 101, "languages": ["English", "German", "Japanese"]}
person2 = {"name": "Jane Doe", "age": 25, "dept": 102, "languages": ["English", "Spanish", "French"]}

print "clearing"
employees.remove()

print "saving"
employees.save(person1)
employees.save(person2)

obj = employees.find({"age": 25})


def extract(obj):
    for (x, y) in enumerate(obj):
        for i in y:
            if type(y[i]) == list:
                for x in xrange(0, len(y[i])):
                    print "%s --- %s" % (i, y[i][x])
            else:
                print "%s --- %s" % (i, y[i])

extract(obj)
