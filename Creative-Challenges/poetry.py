import syllables
import random

# Finds words with particular number of syllables
def find_word(num_syllables):
    with open("Creative-Challenges\word_list.txt") as f:
        syllable = float('inf')
        r = f.readlines()
        word = random.choice(r)
        while syllable != num_syllables:
            word = random.choice(r)
            if word != 'yourself':
                word = word[:-1]
            syllable = syllables.estimate(word)
        return word

def make_line(num_syllables):
    with open("Creative-Challenges\word_list.txt") as f:
        syllable = float('inf')
        r = f.readlines()
        word = random.choice(r)
        while syllable > num_syllables:
            word = random.choice(r)
            if word != 'yourself':
                word = word[:-1]
            syllable = syllables.estimate(word)
    
    if num_syllables != syllable:
        word += " " + find_word(num_syllables-syllable)
    return word
        
    # returns line with given syllables

if __name__ == "__main__":
