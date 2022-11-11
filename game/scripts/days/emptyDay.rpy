label EmptyDay:

    if emptyDays == 0:

        "\"Hmm... I guess nobody came today.\""

    elif emptyDays == 1:

        "\"Empty again... Am I doing something wrong?\""

    else:

        "\"It's empty again! This is getting ridiculous!\""

    $ emptyDays += 1

    jump DayTransition