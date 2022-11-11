label KuinGoodEndingPartI:

    if not kuinGoodEndingPartIChug:

        "\"Hello!{w=0.5} How ar-\""

        QB "You know.{w=0.2}.{w=0.2}.{w=0.2} I've noticed you don't utilize the proper term of adressing me,{w=0.2} as i said \"Your Majesty\" was the only acceptable choice."

        QB "Nonetheless,{w=0.2} I seem to have grown quite fond of you little bud,{w=0.2} which is why i will allow you the honor of using my nickname."

        QB "Kuin.{w=0.5} K:U:I:N:"

        "\"Your nickname?I was just saying-\""

        K "Yess yeeeeeessss I KNOOOWWW an honor like this would leave anyone speechless!"

        K "BUT WORRY NOT,{w=0.2} I hold no grudges for I am a forgiving ruler."

        "\"Right.\""

        "\"So..{w=0.2}.{w=0.2}.{w=0.2} Whats Kuin short for?\""

        K "{i}GASP{/I}" 

        "\"Um im sorry did i say something wrong?\""

        K "nono i was just um.{w=0.2}.{w=0.2}.{w=0.2} surprised.{w=0.2}.{w=0.2}.{w=0.2} its been a while since i had this talk."

        QB "Its short for QUEENIFER..."

        "\"Oh ok then isnt the spelling-\""

        K "WHATS WRONG WITH THE SPELLING?!"

        "\"Nothing.\""

        K ".........I'll take another drink."

        $ kuinGoodEndingPartIChug = True

        jump Tavern

    else:

        "You see Kuin chug drink after drink.{w=0.5} You hesitate but you approach her."

        "\"Sooo how are things over her-\""

        K "PFFTTT WHAT A JOKE AS IF SHE COULD EVER STAND UP TO ME....{w=0.2}.{w=0.2}.{w=0.2} i mean to US!{w=0.5} Me and my hive.{w=0.2}.{w=0.2}.{w=0.2} not to ME why would she talk to me ...its not like we were close or something..."
        
        K "WHY WOULD I be close to HER.{w=0.2}.{w=0.2}.{w=0.2} SHE WISHES!{w=0.5} I mean who WOULDN'T WANT TO BE CLOSE TO ME IM AMAZIN-"

        K "...................................................."

        "\"What happened???Did things not go well with the workers?\""

        K "Everything is great with the workers.{w=0.2}.{w=0.2}.{w=0.2} Better than ever actually.{w=0.2}.{w=0.2}.{w=0.2} who would've thought....~Giving them good work conditions would like make them like happy and stuff.{w=0.2}.{w=0.2}.{w=0.2} funny right?"

        "\"So what's wrong?\""

        K "IT'S BREETANY BEETCH!"

        "\"Im sorry I'm confused,{w=0.2} your rival?\""

        K "Yes...."

        "\"Don't worry you can still win!\""

        K "What are you talking about?{w=0.5} This was never about winning I mean yeah winning would be nice but mostly to SHOW HER SHE CAN'T IGNORE ME."

        "\"UOUH.{w=0.5} Thats.{w=0.2}.{w=0.2}.{w=0.2} well toxic\""

        K "WHAT WAS I MEANT TO DO she doesn't speak to me anymore we were BEST FRIENDS but ever since she decided all on her own we COULDN'T BE just because she SOOO SERIOUSS"

        K "About being the queen of her own hive blah blah and that I'm from a different hive blah blah and that we shouldn't fu-.......{w=0.2}.{w=0.2}.{w=0.2} facilitate comunications between rivals.{w=0.5} Yes."

        "\"Right so here's the deal you gotta work that shit out.{w=0.5} Obviously you're not okay with the situation.\""

        menu:

            "\"You gotta go after her!\"":

                jump KuinGoAfterHer

            "Maybe its enough honeylicor for the day...":

                jump KuinWorkers

label kuinGoAfterHer:

    "\"Go after her!You don't need to accept things as they are!{w=0.5} Make peace with her!\""

    "\"WHY NOT?\""

    K "YOU'RE RIGHT IM GONNA GO TALK TO HER!!"

    "\"YEAH!\""

    K "YEAH!{w=0.5} AND WE WILL TALK!"

    "\"YEAAAH!\""

    K "AND SHE WILL SEE SHE IS WRONG!"

    "\"YEA-UM..ok ..yeahhh but you see that was not the point you were trying to make.\""

    K "YEAAAHH!!!!!!!{w=0.5} WaitT ItS nOt?"

    "\"...{w=0.2}.{w=0.2}.{w=0.2} No?{w=0.5} Friendship and stuff remember?Listening to others make heart feel good.\""

    K "Oh..{w=0.2}.{w=0.2}.{w=0.2} ok sure whatever you say just bring me another one dear."

    "\"Maybe it's enough honeylicor for the day...\""

label KuinWorkers:

    "You walk away for a minute and when you look back at Kuin she is facedown on the table."

    K "bzzzzzz bzzzzzz"

    "Two working bees show up and take her away"

    $ kuinGoodEndingPartIDone = True

    jump Tavern