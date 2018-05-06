label lodge:
    scene bg lodge
    show marina happy
    "Ahh the lodge"
    t "Are you done yet?"
    if tourguide_fight == False:
        label lodge2:
            menu:
                "Have you noticed anything odd about the area before the murder took place?":
                    "Not much . . . I DID notice the sacred pole missing from the shrine after dinner, but I'm sure you know where it went."
                    jump lodge2
                "What relations do you have with the Priest?":
                    "I'm just a tour guide here . . . Can’t you not see my Badge?"
                    "No?"
                    "Oh, well, I left it on my other shirt. It has been a hectic day."
                    jump  lodge2
                "Do you have any suspects?":
                    "There is this one guy I brought here with the tour group, name is John Shady."
                    "He’s on the bus. The guy has been complaining the whole trip."
                    "All day he's been going on and on about how The service is terrible and how He thinks the water is *Too Cold*."
                    "He was arguing with the priest about being an imposter and making a mockery of the Goat Religion. "
                    "I don’t have anything solid on him but I'd keep an eye on him if I were you."
                    jump lodge2
                "Thank you for your time":
                    jump pond
    else:
        label lodge3:
            menu:
                "Have you noticed anything odd about the area before the murder took place?":
                    "Not much . . . I DID notice the sacred pole missing from the shrine after dinner, but I'm sure you know where it went."
                    jump lodge3
                "What relations do you have with the Priest?":
                    "I'm just a tour guide here . . . Can’t you not see my Badge?"
                    "No?"
                    "Oh, well, I left it on my other shirt. It has been a hectic day."
                    jump lodge3
                "Do you have any suspects?":
                    "There is this one guy I brought here with the tour group, name is John Shady."
                    "He’s on the bus. The guy has been complaining the whole trip."
                    "All day he's been going on and on about how The service is terrible and how He thinks the water is *Too Cold*."
                    "He was arguing with the priest about being an imposter and making a mockery of the Goat Religion. "
                    "I don’t have anything solid on him but I'd keep an eye on him if I were you."
                    jump lodge3
                "(Secret) You left with the priest after dinner. Where did you go?":
                    "I went to talk to the Priest. That creepy guy on the bus, John, complained to me about how he wasn't good at his job."
                    "The tour company paid good money to make this a true Goat Religion trip, but that John creep was demanding his money back due to him being a fake imposter."
                    "Turns out there are a few different sects of the Goat Religion. It’s not his fault, but I’ve got to pay back John for his"
                    jump lodge3
                "Thank you for your time":
                    jump pond
