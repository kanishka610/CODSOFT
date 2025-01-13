import random

def treas():
    print("Welcome to Chatbot's Treasure Hunt!")
    print("Chatto: Your goal is to find the hidden treasure by tackling riddles and more.")
    print("Chatto: Type 'exit' anytime to quit the game.\n")
    
    # Game setup
    current_location = "start"
    treasure_location = "hidden_temple"
    score = 0
    inventory = []

    # Riddles and answers
    riddles = {
        "forest": {
            "question": "What has hands but can't clap?",
            "answer": "clock"
        },
        "river": {
            "question": "I have many teeth but can't bite. What am I?",
            "answer": "comb"
        },
        "hidden_temple": {
            "question": "What gets wetter the more it dries?",
            "answer": "towel"
        },
        "cave": {
            "question": "The more of me you take, the more you leave behind. What am I?",
            "answer": "footsteps"
        },
    }

    # Locations with left/right movement
    locations = {
        "start": {
            "description": "You are at the starting point. Paths lead left to the forest and right to the river.",
            "options": {"left": "forest", "right": "river"}
        },
        "forest": {
            "description": "You are in a dark forest. A narrow path continues left, and you see a cave on the right.",
            "options": {"left": "hidden_temple", "right": "cave"}
        },
        "river": {
            "description": "You are by a river. The current is strong, and there's a rickety bridge to the left.",
            "options": {"left": "hidden_temple", "right": "forest"}
        },
        "hidden_temple": {
            "description": "You have reached the hidden temple. Solve the final riddle to claim the treasure!",
            "options": {}
        },
        "cave": {
            "description": "You are in a dark, damp cave. The air feels heavy. There's an exit to the left.",
            "options": {"left": "hidden_temple"}
        }
    }

    while True:
        # Exit condition
        if current_location == treasure_location:
            print("\nChatto: 🎉 You found the treasure! Final riddle:")
            riddle = riddles[current_location]
            answer = input(f"Chatto: {riddle['question']}\nYou: ").strip().lower()
            
            if answer == riddle['answer']:
                score += 50
                print(f"Chatto: Correct! You've completed the treasure hunt with a score of {score}. Congratulations!")
                print("Chatto: 🎉 Game over! Thanks for playing!")
                break
            else:
                print("Chatto: Incorrect. The treasure remains hidden. Try again later!")
                break

        # Display location description
        print(f"\nChatto: {locations[current_location]['description']}")

       
        if current_location in riddles:
            riddle = riddles[current_location]
            print(f"Chatto: Solve this riddle to proceed:")
            answer = input(f"Chatto: {riddle['question']}\nYou: ").strip().lower()
            
            if answer == riddle['answer']:
                print("Chatto: Correct! You may proceed.")
                score += 20
                if current_location == "forest":
                    print("Chatto: You found an ancient map! Adding it to your inventory.")
                    inventory.append("ancient map")
                elif current_location == "cave":
                    print("Chatto: You found a glowing gem! Adding it to your inventory.")
                    inventory.append("glowing gem")
            else:
                print("Chatto: Incorrect answer. You remain stuck here.")
                continue  

      
        options = locations[current_location]["options"]
        if not options:
            print("Chatto: There are no more paths. The game is over.")
            break

        print("Chatto: Where do you want to go?")
        for direction, location in options.items():
            print(f"- {direction.capitalize()}: {location.capitalize()}")
        
        # Get player input
        player_choice = input("You: ").strip().lower()

        # Exit game
        if player_choice == "exit":
            print("Chatto: Goodbye! Thanks for playing!")
            break

        # Validate player choice
        if player_choice in options:
            current_location = options[player_choice]
        else:
            print("Chatto: Invalid choice. Please try again.")

     
        print(f"Chatto: Your inventory: {inventory}")
        print(f"Chatto: Your score: {score}")



treas()
