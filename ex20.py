from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(f, line_count):
	print line_count, f.readline()
	
current_file = open(input_file)

print "first print the whole file:\n"

print_all(current_file)

print "now we rewind"
rewind(current_file)

print "lets print three lines:"
current=1
print_a_line(current_file, current)
current+=1
print_a_line(current_file, current)
current+=1
print_a_line(current_file, current)