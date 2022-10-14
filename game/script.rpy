define J = Character("John Woof", color="#ffffff")

label start:

    play music "audio/jam_cozy_bg.mp3"

    scene bg

label JohnWoof_start:

    show john charisma at truecenter
    with dissolve

    J "\"Hi! I'd like some dog food please!\""

    "\"Sure! Here.\""

    J "\"Thanks\""

    J "\"...\""

    J "\"From the look on your face I can tell that you don't know me.\""

    J "\"I'm John Woof, you can follow my account: @totallynotadog_woofwoof.\""

    "\"Ah... Thanks.\""

    "John proceeds to sit on one of the chairs. You notice that he's really struggling to eat his food."

    "You approach him with curiosity."

    menu:

        "Ask if he needs help.":

            jump AskHelp

        "Tell him that he's not actually a dog.":

            jump NotActuallyDog

label AskHelp:

    "\"Can I help with anything, sir?\""

    show john uwu

    J "\"Ah... no, no. I'm fine, thanks. Ha ha ha...\""

    menu:

        "Offer him other food.":

            jump OfferFood

        "Ignore him":

            jump Ignore

label OfferFood:

    "\"Maybe you would like another type of food, sir?\""

    J "\"Ah... Hmm... Ok, I guess...\""

    "You make him a really nice looking salad."

    "John tries it. You see his eyes shining like never before, like it was the first time that he ate something meant for humans."

    show john salada

    J "\"OMG, it's so good!!! What is this?\""

    "\"It's just salad.\""

    J "\"I don't even know when was the last I had something like this! Thank you!\""

    show john sad mask

    J "\"I'm gonna be honest. This influencer life is taking a toll on me.\""

    "\"Maybe you should take a break. It's nothing to be ashamed of.\""

    J "\"The thing is: I can't. In case you didn't know, we're in the middle of a online war between dogs and humans and I'm like super involved. I can't stop now.\""

    "\"That sound too serious for an influencer.\""

    J "\"Yeah I know! I didn't wanna any of this.\""

    J "\"But now my fans expect too much of me. I don't think I can continue with this type of life.\""

    "\"...\""

    "John finishes his food."

label Confess:

    show john selfie

    J "\"Hey, I'm gonna confess something: I'm not actually a dog!\""

    "\"No way...\""

    J "\"I KNOW RIGHT?!!\!"

    J "\"A couple of months ago, I was shopping at the market when I found a mask of a dog. I bought it, put it on and took a selfie, then posted it, just for a laugh you know?\""

    J "\"But for some reason, in just one day, I got like 1000 likes, all of them from dogs.\""

    J "\"So I had this CRAZY idea: Imma just be one of them.\""

    J "\"I deleted every photo I had with my face on it, changed my username and gained a crazy amount of followers, all dogs of course.\""

    J "\"And being a \"dog celebrity\"  I have to be pro-dog and totally toxic against humans.\""

    J "\"That's why this war thing is being so stressful to me. I kinda don't wanna be bad to humans, but I also like my fans a lot.\""

    J "\"I don't know what to do...\""

    menu:

        "Tell him to keep his secret identity.":

            jump TellKeepSecret

        "Convince John to tell the truth.":

            jump TellTruth

label TellKeepSecret:

    "\"I think you should keep your secret identity.\""

    J "\"I don't know man, I don't wanna be involved in more drama and stuff.\""

    menu:

        "Tell him he should embrace the mask.":

            jump EmbranceMask

        "Tell him it's to late to reveal his identity, but to keep a low profile":

            jump KeepLow

label EmbranceMask:

    "\"You should embrace your mask! Look at how many followers you have! You don't want to disappoint them.\""

    show john charisma

    J "\"Maybe you're right... It's better to keep it this way.\""

    J "\"Thank you so much for your advice dude. I think Imma head out and think about all of this stuff.\""

    jump TheyFoundOut

label TheyFoundOut:

    hide john charisma with dissolve

    scene bg with fade

    "*Next day.*"

    "John woof enters. He approaches you with a sad look on his face."

    show john sad
    
    J "\"They found out.\""

    "\"Wait... How?\""

    J "\"I was doing a livestream for about 4 hours. At some point I started to get really sweaty and my mask fell off.\""

    jump Canceled

label Canceled:

    show john sad

    J "\"I got cancelled.\""

    "\"Oh no...\""

    J "\"I don't what to do this anymore. Everyone hates me now.\""

    "\"I'm sure they'll forget at some point in the future.\""

    J "\"Maybe...\""

    J "\"Well... Right now, I just want a drink.\""

    "\"Sure, what would you like to have?\""

    J "\"A glass of milk please.\""

    "You give the glass of milk. John takes it and sits at the corner of the room."

    jump end

label Ignore:

    show john uwu

    "You ignore him, but you can notice by the corner of your eye, he's getting impatience and failing hard to look casual about it."

label Honest:

    show john selfie

    J "\"I'm gonna be honest. This influencer life is taking a toll on me.\""

    "\"Maybe you should take a break. It's nothing to be ashamed of.\""

    J "\"The thing is: I can't. In case you didn't know, we're in the middle of a virtual war between dogs and humans and I'm like super involved. I can't stop now.\""

    "\"That sound too serious for an influencer.\""

    J "\"Yeah I know! I didn't wanna any of this.\""

    J "\"But now my fans expect too much of me. I don't think I can continue with this type of life.\""

    "\"...\""

    "John finishes his food."

    menu:

        "Sympathize with him.":

            jump Sympathize

        "Tell him that it's his fault.":

            jump HisFault

label Sympathize:

    "\"I understand...but you also need time for self-care, bud. If your fans are really your fans, I'm sure they'll understand.\""

    show john uwu

    J "\"Thank you, I needed that.\""

    jump Confess

label TellTruth:

    "\"You should tell the truth to your fans.\""
    
    show john uwu

    J "\"Well, I thought of doing that, but I don't know what to say!\""

    menu:

        "Tell him it was the fans fault for believing him.":

            jump FansFault

        "Tell him to be honest.":

            jump BeHonest

label FansFault:

    "\"It's the fans fault for believing in you in the first place!  Just tell them.\""

    J "\"Uhh... Are you sure?\""

    "\"Yeah, I am! Just do it.\""

    hide john uwu with dissolve

    scene bg with fade

    "*Next day.*"

    jump Canceled

label KeepLow:

    "\"I think it's too late now. You should keep a low profile and keep your account. Maybe sell some merch!\""

    show john uwu

    J "\"You really think so?\""

    "\"Yeah!\""

    J "\"Well... if you say so...\""
    
    "John leaves the tavern."

label LostHumanity:

    hide john uwu with dissolve

    scene bg with fade

    "*Next day.*"

    "You see John Woof entering. He looks around a bit, then sits."

    show john masked

    "He looks a bit off..."

    "You slowly approach him."

    "\"Hey, is everything alright?\""

    J "\"Woof woof!!!\""

    "\"Wha-\""

    J "\"BARK!\""

    "Oh no... He completely lost his humanity."

    jump end

label BeHonest:

    "\"Just be honest. I'm sure your fans will accept you by how you are!\""

    J "You sure?"

    "\"Yes!!!\""

    show john charisma

    J "\"Well, I'll believe you then!\""

    J "\"Imma head out and just let all out!\""

    hide john charisma with dissolve

    scene bg with fade

    "*Next day.*"    

    "You see John Woof entering the tavern. He's not using his mask and seems really happy."

    show john merch
    
    J "\"Hey!\""

    "\"Hi! So, what happened?\""

    J "\"Everything went smoothly! And guess what? The war between humans and dogs is over!\""

    "\"Wait, how?\""

    J "\"I guess due to my fans accepting me, the other dogs started to be more open minded.\""

    J "\"Which is, like, super cool!\""

    "\"That's really good. I'm really happy for you!\""

    J "\"Thank you!\""

    J "\"By the way, do you have chocolate, it's been a long time since I ate some.\""

    "\"Yeah, I do. Here.\""

    J "\"Thanks.\""

    jump end

label HisFault:

    "\"You brought this to yourself. You looked for attention in the wrong places and now you're collecting the fruits of your work.\"" 
    
    "\"You had it coming.\""

    show john sad mask

label GetOut:

    "John gets up in a pouty way, stomps in place and leaves without glancing twice at you. His diva personality clearly wasn't \"vibing\" with your honesty."

    jump TheyFoundOut

label NotActuallyDog:

    "\"You know you're not actually a dog, right?\""

    show john uwu

    J "\"Uhhhh... I don't know what you're talking about.\""

    menu:

        "Apologize.":

            jump Apologize

        "Insist.":

            jump Insist

label Apologize:

    "\"Sorry, I didn't mean to sound rude.\""

    J "\"It's ok, all humans make mistakes.\""

    show john charisma

    jump Honest

label Insist:

    "\"You can cut the act, I can clearly see that's a mask you're wearing.\""

    show john selfie

    J "\"What the hell are you talking about?!\""

    J "\"Don't you see this is how I look?!\""

    "\"Yeah I see, like a fool.\""

    J "\"Ok ok, you don't need to be so mean!\""

    J "\"Yes, I'm a human. Are you happy now?!\""

    menu:

        "Convince him to tell the truth.":

            jump ConvinceTruth

        "Tell him it's to late to reveal his identity, but to keep a low profile.":

            jump LateReveal

label ConvinceTruth:

    "\"Buddy...I've seen it all in my time, lying won't help you in the long run. The longer you drag it the more it will worn out.\""

    "\"Be honest to your fans as soon as you can.\""

    show john big

    J "\"*{i}gasps{/i}* WHY DO SUCH THING?! I don't need to prove anything! MY FANS know how I am totally honest and totally MYSELF in everything I do!\""

    jump GetOut

label LateReveal:

    "\"I think it's too late now. You should keep a low profile and keep your account. Maybe sell some merch!\""

    J "\"You really think so?\""

    "\"Yeah!\""

    J "\"Well... if you say so...\""

    "John leaves the tavern."

    jump LostHumanity

label end:
    return
