label lodge:
    scene bg lodge
    show marina happy
    "Ahh the lodge"
    t "Are you done yet?"
    if t == 0:
        label lodge2:
            menu:
                "":
                    jump lodge2
                "":
                    jump  lodge2
                "":
                    jump lodge2
                "":
                    jump pond
    else:
        label lodge3:
            menu:
                "":
                    jump lodge3
                "":
                    jump lodge3
                "":
                    jump lodge3
                "":
                    jump lodge3
                "":
                    jump pond
