label start:
    jump hub

label hub:
    menu:
        "Train":
            jump training
        "Rest":
            jump rest

label training:
    "You train hard."
    jump hub

label rest:
    "You take a break."
    jump hub

label abandoned:
    "This path leads nowhere."