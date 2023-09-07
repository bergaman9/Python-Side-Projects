
import random

# temel oyun yapısını oturttuktan sonra class yapısını kullanarak tekrar düzenleyeceğim.

list = ["Rock", "Paper", "Scissor"]

person1_score = 0
person2_score = 0

while person1_score <= 3 or person1_score <= 3:
    person1 = random.choice(list)
    person2 = random.choice(list)

    if person1 == person2:
        print("They are equal.")
    elif person1 == "Rock" and person2 == "Paper":
        person2_score += 1
        print(person1_score, person2_score)
    elif person1 == "Rock" and person2 == "Scissor":
        person1_score += 1
        print(person1_score, person2_score)
    else:
        print(person1_score, person2_score)

if person1_score == 3:
    print("Person 1 kazandı.")
elif person2_score == 3:
    print("Person 2 kazandı.")
elif person1_score == person2_score:
    print("Eşitler.")