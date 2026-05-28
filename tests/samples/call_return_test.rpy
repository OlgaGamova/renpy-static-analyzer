# Simple test scenario for call/return support

label start:
    $score = 0
    "Welcome to the call/return test!"
    call subroutine
    "Back from subroutine, score is now increased"
    if score > 5:
        jump good_ending
    else:
        jump bad_ending

label subroutine:
    $score += 10
    "Inside subroutine - increased score by 10"
    return

label good_ending:
    "Good ending! Your score is high enough."
    return

label bad_ending:
    "Bad ending! Your score is too low."
    return
