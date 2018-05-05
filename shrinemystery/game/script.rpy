define d = Character("Ducktective")
# Player Character
define t = Character("Marina")
# First encounter name is tourguide
define s = Character("John Shady")
# Disgruntled Zealot
define n = Character("Sister Mary")
# Nun
define g = Character("Bill")
#
# The Priest's Name is Father Joseph Flirteen
# The game starts here.

label start:
scene bg start
show Ducktective
"I was sitting in my office when the call came in."
"The crime was interesting; a priest was stabbed using his own sacred artifact"
"It happened while a tour group was staying by a shrine"
"The tour guide was stumbling over the phone, giving me the details crime as it unfolded."
"I arrived at the scene, not knowing that this would be the biggest mystery of my life . . ."
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

scene bg pond
d "Let me see some ID from all of you"
 scene bg id
"(Press the mousewheel button to hide the text box)"
scene bg pond
d "Alright, you can go free, but just let me investigate until I talk to you."


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
scene bg bus
show zealot happy
"Who might you be?"
show zealot angry
s "I am the candy man"

#ends the game
return
