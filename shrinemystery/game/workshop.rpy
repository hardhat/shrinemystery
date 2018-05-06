# This is the workshop with Bill in it.

label workshop:
    scene bg workshop
    show brother neutral at topright
    g "What brings you to see me detective?"
    label workshop2:
        show brother neutral at topright
        if brother_fight == False:
            menu:
                "How did you know the priest?":
                    show brother upset at topright
                    g "He’s my brother. Together we run . . . ran this place. I guess I own it now."
                    jump workshop2
                "Have you noticed anything odd last night with the group":
                    show brother upset at topright
                    g "Now that you mention it, I noticed the tour guide leave just after the Priest left after dinner. I’d ask her if I were you."
                    $ tourguide_fight = True
                    jump workshop2
                "Who do you think did it?":
                    show brother happy at topright
                    g "No idea. Could be anyone."
                    jump workshop2
                "Thank you for your time":
                    show brother happy at topright
                    g "No need to thank me, You're the one solving the case."
                    jump pond
        else:
            label workshop3:
                show brother neutral at topright
                menu:
                    "How did you know the priest?":
                        show brother upset at topright
                        g "He’s my brother. Together we run . . . ran this place. I guess I own it now."
                        jump workshop2
                    "Have you noticed anything odd last night with the group":
                        show brother upset at topright
                        g "Now that you mention it, I noticed the tour guide leave just after the Priest left after dinner. I’d ask her if I were you."
                        $ tourguide_fight = True
                        jump workshop2
                    "Who do you think did it?":
                        show brother happy at topright
                        g "No idea. Could be anyone."
                    "(Secret) What were you arguing with your brother about?":
                        g "What argument?"
                        "The Nun said you were arguing two days ago."
                        show brother angry at topright
                        g "Look. He and I have butted heads for a while. This place doesn’t make money because he doesn’t expand the lodge and advertise it to tourists."
                        g "I’ve wanted to expand this into a fully finished, five-star resort built into the gorgeous landscape this area was gifted with!"
                        g "With him gone I own the deed and can finally make money off this place. "
                        jump workshop2
                    "Thank you for your time":
                        show brother happy at topright
                        "No need to thank me, You're the one solving the case."
                        jump pond
