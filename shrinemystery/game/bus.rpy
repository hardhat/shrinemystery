label bus:
    scene bg bus
    show zealot happy
    "Who might you be?"
    show zealot angry
    s "I am John Shady"

    if zealot_fight == True:
        jump bus_loop2
    else:
        jump bus_loop

    label bus_loop:
        menu:
            "What relations do you have with the Priest?":
                s "Nothing. Sadly he claimed to follow the Goat, but is truly a shame."
                jump bus_loop
            "Did you observe anything odd yesterday?":
                s "TERRIBLE service, horrible water, a shameful priest, and, well, I did notice the nun leaving the monastery leave just after dinner. You should ask her where she went."
                $ nun_fight = True # (Unlocks dialogue for Nun)
                jump bus_loop
            "That's all for now, thanks.":
                jump pond


    label bus_loop2:
        menu:
            # - (Unlocked after Tour Guide)
            "What relations do you have with the Priest?":
                s "Nothing. Sadly he claimed to follow the Goat, but is truly a shame."
                jump bus_loop2
            "What were you arguing with the Priest about?":
                s "He is not a devout Goat Priest! He is an imposter!  Not wearing traditional robes made from goat wool cloth! The Goat Pole on the shrine was upside down which is almost justification for his death!"
                s "I spoke to him last night asking for his repentance, but he pushed me away. Now, I did not kill him, but I am shedding no tears for the death of such a shame to our god."
                jump bus_loop2
            "Did you observe anything odd yesterday?":
                s "TERRIBLE service, horrible water, a shameful priest, and, well, I did notice the nun leaving the monastery leave just after dinner. You should ask her where she went."
                $ nun_fight = true # (Unlocks dialogue for Nun)
                jump bus_loop2
            "That's all for now, thanks.":
                jump pond
