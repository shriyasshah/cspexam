import random

flashcards = [
    {'term': 'Biodiversity', 'definition': 'The variety of life in the world or in a particular habitat or ecosystem.'},
    {'term': 'Climate Change', 'definition': 'A long-term change in Earth’s overall temperature and weather patterns.'},
    {'term': 'Deforestation', 'definition': 'The removal of trees and forests, often to clear land for farming or development.'},
    {'term': 'Carbon Footprint', 'definition': 'The total amount of greenhouse gases emitted by an individual, organization, event, or product.'},
    {'term': 'Renewable Resource', 'definition': 'A natural resource that can be replenished over time, like solar or wind energy.'},
    {'term': 'Greenhouse Effect', 'definition': 'The trapping of heat in Earth’s atmosphere by greenhouse gases like CO2 and methane.'},
    {'term': 'Sustainability', 'definition': 'Meeting our own needs without compromising the ability of future generations to meet theirs.'},
    {'term': 'Thermal Pollution', 'definition': 'Heat released into the water produces negative effects to the organisms in that ecosystem and can cause eutrophication.'},
    {'term': 'Ecosystem', 'definition': 'A biological community of interacting organisms and their physical environment.'},
    {'term': 'Overfishing', 'definition': 'Depleting fish populations by catching fish faster than they can reproduce.'},
    {'term': 'Acid Rain', 'definition': 'Rainfall made acidic by pollution that causes harm to the environment.'},
    {'term': 'Fossil Fuels', 'definition': 'Natural fuels like coal, oil, and gas formed from the remains of ancient organisms.'},
    {'term': 'Thermal Inversion', 'definition': 'Warm air blankets cool air, traps pollution, forms easily in valleys.'},
    {'term': 'Watershed', 'definition': 'An area of land where all the water drains into a common body of water like a river or lake.'},
    {'term': 'Invasive Species', 'definition': 'Non-native organisms that spread quickly and harm local ecosystems.'}
]

def run_quiz(num_questions):
    score = 0
    questions = random.sample(flashcards, num_questions)
    for i, card in enumerate(questions, 1):
        print(f"\nQuestion {i}: {card['definition']}")
        answer = input("Your answer: ").strip()
        if answer.lower() == card['term'].lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was: {card['term']}\n")
    print(f"\n🎓 You got {score} out of {num_questions} correct.")

try:
    max_questions = len(flashcards)
    num = int(input(f"How many questions would you like to attempt? (1-{max_questions}): "))
    if 1 <= num <= max_questions:
        run_quiz(num)
    else:
        print("❗ Please enter a valid number within the range.")
except ValueError:
    print("❗ Invalid input. Please enter a number.")