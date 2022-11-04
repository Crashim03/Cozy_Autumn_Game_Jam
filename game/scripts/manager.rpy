label start:

    $ day = 1
    $ johnEnding = 0
    $ johnEndingDone = False
    $ croakneyEnding = 0
    $ croakneyEnding = False

    jump Tavern

label Tavern:

    scene bg

    if day == 1:
        jump Day1

    elif day == 2:
        jump Day2

    elif day == 3:
        jump Day3

    elif day == 4:
        jump Day4
    
    elif day == 5:
        jump end