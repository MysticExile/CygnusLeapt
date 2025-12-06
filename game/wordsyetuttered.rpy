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
        "Commitment",
        "Embarrassment",
        "ToTheOcean",
        "Weakspot",
        "TheLighthouse",
        "TheDragon",
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

screen unspokenWords():
    on "show" action Play("sound", "/audio/music/The_Falling_Swan_boxver.mp3", loop=True, fadein=0.25)
    on "hide" action Stop("sound")
    tag menu
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        viewport:
            draggable True
            mousewheel True

            vbox:
                spacing 10
                for unspokenWords_entry in sorted(persistent.unspokenWords_unlockable):
                    textbutton "[unspokenWords_entry]":
                        action Show(unspokenWords_entry)
                        text_color "#000"
                        text_hover_color "#963838"

        textbutton "Resume" action [
            Function(resume_music),
            Hide("unspokenWords")
        ]

screen TheSun():
    text "“just like the sun: burns everything that gets too close to it, a melt down near death, and it’s hard to look directly at the truth of you”"
    textbutton "Back" action [
            Hide("TheSun")
        ]