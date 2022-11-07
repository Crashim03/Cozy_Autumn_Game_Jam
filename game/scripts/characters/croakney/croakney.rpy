define F = Character("Croakney", color="#ffffff")

label CroakneyStart:

    "You start staring at a frog wearing about a pound of makeup but, for some reason, she's still putting on more with a worried look on her face."

    "She realizes she's being watched and turns to you looking displeased."

    F "\"Honeeey, take a pictureee...It lasts longeeer...\"" 
    
    "She rolls her eyes."

    "\"Are you ready to order m'am?\""

    "She sighs sitting back on her seat with her arms crossed."

    F "\"Ordeeer? Do you know what I need, likeee, right now?\""

    "\"What, miss?\""

    F "\"A S-O-L-U-tion to this mess of courseee...\""

    menu:

        "\"I can only help you with your order.\"":
            jump CroakneyHelpOrder

        "\"What solution can I serve you with your order?\"":
            jump CroakneySolution

label CroakneyHelpOrder:

    "\"Miss... I can only help you with your order. What are you going to have today?\""

    "The Frog gasps shocked at your lack of interest. She sulks pouting."

    "Since she keeps locking eyes with you, you decide to server her a fly mousse you had in the fridge."

    "When the Frog realizes what you just did, she dramatically shoves the bowl almost throwing it to the ground"

    F "\"ARE YOU TRYING TO MAKE MYY DAY EVEN WORSE?! IT'S ALREADY TOUGH ENOUGH WITH MY HUBBIE AND NOW YOU DO THIIIIS?!\""

    menu:

        "\"I'm sorry, Miss. I'll get you something else.\"":

            jump CroakneyLove1

        "\"Miss, if you keep up with this behaviour, I'll have to ask you to leave.\""

            jump CroakneyLove2

label CroakneyLove1:

    "You raise one eyebrow."

    "\"I'm sorry, Miss. I'll get you something else.\""

    "You take the mousse away and bring her a glass of lotus water."

    jump CroakneyLove

label CroakneyLove2:

    "\"Miss, if you keep up with this behaviour, I'll have to ask you to leave.\""

    "The Frog completely ignores you and continues with her rambling."

    jump CroakneyLove

label CroakneySolution:

    "You sigh."

    "\"What solution can I serve you with your order?\""

    "She slowly uncrosses her arms as her smile grows."

    F "\"You seeeee... I'm a bride to beee!\""

    "Croakney shows you her engagement ring made out of moss and leftover bread crumbs on top as a jewel "

    F "\"I'm gonna marry my very fly guy! My pond sweetheart, it is tooootally a dream come trueee!\""

    "Her euforia slowly vanishes, she dramatically rests her head on the counter."

    F "\"But sometimes! IT IS SO HAAARD, YOU KNOOOW!\""

    menu:
        "\"No, I don't know what's so hard, miss.\"":

            jump CroakneyDontKnow

        "\"Yes, I do understand.\"":

            jump CroakneyIUnderstand

label CroakneyDontKnow:

    "\"No, I don't know what's so hard, miss.\""

    F "\"HOW CAN YOU BE SO RUDEEE?! LIKE, CAN'T YOU SEE I'M SUFFERIIING?!\""

    "She sat straight and gives you a judgy look. posing in a sassy manner"

    F "\"It is , like, totally a matter of life or death, you should be more respectful!\""

    "\"Why is it a matter of life or death?\""

    jump CroakneyLove

label CroakneyIUnderstand:

    "\" Yes, I do understand. Do you want to order a drink to make it easier to relax and unwind?\""

    F "\"Sure honeeey... Give me a Diet Croak pleaseee.\""

    "Once you present her the drink, the Frog immediately grabs it with her tongue dragging it to her. She drinks a bit and places the glass back on the counter."

label CroakneyLove:

    "She sighs."

    F "\"Oh my sweet, sweet Ricardo...I LOVEEE HIM SO MUCH! But...\""
    
    "The Frog stops looking embarassed"

    F "\"Sometimes I almost can't contain myself and the urge of consuming him in very unpleasant ways grows inside of me...\""
    
    F "\"My heart ACHEEES at the thought of me having to leave him foreveer...\""

    F "\"WHAT CAN I DO?!\""

    menu:

        "\"So let me get this straight, you want to eat your groom-to-be?\"":

            jump CroakneyEatGroom

        "\"I see. Have you tried any substitutes before?\"":

            jump CroakneySubstitutes

        "\"If your relationship as lasted as long as it has, you sure will surprass the rest of your differences.\"":

            jump CroakneyKnowEachOther

label CroakneyEatGroom:

    "\"So let me get this straight, you want to eat your groom-to-be?\""

    "She gets even more embarassed."

    F "\"DON'T SAY IT LIKE THAAAT! It's not my fault he looks delicious on his Vertrashy thong...\""

    menu:

        "\"I think if it gets that bad all the time, you two should split up.\"":

            jump CroakneyFrailHeart

        "\"If your relationship as lasted as long as it has, you sure will surprass the rest of your differences.\"":

            jump CroakneyKnowEachOther

label CroakneyFrailHeart:

    "\"I think if it gets that bad all the time, you two should split up.\""

    F "\"BUT?! MY FRAIL LITTLE HEEEART?!\""

    "\"If you love him so much, you should let him live.\""

    F "\"FINEEE!\""

    "The Frog rolls her eyes and sighs."

    F "\"It is for the best...\""

    croakneyEnding = 2

    jump CroakneyEnd

label CroakneySubstitutes:

    "\"I see. Have you tried any substitutes before?\""

    "She gasps."

    F "\"OH ! I could neveeer! They don't taste as good as the real thing...\""

    "\"If you love your Ricardo that much, I think you should give it another try.\""

    F "\"You're right...I need to change my habits...\""

    F "\"Starting tomorrow, I will only eat those who had it coming!\""

    "\"That's...not what I meant...\""

    "Croakney chugs the rest of her Diet Croak and leaves, thanking you with a smile on her face."

    croakneyEnding = 1

    jump CroakneyEnd

label CroakneyKnowEachOther:

    "\"You two know each other for years now, right?\""
    
    "\"If your relationship as lasted as long as it has, you sure will surprass the rest of your differences and everything will be fine in end.\""

    croakneyEnding = 3

    jump CroakneyEnd

label CroakneyEnd:

    jump Day1