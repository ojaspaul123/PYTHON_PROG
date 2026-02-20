## MCQs Pattern Using Python
questions = (("How many colors are in a rainbow?"),
             ("What is the capital of India?"),
             ("Which animal is known as the Ship of the Desert?"),
             (" What is the national animal of India?"),
             ("What color is a polar bear?"))

options =   (("A.8","B.3","C.7","D.11"),
            ("A.AGARTALA","B.DELHI","C.KOLKATA","D.BHUBANESWAR"),
            ("A.FLYER","B.SNAKE","C.CAMEL","D.CACTUS"),
            ("A.TIGER","B.LION","C.DEER","D.COW"),
            ("A.BROWN","B.ORANGE","C.WHITE","D.RED"))

answers = (("C"),("B"),("C"),("A"),("C"))
guesses = []
score =0
question_num=0   

for question in questions:
    print("--------------------------------------------")
    print(question)
    for option in options[question_num]:
            print(option)
    guess = input("Enter your wise option(A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
       score += 1  
       print("CORRECT!")
    else :
        print("INCORRECT!")
        print(f"{answers[question_num]} is the corrcet answer")         
    question_num += 1 
    
        
print("----------RESULT----------")        

print("Correct Answers : ")
for answer in answers:
    print(answer,end  =" ")
    
print()  
print("Guesses Answers : ")  
for guess in guesses:
    print(guess,end =" ")        
print()
score = int(score / len(questions) * 100)
print(f"Your score is {score}%")