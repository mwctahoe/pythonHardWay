formatter = "%r %r %r %r"

print formatter %(1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("They had a broken keyboard", 
					"bought a broken keyboard",
					"I bought a ski blanket",
					"then I bought a kneeboard"
)