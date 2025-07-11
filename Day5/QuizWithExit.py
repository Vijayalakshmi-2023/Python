questions = [
    "What is the capital of France? ",
    "What is 5 + 7? ",
    "Name the largest planet in our solar system: ",
    "What language is this program written in? ",
    "Who wrote 'Romeo and Juliet'? "
]

index = 0

while index < len(questions):
    answer = input(questions[index]).strip().lower()
    if answer == "quit":
        print("🛑 Quiz exited early.")
        break
    index += 1
else:
    print("🎉 Quiz complete! Thanks for participating.")
