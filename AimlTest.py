import aiml
#AimlTest.py	
#	- Kernel of chat rot 
#	- setting xml for chat rot
#	- create a loop waitting question or sentence
#       - using aiml

# creat aiml.Kernel
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# pushed CTRL-C to stop the loop
while True:
	print kernel.respond(raw_input("Enter your message >> "))
