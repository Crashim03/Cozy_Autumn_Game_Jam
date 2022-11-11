label CroakneyStart:

    "You stare at a frog wearing about a pound of makeup but,{w=0.2} for some reason,{w=0.2} she's still putting on more with a worried look on her face."

    "She realizes she's being watched and turns to you looking displeased."

    F "\"Honeeey,{w=0.2} take a pictureee...It lasts longeeer...\"" 
    
    "She rolls her eyes."

    "\"Are you ready to order m'am?\""

    "She sighs sitting back on her seat with her arms crossed."

    F "\"Ordeeer?{w=0.5} Do you know what I need,{w=0.2} likeee,{w=0.2} right now?\""

    "\"What,{w=0.2} miss?\""

    F "\"A S-O-L-U-tion to this mess of courseee...\""

    menu:

        "\"I can only help you with your order.\"":

            jump CroakneyHelpOrder

        "\"What solution can I serve you with your order?\"":

            jump CroakneySolution

label CroakneyHelpOrder:

    "\"Miss.{w=0.2}.{w=0.2}.{w=0.2} I can only help you with your order.{w=0.5} What are you going to have today?\""

    "Croakney gasps shocked at your lack of interest.{w=0.5} She sulks pouting."

    "Since she keeps locking eyes with you,{w=0.2} you decide to server her a fly mousse you had in the fridge."

    "When T realizes what you just did,{w=0.2} she dramatically shoves the bowl almost throwing it to the ground"

    F "\"ARE YOU TRYING TO MAKE MYY DAY EVEN WORSE?!{w=0.5} IT'S ALREADY TOUGH ENOUGH WITH MY HUBBIE AND NOW YOU DO THIIIIS?!\""

    menu:

        "\"I'm sorry,{w=0.2} Miss.{w=0.5} I'll get you something else.\"":

            jump CroakneyLove1

        "\"Miss,{w=0.2} if you keep up with this behaviour,{w=0.2} I'll have to ask you to leave.\"":

            jump CroakneyLove2

label CroakneyLove1:

    "You raise one eyebrow."

    "\"I'm sorry,{w=0.2} Miss.{w=0.5} I'll get you something else.\""

    "You take the mousse away and bring her a glass of lotus tea."

    jump CroakneyLove

label CroakneyLove2:

    "\"Miss,{w=0.2} if you keep up with this behaviour,{w=0.2} I'll have to ask you to leave.\""

    "Croakney completely ignores you and continues with her rambling."

    jump CroakneyLove

label CroakneySolution:

    "{i}sigh{/i}"

    "\"What solution can I serve you with your order?\""

    "She slowly uncrosses her arms as her smile grows."

    F "\"You seeeee.{w=0.2}.{w=0.2}.{w=0.2} I'm a bride to beee!\""

    "Croakney shows you her engagement ring made out of moss and leftover bread crumbs on top as a jewel "

    F "\"I'm gonna marry my very fly guy!{w=0.5} My pond sweetheart,{w=0.2} it is tooootally a dream come trueee!\""

    "Her euforia slowly vanishes,{w=0.2} she dramatically rests her head on the counter."

    F "\"But sometimes!{w=0.5} IT IS SO HAAARD,{w=0.2} YOU KNOOOW!\""

    menu:
        "\"No,{w=0.2} I don't know what's so hard,{w=0.2} miss.\"":

            jump CroakneyDontKnow

        "\"Yes,{w=0.2} I do understand.\"":

            jump CroakneyIUnderstand

label CroakneyDontKnow:

    "\"No,{w=0.2} I don't know what's so hard,{w=0.2} miss.\""

    F "\"HOW CAN YOU BE SO RUDEEE?!{w=0.5} LIKE,{w=0.2} CAN'T YOU SEE I'M SUFFERIIING?!\""

    "She sat straight and gives you a judgy look.{w=0.5} posing in a sassy manner"

    F "\"It is ,{w=0.2} like,{w=0.2} totally a matter of life or death,{w=0.2} you should be more respectful!\""

    "\"Why is it a matter of life or death?\""

    jump CroakneyLove

label CroakneyIUnderstand:

    "\" Yes,{w=0.2} I do understand.{w=0.5} Do you want to order a drink to make it easier to relax and unwind?\""

    F "\"Sure honeeey.{w=0.2}.{w=0.2}.{w=0.2} Give me a Diet Croak pleaseee.\""

    "Once you present her the drink,{w=0.2} Croakney immediately grabs it with her tongue dragging it to her.{w=0.5} She drinks a bit and places the glass back on the counter."

label CroakneyLove:

    F "{i}sigh{/i}"

    F "\"Oh my sweet,{w=0.2} sweet Ricardo...I LOVEEE HIM SO MUCH!{w=0.5} But...\""
    
    "Croakney stops looking embarassed"

    F "\"Sometimes I almost can't contain myself and the urge of consuming him in very unpleasant ways grows inside of me...\""
    
    F "\"My heart ACHEEES at the thought of me having to leave him foreveer...\""

    F "\"WHAT CAN I DO?!\""

    menu:

        "\"So let me get this straight,{w=0.2} you want to eat your groom-to-be?\"":

            jump CroakneyEatGroom

        "\"I see.{w=0.5} Have you tried any substitutes before?\"":

            jump CroakneySubstitutes

        "\"If your relationship as lasted as long as it has,{w=0.2} you sure will surprass the rest of your differences.\"":

            jump CroakneyKnowEachOther

label CroakneyEatGroom:

    "\"So let me get this straight,{w=0.2} you want to eat your groom-to-be?\""

    "She gets even more embarassed."

    F "\"DON'T SAY IT LIKE THAAAT!{w=0.5} It's not my fault he looks delicious on his Vertrashy thong...\""

    menu:

        "\"I think if it gets that bad all the time,{w=0.2} you two should split up.\"":

            jump CroakneyFrailHeart

        "\"If your relationship as lasted as long as it has,{w=0.2} you sure will surprass the rest of your differences.\"":

            jump CroakneyKnowEachOther

label CroakneyFrailHeart:

    "\"I think if it gets that bad all the time,{w=0.2} you two should split up.\""

    F "\"BUT?!{w=0.5} MY FRAIL LITTLE HEEEART?!\""

    "\"If you love him so much,{w=0.2} you should let him live.\""

    F "\"FINEEE!\""

    "Croakney rolls her eyes and sighs."

    F "\"It is for the best...\""

    $ croakneyEnding = 2

    jump CroakneyEnd

label CroakneySubstitutes:

    "\"I see.{w=0.5} Have you tried any substitutes before?\""

    "She gasps."

    F "\"OH!{w=0.5} I could neveeer!{w=0.5} They don't taste as good as the real thing...\""

    "\"If you love your Ricardo that much,{w=0.2} I think you should give it another try.\""

    F "\"You're right...I need to change my habits...\""

    F "\"Starting tomorrow,{w=0.2} I will only eat those who had it coming!\""

    "\"That's...not what I meant...\""

    "Croakney chugs the rest of her Diet Croak and leaves,{w=0.2} thanking you with a smile on her face."

    $ croakneyEnding = 1

    jump CroakneyEnd

label CroakneyKnowEachOther:

    "\"You two know each other for years now,{w=0.2} right?\""
    
    "\"If your relationship as lasted as long as it has,{w=0.2} you sure will surprass the rest of your differences and everything will be fine in end.\""

    $ croakneyEnding = 3

    jump CroakneyEnd

label CroakneyEnd:

    jump Day1