"""
An email-based version of Secret Hitler
Author: redd, bryan.d.redd@gmail.com
"""

#%%
import smtplib
import random
import time

class SecretHitler:

    def __init__(self, emaildict, sender_email, sender_email_password, sendemails=False, invite_link=""):

        self.sender_email = sender_email
        self.sender_email_password = sender_email_password

        self.sendemails = sendemails # True sends emails, False prints information for testing
        self.gamenumber = random.randint(100, 99999) # Game ID for clarity
        self.policydict = {'l': 'Liberal', 'f': 'Fascist'}
        self.roles = ['h','f','l','l','l','l','f','l','f','l'] # the order in which roles are assigned
        self.message_number = 0

        self.players = list(emaildict.keys())
        self.emaildict = emaildict

        if len(self.players) < 5 or len(self.players) > 10:
            print("You don't have a valid number of players.")
            print("You're entering uncharted territory here.")

        self.deck = []
        self.fascist_score = 0
        self.liberal_score = 0

        self.assignRoles(invite_link=invite_link)
        self.initPolicyDeck()

        self.presidential_powers = [
            [
                "The president has no special power.\n",
                "The president has no special power.\n",
                "The president examines the top three cards.\n",
                "The president must kill a player.\n",
                "The president must kill a player.\n"
            ], # 5 or 6 players
            [
                "The president has no special power.\n",
                "The president investigates a player's party membership card.\n",
                "The president picks the next presidential candidate.\n",
                "The president must kill a player.\n",
                "The president must kill a player.\n"  
            ], # 7 or 8 players
            [
                "The president investigates a player's party membership card.\n",
                "The president investigates a player's party membership card.\n",
                "The president picks the next presidential candidate.\n",
                "The president must kill a player.\n",
                "The president must kill a player.\n"                 
            ] # 9 or 10 players
        ]

    def sendemail(self, from_addr, to_addr_list, cc_addr_list,
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

    def sendMessage(self, player, subject, msg):
        if self.sendemails:
            self.sendemail(
                "Secret Hitler quaranteam.game@gmail.com",
                [self.emaildict[player]],
                [""],
                subject,
                msg,
                self.sender_email,
                self.sender_email_password
            )
            text = "Email sent!"
        else:
            text = player + ": " + subject + "\n\n" + msg
            # print(text)
        
        return text

    def sendRole(self, player, msg):
        """
        Send an email with the player's role
        """
        subject = "Secret Role for Game #" + str(self.gamenumber)
        return self.sendMessage(player, subject, msg)

    def assignRoles(self, invite_link=""):
        """
        Assign players' roles, and send them emails
        """

        random.shuffle(self.players)

        seating_msg = "The succession of the presidency will occur in the following order:\n"
        for i in range(0, len(self.players)):
            seating_msg += self.players[i] + "\n"

        random.shuffle(self.players)

        for i in range(0, len(self.players)):

            msg = "\n\n" # must start with this, or else the first line will be lost
            msg += "Welcome to Secret, Socially-Distanced Hitler.\n\n"
            if invite_link != "":
                msg += invite_link
                msg += "\n\n"
            
            if self.roles[i] == 'h':
                msg += "You are the Secret, Socially-Distanced Hitler."
                if len(self.players) <= 6:
                    msg += " The other fascist is " + self.players[1] + "."
                msg += "\n\n"
            elif self.roles[i] == 'f':
                msg += "You are a socially-distanced fascist.\n\n"
                msg += self.players[0] + " is Secret, Socially-Distanced Hitler.\n\n"
                try:
                    self.players[6]
                    msg += "The fascists are:\n"
                    msg += self.players[1] + "\n"
                    msg += self.players[6] + "\n"
                    try:
                        msg += self.players[8] + "\n"
                    except:
                        pass
                    msg += "\n"
                except:
                    pass

            elif self.roles[i] == 'l':
                msg += "You are a socially-distanced liberal. Find the Secret, Socially-Distanced Hitler!\n\n"

            msg += seating_msg + "\n"

            self.sendRole(self.players[i], msg)

    def sendPolicyCards(self, player, policies, codes):
        """
        Send the policy cards
        """

        msg = "You have received the following policy cards:\n"
        for i in range(0,len(policies)):
            msg += str(i+1) + ". " + self.policydict[policies[i]] + "\n"

        if len(policies) == 3:
            msg += "To DISCARD the first and PASS the second and third, say " + str(codes[0]) + ".\n"
            msg += "To DISCARD the second and PASS the first and third, say " + str(codes[1]) + ".\n"
            msg += "To DISCARD the third and PASS the first and second, say " + str(codes[2]) + ".\n"
        else:
            msg += "To enact the first policy, say " + str(codes[1]) + ".\n"
            msg += "To enact the second policy, say " + str(codes[0]) + ".\n"
            msg += "(If applicable, say -1 to veto.)\n"

        subject = "Policy Cards for Game #" + str(self.gamenumber) + " " + str(random.randint(0, 10000000))
        text = self.sendMessage(player, subject, msg)

        return text

    def initPolicyDeck(self):
        """
        Creates a shuffled deck of policy cards
        """
        self.deck = ['f','f','f','f','f','f','f','f','f','f','f','l','l','l','l','l','l']
        random.shuffle(self.deck)

    def randomIntObfuscate(self):
        """
        Creates a random-ish number so that players can verbally pass cards without anyone knowing what's being passed.
        """
        return int((random.randint(0, 2**9-1) << 4) + random.randint(0, 1))

    def drawThree(self, player):
        """
        For the president to draw three policy cards
        Also creates the randomish numbers as option IDs
        """
        first = int(0b1000) + self.randomIntObfuscate()
        second = int(0b0100) + self.randomIntObfuscate()
        third = int(0b0010) + self.randomIntObfuscate()
        codes = [first, second, third]
        msg = self.sendPolicyCards(player, self.deck[0:3], codes)
        return msg

    def passTwo(self, player, option):
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
            msg = "Something went horribly wrong in passing."
            return self.deck, msg

        self.deck.append(self.deck[i])
        del self.deck[i]

        first = int(0b1000) + self.randomIntObfuscate()
        second = int(0b0100) + self.randomIntObfuscate()
        codes = (first, second)

        msg = self.sendPolicyCards(player, self.deck[0:2], codes)

        return self.deck, msg

    def chooseFromTwo(self, option):
        """
        Chancellor plays a policy card
        """
        played = 'v'

        if option == -1: # vetoed
            self.deck.append(self.deck[0])
            self.deck.append(self.deck[1])
            del self.deck[0]
            del self.deck[0]
            return self.deck, played

        if option & int(0b1000):
            i = 0
        elif option & int(0b0100):
            i = 1
        else:
            # print("Something went horribly wrong in passing.")
            return self.deck, played

        self.deck.append(self.deck[i])
        del self.deck[i]

        played = self.deck[0]
        del self.deck[0]

        return self.deck, played

    def examineTopThree(self, player=''):
        """
        Allows a player to look at the top three cards of the deck
        """

        if player == '':
            player = input('TO WHOM shall I send the information?')

        try:
            self.emaildict[player]
        except:
            msg = "You misspelled someone's name."
            # print(msg)
            return msg

        msg = "Top three cards, starting with the topmost card:\n"

        for i in range(0,3):
            msg += str(i+1) + ". " + self.policydict[self.deck[i]] + "\n"

        subject = "Top Three Cards for Game #" + str(self.gamenumber)
        return self.sendMessage(player, subject, msg)

    def revealParty(self, to_player='', about_player=''):
        """
        Reveals about_player's party to to_player
        """

        if to_player == '':
            to_player = input('TO WHOM shall I send the information?')
        
        if about_player == '':
            about_player = input('Whose party shall be revealed?')

        try:
            self.emaildict[to_player]
            self.emaildict[about_player]
        except:
            msg = "You misspelled someone's name."
            # print(msg)
            return msg
        
        party = self.roles[self.players.index(about_player)]

        if party == 'h' or party == 'f':
            msg = about_player + " is a member of the Fascist party.\n" + about_player + " might be the Secret, Socially-Distanced Hitler..."
        else:
            msg = about_player + " is a socially-distanced liberal."

        subject = "Party Affliation of " + about_player + " for Game #" + str(self.gamenumber)
        return self.sendMessage(to_player, subject, msg) 

    def updateGameStatus(self, policy):

        presidential_power = False

        msg = ""

        if policy == 'l':
            msg += "A " + self.policydict[policy] + " policy was played.\n"
            self.liberal_score += 1
        elif policy == 'f':
            msg += "A " + self.policydict[policy] + " policy was played.\n"
            self.fascist_score += 1
            presidential_power = True
        elif policy == 'v':
            msg += "The policies were vetoed.\n"
        else:
            msg += "Something really bad happened.\n"

        msg += "The liberals have " + str(self.liberal_score) + " policies.\n"
        msg += "The fascists have " + str(self.fascist_score) + " policies.\n"

        if self.liberal_score == 5:
            msg += "The liberals win!\n"
            return msg
        elif self.fascist_score == 6:
            msg += "The fascists win!\n"
            return msg

        if self.liberal_score == 4:
            msg += "The liberals will win upon enacting one more liberal policy.\n"
        
        if self.fascist_score == 5:
            msg += "The fascists will win upon enacting one more fascist policy.\n"
        
        if self.fascist_score >= 3:
            msg += "The fascists will win upon electing Hitler as chancellor.\n"

        if presidential_power:
            if len(self.players) == 5 or len(self.players) == 6:
                i = 0
            elif len(self.players) == 7 or len(self.players) == 8:
                i = 1
            elif len(self.players) == 9 or len(self.players) == 10:
                i = 2
            else:
                msg += "Warning: You don't have a valid number of players, so I can't decide what the presidential power is.\n"
                return

            msg += self.presidential_powers[i][self.fascist_score-1]
        
        return msg

    def passSequence(self):

        president = input('Who is the president?')
        chancellor = input('Who is the chancellor?')

        try:
            self.emaildict[president]
            self.emaildict[chancellor]
        except:
            msg = "You misspelled someone's name."
            # print(msg)
            return msg

        msg = self.drawThree(president)
        print(msg)
        option = int(input("President's decision:"))
        deck, msg = self.passTwo(chancellor, option)
        print(msg)
        option = int(input("Chancellor's decision (-1 for veto):"))
        self.deck, played = self.chooseFromTwo(option)

        msg = self.updateGameStatus(played)
        return msg

    def enactTopPolicy(self):
        policy = self.deck[0]
        del self.deck[0]
        return self.updateGameStatus(policy)

