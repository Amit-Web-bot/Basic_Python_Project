#String concatination (aka how to put string together)
# few ways to do this 
youtuber = "Messy Ant"

# print("Subscribe to "+youtuber)
# print("Subscribe to {}".format(youtuber))
print(f"Subscribe to {youtuber}")
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hyderated and {verb2} Like you are {famous_person}"

print(madlib)
