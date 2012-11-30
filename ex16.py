from sys import argv

script, filename = argv

print "We're gonna erase %r" % filename
print "if you dont want that, hit ctrl-c (^C)."
print "if you do want that hit return."

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("ah one: ")
line2 = raw_input("ah twooo: ")
line3 = raw_input("three CRUNCH:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And now, we close the file"
target.close()