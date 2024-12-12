import random
cp = up = 0
d = {"R":"🪨", "P":"📃", "S":"✂"}
winning_score = int(input("Enter the winning score: "))
while cp < winning_score and up < winning_score:
    
    c = random.randint(1,3)
    u = input("Enter Your Choice [R, S, P]: ").strip().upper()
    if u not in d:
        print("Invalid choice. Please enter R, P, or S.")
        continue
    
    if c == 1: c = "R"
    if c == 2: c = "S"
    if c == 3: c = "P"
    
    if (c == "R" and u == "S")or (c == "P" and u == "R") or (c == "S" and u == "P"):
        cp += 1
        print(f'User : {d[u]} and Computer : {d[c]}. Computer Wins This Round')
    elif (u == "R" and c == "S") or (u == "P" and c == "R") or (u == "S" and c == "P"):
        up += 1
        print(f'User : {d[u]} and Computer : {d[c]}. User Wins This Round')
    else:
        print(f'User: {d[u]} and Computer: {d[c]}. It\'s a Tie!')
        
    print(f'Score -> User : {up} and Computer : {cp}')
    
if cp == 5:
    print('Computer Wins the Game! Better luck next time.')
else:
    print('User Wins the Game! Congratulations!')