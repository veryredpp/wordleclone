import requests
import time
print("Welcome to the ghetto Wordle!")
url = "https://thatwordleapi.azurewebsites.net/get/"
alphabet = []
for i in range(97,123):
    alphabet.append(chr(i))
    
def checkLetters(guess):
    for letter in guess:
        if letter not in alphabet:
            return False
    return True

def main():
    response = requests.get(url)
    response = response.json()
    while response['Status'] != 200:
        response = requests.get(url)
        response = response.json()
        print("API Status:", response['Status'])
        print("Trying again...")
    print("API Status: OK\n")
    
    word = response['Response']
    print(word)
    print(len(word)*"_")
    
    guess = ""
    count = 0
    while (guess != word) and (count != 6):
        goodword = False
        print("\n")
        while goodword is False:
            guess = input('\033[1A' + "" + '\033[K').lower()
        
            if len(guess) != 5:
                print('\033[1A' + "Word length out of range." + '\033[K')
                time.sleep(1)
                print('\033[1A' + "" + '\033[K')
                goodword = False
            else:
                goodword = True
                
        
            if checkLetters(guess) is False:
                print('\033[1A' + "Invalid characters used." + '\033[K')
                time.sleep(1)
                print('\033[1A' + "" + '\033[K')
                goodword = False
            elif goodword == True:
                pass
            
        print('\033[1A' + "" + '\033[K')
        word_list = list(guess)
        print(word_list)
        
        count += 1
    for i in range(8):
        print(f"\033[4{i}m{i}\033[m")
    
if __name__ == "__main__":
    main()