label Day3:

    if johnEnding == 4 and not johnEndingDone:
        jump JohnBadEnding

    menu:
        "Next day.":
            jump DayTransition

    jump DayTransition