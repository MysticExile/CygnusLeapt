python early:
    def unlock_unspokenWord(entry):
        persistent.unspokenWords_unlockable.add(unspokenWords_unlockable[entry])

init python:
    def pause_music():
        renpy.music.set_pause(True)

    def resume_music():
        renpy.music.set_pause(False)

init:
    define unspokenWords_unlockable = (
        "TheSun",
        "Sand",
        "Hiding",
        "RepeatOffender",
        "BiteBack",
        "Confession",
        "Embarrassment",
        "ToTheOcean",
        "Weakspot",
        "Lighthouse",
        "TheDragon",
        "TheSunshine",
        "Icarus",
        "Pressure",
        "WolfHowl",
        "TwoOfCups",
        "Repeat",
        "BalletAstronomy",
        "PoetSoulReleaseMe",
        "YourLifeAfter9AM",
        "YourLifeAfter9PM",
        "FourthWallVanity",
        "WhoIsTheMoth",
        "TheSunlight",
        "Chronic",
        "TheMiddleOfIt",
        "Anagnorisis",
        "Slip",
        "LosingHand",
        "Checkpoint",
        "YourKindOfWater",
        "ToShredsYouSay",
        "SisyphusTantalusAndMe"
        )

default persistent.unspokenWords_unlockable = set()
default persistent.unspokenWordsUI = False
default persistent.randpose = 1

transform dissolve_hover(idle_image, hover_image):
    alpha 0.40
    on idle:
        idle_image with Dissolve(0.05)
    on hover:
        hover_image with Dissolve(0.05)

screen unspokenWords():
    $ persistent.randpose = renpy.random.randint(1,4)
    on "show" action Play("sound", "/audio/music/The_Falling_Swan_boxver.mp3", loop=True, fadein=0.25)
    on "hide" action Stop("sound")
    #tag menu
    #add "filmbg"
    modal True
    frame:
        background "filmbg"
        xalign 0.95
        ysize 1080
        add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
        viewport id "unspokenwords":
            draggable True
            mousewheel True
            xalign 0.95
            xfill False
            vbox:
                xalign 0.95
                spacing 10
                for unspokenWords_entry in persistent.unspokenWords_unlockable:
                    if(unspokenWords_entry == "TheSun"):
                        textbutton "The Sun":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "RepeatOffender"):
                        textbutton "Repeat Offender":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "BiteBack"):
                        textbutton "Bite Back":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "Confession"):
                        textbutton "Confession and Commitment":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "ToTheOcean"):
                        textbutton "To The Ocean":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "TheDragon"):
                        textbutton "The Dragon":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "TheSunshine"):
                        textbutton "The Sunshine":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "WolfHowl"):
                        textbutton "Wolf Howl":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "TwoOfCups"):
                        textbutton "spuc fo owT":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "BalletAstronomy"):
                        textbutton "Ballet Astronomy":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "PoetSoulReleaseMe"):
                        textbutton "Poet Soul Release Me":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "YourLifeAfter9AM"):
                        textbutton "Your Life After 9am":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "YourLifeAfter9PM"):
                        textbutton "Your Life After 9pm":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "FourthWallVanity"):
                        textbutton "Fourth Wall Vanity":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "WhoIsTheMoth"):
                        textbutton "Who is the Moth?":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "TheSunlight"):
                        textbutton "The Sunlight":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "TheMiddleOfIt"):
                        textbutton "The Middle of It":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "LosingHand"):
                        textbutton "Losing Hand":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "YourKindOfWater"):
                        textbutton "Your Kind of Water":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "ToShredsYouSay"):
                        textbutton "To Shreds, You Say?":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    elif(unspokenWords_entry == "SisyphusTantalusAndMe"):
                        textbutton "Sisyphus, Tantalus, and Me":
                            action ShowMenu(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
                    else:
                        textbutton "[unspokenWords_entry]":
                            action Show(unspokenWords_entry)
                            text_color "#fff"
                            text_hover_color "#963838"
                            text_align 1.0
        vbar value YScrollValue("unspokenwords") xalign 1.0

    if main_menu:
        textbutton "Resume" action [
        Function(resume_music),
        Hide("unspokenWords")
    ] xalign 0.5 yalign 1.0
    elif not main_menu:
        textbutton "Resume" action [
        Function(resume_music),
        Return()
    ] xalign 0.5 yalign 1.0

screen TheSun():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“just like the sun: burns everything that gets too close to it, a melt down near death, and it’s hard to look directly at the truth of you”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("TheSun") xalign 0.5

screen Sand():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“too much, but never enough, all the words pour out of you and they're almost the right ones. the pieces are all there, you just can't make them fit. It slips through your fingers again”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Sand") xalign 0.5

screen Hiding():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“sometimes you want to scream and thrash and tear the parts that whispered right out to where everyone can see them”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Hiding") xalign 0.5

screen RepeatOffender():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“can you still love me after the calamity? how far can I fall and still see you waiting for me arms out stretched, at the end”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("RepeatOffender") xalign 0.5

screen BiteBack():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“hold your breath until you can taste the blood”\n“the taste of bile and blood”\n“it burns and stings and sings at me but I can't let it go”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("BiteBack") xalign 0.5

screen Confession():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“is this what's best, or is it what I want? are they allowed to be the same?”\n“bruises on my throat from pulling on my chains”\n“I just want someone to care about me as much as I care about them”\n“maybe it's silly to want to be loved like that”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Confession") xalign 0.5

screen Embarrassment():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“If only there was the catharsis of crying without the shedding of tears. if only there was the you that existed all of the time instead of the you that exists between the lives of others. Are your masks bearing down on you?”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Embarrassment") xalign 0.5

screen ToTheOcean():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“the river of who I am had changed so much through the way it had flowed against you. It runs its course and diverts at all your angles. but rivers always flow away, and may not always take you with them”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("ToTheOcean") xalign 0.5

screen Lighthouse():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“but does anyone need me?”\n“I have never felt more like a cage”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Lighthouse") xalign 0.5

screen Weakspot():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“I want to be vulnerable, and I want it to help for once. I want to tell someone my problem and not feel worse off for it. I want you to pierce me right through the heart and leave it still whole and beating”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Weakspot") xalign 0.5

screen TheDragon():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“like anyone I want to be loved. like a monster I want to be coveted”\n“can your heart take it? can't your heart take it? when will you be learn to be happy with what you have, why must you keep asking for more?”\n“I want to be loved. so it is. I want to feel loved too... I crave it. it's not enough to know and to know it's not enough”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("TheDragon") xalign 0.5

screen TheSunshine():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“I just want to be the priority. I just want to be the sweet spot. I just want to be loved and not have to ask for it. maybe the sun is easy to take for granted”\n“is it hard for the sun after all? to rise in the morning and set in the evening? this massive celestial body of nuclear fusion. maybe it's more work than we give it credit for”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("TheSunshine") xalign 0.5

screen Icarus():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“sometimes bad news is a gift. A reason to give up and stop fighting. To have choice stolen from you so you can tip back into the vortex and take false solace that this time there's no reason to resist.”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Icarus") xalign 0.5

screen Pressure():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“you worry you're not right for my love, and the sky worries it's not right for the sun, the bird worries it's not right for the song, the applause worries it's not right for the story. But I wonder (maybe selfishly) if the sun isn't right for the sky where does it go? Who is this song for if not the breath of the bird? Why is this story told if not for the rapture of the audience? who am I right for, if not you”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Pressure") xalign 0.5

screen WolfHowl():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“I wasted my time with you!!!”\n“I should have asked for it! I tear and scream and yell because I endured and for what? Who was this for, if not myself and if not for you! I deserved better! I'm real! I'm real!!! I am calamity and I deserve to be loved!”\n“I trusted you with my worst and it made you forget my best. how long have you been seeing me as a shade of who I am”\n“am I really so pathetic, so weak willed? the wilting flower was only an act, time to steel that resolution”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("WolfHowl") xalign 0.5

screen TwoOfCups():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“I poured all of it into your cup. I left it full and brimming and yet you tell me that what, you thought it was the leftover wine from the party? my cup runneth over":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("TwoOfCups") xalign 0.5

screen Repeat():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“Hard to love, Easy to thrill”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Repeat") xalign 0.5

screen BalletAstronomy():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“at the center of our universe is a super massive black hole. it's so large we can't even measure it, but we can see the outline and it's the only thing that makes sense.”\n“and this abyss at the center of everything is slowly pulling everything apart.” \n“I will always be here for you to hold on to, to resist that pull, as long as you want me.” \n“but that's the crux of it, you have to be the one that holds on. I'll always want to hold you, and that's why I have to make sure you know you're free to go.” \n“You, who are so reluctant to stay, or maybe even to start, have to be the one to choose this. and keep choosing it. to dig your fangs in and hold fast when when it's hard. you have to keep choosing me. you have to keep choosing us.”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("BalletAstronomy") xalign 0.5

screen PoetSoulReleaseMe():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“I think of you. I don't know what to write or what to say or how to fix it. I just want you to love me”\n“I feel like I'm just waiting for you to come home I feel like I'm just waiting for you to say goodbye”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("PoetSoulReleaseMe") xalign 0.5

screen Hope():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“There are so many more ways I want to know you. So many moves left to make. Do not borrow pain from the future. Suffering now will not lessen the suffering if it is to come. If it goes wrong? so be it. but it can still go right”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Hope") xalign 0.5

screen YourLifeAfter9AM():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“the despair sets in slowly and gently, like dew upon the grass”\n“how many battles can you lose and still win the war”\n“please just figure it out already”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("YourLifeAfter9AM") xalign 0.5 yalign 0.0

screen YourLifeAfter9PM():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“what if I'm not as strong as i thought I was. it becomes harder each time not to let you go”\n“I love you so much but you've left me so undone”\n“late at night, I miss you. I wait by the gate patiently to see you again. I just worry the time you'll be on the other side, where I cannot cross”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("YourLifeAfter9PM") xalign 0.5 yalign 0.0

screen FourthWallVanity():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“the unstoppable entropy of the self crashing into the simple husk of the soul. string words together to mean nothing”\n“I have feelings for you. do you even understand what that means? am I a real person to you or just a trick? do you understand the consequences? are you even trying to? by the end of this sentence? 70 characters left. speak quickly to my heart. above the rush of blood”\n“I've come to terms with it, in my heart I think. or maybe I've come to terms with it in my head and my heart still clings desperately”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("FourthWallVanity") xalign 0.5 yalign 0.0

screen WhoIsTheMoth():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“when I wake up I will love you but for now I am fire”\n“put me out then reignite me”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("WhoIsTheMoth") xalign 0.5

screen TheSunlight():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“I want you to know I notice not only your presence in the room, but your absence too. we move separately together and when we cross back over to each other's light, I always smile at your warmth”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("TheSunlight") xalign 0.5

screen Chronic():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“Sad forever. What has it cost you? What will it cost you further?”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Chronic") xalign 0.5

screen TheMiddleOfIt():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“that little death that little death that little death that little death that little death that little death that little death that little death that little death that little death that little death that little death that little death that little death that little death that little death”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("TheMiddleOfIt") xalign 0.5

screen Anagnorisis():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“I shiver, recede at the touch. the truth is too close to me now, and what if it's one I don't like”\n“if you must ask for so much, what are you allowed to ask for in return. how much must a calamity bear to atone for its own cost”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Anagnorisis") xalign 0.5

screen Slip():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“may the vortex take me”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Slip") xalign 0.5

screen LosingHand():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“the gamblers prayer... the thousand sided die... how many times have I lost this bet, and yet I still make it again and again”":
            xalign 0.5 yalign 0.5
    textbutton "Back" action Hide("LosingHand") xalign 0.5

screen Checkpoint():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“what did I miss how did I miss it? why do I feel such dread for something I don't even know that's passed me by?”\n“it clicks, like bone against bone. grating. hurting. it wears itself down but it must keep going”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("Checkpoint") xalign 0.5

screen YourKindOfWater():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“please just let me out, wake me up, cast me so far out I can't see the shore”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("YourKindOfWater") xalign 0.5

screen ToShredsYouSay():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“I thought about breaking myself a few times. it wouldn't be hard. to grab the sides with both hands and place my thumbs in the center. push and pull and twist it until it shatters to pieces. let someone be put back together who can actually handle all this. I won't. but I think about it. I could.”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("ToShredsYouSay") xalign 0.5

screen SisyphusTantalusAndMe():
    add "filmbg"
    add "game/images/cgs/cygnuspose 1.webp" at cygnusdancing
    frame:
        xalign 0.5 yalign 0.5 xsize 800 ysize 300 background None
        text "“it's so exhausting, always holding back”":
            xalign 0.5 yalign 0.5 text_align 0.5 xmaximum 780
    textbutton "Back" action Hide("SisyphusTantalusAndMe") xalign 0.5
