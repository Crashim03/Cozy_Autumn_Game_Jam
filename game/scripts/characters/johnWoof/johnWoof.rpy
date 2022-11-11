label JohnWoofStart:

    scene bg

    show john charisma at truecenter
    with dissolve

    "\"Hello,{w=0.2} what would you like to order?\""

    J "Hi!{w=0.5} I'd like some dog food please!"

    "\"Sure!\""

    "..."

    "\"Here!\""

    J "Thanks"

    "..."

    J "From the look on your face I can tell that you don't know me."

    J "I'm John Woof,{w=0.2} you can follow my account: @totallynotahuman_woofwoof."

    "\"Ah.{w=0.2}.{w=0.2}.{w=0.2} Thanks.\""

    "You go back to the counter.{w=0.5} You notice that he's really struggling to eat his food."
    
    "You approach him again with curiosity."
    

    menu:

        "\"Can I help with anything?\"":

            jump AskHelp

        "\"You know you're not actually a dog,{w=0.2} right?\"":

            jump NotActuallyDog

label AskHelp:

    "\"Can I help with anything,{w=0.2} sir?\""

    show john uwu

    J "\"Ah.{w=0.2}.{w=0.2}.{w=0.2} no,{w=0.2} no. I'm fine,{w=0.2} thanks.{w=0.5} Ha ha ha...\""

    menu:

        "\"Would you like another type of food?\"":

            jump OfferFood

        "Ignore him":

            jump Ignore

label OfferFood:

    "\"Maybe you would like another type of food,{w=0.2} sir?\""

    J "\"Ah.{w=0.2}.{w=0.2}.{w=0.2} Hmm.{w=0.2}.{w=0.2}.{w=0.2} Ok,{w=0.2} I guess...\""

    "You make him a really nice looking salad."

    "John tries it.{w=0.5} You see his eyes shining like never before,{w=0.2} like it was the first time that he ate something meant for humans."

    show john salada

    J "\"OMG,{w=0.2} it's so good!!!{w=0.5} What is this?\""

    "\"It's just salad.\""

    J "\"I don't even know when was the last I had something like this!{w=0.5} Thank you!\""

    show john sad mask

    J "\"I'm gonna be honest.{w=0.5} This influencer life is taking a toll on me.\""

    "\"Maybe you should take a break.{w=0.5} It's nothing to be ashamed of.\""

    J "\"The thing is: I can't.{w=0.5} In case you didn't know,{w=0.2} we're in the middle of a online war between dogs and humans and I'm like super involved.{w=0.5} I can't stop now.\""

    "\"That sounds too serious for an influencer.\""

    J "\"Yeah I know!{w=0.5} I didn't wanna any of this.\""

    J "\"But now my fans expect too much of me.{w=0.5} I don't think I can continue with this type of life.\""

    "\".{w=0.2}.{w=0.2}.{w=0.2}\""

    "John finishes his food."

label Confess:

    show john selfie

    J "\"Hey,{w=0.2} I'm gonna confess something: I'm not actually a dog!\""

    "\"No way.{w=0.2}.{w=0.2}.{w=0.2}\""

    J "\"I KNOW RIGHT?!!!\""

    J "\"A couple of months ago,{w=0.2} I was shopping at the market when I found a mask of a dog.{w=0.5} I bought it,{w=0.2} put it on and took a selfie,{w=0.2} then posted it,{w=0.2} just for a laugh you know?\""

    J "\"But for some reason,{w=0.2} in just one day,{w=0.2} I got like 1000 likes,{w=0.2} all of them from dogs.\""

    J "\"So I had this CRAZY idea: Imma just be one of them.\""

    J "\"I deleted every photo I had with my face on it,{w=0.2} changed my username and gained a crazy amount of followers,{w=0.2} all dogs of course.\""

    J "\"And being a \"dog celebrity\"  I have to be pro-dog and totally toxic against humans.\""

    J "\"That's why this war thing is being so stressful to me.{w=0.5} I kinda don't wanna be bad to humans,{w=0.2} but I also like my fans a lot.\""

    J "\"I don't know what to do...\""

    menu:

        "\"Keep your secret identity.\"":

            jump TellKeepSecret

        "\"You should tell the truth.\"":

            jump TellTruth

label TellKeepSecret:

    "\"I think you should keep your secret identity.\""

    J "\"I don't know man,{w=0.2} I don't wanna be involved in more drama and stuff.\""

    menu:

        "\"You should embrace the mask.\"":

            jump EmbranceMask

        "\"It's too late now.\"":

            jump KeepLow

label EmbranceMask:

    "\"You should embrace your mask!{w=0.5} Look at how many followers you have!{w=0.5} You don't want to disappoint them.\""

    show john charisma

    J "\"Maybe you're right.{w=0.2}.{w=0.2}.{w=0.2} It's better to keep it this way.\""

    J "\"Thank you so much for your advice dude.{w=0.5} I think Imma head out and think about all of this stuff.\""

    $ johnEnding = 2

    jump Tavern

label Ignore:

    show john uwu

    "You ignore him,{w=0.2} but you can notice by the corner of your eye,{w=0.2} he's getting impatience and failing hard to look casual about it."

label Honest:

    show john selfie

    J "\"I'm gonna be honest.{w=0.5} This influencer life is taking a toll on me.\""

    "\"Maybe you should take a break.{w=0.5} It's nothing to be ashamed of.\""

    J "\"The thing is: I can't.{w=0.5} In case you didn't know,{w=0.2} we're in the middle of a virtual war between dogs and humans and I'm like super involved.{w=0.5} I can't stop now.\""

    "\"That sound too serious for an influencer.\""

    J "\"Yeah I know!{w=0.5} I didn't wanna any of this.\""

    J "\"But now my fans expect too much of me.{w=0.5} I don't think I can continue with this type of life.\""

    "\".{w=0.2}.{w=0.2}.{w=0.2}\""

    "John finishes his food."

    menu:

        "\"I understand.\"":

            jump Sympathize

        "\"It's your fault.\"":

            jump HisFault

label Sympathize:

    "\"I understand.{w=0.2}.{w=0.2}.{w=0.2}but you also need time for self-care,{w=0.2} bud.{w=0.5} If your fans are really your fans,{w=0.2} I'm sure they'll understand.\""

    show john uwu

    J "\"Thank you,{w=0.2} I needed that.\""

    jump Confess

label TellTruth:

    "\"You should tell the truth to your fans.\""
    
    show john uwu

    J "\"Well,{w=0.2} I thought of doing that,{w=0.2} but I don't know what to say!\""

    menu:

        "\"It's the fans' fault for believing you.\"":

            jump FansFault

        "\"Just be honest.\"":

            jump BeHonest

label FansFault:

    "\"It's the fans' fault for believing you in the first place!{w=0.5}  Just tell them.\""

    J "\"Uhh.{w=0.2}.{w=0.2}.{w=0.2} Are you sure?\""

    "\"Yeah,{w=0.2} I am!{w=0.5} Just do it.\""

    hide john uwu with dissolve

    $ johnEnding = 3

    jump Tavern

label KeepLow:

    "\"I think it's too late now.{w=0.5} You should keep a low profile and keep your account.{w=0.5} Maybe sell some merch!\""

    show john uwu

    J "\"You really think so?\""

    "\"Yeah!\""

    J "\"Well.{w=0.2}.{w=0.2}.{w=0.2} if you say so...\""
    
    "John leaves the tavern."

    $ johnEnding = 4

label BeHonest:

    "\"Just be honest.{w=0.5} I'm sure your fans will accept you by how you are!\""

    J "You sure?"

    "\"Yes!!!\""

    show john charisma

    J "\"Well,{w=0.2} I'll believe you then!\""

    J "\"Imma head out and just let all out!\""

    hide john charisma with dissolve

    $ johnEnding = 1

    jump Tavern

label HisFault:

    "\"You brought this to yourself.{w=0.5} You looked for attention in the wrong places and now you're collecting the fruits of your work.\"" 
    
    "\"You had it coming.\""

    show john sad mask

label GetOut:

    "John gets up in a pouty way,{w=0.2} stomps in place and leaves without glancing twice at you.{w=0.5} His diva personality clearly wasn't \"vibing\" with your honesty."

    $ johnEnding = 3

    jump Tavern

label NotActuallyDog:

    "\"You know you're not actually a dog,{w=0.2} right?\""

    show john uwu

    J "\"Uhhhh.{w=0.2}.{w=0.2}.{w=0.2} I don't know what you're talking about.\""

    menu:

        "\"Sorry.\"":

            jump Apologize

        "\"Cut the act.\"":

            jump Insist

label Apologize:

    "\"Sorry,{w=0.2} I didn't mean to sound rude.\""

    J "\"It's ok,{w=0.2} all humans make mistakes.\""

    show john charisma

    jump Honest

label Insist:

    "\"You can cut the act,{w=0.2} I can clearly see that's a mask you're wearing.\""

    show john selfie

    J "\"What the hell are you talking about?!\""

    J "\"Don't you see this is how I look?!\""

    "\"Yeah I see,{w=0.2} like a fool.\""

    J "\"Ok ok,{w=0.2} you don't need to be so mean!\""

    J "\"Yes,{w=0.2} I'm a human.{w=0.5} Are you happy now?!\""

    J "\"I kept this secret for a long time now,{w=0.2} but if dogs,{w=0.2} or {i}people{/i} find out like you just did,{w=0.2} I might be in big trouble.\""

    menu:

        "\"Lying won't help in the long run.\"":

            jump ConvinceTruth

        "\"Keep a low profile.\"":

            jump LateReveal

label ConvinceTruth:

    "\"Buddy.{w=0.2}.{w=0.2}.{w=0.2} I've seen it all in my time,{w=0.2} lying won't help you in the long run.{w=0.5} The longer you drag it the more it will worn out.\""

    "\"Be honest to your fans as soon as you can.\""

    show john big

    J "\"*{i}gasps{/i}* WHY DO SUCH THING?!{w=0.5} I don't need to prove anything!{w=0.5} MY FANS know how I am totally honest and totally MYSELF in everything I do!\""

    jump GetOut

label LateReveal:

    "\"I think it's too late now.{w=0.5} You should keep a low profile and keep your account.{w=0.5} Maybe sell some merch!\""

    J "\"You really think so?\""

    "\"Yeah!\""

    J "\"Well.{w=0.2}.{w=0.2}.{w=0.2} if you say so...\""

    "John leaves the tavern."

    $ johnEnding = 4

    jump Day1

label end:
    return
