# This program creates a dict containing the US states as keys and their capitals as values. It then quiz the user
    # by displaying the name of a state and asking the user to enter the states capital. The program keeps a
    # count of the number of correct and incorrect responses.
import random

def main():

    state_and_capital_dict = get_state_and_capital()

    state_name_list = get_random_value_dict(state_and_capital_dict)

    take_test(state_name_list, state_and_capital_dict)

def get_state_and_capital():

    state_and_capital_dict = {
        "Alabama"	: "Montgomery",
        "Alaska" : "Juneau",
        "Arizona" : "Phoenix",
        "Arkansas" : "Little Rock",
        "California" : "Sacramento",
        "Colorado" : "Denver",
        "Connecticut" :	"Hartford",
        "Delaware" : "Dover",
        "Florida" : "Tallahassee",
        "Georgia" : "Atlanta",
        "Hawaii" : "Honolulu",
        "Idaho" : "Boise",
        "Illinois" : "Springfield",
        "Indiana" : "Indianapolis",
        "Iowa" : "Des Moines",
        "Kansas" :	"Topeka",
        "Kentucky" : "Frankfort",
        "Louisiana" : "Baton Rouge",
        "Maine" : "Augusta",
        "Maryland" : "Annapolis",
        "Massachusetts" : "Boston",
        "Michigan" : "Lansing",
        "Minnesota" : "Saint Paul",
        "Mississippi" :	"Jackson",
        "Missouri" : "Jefferson City",
        "Montana" :	"Helena",
        "Nebraska" : "Lincoln",
        "Nevada" : "Carson City",
        "New Hampshire" : "Concord",
        "New Jersey" : "Trenton",
        "New Mexico" : "Santa Fe",
        "New York" : "Albany",
        "North Carolina" : "Raleigh",
        "North Dakota" : "Bismarck",
        "Ohio" : "Columbus",
        "Oklahoma" : "Oklahoma City",
        "Oregon" : "Salem",
        "Pennsylvania" : "Harrisburg",
        "Rhode Island" : "Providence",
        "South Carolina" :	"Columbia",
        "South Dakota" : "Pierre",
        "Tennessee" : "Nashville",
        "Texas" : "Austin",
        "Utah" : "Salt Lake City",
        "Vermont" :	"Montpelier",
        "Virginia" : "Richmond",
        "Washington" : "Olympia",
        "West Virginia" : "Charleston",
        "Wisconsin" : "Madison",
        "Wyoming" :	"Cheyenne",
    }

    return state_and_capital_dict

def get_random_value_dict(state_and_capital_dict):

    print()
    print("This program is going to quiz you its going to give u the name of a state"
          "\nand its your job to figure out the capital: ")

    state_name_list = []

    for each_name in state_and_capital_dict.keys():
        state_name_list.append(each_name)

    return state_name_list

def take_test(state_name_list, state_and_capital_dict):

    wrong_count = 0
    right_count = 0

    another = "Y"

    while another.upper() == "Y":

        state_random_choice = random.choice(state_name_list)

        print(f"\nWhat is the capital of {state_random_choice}?")

        user_input = input("Enter your answer: ")

        if user_input in state_and_capital_dict.values():
            print("That is the correct answer")
            right_count += 1
        else:
            print("That is incorrect")
            wrong_count += 1

        print("Enter R to get your results:")
        another = input("Would you like to do another question? (Y to keep going anything else to stop) ")

        if another.upper() == "R":

            print(f"The amount that you got wrong is {wrong_count}")
            print(f"The amount that you got right is {right_count}")

main()