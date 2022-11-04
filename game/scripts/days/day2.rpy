label Day2:

    if johnEnding == 1 and not johnEndingDone:
        jump JohnGoodEnding

    menu:
        "Next day.":
            jump DayTransition

    jump DayTransition