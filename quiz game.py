n = 30
d = {
    1: [1, "Who is the founder of Tesla?", "elon musk", "jeff bezos", "bill gates"],
    2: [1, "Tesla is a ____ company.", "car", "phone", "soap"],
    3: [2, "Who is the CEO of Amazon?", "sundar pichai", "jeff bezos", "tim cook"],
    4: [3, "What is the capital of France?", "Berlin", "Madrid", "Paris"],
    5: [1, "Which planet is known as the Red Planet?", "Mars", "Venus", "Jupiter"],
    6: [3, "Which element has the chemical symbol 'O'?", "Gold", "Hydrogen", "Oxygen"],
    7: [1, "Which is the largest mammal?", "Blue Whale", "Elephant", "Giraffe"],
    8: [2, "Which is the longest river in the world?", "Amazon", "Nile", "Yangtze"],
    9: [1, "Which is the smallest prime number?", "2", "3", "1"],
    10: [3, "What is the boiling point of water in Celsius?", "50°C", "90°C", "100°C"],
    11: [2, "Who painted the Mona Lisa?", "Van Gogh", "Leonardo da Vinci", "Picasso"],
    12: [1, "What is the square root of 64?", "8", "6", "10"],
    13: [3, "What is the largest continent?", "Europe", "Africa", "Asia"],
    14: [1, "Which organ is responsible for pumping blood in the body?", "Heart", "Lungs", "Kidney"],
    15: [2, "Who wrote 'Romeo and Juliet'?", "Mark Twain", "William Shakespeare", "Jane Austen"],
    16: [3, "What is the capital of Japan?", "Seoul", "Bangkok", "Tokyo"],
    17: [1, "How many colors are there in a rainbow?", "7", "5", "9"],
    18: [2, "Who discovered gravity?", "Albert Einstein", "Isaac Newton", "Galileo"],
    19: [3, "Which is the tallest mountain in the world?", "K2", "Kangchenjunga", "Mount Everest"],
    20: [1, "Which is the national animal of India?", "Tiger", "Elephant", "Peacock"],
    21: [2, "What is the chemical formula of water?", "H2", "H2O", "O2"],
    22: [1, "Which country is known as the Land of the Rising Sun?", "Japan", "China", "Thailand"],
    23: [3, "Which gas is most abundant in the Earth's atmosphere?", "Carbon Dioxide", "Oxygen", "Nitrogen"],
    24: [1, "How many days are there in a leap year?", "366", "365", "364"],
    25: [2, "What is the fastest land animal?", "Cheetah", "Lion", "Tiger"],
    26: [3, "Which is the largest ocean on Earth?", "Indian Ocean", "Atlantic Ocean", "Pacific Ocean"],
    27: [1, "What is the freezing point of water in Celsius?", "0°C", "32°C", "100°C"],
    28: [2, "Who is known as the Father of Computers?", "Thomas Edison", "Charles Babbage", "Alexander Graham Bell"],
    29: [1, "What is the value of pi (approx)?", "3.14", "2.17", "4.28"],
    30: [3, "What is the main component of the sun?", "Iron", "Oxygen", "Hydrogen"]
}

cor = []
wrg = []
point = 0
for i in range(1,n+1):
    print(f'\nQ{i} : {d[i][1]}')
    for j in range(2,len(d[i])):
        print(f'{j-1}) {d[i][j]}')
        
    while True:
        try:
            user_input = input("Enter your choice [1, 2, 3] or type 'exit' to quit: ")
            if user_input.lower() == "exit":
                print("\nExiting the quiz. Thank you for playing!")
                break
            x = int(user_input)
            if 1 <= x <= len(d[i]) - 2:
                if d[i][0] == x:
                    point += 1
                    cor.append(i)
                else:
                    wrg.append((i, x))
                break
            else:
                print("Invalid choice. Please select a number from the given options.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3 or type 'exit' to quit.")
            
print("\nAnswers:")
for i in range(1,n+1):
    correct_answer = d[i][d[i][0] + 1]
    if i in cor:
        print(f'{i}) {d[i][1]}. {correct_answer} ✅')
    else:
        user_choice_index = next(x[1] for x in wrg if x[0] == i) - 1
        user_answer = d[i][user_choice_index + 1]
        print(f'{i}) {d[i][1]}. {user_answer} ❌ . {correct_answer} ✅')

print(f'\nYour Total Points : {point}/{n}')