# Secret Socially-Distanced Hitler

Bored from the quarantine? This script allows you and your friends to play Secret Hitler from the comfort of your respective quarantines. This Python script uses a simple SMTP library to send messages to players. Players will randomly be assigned roles and sent emails accordingly. All information needed will be provided in the email (e.g. fascists will know who the other fascists are). A random succession of presidents will be sent in that email as well.

## GUI Version

As long as you know the rules of Secret Hitler, the GUI should be relatively easy to use.

### Set Up

1. When opened, the application will automatically start a demo game that shows the necessary information above the action tabs. You can click through a game to see how it works. No emails will be sent.
2. You can restart the round by clicking ``Start New Game`` in the ``File`` menu.
3. You can edit the players by typing ``Ctrl+P`` or clicking on ``Update Players`` in the ``File`` menu. Note that both a name and email must be included, or else the player will be completely removed from the list.
4. If you want to play a round with friends, update their names and emails. Then click on ``Add Sender Email`` in the ``File`` menu. This will ask for the email address and password of the account that will send all of the informational emails. I have only tested Gmail accounts. Make sure that you have turned on [access for less secure apps](https://support.google.com/accounts/answer/6010255?hl=en). I chose to create an email specifically for playing this game.
5. The dame dialog box allows you to send a link or message to every player (e.g. a Zoom meeting link) so that everyone has easy access to the game.
6. Check the ``Send Emails`` radio box. You can start a new game from that dialog if you have already updated the players list. Otherwise, click ``Okay`` and then edit the player list prior to sending the emails.
7. Enjoy the game!

## OG Script Version

You can play the OG script version using [play.py](play.py) as outlined below. There really isn't any reason to do so at this point.

### Set Up

1. You will need an email account that manages all of the emails. Be sure to include both the email address and password when you instantiate the ``SecretHitler`` class.
2. I have only tested this game using a Gmail account. Make sure that you have turned on [access for less secure apps](https://support.google.com/accounts/answer/6010255?hl=en). I chose to create an email specifically for playing this game.
3. Include every player's name and email address in the dictionary called ``emaildict``.
4. If you want to test out the functionality of this script without sending a billion emails (Gmail does limit the number of emails you can send in a day), when you instantiate the class, use ``sh = SecretHitler(emaildict, sendemails=False)``. When you are ready to play for real, use ``sh = SecretHitler(emaildict, sendemails=True)``
5. You must keep track of your SecretHitler object. You can either import the class into a Python terminal and type the appropriate commands as needed or you can run individual cells like the commented code at the bottom of [secret_hitler.py](secret_hitler.py).

### Playing the Game

An example of how you might use the ``SecretHiter`` class is given in play.py.

1. To start the game, simply instantiate a SecretHitler class and store the object as a variable. E.g. ``sh = SecretHitler(emaildict, sendemails=True)``. This will randomly assign roles and send the appropriate emails.
2. Nominating chancellors is done over video call. When a chancellor has been nominated, use ``sh.passSequence()``. This will prompt you to enter the president's and chancellor's names. Their names are the keys used in ``emaildict``. The president will then receive an email with certain 3- or 4- digit numbers that correspond to a certain action. These numbers are read aloud and entered as input to the script. Once the number is entered, an email will be sent to a chancellor who will be given two options. The option is then entered like before. The policy played will then be displayed.
3. Accuse people of being Hitler.
4. Presidential powers can be enacted using ``sh.revealParty()`` or ``sh.examineTopThree()``.
5. If five fascist policies have been played, the president and chancellor can veto the policy. This is done by entering a -1 for the chancellor's decision in ``sh.passSequence()``.
6. In the case of three unsuccessful elections, the top policy card can be played using ``sh.enactTopPolicy()``.
