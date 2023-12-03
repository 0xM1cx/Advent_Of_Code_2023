import re

allowed_Games = []

def checkGameSet(sets):
    MAX_COLOR = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    # Getting each set
    for set in sets:
        pattern = re.compile(r'(\d+) (red|green|blue)')
        matches = pattern.findall(set)
        
        for digit in matches:
            if int(digit[0]) > MAX_COLOR[digit[1]]:
                return False

    return True



def separateBySemiColon(line):
    splited_Line = line.split(";")

    # Get the 1st index so that the Game_ID will be removed
    index_Zero = splited_Line.pop(0)

    # Get the "Game <ID>"
    pattern = re.compile(r'Game \d+:', re.IGNORECASE)
    Game_ID = pattern.findall(index_Zero)

    # Remove the pattern
    removedGameID = re.sub(pattern, '', index_Zero)
    splited_Line.insert(0, removedGameID.strip()) 

    splited_Line = [x.strip() for x in splited_Line]

    Game_Verdict = checkGameSet(splited_Line)
    
    if Game_Verdict == True:
        allowed_Games.append((Game_ID))

def main():
    sum = 0 
    Games  = []
    with open("day2Input", "r") as f:
        for line in f:
            Games.append(line.strip()) 
        
    for i in range(0, len(Games)):
        separateBySemiColon(Games[i])
    pattern = re.compile(r'\d+') 
    for games in allowed_Games:
        pattern = re.compile(r'(\d+)', re.IGNORECASE)
        matches = pattern.findall(games[0])
        sum += int(matches[0])


    print(sum)
main()

