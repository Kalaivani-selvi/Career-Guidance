import pandas as pd
import random

# Define the questions, options, and correct answers
questions = [
    "If a car travels 360 miles in 6 hours, what is its average speed in miles per hour?",
    "A box contains 12 blue pens, 8 red pens, and 5 green pens. If a pen is randomly selected from the box, what is the probability that it is either blue or red?",
    "If the ratio of the lengths of two rectangles is 3:5 and the perimeter of the smaller rectangle is 24 cm, what is the perimeter of the larger rectangle?",
    "If a number is increased by 20% and then decreased by 10%, what is the net percentage change?",
    "A train travels from City A to City B at an average speed of 60 km/h and returns to City A at an average speed of 75 km/h. What is the average speed for the entire round trip?",
    "If the area of a square is 64 square meters, what is the length of its diagonal?",
    "A father is three times as old as his son. Five years ago, the sum of their ages was 48. What is the father's current age?",
    "If x + 2y = 10 and x - y = 4, what is the value of x?",
    "A retailer bought 80 shirts at $12 each and sold them at $15 each. What is the percentage profit earned?",
    "If 3 workers can complete a task in 8 days, how many days will it take for 6 workers to complete the same task?",
    "If a bicycle wheel has a diameter of 70 centimeters, what is its circumference?",
    "In a class of 30 students, 18 play football, 12 play cricket, and 8 play both. How many students do not play either football or cricket?",
    "A boat travels downstream 20 miles in 2 hours. If the speed of the current is 5 mph, what is the speed of the boat in still water?",
    "If 3x−7=5, what is the value of x?",
    "A rectangle has a length twice its width. If the perimeter of the rectangle is 24 meters, what is its area?",
    "If 3/5 of a number is 36, what is 40% of that number?",
    "A shopkeeper sells a shirt for $45, which is 20% more than the cost price. What is the cost price of the shirt?",
    "If 4/7 of a number is 28, what is 5/7of that number?",
    "A train covers a distance of 480 km at a uniform speed. If the speed had been 10 km/h more, it would have taken 2 hours less for the same journey. What is the speed of the train?",
    "If 2^x+1=32, what is the value of x?",
    "What is the relationship between a niece and her uncle's sister?",
    "If John's father is Mike, what is the relationship between Mike and John?",
    "If Maria's husband is Peter's brother, what is Maria's relationship to Peter?",
    "If Jane's daughter is Sarah's niece, what is Jane's relationship to Sarah?",
    "If Alex's mother is Alice, what is the relationship between Alice and Alex?",
    "If David's wife is Mary, what is Mary's relationship to David's brother?",
    "If Tom's grandmother is Lucy, what is Lucy's relationship to Tom?",
    "If Sarah's father is Mark, what is the relationship between Mark and Sarah?",
    "If Laura's son is Jack's father, what is Laura's relationship to Jack?",
    "If Paul's wife is Lisa, what is Lisa's relationship to Paul's mother?",
    "What is the square root of 144?",
    "What is the square root of 225?",
    "Simplify:   the square root of  81",
    "What is the square root of 64?",
    "What is the square root of  100?",
    "What is the square root of 400?",
    "What is the square root of 169?",
    "What is the square root of 256?",
    "What is the square root of 36?",
    "What is the square root of 625?",
    "Find the cube root of 3375.",
    "Calculate the cube root of 5832.",
    "Determine the cube root of 9261.",
    "Find the cube root of 10648.",
    "Calculate the cube root of 13824.",
    "Determine the cube root of 19683.",
    "Find the cube root of 32768.",
    "Calculate the cube root of 46656.",
    "Determine the cube root of 64000.",
    "Find the cube root of 97336."
]

options = [
    ["40 mph","50 mph","60 mph","70 mph"],
    ["5/12","8/25","10/25","20/25"],
    ["35 cm","40 cm","45 cm","50 cm"],
    ["8%","10%","12%","14%"],
    ["65 km/h","67.5 km/h","70 km/h","72.5 km/h"],
    ["8 meters","10 meters","12 meters","16 meters"],
    ["35 years","40 years","45 years","50 years"],
    [" 2"," 3"," 4" ,"5"],
    ["20%","25%","30%","35%"],
    ["4 days","6 days","8 days","12 days"],
    ["110 cm","140 cm","154 cm","220 cm"],
    ["2","4","6","8"],
    ["10 mph","12 mph","15 mph","20 mph"],
    ["4","6","7","8"],
    ["16 sq meters","24 sq meters","32 sq meters","48 sq meters"],
    ["24","32","54 ","60"],
    ["$35","$36","$37.50","$38"],
    ["30","35","40","45"],
    ["40 km/h","50 km/h","60 km/h","70 km/h"],
    [ "3","4","5","6"],
    ["Mother","Aunt","Cousin","Sister"],
    ["Father and son","Brothers","Uncle and nephew","Grandfather and grandson"],
    ["Sister","Sister-in-law","Cousin","Aunt"],
    ["Mother","Aunt","Sister","Cousin"],
    ["Mother and son","Sisters","Aunt and nephew ","Grandmother and grandson"],
    ["Sister-in-law","Mother","Cousin","Aunt"],
    ["Mother","Aunt","Grandmother","Sister"],
    ["Father and daughter","Brother and sister","Uncle and niece","Grandfather and granddaughter"],
    ["Mother","Grandmother","Aunt","Sister"],
    ["Daughter","Daughter-in-law","Sister-in-law","Niece"],
    ["10","12","14","16"],
    ["12","15","20","25"],
    ["7","8","9","10"],
    ["6","7","8","9"],
    ["8","9","10","11"],
    ["16","18","20","22"],
    ["12","13","14","15"],
    ["14","16","18","20"],
    ["4","5","6","7"],
    ["20","25","30","35"],
    ["15","25","45","55"],
    ["18","24","36","42"],
    ["21","27","31","37"],
    ["18","22","28","34"],
    ["24","36","48","54"],
    ["23","33","43","53"],
    ["28","38","48","58"],
    ["16","36","54","64"],
    ["20","40","60","80"],
    ["26","46","66","26"]
    
    
  
]

correct_answers =  ['c','d','c','a','b','c','b','c','b','a','c','b','c','b','a','b','c','b','b','a','b','a','b','b','a','a','c','a','a','b','b','b','c','c','c','c','b','b','c','b','b','a','b','b','a','b','a','b','a','a']

# Generate synthetic dataset
data = {"Question": questions, "Option A": [], "Option B": [], "Option C": [], "Option D": [], "Correct Answer": []}

for options_list, correct_answer in zip(options, correct_answers):
    # random.shuffle(options_list)  # Remove this line to avoid shuffling options
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
df.to_csv("round2.csv", index=False)
