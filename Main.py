#############################################
# Name: Your name
# Class: ICS3C
# Date: Friday Sept 18
# Project Name: MadLibs
#
# Project Description
# You will read in multiple entries from the user and store the results in variables
# You will then insert those variables into the following story to create a MadLib style result

# A recent survey informs us that one out of every five PLURALNOUN1 owns a/an ADJECTIVE1 phone.
# Fortunately, VERB_ENDING_IN_ING1 over a mobile NOUN1 in recent years has improved ADVERB1.
# Today, BODYPART1-held PLURALNOUN2 are all the rage.
# In restaurants, you find many PLURALNOUN3 talking ADVERB2 into their ADJECTIVE2 phones as they eat their NOUN2.
# NUMBER1 percent of American PLURALNOUN4 place their NOUN3 calls from their cars as they are VERB_ENDING_IN_ING2 to and from their home, office, or NOUN4.
# Walking and talking are now the "in" NOUN5 to do.
# Over NUMBER2 percent of Americans walk our ADJECTIVE3 streets with a handheld PLURALNOUN5 pressed against their BODYPART2.

# Ask for the capitalized words in the input. Print out the full story in the output.
# See https://www.thewordfinder.com/wordlibs/story/41/ for an example.
#############################################

# THIS IS WHERE YOU CODE
print("Welcome to my MadLib!")
print("Enter a plural noun: ")
plu1=input()
print("Enter an adjective: ")
adj1=input()
print("Enter a verb ending in ing: ")
verb1=input()
print("Enter a noun: ")
noun1=input()
print("You're doing great, keep going! Now enter an adverb: ")
adv1=input()
print("Enter a body part: ")
bodyp1=input()
print("Hurry up and give me another plural noun: ")
plu2=input()
print("Enter another plural noun: ")
plu3=input()
print("Time for a second adverb now: ")
adv2=input()
print("Now enter another adjective: ")
adj2=input()
print("Enter a noun: ")
noun2=input()
print("Good job! Now enter a number: ")
num1=input()
print("Now give me another plural noun: ")
plu4=input()
print("Enter a noun: ")
noun3=input()
print("Great! Now enter a verb ending in ing: ")
verb2=input()
print("Give me a noun: ")
noun4=input()
print("Now enter another noun: ")
noun5=input()
print("You're almost there! Now give me a number: ")
num2=input()
print("Enter an adjective: ")
adj3=input()
print("Enter a plural noun: ")
plu5=input()
print("This is the last one I promise! Enter a body part: ")
bodyp2=input()

print("A recent survey informs us that one out of every five",plu1,"owns a",adj1,"phone.")
print("Fortunately",verb1,"over a mobile",noun1,"in recent years has improved",adv1,".")
print("Today,",bodyp1,"-held",plu2,"are all the rage.")
print("In restaurants, you find many",plu3,"talking",adv2,"into their",adj2,"phones as they eat their",noun2,".")
print(num1,"percent of American",plu4,"place their",noun3,"calls from their cars as they are",verb2,"to and from their home, office, or",noun4,".")
print("Walking and talking are now in",noun5,"to do.")
print("Over",num2,"percent of Americans walk our",adj3,"streets with a handheld",plu5,"pressed against their",bodyp2,".")
print("The End.")


