label KuinStart:

    QB "Good Afternoon servant of this establishment."

    "\"Umm.{w=0.2}.{w=0.2}.{w=0.2} hi there!\""

    QB "Shall i instruct you on how to proceed?{w=0.5} You seem to be inadequate."

    menu:

        "\"No its just your way of speech was a bit peculiar.\"":
            
            jump KuinPeculiar

        "\"You caught me off guard!\"":

            jump KuinOffGuard

label KuinPeculiar:

    "\"What?.{w=0.2}.{w=0.2}.{w=0.2} No its just your way of speech was a bit.{w=0.2}.{w=0.2}.{w=0.2} peculiar.\"" 

    "\"What will it be?\""

    QB "Good,{w=0.2} now that we reached an understanding you shall only adress me as \"Your Majesty\"."

    QB "For starters,{w=0.2} a latte with two pumps of pure gluten free honey will do."

    menu:

        "\"As you wish.\"":

            jump KuinWish

        "\"What?\"":

            jump KuinWhat

label KuinWish:

    "\"Umm,sure.\""

    "\"As you wish...\""

    QB "Excuse me you seem to enjoy a life of servitude.{w=0.5} So tell me.{w=0.2}.{w=0.2}.{w=0.2} am i SOO wrong for wishing the best for my hive??!!"
    
    QB "All it takes is just a littleeee overtime.{w=0.5} which is basically asking nothing right?!RIGHT?!"

    menu:

        "Keep silent.":

            jump KuinSilent

        "\"Everyone deserves to rest.\"":

            jump KuinRest

label KuinSilent:

    QB "EXACTLY!{w=0.5} All i do is for the greater good!"

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

        "\"Competition?{w=0.5} What competition?\""

        QB "THE BEST BEE HIVE COMPETITION WHAT ELSE COULD I BEE TALKING ABOUT?!{w=0.5} And you bet your  beeswax that we are gonna produce the most honey in bee hive history!!"

        $ kuinCompetion = True

    else:

        QB "Are you deaf?{w=0.5} Do I really need to repeat myself?"

    jump KuinHoldOn

label KuinBreetany:

    if kuinBreetany:

        "\"Who's Breetany?\""

        QB "Obviously you wouldn't know about that second grade B lister joke of a \"queen\"." 

        QB "We are going against her hive in the finals,{w=0.2} some dare say they are our biggest competition."

        QB "NONSENSE!"

        $ kuinCompetion = True

    else:

        QB "Are you deaf?{w=0.5} Do I really need to repeat myself?"

    jump KuinHoldOn

label KuinWork:

    "\"YOU WORK SO HARD FOR THEM!\""

    QB "I DO.{w=0.5} I REALLY DO."

    QB "FINALLY someone who appreciates me and my leadership."

    QB "THANK YOU SERV you really sweetened my thoughts."

    "\"YAS QUEEN SLAY!\""

    QB "I WILL.{w=0.5} I.{w=0.5} Always.{w=0.5} Do."

    jump Tavern

label KuinOffGuard:

    "\"That's mean!{w=0.5} You caught me off guard!!!\""

    QB "Oh honey,{w=0.2} you can hardly call it that!{w=0.5} You work on a tree for beesake."

    QB "Good,{w=0.2} now that we reached an understanding you shall only adress me as \"Your Majesty\"."

    "\"Look,{w=0.2} you don't have to bee here if you don't want to.\""

    jump KuinNobody

label KuinWhat:

    "\"Excuse me.{w=0.2}.{w=0.2}.{w=0.2} a what?{w=0.5} Are aware of what you're asking??\""

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

    "\"I'm sorry,{w=0.2} you're right i was rude.\""

label KuinGreater:

    QB "All i do is for the greater good!"

    QB "YES.{w=0.2}.{w=0.2}.{w=0.2} the greater good.{w=0.2}.{w=0.2}.{w=0.2} ALL WE NEED IS TO WIN THE COMPETITION AND THEN ALL IS GONNA BE OKAY!"

    QB "They should be worshipping me...{w=0.2}.{w=0.2}.{w=0.2} But NOOOOO what do I GET?!"

    QB "COMPLAINS!"

    QB "\"uwu theres no wifi in my side of the hive uwuwuwuwu\" HOW'S THAT MY FAULT?"

    QB "Can you believe that?!"

    QB "And the worst part is i have  to deal with that beetch Breetanny......"

    $ kuinEnding = 1

    jump KuinHoldOn

label KuinNot:

    "\"You're not my q-\""

    QB "All i do is for the greater good!"

    QB "YES.{w=0.2}.{w=0.2}.{w=0.2} the greater good.{w=0.2}.{w=0.2}.{w=0.2} ALL WE NEED IS TO WIN THE COMPETITION AND THEN ALL IS GONNA BE OKAY!"

    QB "They should be worshipping me...{w=0.2}.{w=0.2}.{w=0.2} But NOOOOO what do I GET?!"

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

    QB "Ok.{w=0.2}.{w=0.2}.{w=0.2} i see your point maybe it is worth investing in such frivolous behaviour..."

    "\"YES how WISE of you to let them have fair wages and working schedules!\""

    QB "Wait a minute.........."

    QB "I said that?"

    "\"......................yes...\""

    QB "After all,{w=0.2} i am just that wise."

    "\"yes my queen yes.....\""

    jump Tavern

label KuinChill:

    "\"You need to chill.\""

    QB "HOW DARE YOU?!"

    QB "I DONT NEED TO \"CHILL\" I NEED TO WIN!" 

    QB "im gonna show you all..{w=0.2}.{w=0.2}.{w=0.2} AND THEN THEY WILL ALL SEE.{w=0.2}.{w=0.2}.{w=0.2} she will have to see....ANYWAY"

    QB "NOBODY RESTS UNTIL I SAY SO!"

    QB "I would say it was a pleasure to meet you but I prize myself in my honesty with the servants."

    QB "I've mingled enough with the plebe for a day...."

    jump Tavern