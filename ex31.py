#decisions decisions
print """
You enter a dark room.
Across the abyss you seen the slimmest sliver of light beneath two doors. 
Which door do you take, #1 or #2
"""

door = raw_input("> ")

if door == "1":
	print "THERE IS A FUCKING BEAR IN THE ROOM! He has cake, what do you do?"
	print "1. take the cake"
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The Cake is a Lie. Bear mauls you to death for your ignorance."
	elif bear == "2":
		print "Bear finds your feminine scream annoying. He slaughters your family."
	else:
		print "You have died of dysentery. Oregon Trail was such a good game, Bear starts playing it."
		
elif door == "2":
	print "The light was eminating from Cthulhu's eyes."
	print "1. Bluberries"
	print "2. Yellow jacket clothespins."
	print "3. UNderstanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good Job!"
	else:
		print "Insanity melts your face, raiders of the lost ark style. You have fucked up now."
		
else:
	print "You wander through the endless darkness forever. You suck at this game, User."