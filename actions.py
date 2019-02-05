# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Fahad"
my_age = 23
my_bio = "I am Software engineering "
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)
    print("---------------------------")
    options()

def options():
    # your code goes here!
    print("Would you like to:")
    print("1) Create a new club.")
    print("or:")
    print("2) Browse and join clubs.")
    print("or:")
    print("3) View existing clubs.")
    print("or:")
    print("4) Display members of a club.")
    print("or:")
    print("-1) Close application.")
    chose = input("> ")

    if chose == "1":
    	create_club()
    elif chose == "2":
    	join_clubs()
    elif chose == "3":
    	view_clubs()
    elif chose == "4":
    	view_club_members()
    elif chose == "-1":
    	return True
    else:
    	print("Your input is Wrong Please try again:")
    	options()
    
    

def create_club():
    # your code goes here!
    name_of_club = input("Pick a name for your awesome new club:")
    print("What is your club about? ")
    desc_of_club = input("")
    new_club = Club(name_of_club,desc_of_club)
    print ("Enter the numbers of the people ypu Would like to recruit to your new club (-1 to stop):")
    print ("-----------------------------------------------------------")
    for item in population:
    	print ("[%s] %s" % (population.index(item)+1, item.name))
    member = input("> ")
    while member != "-1":
    	if population[int(member)-1] in population:
    		new_club.recruit_member(population[int(member)-1])
    		member = input("> ")
    print ("Here's your club:")
    print (new_club.name)
    print (new_club.description)
    print ("Members:")
    total_age = 0 
    for member in new_club.members:
    	print ("- %s (%s years old) - %s" % (member.name , member.age , member.bio))
    	print ("")
    	total_age += member.age
    Avreg = float(total_age) / len(new_club.members)
    print ("Average age in this club: %.2fyr" % Avreg)
    clubs.append(new_club)
    print ("Ok %s Club is Successfully Created" % new_club.name)
    options()

def view_clubs():
    # your code goes here!
    for club in clubs:
    	print ("NAME: %s" % club.name)
    	print ("DESCRIPTION: %s" % club.description)
    	print ("MEMBERS: %s" % len(club.members))
    	print ("")


def view_club_members():
    # your code goes here!
    view_clubs()
    print ("")
    name_the_club_see_members = input ("Enter the name of the club whose members you'd like to see: ")
    obj_club = None
    for club in clubs:
    	if (club.name == name_the_club_see_members):
    		obj_club = club
    		for member in obj_club.members:
    			print ("- %s (%s years old) - %s" % (member.name , member.age , member.bio))
    			print ("")
    options()

def join_clubs():
    # your code goes here!
    view_clubs()
    print ("")
    name_the_club_join = input ("Enter the name of the club you'd like to join: ")
    obj_club = None
    for club in clubs:
    	if (club.name == name_the_club_join):
    		obj_club = club
    		obj_club.recruit_member(myself)
    		break
    print ("%s just joined %s" % (myself.name , obj_club.name))
    options()

def application():
    introduction()
    # your code goes here!
    
