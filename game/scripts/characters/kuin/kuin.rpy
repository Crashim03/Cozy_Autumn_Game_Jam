label KuinStart:

    QB "Good Afternoon servant of this establishment."

    "\"Umm... hi there!\""

    QB "Shall i instruct you on how to proceed? You seem to be inadequate."

    menu:

        "\"No its just your way of speech was a bit peculiar.\"":
            
            jump KuinPeculiar

        "\"You caught me off guard!\"":

            jump KuinOffGuard

label KuinPeculiar:

    "\"What?... No its just your way of speech was a bit... peculiar.\"" 

    "\"What will it be?\""

    QB "Good, now that we reached an understanding you shall only adress me as \"Your Majesty\"."

    QB "For starters, a latte with two pumps of pure gluten free honey will do."

    menu:

        "\"As you wish.\"":

            jump KuinWish

        "\"What?\"":

            jump KuinWhat

label KuinWish:

    "\"Umm,sure.\""

    "\"As you wish...\""

    QB "Excuse me you seem to enjoy a life of servitude. So tell me... am i SOO wrong for wishing the best for my hive??!!"
    
    QB "All it takes is just a littleeee overtime. which is basically asking nothing right?!RIGHT?!"

    menu:

        "Keep silent.":

            jump KuinSilent

        "\"Everyone deserves to rest.\"":

            jump KuinRest

label KuinSilent:

    QB "EXACTLY! All i do is for the greater good!"

    QB "YES...the greater good...ALL WE NEED IS TO WIN THE COMPETITION AND THEN ALL IS GONNA BE OKAY!"

    QB "They should be worshipping me .....But NOOOOO what do I GET?!"

    QB "COMPLAINS!"

    QB "\"uwu we are working non stop uwuwuwuwu\"They have 1 minute breaks what more do they want?"

    QB "Can you believe that?!"

    QB "And the worst part is i have  to deal with that beetch Breetany......"

    $ kuinEnding = 2

    jump KuinHoldOn

label KuinHoldOn:

    "\"OK HOLD ON A SECOND!\""

    if kuinEnding == 1:

        menu:

            "\"What competition?\"":

                jump KuinCompetion

            "\"Who's Breetany?\"":

                jump KuinBreetany

            "\"Maybe you could talk to your workers?\"":

                jump KuinTalk

    elif kuinEnding == 2:

        menu:

            "\"What competition?\"":

                jump KuinCompetion

            "\"Who's Breetany?\"":

                jump KuinBreetany

            "\"YOU WORK SO HARD FOR THEM!\"":

                jump KuinWork

    elif kuinEnding == 3:

        menu:

            "\"What competition?\"":

                jump KuinCompetion

            "\"Who's Breetany?\"":

                jump KuinBreetany

            "\"You need to chill.\"":

                jump KuinChill

label KuinCompetion:

    if kuinCompetion:

        "\"Competition? What competition?\""

        QB "THE BEST BEE HIVE COMPETITION WHAT ELSE COULD I BEE TALKING ABOUT?! And you bet your  beeswax that we are gonna produce the most honey in bee hive history!!"

        $ kuinCompetion = True

    else:

        QB "Are you deaf? Do I really need to repeat myself?"

    jump KuinHoldOn

label KuinBreetany:

    if kuinBreetany:

        "\"Who's Breetany?\""

        QB "Obviously you wouldn't know about that second grade B lister joke of a \"queen\"." 

        QB "We are going against her hive in the finals, some dare say they are our biggest competition."

        QB "NONSENSE!"

        $ kuinCompetion = True

    else:

        QB "Are you deaf? Do I really need to repeat myself?"

    jump KuinHoldOn

label KuinWork:

    "\"YOU WORK SO HARD FOR THEM!\""

    QB "I DO. I REALLY DO."

    QB "FINALLY someone who appreciates me and my leadership."

    QB "THANK YOU SERV you really sweetened my thoughts."

    "\"YAS QUEEN SLAY!\""

    QB "I WILL. I. Always. Do."

    jump Tavern

label KuinOffGuard:

    "\"That's mean! You caught me off guard!!!\""

    QB "Oh honey, you can hardly call it that! You work on a tree for beesake."

    QB "Good, now that we reached an understanding you shall only adress me as \"Your Majesty\"."

    "\"Look, you don't have to bee here if you don't want to.\""

    jump KuinNobody

label KuinWhat:

    "\"Excuse me... a what? Are aware of what you're asking??\""

label KuinNobody:

    QB "Nobody wants to work these days!"

    QB "Whats so wrong about serving your queen?!"

    menu:

        "\"You're right.\"":

            jump KuinRight

        "\"You're not my queen!\"":

            jump KuinNot

label KuinRest:

    "\"I know it's not my place to say but everyone deserves to rest.\""

    jump KuinGreater

label KuinRight:

    "\"I'm sorry, you're right i was rude.\""

label KuinGreater:

    QB "All i do is for the greater good!"

    QB "YES... the greater good... ALL WE NEED IS TO WIN THE COMPETITION AND THEN ALL IS GONNA BE OKAY!"

    QB "They should be worshipping me..... But NOOOOO what do I GET?!"

    QB "COMPLAINS!"

    QB "\"uwu theres no wifi in my side of the hive uwuwuwuwu\" HOW'S THAT MY FAULT?"

    QB "Can you believe that?!"

    QB "And the worst part is i have  to deal with that beetch Breetanny......"

    $ kuinEnding = 1

    jump KuinHoldOn

label KuinNot:

    "\"You're not my q-\""

    QB "All i do is for the greater good!"

    QB "YES... the greater good... ALL WE NEED IS TO WIN THE COMPETITION AND THEN ALL IS GONNA BE OKAY!"

    QB "They should be worshipping me..... But NOOOOO what do I GET?!"

    QB "COMPLAINS!"

    QB "\"uwu I havent seen my family in months uwuwuwuwu\" HOW'S THAT MY FAULT?"

    QB "Can you believe that?!"

    QB "And the worst part is i have  to deal with that beetch Breetanny......"

    $ kuinEnding = 3

    jump KuinHoldOn

label KuinTalk:

    "\"Maybe you could talk to your workers?\""

    QB "And why would I do that?"

    "\"Um...because...clears throat BECAUSE MY QUEEN THEY WOULD LOVE YOU EVEN MORE!\""

    QB "Ok... i see your point maybe it is worth investing in such frivolous behaviour..."

    "\"YES how WISE of you to let them have fair wages and working schedules!\""

    QB "Wait a minute.........."

    QB "I said that?"

    "\"......................yes...\""

    QB "After all, i am just that wise."

    "\"yes my queen yes.....\""

    jump Tavern

label KuinChill:

    "\"You need to chill.\""

    QB "HOW DARE YOU?!"

    QB "I DONT NEED TO \"CHILL\" I NEED TO WIN!" 

    QB "im gonna show you all.... AND THEN THEY WILL ALL SEE... she will have to see....ANYWAY"

    QB "NOBODY RESTS UNTIL I SAY SO!"

    QB "I would say it was a pleasure to meet you but I prize myself in my honesty with the servants."

    QB "I've mingled enough with the plebe for a day...."

    jump Tavern