label start:
    jump chapter1

label chapter1:
    menu:
        "Path A":
            jump chapter2a
        "Path B":
            jump chapter2b

label chapter2a:
    jump chapter3

label chapter2b:
    jump chapter3

label chapter3:
    menu:
        "Secret path":
            jump secret
        "Normal ending":
            jump end

label secret:
    jump secret

label end:
    "Standard ending."

label hidden_end:
    "This ending is never used."
