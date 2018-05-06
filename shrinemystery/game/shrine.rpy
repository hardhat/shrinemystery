
label shrine:
    scene bg shrine
    #show nun happy
    #menu
    #"Time to pray?"
    #n "I am always praying, even while conversing with you."
    #jump pond
    show nun happy
    if nun_fight == True:
        jump shrine_loop2
    else:
        jump shrine_loop

    label shrine_loop:
        menu:
            "How well did you know the Priest?":
                s "I've been here for about a month, but I barely knew him."
                s "He was nice I guess, not much else I can say."
                jump shrine_loop

            "Have you noticed anything odd in the days leading up the murder?":

                n "There was a letter that came about a week ago..."
                n "With a DNA test as proof, a Mrs. Amberger claims to be his daughter."
                n "Outside of that, Bill, the Prist’s brother has been arguing a lot of late."
                n "An argument got really heated two days ago."
                $ brother_fight = True
                jump shrine_loop
            "Thanks for the info.":
                jump pond


    label shrine_loop2:
        menu:
            # - (Unlocked after Zealot)
                        "How well did you know the Priest?":
                            s "I've been here for about a month, but I barely knew him."
                            s "He was nice I guess, not much else I can say."
                            jump shrine_loop2
                        "Have you noticed anything odd in the days leading up the murder?":
                            n "There was a letter that came about a week ago..."
                            n "With a DNA test as proof, a Mrs. Amberger claims to be his daughter."
                            n "Outside of that, Bill, the Prist’s brother has been arguing a lot of late."
                            n "An argument got really heated two days ago."
                            $ brother_fight = True
                            jump shrine_loop2
                        "Where were you on the night of the event?":
                            n "Oh! I was in town."
                            d "Town?"
                            n "Yes. I was. I wasn’t anywhere near the shrine."
                            d "So if I go to the town someone could prove your alibi that you didn’t kill the Priest?"
                            n "I, well, look. I am in love with this mechanic in the city and we went out for a drive last night."
                            n "He picked me up and we went to the arcade and played GOAT simulator"
                            d "The Goat Religion prohibits that no? If the Priest found out, you would be sent back to the Basilica."
                            n "Yes, I would. The Priest knew, but he promised not to tell. If he did, my life would be ruined."
                            jump shrine_loop2
                        "Thanks for the info.":
                            jump pond
