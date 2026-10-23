# The script of the game goes in this file.

# The game starts here.

label start:
show ev neutral 1
ev "Hello my dear student, welcome to Frescto Academy! Where you'll be living your new life for the rest of the school year"
ev "I’m Ms. Everleif, your principal. I’ll be guiding you up until the beginning of your journey."
ev "Here at Frescto Academy, most students have been settled in for some time now, but fear not, everyone you’ll be meeting and dealing with on a daily basis will be as new to this place as you!"
ev "Now, a little bit of a reminder of your situation.."
ev "You, and the rest of your “Class“ / “Building“  just transferred over from another school due to an incident."
ev "All students from your old school were transferred to other schools, such as this one, not fully at random but partially at random."
ev "Meaning, not all students came from the same class in your old school, so not everyone knows each other, don’t worry, you won’t be the only new face to your classmates."
ev "Lets shift the focus to you. What would you like to be called?"
python:
    povname = renpy.input("Insert Name", length=32)
    povname = povname.strip()
    
    if not povname:
        povname = Y/N
ev "That's a lovely name, [povname]."
ev "Now, it's time for you to actually start your journey."
ev "I wish you the best of luck."
hide ev neutral 1 with dissolve
"I stare out the window out into the passing wilderness with my headphones on, the whole world around me feels to be nonexistent.. Then, I suddenly hear the bus halt to another stop."
"This time, being more aware than the last, I stumble around for my overstuffed backpack wondering if I had finally arrived."
"The bus’ door seems to start closing, in a panic I realize I need to get out those doors."
"I quickly jumped out of my seat and in a rush I grabbed my suitcase while making my way to the door."
"Luckily the bus driver noticed me in time for me to manage getting off the bus at the right spot."
"I thank the bus driver and turn around to take a look at my new school."
pov "Wow.."
"Is all I ended up muttering before I notice there's another student next to me."
menu:
    "Greet him":
        jump greet_zach
    "Ignore him":
        jump new_school

label greet_zach:
    "I stare at the kid for a second and get ready to say hello."
    pov "..Uhm, Hello! Are you new to this school as well?"
    "He doesn't respond to my hello, maybe he didn't hear me."
    pov "..."
    "I tap him on the shoulder"
    "This time he gives me an annoyed grunt."
    zachq "What do you want."
menu: 
    "Dismiss his anger":
        pov "Oh, I was just asking if you were new to this school"
        zachq "That's none your business. You planning somethin' or what? If you're looking for a fight, go ahead, I'm right here."
        pov "Sorry, I was just wondering because I'm new. It would just be nice to have help."
        zachq "I don't know the school, can't help ya'"
        pov "So you are new! Doesn't that mean we'll be in the same class?"
        zachq "What?? I don't know."
        pov "I think thats what I remember. Well, its nice to meet you, I'm [povname]."
        
    "Leave him be":
        "Sorry, I'll be on my way.."
        jump new_school

label new_school:
    "I look up at the campus and focus on how gorgeous it looks from down here."
return 