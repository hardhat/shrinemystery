# This is the workshop with Bill in it.

label workshop:
    scene bg workshop
    show brother happy
    g "What brings you to see me detective?"
    label workshop2:
    menu:
        "How did you know the priest?":
            "He’s my brother. Together we run . . . ran this place. I guess I own it now."
            jump workshop2
        "Have you noticed anything odd last night with the group":
            "Now that you mention it, I noticed the tour guide leave just after the Priest left after dinner. I’d ask her if I were you."
            $ tourguide_fight = True
            jump workshop2
        "Who do you think did it?":
            ""
            jump workshop2
        "Thank you for your time":
            "No need to thank me, You're the one solving the case."
            jump pond
