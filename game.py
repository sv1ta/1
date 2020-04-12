from Hero import *

print('Information about your hero:')
myHero1 = Hero("Terrorist", 1, "Russian")

myHero1.show_hero()
myHero1.move()
myHero1.level_up()
print(" ")


print('Information about your enemy:')
myBadHero1 = BadHero("Counter-Terrorist", 1, "American")

myBadHero1.show_BadHero()
myBadHero1.move()
myBadHero1.level_up()
print(" ")
print('Time to Fight!')
if(myHero1.level > myBadHero1.level):
    print('Congratulations!Your hero Terrorist killed Counter-Terrorist and he`s won! :)')
elif(myHero1.level < myBadHero1.level):
    print('Sorry, your hero died and you lost, try again :(')
if(myHero1.level == myBadHero1.level):
    print('DRAW!Friendship won :)')