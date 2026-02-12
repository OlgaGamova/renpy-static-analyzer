label start:
    "You wake up in a forest."
    menu:
        "Explore the cave":
            jump cave
        "Walk to the village":
            jump village

label cave:
    "The cave is dark."
    menu:
        "Go deeper":
            jump monster
        "Run away":
            jump start

label monster:
    "A monster appears!"
    jump end_bad

label village:
    "The village seems quiet."
    menu:
        "Enter the tavern":
            jump tavern
        "Leave":
            jump end_neutral

label tavern:
    "You meet a stranger."
    jump end_good

label end_good:
    "You found allies. Good ending."

label end_bad:
    "The monster defeated you."

label end_neutral:
    "You leave the forest safely."

label secret_area:
    "This area is never reached."

label broken_path:
    jump nowhere
