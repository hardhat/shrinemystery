define d = Character("Ducktective")
# Player Character
define t = Character("Marina")
# First encounter name is tourguide
define s = Character("John Shady")
# Disgruntled Zealot
define n = Character("Sister Mary")
# Nun
define g = Character("Bill")
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
"I was sitting in my office when the call came in."
"The crime was interesting; a priest was stabbed using his own sacred artifact"
"It happened while a tour group was staying by a shrine"
"The tour guide was stumbling over the phone, giving me the details crime as it unfolded."
"I arrived at the scene, not knowing that this would be the biggest mystery of my life . . ."
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
    d "I know who done it!"
    t "You know who did it, you mean."
    d "What?"
    t "'You know who did it, not 'you know who done it'."
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
    show zealot angry
    d "John did it! He was furious at the priest for being an imposter"
    t "I knew it!"
    s "It was not me! I may have hated the man, but not enough to kill him!"
    d "you even told me his death was justified and nobody can say where you were last night!"
    s "I was on the bus! It’s the truth!"
    d "Well, my job here is done, take him away!"
    "YOU LOSE. JOHN, THE GUY NOBODY LIKED WAS SENT TO PRISON FOR A FLASE MURDER, THOUGH NOBODY REALLY MINDS. HE WAS A JERK."
    jump done

label accusebrother:
    scene bg pond
    show brother angry
    g "Wrong."
    jump done

label accusemarina:
    scene bg pond
    show marina bloody
    t "Now you die."
    jump done

label accusenun:
    scene bg pond
    show nun angry
    n "Wrong."
    jump done

label done:
#ends the game
return
