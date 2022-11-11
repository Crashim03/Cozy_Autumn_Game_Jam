# Characters

define F = Character("Croakney", color="#ffffff")
define J = Character("John Woof", color="#ffffff")
define R = Character("Ricardo", color="#ffffff")
define QB = Character("Queen Bee", color="#ffffff")


label start:

    $ day = 1

    $ johnEnding = 0
    $ johnEndingDone = False

    $ croakneyEnding = 0
    $ croakneyEndingDone = False

    $ kuinEnding = 0
    $ kuinEndingDone = False
    $ kuinCompetion = False
    $ kuinBreetany = False
    $ kuinGoodEndingPartIDone = False
    $ kuinGoodEndingPartIChug = False
    $ kuinNeutralEndingPartI = False

    $ emptyDays = 0

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