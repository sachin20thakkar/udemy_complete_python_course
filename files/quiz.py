questions = open('questions.txt', 'r')
questions_list = questions.readlines()
questions.close()

questions_list = [q.strip() for q in questions_list if q.strip()]
score = 0
total = len(questions_list)
for question in questions_list:
    q, a = question.split('=')
    user_answer = input(f"What is {q}? ")
    if user_answer.strip().lower() == a.strip().lower():
        print("Correct!")
        score += 1
print(f"You scored {score} out of {total}.")
result = open('results.txt', 'a')
result.write(f"Score: {score} out of {total}\n")
result.close()