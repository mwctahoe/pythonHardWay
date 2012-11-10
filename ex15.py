from sys import argv

script, filename = argv

txt = open(filename)

print "here's your stinking file %r:" % filename
print txt.read()

print "Type that filename again:"
file_again=raw_input("> ")

txt_again = open(script)

print txt_again.read()