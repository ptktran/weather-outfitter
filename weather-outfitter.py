import random   #random function needed in order for the program to suggest random outfits
#This program is designed to give the user some inspiration for what to wear depending on the given temperature outside.
#The program will not be able to suggest items that the user owns, but rather it will give the user an idea of what kind of outfit is suitable according to the temperature provided by the user.
#There will be a user menu for the user to choose if they want more suggestions or exit the program.
#The program is designed for my personal preferences, so my "cold" might be different from everyone else's.
#Because I am a male, the program will only give suggestions of outfits for men.

#LISTS OF CLOTHING:
shirts = ["Basic T-Shirt", "Button Down Shirt", "Graphic Tee", "Polo Shirt", "Short Sleeved Button Down Shirt", "Oversized T-Shirt"]    #summer items are exclusive to summer, so no temperature required
shorts = ["Sport Shorts", "Sweatshorts", "Cotton Shorts", "Chino Shorts", "Nylon Shorts"]                                                                 
pants = ["Slim Jeans", "Relaxed Jeans", "Chino Pants", "Joggers", "Cropped Trousers", "Cargo Pants"]    #pants are suitable all year round so no temperatures required
sweaters = [["Hoodie", [16, 12, 5, -5]], ["Sweater", [16, 12]], ["Long-Sleeve Tee", [16]], ["Rugby Shirt", [16]], ["Turtleneck", [13, 5, -5]], ["Wool Sweater", [13, 5, -5]], ["Half-Zip Sweater", [13, 5, -5]], ["Cashmere Sweater", [13, 5, -5]]]    #fall/winter sweaters
outerwear = [["Denim Jacket", [12]], ["Overshirt", [12]], ["Windbreaker", [12]], ["Bomber Jacket", [12]], ["Cardigan", [12]], ["Peacoat", [5]], ["Trench Coat", [5]], ["Corduroy Jacket", [12]], ["Fleece Jacket", [12]], ["Hooded Puffer Jacket", [5, -5]], ["Hooded Parka", [-5]]]    #fall/winter outerwear
#numbers in the nested lists indicate appropriate temperatures for certain clothing pieces
#temperatures in the lists are picked randomly, as long as they are within the temperature ranges defined in the function suggestion

def intro():
    global name
    name = input("What would you like me to call you? ")  #asks user for name
    print(f"Hello {name}, I am your Fashion Assistant! I will be giving you some inspiration for what to wear.")    #introduction
    global temperature
    temperature = int(input("How's the weather looking like today? Please give me a specific temperature in Celsius, and I'll give some suggestions! "))

intro()

def suggestion(temperature):
    too_cold = temperature < -30        
    too_hot = temperature >= 40
    summer = 40 > temperature > 20
    #boolean
    #if the weather is too extreme, program suggests user to stay home
    if too_cold == True:           
        print("Please stay home and stay warm!")
    elif too_hot == True:
        print("Please stay home and stay cool!")
    elif summer == True:     #if summer weather then suggest summer outfits
        print(f"Looks like summer! Here's a random outfit: {random.choice(shirts)} and {random.choice(shorts)} ")     #suggests a random shirt and shorts when the weather is warm
        print(f"Wanna wear pants instead? Here's another outfit: {random.choice(shirts)} and {random.choice(pants)}")     #suggests an extra outfit with pants just in case the user prefer pants
    #empty lists where elements will be added from clothing lists later on, depending on conditions
    tops = []                            
    outers = []

    if 20 >= temperature > 14:           #temperature range from 14 to 20
        for x in sweaters:              #loops through the first list
            for y in x[1]:              #loops through the nested list
                if 20 > y > 14:         #search for the temperatures included in the lists 
                    tops.append(x[0])   #append items appriopriate for given temperature into the empty lists above
        print(f"It's quite nice outside. Here's a random outfit: {random.choice(tops)} and {random.choice(pants)}. {random.choice(shorts)} might work too!")  #picks and prints random items from the new lists, except for bottoms
                                        #FROM HERE AND ON: repeating the same process but for different temperature ranges
    if 14 >= temperature > 10:          #temperature range from 10 to 14
        for x in sweaters:
            for y in x[1]:
                if 14 >= y > 10:
                    tops.append(x[0])
        for x in outerwear:
            for y in x[1]:
                if 14 >= y > 10:
                    outers.append(x[0])
        print(f"It's cold outside. Here's a random outfit: {random.choice(outers)}, {random.choice(tops)}, {random.choice(pants)}")

    if 10 >= temperature > 0:           #temperature range from 0 to 10
        for x in sweaters:
            for y in x[1]:
                if 10 > y > 0:
                    tops.append(x[0])
        for x in outerwear:
            for y in x[1]:
                if 10 > y > 0:
                    outers.append(x[0])
        print(f"It's cold outside. Here's a random outfit: {random.choice(outers)}, {random.choice(tops)}, {random.choice(pants)}, and thermals if you want")

    if temperature <= 0:                 #temperatures less than 0
        for x in sweaters:
            for y in x[1]:
                if y < 0:
                    tops.append(x[0])
        for x in outerwear:
            for y in x[1]:
                if y < 0:
                    outers.append(x[0])
        print(f"It's freezing outside. Here's a random outfit: {random.choice(outers)}, {random.choice(tops)}, {random.choice(pants)}, Thermals, and Boots")



choice = input("Type: \n 's' to get suggestions \n 'e' to exit \n Your choice: ")   #user menu 
while choice != 'e':    #this while loop forces the user to input a choice
    if choice == 's':   #when choice is s, the program's main function will run
        suggestion(temperature) 
        break
    else:
        choice = input("\n What else are you looking for? Type: \n 's' to search for another outfit \n 'e' to exit \n Your choice: ")   #program will continue to ask the user until they input e
    

