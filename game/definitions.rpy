init:
    define E = Character(
            "Erin",
            color = "#a0aac7",
            what_prefix = "\"",
            what_suffix = "\"",
            cb_character = "E",
            image = "e"
    )

    define C = Character(
            "Cygnus",
            color = "#862f2f",
            what_prefix = "\"",
            what_suffix = "\"",
            cb_character = "C",
            image = "c"
    )

    define K = Character(
            "Kosta",
            color = "#aa6acf",
            what_prefix = "\"",
            what_suffix = "\"",
            cb_character = "K",
            image = "k"
    )

    define D = Character(
            "Director",
            color = "#00ff95",
            what_prefix = "\"",
            what_suffix = "\"",
            cb_character = "D",
            image = "d"
    )

    define B = Character(
            "Boss",
            color = "#3cff00",
            what_prefix = "\"",
            what_suffix = "\"",
            cb_character = "D",
            image = "d"
    )

    define G = Character(
            "Security Guard",
            color = "#ffffff",
            what_prefix = "\"",
            what_suffix = "\"",
            cb_character = "G",
            image = "g"
    )

    layeredimage c:
        zoom 0.30
        always:
                "sprites/cygnus/cygnus normal/base.webp"

        group body:
                attribute arm_neutral default:
                        "sprites/cygnus/cygnus normal/arm pitflash neutral.webp"
                attribute arm_laugh:
                        "sprites/cygnus/cygnus normal/arm pitflash laugh.webp"
                attribute arm_smug:
                        "sprites/cygnus/cygnus normal/arm pitflash smug.webp"
                attribute arm_speaking:
                        "sprites/cygnus/cygnus normal/arm pitflash speaking.webp"
                attribute arm_surprise:
                        "sprites/cygnus/cygnus normal/arm pitflash surprise.webp"
                attribute arm_resting:
                        "sprites/cygnus/cygnus normal/arm resting.webp"
                attribute arm_hand:
                        "sprites/cygnus/cygnus normal/arm hand.webp"

        group face auto:
                attribute neutral default:
                        "sprites/cygnus/cygnus normal/head neutral.webp"
                attribute happy:
                        "sprites/cygnus/cygnus normal/head happy.webp"
                attribute laugh:
                        "sprites/cygnus/cygnus normal/head laugh.webp"
                attribute smug:
                        "sprites/cygnus/cygnus normal/head smug.webp"
                attribute speaking:
                        "sprites/cygnus/cygnus normal/head speaking.webp"
                attribute surprise:
                        "sprites/cygnus/cygnus normal/head surprise.webp"

        group leotard:
                attribute leotard default:
                        "sprites/cygnus/cygnus normal/leotard normal.webp"
                attribute leotard_pitflash:
                        "sprites/cygnus/cygnus normal/leotard pitflash.webp"

        group jacket_left:
                attribute jacket_left default:
                        "sprites/cygnus/cygnus normal/jacket leftside.webp"

        group jacket:
                attribute jacket_laugh:
                        "sprites/cygnus/cygnus normal/jacket arm pitflash laugh.webp"
                attribute jacket_neutral default:
                        "sprites/cygnus/cygnus normal/jacket arm pitflash neutral happy.webp"
                attribute jacket_smug:
                        "sprites/cygnus/cygnus normal/jacket arm pitflash smug.webp"
                attribute jacket_speaking:
                        "sprites/cygnus/cygnus normal/jacket arm pitflash speaking.webp"
                attribute jacket_surprise:
                        "sprites/cygnus/cygnus normal/jacket arm pitflash neutral.webp"
                attribute jacket_resting:
                        "sprites/cygnus/cygnus normal/jacket arm resting.webp"
                attribute jacket_hand:
                        "sprites/cygnus/cygnus normal/jacket arm hand.webp"
        
        group tail:
                attribute tail_noclothes:
                        "sprites/cygnus/cygnus normal/tail no clothes.webp"
                attribute tail_clothes default:
                        "sprites/cygnus/cygnus normal/tail under jacket.webp"

        group pants:
                attribute pants default:
                        "sprites/cygnus/cygnus normal/pants.webp"

layeredimage c_sad:
        zoom 0.3
        always:
                "sprites/cygnus/cygnus sad/base.webp"
        
        group face:
                attribute depressed default:
                        "sprites/cygnus/cygnus sad/head depressed.webp"
                attribute sad:
                        "sprites/cygnus/cygnus sad/head sad.webp"

        group leotard:
                attribute jacket default:
                        "sprites/cygnus/cygnus sad/leotard.webp"

        group pants:
                attribute pants default:
                        "sprites/cygnus/cygnus sad/pants.webp"

        group jacket:
                attribute jacket default:
                        "sprites/cygnus/cygnus sad/jacket.webp"

        group tail:
                attribute tail default:
                        "sprites/cygnus/cygnus sad/tail under jacket.webp"
                attribute tail default:
                        "sprites/cygnus/cygnus sad/tail no clothes.webp"

image blankiedthefuckup:
        zoom 0.3
        "sprites/cygnus/cygnus sad/blankied the fuck up.webp"
        

layeredimage k:
        zoom 0.30
        always:
                "sprites/kosta/base.webp"

        group tails:
                attribute tail_sad:
                        "sprites/kosta/tail sad.webp"
                attribute tail default:
                        "sprites/kosta/tail normal.webp"

        group body:
                attribute arms_resting default:
                        "sprites/kosta/arms normal.webp"
                attribute arms_crossed:
                        "sprites/kosta/arms crossed.webp"

        group face auto:
                attribute neutral default:
                        "sprites/kosta/head normal.webp"
                attribute funeral:
                        "sprites/kosta/head funeral.webp"
                attribute laugh:
                        "sprites/kosta/head laugh.webp"
                attribute smug:
                        "sprites/kosta/head smug.webp"
                attribute speaking:
                        "sprites/kosta/head speaking.webp"
                attribute concern:
                        "sprites/kosta/head concern.webp"
                attribute sad:
                        "sprites/kosta/head sad.webp"

        group shirt:
                attribute shirt_normal default:
                        "sprites/kosta/shirt arms normal.webp"
                attribute shirt_crossed:
                        "sprites/kosta/shirt arms crossed.webp"

        group pants:
                attribute pants_normal default:
                        "sprites/kosta/pants arms normal.webp"
                attribute pants_crossed:
                        "sprites/kosta/pants arms crossed.webp"

layeredimage e:
        zoom 0.30
        always:
                "sprites/erin/base.webp"

        group pants:
                attribute pants default:
                        "sprites/erin/pants .webp"
                attribute pants_shy:
                        "sprites/erin/pants arms shy.webp"

        group arms auto:
                attribute arms_crossed default:
                        "sprites/erin/arms crossed.webp"
                attribute arms_heart:
                        "sprites/erin/arms heart.webp"
                attribute arms_shy:
                        "sprites/erin/arms shy.webp"

        group face:
                attribute neutral default:
                        "sprites/erin/head neutral.webp"
                attribute funeral:
                        "sprites/erin/head funeral.webp"
                attribute laugh:
                        "sprites/erin/head laugh.webp"
                attribute smug:
                        "sprites/erin/head smug.webp"
                attribute speaking:
                        "sprites/erin/head speaking.webp"
                attribute concern:
                        "sprites/erin/head concern.webp"
                attribute happy:
                        "sprites/erin/head happy.webp"
                attribute annoyed:
                        "sprites/erin/head annoyed.webp"
                attribute pensive:
                        "sprites/erin/head pensive.webp"
                attribute sad:
                        "sprites/erin/head sad.webp"
                attribute surprise:
                        "sprites/erin/head surprise.webp"

        group shirt:
                attribute shirt_crossed default:
                        "sprites/erin/blouse arms crossed.webp"
                attribute shirt_heart:
                        "sprites/erin/blouse arms heart.webp"
                attribute shirt_shy:
                        "sprites/erin/blouse arms shy.webp"

        group pendant:
                attribute pendant:
                        "sprites/erin/pendant.webp"
                attribute pendant_heart:
                        "sprites/erin/pedant arms heart.webp"


image apartmentD:
        "bgs/ErinBedroomDrawer_Day.webp"

image apartmentNL:
        "bgs/ErinBedroomDrawerPhoneLit_Night.webp"

image apartmentN:
        "bgs/ErinBedroomDrawerPhoneUnlit_Night.webp"

image cityAtNight:
        "bgs/cityAtNight.webp"

image notification:
        "phone/Notification.png"
        yalign 0.518
        xoffset 2
        zoom 1.004

image cygrinkiss1:
        zoom 0.67
        "cgs/cg cygnus erin silhouette kiss 1.webp"

image cygrinkiss2:
        zoom 0.67
        "cgs/cg cygnus erin silhouette kiss 2.webp"

image cygrinkiss3:
        zoom 0.67
        "cgs/cg cygnus erin silhouette kiss 3.webp"

image boss:
        zoom 0.30
        "sprites/extras/erin coworker.webp"

image faggylizzard:
        zoom 0.3
        "sprites/extras/faggy lizard.webp"

image security:
        zoom 0.3
        "sprites/extras/security bear.webp"

image cgerinsex:
        zoom 0.67
        "cgs/cg cygnus erin sex.webp"

image cygnusRoom:
        "bgs/cygnusBedroom.webp"

image car:
        "bgs/carAtNight.webp"

image ErinApartment_Night:
        "bgs/ErinApartment_Night.webp"

image erinBedroom:
        "bgs/ErinBedroomSex_Twilight.webp"

transform flip:
        xzoom -1.0
        yalign 1.0

transform unflip:
        xzoom 1.0
        yalign 1.0

transform rightFlip:
        yalign 1.0
        xalign 1.0
        xzoom -1.0

transform leftFlip:
        yalign 1.0
        xalign 0.0
        xzoom -1.0

transform middleFlip:
        yalign 1.0
        xalign 0.5
        xzoom -1.0

transform pos1:
        yalign 1.0
        xalign 0.1

transform pos2:
        yalign 1.0
        xalign 0.2

transform pos3:
        yalign 1.0
        xalign 0.3

transform pos4:
        yalign 1.0
        xalign 0.4

transform pos6:
        yalign 1.0
        xalign 0.6

transform pos7:
        yalign 1.0
        xalign 0.7

transform pos8:
        yalign 1.0
        xalign 0.8

transform pos9:
        yalign 1.0
        xalign 0.9

transform easein(duration, startPos, endPos):
        xalign startPos
        yalign 1.0
        ease duration xalign endPos

transform jump:
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0

transform infiniteJump(duration):
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0
    pause duration
    repeat

transform ijsberen:
        xalign 0.0
        yalign 1.0
        ease 3.0 xalign 1.0
        xzoom -1.0
        ease 3.0 xalign 0.0
        xzoom 1.0
        repeat

transform spriteShake:
    linear 0.05 xoffset -5 #move left 20 pixel in 0.2 seconds
    linear 0.05 xoffset +5 #move right 20 pixel in 0.2 seconds
    repeat 5 #repeat the above 5 times