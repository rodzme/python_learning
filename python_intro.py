if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')

volume = 39

#Change the volume if it's too loud or too quiet
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")

if volume < 20:
    print("It's kinda quiet")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

def hi(name):
    print('Hey ' + name + '!')

names = ['Rodrigo', 'Mel', 'Isabela']

for name in names:
    hi(name)
    print('Next person!')

for i in range(1, 6):
    print(i)