import requests
import time
import datetime
print("Welcome to the ghetto Wordle!")

date = datetime.date.today()
url = f"https://www.nytimes.com/svc/wordle/v2/{date:%Y-%m-%d}.json"
alphabet = []
for i in range(97,123):
    alphabet.append(chr(i))
    
def check_letters(guess):
    for letter in guess:
        if letter not in alphabet:
            return False
    return True

def main():
    response = requests.get(url)
    response_content = response.json()
    while response.status_code != 200:
        response = requests.get(url)
        response_content = response.json()
        print("API Status:", response['Status'])
        print("Trying again...")
    print("API Status: OK\n")

    word = response_content['solution']
    print(len(word) * "_")

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

            if check_letters(guess) is False:
                print('\033[1A' + "Invalid characters used." + '\033[K')
                time.sleep(1)
                print('\033[1A' + "" + '\033[K')
                goodword = False
            elif goodword == True:
                pass
        print('\033[1A' + "" + '\033[K')

        # Processing the guess and providing feedback
        from collections import Counter

        word_list = list(word)
        guess_list = list(guess)

        # Prepare counts of each letter in the word
        word_counts = Counter(word_list)
        output = [""] * len(guess_list)  # Initialize an output list of the same length as the word

        # First pass for green (correct positions)
        for index, (guessletter, wordletter) in enumerate(zip(guess_list, word_list)):
            if guessletter == wordletter:
                output[index] = "\033[42m" + guessletter + "\033[m"  # Green for correct position
                word_counts[guessletter] -= 1  # Reduce count as this letter is "consumed"
                guess_list[index] = None       # Mark as handled

        # Second pass for yellow (correct letters, wrong positions)
        for index, guessletter in enumerate(guess_list):
            if guessletter:
                if word_counts[guessletter] > 0:
                    output[index] = "\033[43m" + guessletter + "\033[m"  # Yellow for correct letter
                    word_counts[guessletter] -= 1  # Reduce count as this letter is "consumed"
                else:
                    output[index] = guessletter  # No match, print normally

        # Combine the output list into a single string
        print("".join(output))

        count += 1

    
if __name__ == "__main__":
    main()