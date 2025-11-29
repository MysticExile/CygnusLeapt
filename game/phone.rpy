screen phone(text):
        imagebutton idle "images/phone/background.webp"
        #imagebutton idle "images/phone/Phone.webp"
        frame at openMessage:
                xsize 402
                ysize 702
                background Solid('#fff')
                align (0.501,0.518)
                vbox:
                        spacing 3
                        text "[text]" color "#000"
                        align (0.0,1.0)

transform openMessage:
        yalign 1.0
        alpha 0.0
        ease 0.25 yalign 0.518 alpha 1.0