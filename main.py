"""
An email-based version of Secret Hitler
Author: redd, bryan.d.redd@gmail.com
"""

#%%
import smtplib
import random

sendemails = False # True sends emails, false prints information for testing
gamenumber = random.randint(100, 999) # Game ID for clarity
policydict = {'l': 'Liberal', 'f': 'Fascist'}
roles = ['h','f','l','l','l','l','f','l','f','l'] # the order in which roles are assigned

sender_email = "" # enter the email that will be used to send emails
sender_email_password = "" # enter your password

emaildict = {
    # enter "Name" : "username@email.com" for each player
} 

# These names should match the keys of emaildict
players = ["Bryan",
    "Kristen",
    "Bryant",
    "Haley",
    "Josh",
    "Jackson",
    "Monica"
]

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    '''
    Send an email
    '''
    header = ''
    header += 'From: %s\n' % (from_addr)
    # header += 'To: ' + to_addr_list + '\n'
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n' % subject

    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

def sendRole(player, msg):
    """
    Send an email with the player's role
    """
    if sendemails:
        sendemail(
            "Secret Hitler quaranteam.game@gmail.com",
            [emaildict[player]],
            [""],
            "Secret Role for Game #" + str(gamenumber),
            msg,
            sender_email,
            sender_email_password
        )
    else:
        print(player + ": " + msg)

def assignRoles(players):
    """
    Assign players' roles, and send them emails
    """

    random.shuffle(players)

    seating_msg = "The succession of the presidency will occur in the following order:\n"
    for i in range(0, len(players)):
        seating_msg += players[i] + "\n"

    random.shuffle(players)

    for i in range(0, len(players)): 
        msg = "\n\nTHIS IS NOT A DRILL. Please join our Zoom meeting at https://byu.zoom.us/j/6268068326. We will begin shortly.\n\n"
        if roles[i] == 'h':
            msg += "You are the Secret, Socially-Distanced Hitler."
            if len(players) <= 6:
                msg += " The other fascist is " + players[1] + "."
            msg += "\n\n"
        elif roles[i] == 'f':
            msg += "You are a socially-distanced fascist. " + players[0] + " is Secret Hitler.\n\n"
        elif roles[i] == 'l':
            msg += "You are a socially-distanced liberal. Find the Secret Hitler!\n\n"

        msg += seating_msg + "\n"

        sendRole(players[i], msg)

    return players

def startgame(players):
    """
    Start the game
    """
    players = assignRoles(players)
    deck = initPolicyDeck()
    return deck, players

def sendPolicyCards(player, policies, codes):
    """
    Send the policy cards
    """

    msg = "You have received the following policy cards:\n"
    for i in range(0,len(policies)):
        msg += str(i+1) + ". " + policydict[policies[i]] + "\n"

    if len(policies) == 3:
        msg += "To DISCARD the first and PASS the second and third, say " + str(codes[0]) + ".\n"
        msg += "To DISCARD the second and PASS the first and third, say " + str(codes[1]) + ".\n"
        msg += "To DISCARD the third and PASS the first and second, say " + str(codes[2]) + ".\n"
    else:
        msg += "To enact the first policy, say " + str(codes[1]) + ".\n"
        msg += "To enact the second policy, say " + str(codes[0]) + ".\n"

    if sendemails:
        sendemail(
            "Secret Hitler quaranteam.game@gmail.com",
            [emaildict[player]],
            [""],
            "Policy Cards for Game #" + str(gamenumber),
            msg,
            sender_email,
            sender_email_password
        )
    else:
        print(msg)

def initPolicyDeck():
    """
    Creates a shuffled deck of policy cards
    """
    deck = ['f','f','f','f','f','f','f','f','f','f','f','l','l','l','l','l','l']
    random.shuffle(deck)
    return deck

def randomIntObfuscate():
    """
    Creates a random-ish number so that players can verbally pass cards without anyone knowing what's being passed.
    """
    return int((random.randint(0, 2**9-1) << 4) + random.randint(0, 1))

def drawThree(player, deck):
    """
    For the president to draw three policy cards
    Also creates the randomish numbers as option IDs
    """
    first = int(0b1000) + randomIntObfuscate()
    second = int(0b0100) + randomIntObfuscate()
    third = int(0b0010) + randomIntObfuscate()
    codes = [first, second, third]
    sendPolicyCards(player, deck[0:3], codes)

def passTwo(player, deck, option):
    """
    Chancellor receives two cards
    Also generates option IDs
    """

    if option & int(0b1000):
        i = 0
    elif option & int(0b0100):
        i = 1
    elif option & int(0b0010):
        i = 2
    else:
        print("Something went horribly wrong in passing.")

    deck.append(deck[i])
    del deck[i]

    first = int(0b1000) + randomIntObfuscate()
    second = int(0b0100) + randomIntObfuscate()
    codes = (first, second)

    sendPolicyCards(player, deck[0:2], codes)

    return deck

def chooseFromTwo(deck, option):
    """
    Chancellor plays a policy card
    """
    if option & int(0b1000):
        i = 0
    elif option & int(0b0100):
        i = 1
    else:
        print("Something went horribly wrong in passing.")

    deck.append(deck[i])
    del deck[i]

    played = deck[0]
    del deck[0]

    print("A " + policydict[played] + " policy was played.")

    return deck, played

def examineTopThree(player, deck):
    """
    Allows a player to look at the top three cards of the deck
    """
    msg = "Top three cards, starting with the topmost card:\n"

    for i in range(0,3):
        msg += str(i+1) + ". " + policydict[deck[i]] + "\n"

    if sendemails:
        sendemail(
            "Secret Hitler quaranteam.game@gmail.com",
            [emaildict[player]],
            [""],
            "Top Three Cards for Game #" + str(gamenumber),
            msg,
            sender_email,
            sender_email_password
        )
    else:
        print(msg)

def revealParty(to_player, about_player):
    """
    Reveals about_player's party to to_player
    """
    
    party = roles[players.index(about_player)]

    if party == 'h' or party == 'f':
        msg = about_player + " is a member of the Fascist party. " + about_player + " might be the Secret, Socially-Distanced Hitler..."
    else:
        msg = about_player + " is a socially-distanced liberal."

    if sendemails:
        sendemail(
            "Secret Hitler quaranteam.game@gmail.com",
            [emaildict[to_player]],
            [""],
            "Party Affliation of " + about_player + " for Game #" + str(gamenumber),
            msg,
            sender_email,
            sender_email_password
        )
    else:
        print(msg)  

deck, players = startgame(players)

#%% President (e.g. Jackson) Receives Three Cards
drawThree("Jackson", deck)

#%% Chancellor (e.g. Josh) receives two cards based on the President's decision
deck = passTwo("Josh", deck, 3140)

#%% Chancellor plays a card
deck, played = chooseFromTwo(deck, 6405)

#%% Reveal Monica's Party to Josh
revealParty("Josh", "Monica")

#%% Let Jackson See the Top Three Cards
examineTopThree("Jackson", deck)

#%%
