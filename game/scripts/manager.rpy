# Characters

define F = Character("Croakney",
    screen="bubble_say", 
    what_color="#000000", 
    what_style="bubble_speech_text")

define J = Character("John Woof",
    screen="bubble_say", 
    what_color="#000000", 
    what_style="bubble_speech_text")

define R = Character("Ricardo",
    screen="bubble_say", 
    what_color="#000000", 
    what_style="bubble_speech_text")

define QB = Character("Queen Bee",
    screen="bubble_say", 
    what_color="#000000", 
    what_style="bubble_speech_text")

define K = Character("Kuin",
    screen="bubble_say", 
    what_color="#000000", 
    what_style="bubble_speech_text")


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