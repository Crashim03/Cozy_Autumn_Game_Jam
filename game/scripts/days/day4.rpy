label Day4:

    if johnEnding == 2 and not johnEndingDone:
        jump JohnNeutralEnding1

    elif johnEnding == 3 and not johnEndingDone:
        jump JohnNeutralEnding2

    menu:
        "Next day.":
            jump DayTransition

    jump DayTransition