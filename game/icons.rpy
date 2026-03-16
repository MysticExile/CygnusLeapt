init python:
    import pygame

    # Load icons
    with renpy.loader.load("frame0.png", directory="images") as f:
        icon1 = renpy.display.scale.image_load_unscaled(f, "frame0.png")
    with renpy.loader.load("frame1.png", directory="images") as f:
        icon2 = renpy.display.scale.image_load_unscaled(f, "frame1.png")
    with renpy.loader.load("frame2.png", directory="images") as f:
        icon3 = renpy.display.scale.image_load_unscaled(f, "frame2.png")
    with renpy.loader.load("frame3.png", directory="images") as f:
        icon4 = renpy.display.scale.image_load_unscaled(f, "frame3.png")

    icons = [icon1, icon2, icon3, icon4]
    current_icon_index = 0

    def cycle_icon():
        global current_icon_index
        try:
            pygame.display.set_icon(icons[current_icon_index])
        except Exception as e:
            renpy.log("Icon change failed: " + str(e))
        current_icon_index = (current_icon_index + 1) % len(icons)

# Screen that runs the icon changing
screen icon_cycler():
    timer 0.33 action Function(cycle_icon) repeat True