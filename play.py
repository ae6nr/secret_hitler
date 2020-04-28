"""
Example Usage of SecretHitler
"""
# %%
from SecretHitler import SecretHitler

# Example usage
# %% Start a Round
sender_email = "" # enter the email that will be used to send emails
sender_email_password = "" # enter your password
emaildict = {
    "bryan" : "player1@gmail.com",
    "kristen" : "player2@gmail.com",
    "jason" : "player3@gmail.com",
    "bryant" : "player4@gmail.com",
    "jackson" : "player5@gmail.com",
    "monica" : "player6@gmail.com",
    "haley" : "player7@gmail.com",
    "aleska" : "player8@gmail.com",
    "mark" : "player9@gmail.com",
    "josh" : "player0@gmail.com"
}
sh = SecretHitler(emaildict, sender_email, sender_email_password, sendemails=False) # To actually send emails, set sendemails=True

# %% Complete Entire Passing Sequence for President and Chancellor
sh.passSequence()

# %% Reveal Someone's Party To Another Player
sh.revealParty()

# %% Let Someone See The Top Three Cards
sh.examineTopThree()

# %% Enact Top Policy
sh.enactTopPolicy()

# %%