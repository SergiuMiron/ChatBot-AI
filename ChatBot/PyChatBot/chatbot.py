import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("startup.xml")
kernel.respond("load aiml b")

session = 1
user1 = {}
user2 = {}

# Press CTRL-C to break this loop
while True:
    #print kernel.respond(raw_input("Enter your message >> "))
    message = kernel.respond(raw_input(">>"),session)
    if message == "Bye" or message == "See you later":
        sessionData = kernel.getSessionData(session)
        print message
        if session == 1:
            user1['name'] = sessionData['name']
            user1['age'] = sessionData['age']
            user1['job'] = sessionData['job']
        else:
            user2['name'] = sessionData['name']
            user2['age'] = sessionData['age']
            user2['job'] = sessionData['job']
        if session == 1:
            session = 2
        else:
            session=1
    else:
        if message == "Hmm...":
            if (session == 1 and user2.has_key('name')) or (session == 2 and user1.has_key('name')):
                if session == 1:
                    numele = user2['name']
                if session == 2:
                    numele = user1['name']
                print message+" I've talked with "+ numele +" before"
            else:
                print message+" You are the first I talk to"
        else:
            print message