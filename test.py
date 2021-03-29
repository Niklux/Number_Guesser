import random

print("Which Mode do you want to play?\n")

while True:
    while True:
        try:
            mode = int(input("1 for 1-10; 2 for 1-20; 3 for 1-30\n"))
            break
        except ValueError:
            pass
    if mode != 0 and mode < 4:
        break

if mode == 1:
    game_size = 11
    field = "1-10"
elif mode == 2:
    game_size = 21
    field = "1-20"
else:
    game_size = 31
    field = "1-30"

rdm_number = random.randrange(1,game_size)
print(f"\n\nMode is now {mode}\n")

tries = 0
while tries < 3:
    while True:
        while True:
            try:
                guess = int(input(f"\nInsert integer between {field}\n"))
                break
            except ValueError:
                pass
        if guess != 0 and guess < game_size:
            break

    if guess == rdm_number:
        print(f"\n\nYou WON the number was {guess}. You required {tries +1} tries!")
        break
    else:
        tries+=1
        if guess > rdm_number:
            if tries == 3:
                print(f"\n\nNo tries left! You LOST.\nThe random number was {rdm_number}\n\n")
                break
            else:
                print(f"Your inserted number: {guess} is too high!\n")
        else:
            if tries == 3:
                print(f"\n\nNo tries left! You LOST.\nThe random number was {rdm_number}\n\n")
                break
            else:
                print(f"Your inserted number: {guess} is too low!\n")