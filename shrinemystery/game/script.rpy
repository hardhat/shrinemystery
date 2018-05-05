# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define t = Character("Tour Guide")
define s = Character("John Shady")
define n = Character("Nun")
define g = Character("Groundskeeper")

# The game starts here.

label start:
"I was sitting in my office when the call came in."
"The crime was interesting; a priest was stabbed using his own sacred artifact"
"It happened while a tour group was staying by a shrine"
"The tour guide was stumbling over the phone, giving me the details crime as it unfolded."
"I arrived at the scene, not knowing that this would be the biggest mystery of my life . . ."
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

show eileen happy

    # These display lines of dialogue.

e "You've created a new Ren'Py game."

e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

return
