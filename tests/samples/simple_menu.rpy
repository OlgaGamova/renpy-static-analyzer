label start:
    "Hello"
    menu:
        "Go left":
            jump left
        "Go right":
            jump right

label left:
    "You went left"
    jump end

label right:
    "You went right"
    jump end

label end:
    "The End"