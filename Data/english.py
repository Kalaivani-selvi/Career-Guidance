import pandas as pd
import random

# Define the questions, options, and correct answers
questions = [
    "What is the synonym for 'enormous'?",
    "Which of the following sentences is grammatically correct?",
    "What is the opposite of 'brave'?",
    "Which word is a noun?",
    "Identify the correctly spelled word:",
    "Which sentence uses correct punctuation?",
    "What is the past tense of 'eat'?",
    "Which sentence is grammatically incorrect?",
    "What is the meaning of the word 'conundrum'?",
    "Choose the correct form of the verb:",
    "Which sentence is in the passive voice?",
    "What is the synonym of 'intelligent'?",
    "Identify the sentence with the correct subject-verb agreement:",
    "Which word is a pronoun?",
    "What is the meaning of the word 'ubiquitous'?",
    "Choose the correctly spelled word:",
    "Which sentence is grammatically correct?",
    "What is the past participle of 'go'?",
    "Which word is an adverb?",
    "What is the antonym of 'victory'?",
    "Identify the sentence with the correct use of 'their,' 'there,' or 'they're':",
    "What is the meaning of the word 'eloquent'?",
    "Choose the correct form of the verb:",
    "Which sentence is in the past perfect tense?",
    "What is the antonym of 'joyful'?",
    "Identify the sentence with the correct use of 'its' or 'it's':",
    "What is the meaning of the word 'fascinate'?",
    "Choose the correctly spelled word:",
    "Which sentence is grammatically correct?",
    "What is the plural form of 'child'?",
    "Which word is a conjunction?",
    "What is the meaning of the word 'audacious'?",
    "Choose the correct form of the verb:",
    "Which sentence is in the future perfect tense?",
    "What is the antonym of 'friendly'?",
    "Identify the sentence with the correct use of punctuation:",
    "What is the plural form of 'cactus'?",
    "Which word is an adjective?",
    "What is the meaning of the word 'resilient'?",
    "Choose the correctly spelled word:",
    "Which sentence is grammatically correct?"
]

options = [
    ["Tiny", "Huge", "Small", "Little"],
    ["She runned to the store.", "She ran to the store.", "She have ran to the store.", "She running to the store."],
    ["Fearless", "Timid", "Courageous", "Bold"],
    ["Quickly", "Suddenly", "Happiness", "Quietly"],
    ["Accommadate", "Accommodate", "Acommodate", "Acomodate"],
    ["I went to the store and bought apples oranges and bananas.", 
     "I went to the store and bought apples, oranges, and bananas.", 
     "I went to the store, and bought apples oranges and bananas.", 
     "I went to the store and bought, apples oranges, and bananas."],
    ["Ate", "Eaten", "Eating", "Eats"],
    ["They is going to the party.", "He are swimming in the pool.", "She is cooking dinner.", "We am studying for the exam."],
    ["Solution", "Puzzle", "Problem", "Clue"],
    ["I have went to the store.", "I has gone to the store.", "I have gone to the store.", "I have go to the store."],
    ["The dog chased the cat.", "The cat was chased by the dog.", "The cat chased the dog.", "The dog was chased by the cat."],
    ["Stupid", "Clever", "Dull", "Ignorant"],
    ["The group of students is studying for the exam.", "The group of students are studying for the exam.", 
     "The group of students were studying for the exam.", "The group of students be studying for the exam."],
    ["Jump", "He", "Happy", "Dance"],
    ["Rare", "Scarce", "Abundant", "Uncommon"],
    ["Occasionnally", "Occassionally", "Occasionally", "Ocasionally"],
    ["She don't like pizza.", "She doesn't like pizza.", "She not like pizza.", "She isn't like pizza."],
    ["Gone", "Went", "Going", "Goes"],
    ["Happy", "Beautiful", "Slowly", "Intelligent"],
    ["Success", "Defeat", "Triumph", "Achievement"],
    ["Their going to the park.", "There going to the park.", "They're going to the park.", "They going to the park."],
    ["Quiet", "Talkative", "Fluent", "Inarticulate"],
    ["He have finished his homework.", "He has finish his homework.", "He has finished his homework.", "He have finishes his homework."],
    ["He eats breakfast every morning.", "He was eating breakfast when the phone rang.", 
     "He has eaten breakfast before he went to work.", "He will eat breakfast after he wakes up."],
    ["Happy", "Joyous", "Sorrowful", "Delighted"],
    ["Its a beautiful day.", "It's a beautiful day.", "Its raining outside.", "It's raining outside."],
    ["Bore", "Disinterest", "Entertain", "Dull"],
    ["Rhythym", "Rhythm", "Rhythem", "Rhytm"],
    ["She was went to the store.", "She went to the store.", "She gone to the store.", "She did went to the store."],
    ["Oxen", "Oxes", "Oxs", "Oxen's"],
    ["Fast", "Over", "Dance", "Sing"],
    ["Timid", "Brave", "Shy", "Cowardly"],
    ["They have write the report.", "They has written the report.", "They have written the report.", "They have writing the report."],
    ["I will have finished my work by tomorrow.", "I have finished my work yesterday.", 
     "I am finishing my work now.", "I was finishing my work when you called."],
    ["Kind", "Amicable", "Hostile", "Sociable"],
    ["What is your name?", "What is your name.", "What is your name!", "What is your name,"],
    ["Cactuss", "Cacti", "Cactuses", "Cactus'"],
    ["Happily", "Quickly", "Beautiful", "Dance"],
    ["Weak", "Fragile", "Flexible", "Brittle"],
    ["Disappear", "Dissapear", "Disapear", "Dissappear"],
    ["The cat catched the mouse.", "The cat caught the mouse.", "The cat catch the mouse.", "The cat catches the mouse."]
]

correct_answers = ["b", "b", "b", "c", "b", "b", "a", "a", "b", "c", "b", "b", "a", "b", "c", "c", "b", "a", "c", "b", 
                   "c", "c", "c", "a", "c", "b", "b", "d", "b", "a", "d", "c", "c", "a", "d", "c", "b", "b", "a", "d", 
                   "b", "c", "d", "a", "b", "a", "b", "d"]

# Generate synthetic dataset
data = {"Question": questions, "Option A": [], "Option B": [], "Option C": [], "Option D": [], "Correct Answer": []}

for options_list, correct_answer in zip(options, correct_answers):
    random.shuffle(options_list)  # Shuffle options for each question
    data["Option A"].append(options_list[0])
    data["Option B"].append(options_list[1])
    data["Option C"].append(options_list[2])
    data["Option D"].append(options_list[3])
    data["Correct Answer"].append(correct_answer)

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the synthetic dataset
print(df)

# Save to CSV file
df.to_csv("round1.csv", index=False)
