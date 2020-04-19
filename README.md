# Secret Socially-Distanced Hitler

Bored from the quarantine? This script allows you and your friends to play Secret Hitler from the comfort of your respective quarantines.

# How to Play

This Python script uses a simple SMTP library to send messages to players. Players will randomly be assigned roles and sent emails accordingly. All information needed will be provided in the email (e.g. fascists will know who the other fascists are). A random succession of presidents will be sent in that email as well.

## Set Up

1. You will need an email account that manages all of the emails. Be sure to include both the email address and password in the constructor of the ``SecretHitler`` class.
2. I have only tested this game using a Gmail account. Make sure that you have turned on [access for less secure apps](https://support.google.com/accounts/answer/6010255?hl=en). I chose to create an email specifically for playing this game.
3. Include every player's name and email address in the dictionary called ``emaildict``.
4. If you want to test out the functionality of this script without sending a billion emails (Gmail does limit the number of emails you can send in a day), when you instantiate the class, use ``sh = SecretHitler(emaildict, sendemails=False)``. When you are ready to play for real, use ``sh = SecretHitler(emaildict, sendemails=True)``
5. You must keep track of your SecretHitler object. You can either import the class into a Python terminal and type the appropriate commands as needed or you can run individual cells like the commented code at the bottom of [secret_hitler.py](secret_hitler.py).

## Playing the Game

1. To start the game, simply instantiate a SecretHitler class and store the object as a variable. E.g. ``sh = SecretHitler(emaildict, sendemails=True)``. This will randomly assign roles and send the appropriate emails.
2. Nominating chancellors is done over video call. When a chancellor has been nominated, use ``sh.passSequence()``. This will prompt you to enter the president's and chancellor's names. Their names are the keys used in ``emaildict``. The president will then receive an email with certain 3- or 4- digit numbers that correspond to a certain action. These numbers are read aloud and entered as input to the script. Once the number is entered, an email will be sent to a chancellor who will be given two options. The option is then entered like before. The policy played will then be displayed.
3. Accuse people of being Hitler.
4. Presidential powers can be enacted using ``sh.revealParty()`` or ``sh.examineTopThree()``.
5. If five fascist policies have been played, the president and chancellor can veto the policy. This is done by entering a -1 for the chancellor's decision in ``sh.passSequence()``.

