define d = Character("Ducktective")
# Player Character
define t = Character("Marina")
# First encounter name is tourguide
define s = Character("John Shady")
# Disgruntled Zealot
define n = Character("Sister Mary")
# Nun
define g = Character("Bill")
# Boyfriend
define b = Character("Mary's Boyfriend Brad")
$ m = 0

# state
define zealot_fight = False
define nun_fight = False
define brother_fight = False
define tourguide_fight = False
#
# The Priest's Name is Father Joseph Flirteen
# The game starts here.

label start:
scene bg start
show ducktective
d "I was sitting in my office when the call came in."
d "The crime was interesting; a priest was stabbed using his own sacred artifact"
d "It happened while a tour group was staying by a shrine"
d "The tour guide was stumbling over the phone, giving me the details crime as it unfolded."
d "I arrived at the scene, not knowing that this would be the biggest mystery of my life . . ."
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

scene bg pond
d "Time to review the witness testamony"
#d "Let me see some ID from all of you"
#scene bg id
#"(Press the mousewheel button to hide the text box)"
scene bg pond
d "Alright, you can go free, but just let me investigate until I talk to you."

label pond:
    scene bg pond
    "Let me talk to each of the suspects"
    # scene bg id
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
menu:
    "Visit bus":
        jump bus
    "Visit workshop":
        jump workshop
    "Visit lodge":
        jump lodge
    "Visit shrine":
        jump shrine
    "Solve crime":
        jump solve

label solve:
    scene bg pond
    show ducktective at left
    d "I know who done it!"
    show marina neutral at right
    t "You know who did it, you mean."
    d "What?"
    t "‘You know who did it’, not ‘You know who done it’."
    d "Oh. okay. Yes. I know who did it! the Murder was commited by-"

menu:
    "Accuse Zealot John Shady":
        jump accusezealot
    "Accuse Groundskeeper Bill Flirteen":
        jump accusebrother
    "Accuse Tour Guide Marina Amburgere":
        jump accusemarina
    "Accuse Sister Maria":
        jump accusenun
    "Investigate More":
        jump pond


    #show marina bloody
    #    t "Time to die."
    #    t "Because we know that wining is for losers"
label accusezealot:
    scene bg pond
    d "John did it! He was furious at the priest for being an imposter"
    t "I knew it!"
    show zealot angry at topright
    s "It was not me! I may have hated the man, but not enough to kill him!"
    d "you even told me his death was justified and nobody can say where you were last night!"
    s "I was on the bus! It’s the truth!"
    d "Well, my job here is done, take him away!"
    "YOU LOSE. JOHN, THE GUY NOBODY LIKED WAS SENT TO PRISON FOR A FLASE MURDER, THOUGH NOBODY REALLY MINDS. HE WAS A JERK."
    jump done

label accusebrother:
    scene bg pond
    d "The Groundskeeper did it! He wanted the dead to the land so he could expand this into a massive tourist complex!"
    show brother angry at topright
    g "No you git! It wasn’t me!"
    d "Tell that to the judge! Take him away!"
    "YOU LOSE. HE MAY HAVE DISLIKED HIS BROTHER BUT HE WOULD NEVER KILL HIM. DUE TO HIM LEAVING, THE DUCK POND SHRINE WAS CLOSED AND DUCKS COMPAINED TO DUCTECTIVE FOR YEARS TO COME. THEY BLAME YOU AND DUCKTECTIVE CLOSED DOWN"
    jump done

label accusemarina:
    scene bg pond
    show ducktective at left
    d "THE TOUR GUIDE DID IT! SHE OWED MONEY TO JOHN FOR THIS BEING A FALSE CHURCH OF THE GOAT!"
    show marina upset at right
    t  "Seriously? It’s like $10. I phoned you here anyway. It wasn’t me."
    hide marina upset at right
    show nun surprised at right
    n "Wait! She’s Mrs. Flirteen! She’s the daughter of the priest!"
    d "What?"
    n "A few days ago there was paper about someone being the Priest’s daughter, a Mrs. HHHHH!"
    n "She wanted to meet him, but he wrote back for her to stay away! If the Priest really had a daughter, he would be exiled from the church! His life would be over!"
    hide nun surprised
    show zealot angry at right
    s "What an unholy land this is! I knew he was horrible from the moment I met him!"
    hide zealot angry
    show marina bloody at right
    t "Ha! You found out! He disowned me the moment he met me as I follow the Church of the Duck, not the Goat! I killed him!"
    d "Well, my job here is done. Take her away!"
    "DUCKTECTIVE SOLVED THE CASE!"
    "(Well, Mary solved the case, but DUCTECTIVE TAKES THE CREDIT!)"
    hide marina bloody at right
    show zealot happy at right
    s "WAIT! The priest was horrible and I hold no grudges against you Mrs. Flirteen. And Mary, if you take over this site and follow the True Goat Religion, I will report nothing."
    s "Groundskeeper, I would fund the expansions for this site. If this is reported the church will be shut down. "
    hide zealot happy at right
    show marina bloody at right
    t "As long as nobody is unhappy with the murder-"
    hide marina bloody at right
    show brother happy at right
    g "You’d fund it? Wow! Yeah, I’m on board!"
    hide brother happy at right
    show zealot happy at right
    n "Eh, I don’t mind"
    hide zealot happy at right
    show marina winning at right
    t "Then things are good! Nobody goes to jail."
    d "But you murdered the Priest! I will be reporting this to the police once I leave here!"
    hide marina winning at right
    show brother happy at right
    g "Mrs. Flirteen, the Duck Religion teaches you the many ways to cook a good duck, no?"
    hide brother happy at right
    show marina  bloody at right
    t "I do! I know hundreds of ways to turn a duck into an amazing meal!"
    hide marina bloody at right
    show zealot estatic at right
    s "You know, a duck would be nice now."
    d "Oh dear!"
    hide zealot estatic at right
    show marina winning at right
    "YOU WERE TURNED INTO A DELICIOUS MEAL, 'CAUSE WINNING IS FOR LOSERS!"
label accusenun:
    scene bg pond
    show ducktective at left
    d "Mary did it! The Priest threatened to tell the church she was in love with a mechanic and she would be sent away for doing such a thing!"
    show nun upset at right
    n "I did not! No! It wasn’t me!"
    show zealot upset
    s "Shock! The Church of the Goat allows such a thing!"
    s "This is a corrupt off shoot! The whole area should be burned to the ground!"
    s "I can’t stand this place!"
    d "Well, my job here is done. Take her away!"
    hide zealot
    show boyfriend
    b "Mary! I’m here to take you away"
    d "Wait, boyfriend, you exist! Do you have evidence she was with you last night?"
    b "Yes. Here are receipts from the arcade. We were playing late last night"

    "YOU LOSE. MARY WAS INNOCENT."
    "HER PRECIOUS RELATIONSHIP WAS RUINED AND EVERYONE BLAMES YOU FOR SCREWING UP."
    "SHE SUES YOU WHICH ENDS UP COSTING DUCTECTIVE A MASSIVE BILL."
    jump done

label done:
#ends the game
return
