from time import sleep
from random import randint

status = "on"
money = 0
helplines = ["A) The 50/50", "B) The Audience", "C) The Telephone"]
  

def ask_question(question, answers, correct, amount, audience, phone):  
  print(question)
  sleep(3)
  for answer in answers:
    print(answer)
    sleep(1)
  player_answer = input("What is your answer?(A,B,C,D or H for helpline)")
  if player_answer.upper() == "H":
    use_helpline(correct, amount, audience, phone)
  elif player_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)
  else:
        print(" ")
        game_over()
 

def correct_answer(amount):
    sleep(1)
    print("That is...")
    sleep(1)
    print("CORRECT!!")
    print(" ")
    sleep(1)
    global money
    money = amount
    sleep(1)
    print(f"Very well done {name}, you just won ${money}!")
    print(" ")
    sleep(1)

def use_helpline(correct, amount, audience, phone):
    print(" ")
    global helplines
    if len(helplines) == 0:
        print("Sorry, you have 0 helplines left!")
        sleep(2)
        player_answer = input("what is your answer?: ")
        if player_answer.upper() == correct:
          print(" ")
          correct_answer(amount)
          sleep(2)
        else:
         print(" ")
         game_over()                                                  
    else:
      print("You have the following helplines:")
    sleep(2)
    for helpline in helplines:
       print(f"{helpline}-helpline")
       sleep(1)
    helplines_selection = input("Which helpline would you like to use?")
    if helplines_selection.upper() == "A":
      helplines.remove("A) The 50/50")
      helplineA(correct, amount)
    elif helplines_selection.upper() == "B":
      helplines.remove("B) The Audience")
      helplineB(correct, amount, audience)
    elif helplines_selection.upper() == "C":
      helplines.remove("C) The Telephone")
      helplineC(correct, amount, phone)

def helplineA(correct, amount):
  answers = ["A", "B", "C", "D"]
  helpline_answer = [correct]
  answers.remove(correct)
  number = randint(0, 2)
  helpline_answer.append(answers[number])
  helpline_answer.sort()
  sleep(1)
  print("Deleting.")
  sleep(1)
  print("Deleting..")
  sleep(1)
  print("Deleting...")
  sleep(1)
  print(f"The remaining answers are {helpline_answer[0]} and {helpline_answer[1]}")
  sleep(3)
  player_answer = input("what is your answer: ")
  if player_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)
  else:
    print(" ")
    game_over()

def helplineB(correct, amount, audience):
  sleep(1)
  print("Calculating.")
  sleep(1)
  print("Calculating..")
  sleep(1)
  print("Calculating...")
  sleep(1)
  print(f"The audience vote is: {audience}")
  sleep(3)
  player_answer = input("What Is Your Answer?: ")
  if player_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)
  else:
    print(" ")
    game_over()

def helplineC(correct, amount,phone):
  sleep(1)
  print("brr.")
  sleep(1)
  print("brr..")
  sleep(1)
  print("brr...")
  sleep(1)
  print(f"Here is What They Said:")
  sleep(1.5)
  print(phone)
  sleep(3)
  player_answer = input("What is your final answer?: ")
  if player_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)
  else:
    print(" ")
    game_over()

 

def game_over():
  global status
  status = "off"
  print("That is")
  sleep(1)
  print("incorrect")
  print(" ")
  sleep(1)
  print(f"sorry {name}, Your Going Home With No Money")
  print(" ")
  print(f"It Was a pleasure {name} goodbye")
  sleep(1)
  submit_answer = input ("would you like to Give us a question to Ask in future episode's.")
  if submit_answer.upper() == "YES":
    print("ok go ahead")
    sub_answer = input ()
    print("Thanks For Your Contribution")
    print("GAME OVER!")
  else:
      print("alright it was a pleasure" +name)
  print("GAME OVER!")


question1 = "Q1 for $100: In the UK, the abbreviation NHS stands for National what Service?"
answers1 = ["A) Humanity", "B) Health", "C) Honour", "D) Household"]
correct1 = "B"
amount1 = 100
audience1 = ["A: 1%", "B: 88%", "C: 7%", "D: 4%"]
phone1 = "C'mon Man What A Waste of A Call Ofc It's B"

question2 = "Q2 For $200 : Which Disney character famously leaves a glass slipper behind at a royal ball?"
answers2 = ["A) Pocahontas", "B) Sleeping Beauty", "C) Cinderella", "D) Elsa"]
correct2 = "C"
amount2 = 200
audience2 = ["A: 2%", "B: 5%", "C: 92%", "D: 1%"]
phone2 = "Come on! Who Hasn't Watched Cinderella it's C!"

question3 = "Q3 for $300: What name is given to the revolving belt machinery in an airport that delivers checked luggage from the plane to baggage reclaim?"
answers3 = ["A) Hangar", "B) Terminal", "C) Concourse", "D) Carousel"]
correct3 = "D"
amount3 = 300
audience3 = ["A: 10%", "B: 1%", "C: 9%", "D: 80%"]
phone3 = "I Used To Work In An Airport And I Remember It Was Carousel So D"

question4 = "Q4 for $500:Which of these brands was chiefly associated with the manufacture of household locks?"
answers4 = ["A) Phillips", "B) Flymo", "C) Chubb", "D) Ronseal"]
correct4 = "C"
amount4 = 500
audience4 = ["A: 19%", "B: 3%", "C: 77%", "D: 1%"]
phone4 = "Wait Let Me Ask My Brother 'its c man' He Said C?"

question5 = "Q5 for $1000:  The hammer and sickle is one of the most recognisable symbols of which political ideology?"
answers5 = ["A) Republicanism", "B) Communism", "C) Conservatism", "D) Liberalism"]
correct5 = "B"
amount5 = 1000
audience5 = ["A: 15%", "B: 69%", "C: 15%", "D: 1%"]
phone5 = "I Remember In History Class That's The Soviet Union's Symbol And They Were Communist SO Im Going With B"

question6 = "Q6 for $2000: Which toys have been marketed with the phrase “robots in disguise”?"
answers6 = ["A) Bratz Dolls", "B) Sylvanian Families", "C) Hatchimals", "D) Transformers"]
correct6 = "D"
amount6 = 2000
audience6 = ["A: 9%", "B: 4%", "C: 21%", "D: 66%"]
phone6 = "I Know That Transformers Are Cars That Turn Into Robots D!"

question7 = "Q7 for $4000: What does the word loquacious mean?"
answers7 = ["A) Angry", "B) Chatty", "C) Beautiful", "D) Shy"]
correct7 = "B"
amount7 = 4000
audience7 = ["A: 4%", "B: 3%", "C: 11%", "D: 82%"]
phone7 = "It is his most famous movie! The answer is D!"

question8 = "Q8 for $8000: Obstetrics is a branch of medicine particularly concerned with what?"
answers8 = ["A) Childbirth", "B) Broken bones", "C) Heart conditions", "D) Old age"]
correct8 = "A"
amount8 = 8000
audience8 = ["A: 72%", "B: 12%", "C: 14%", "D: 2%"]
phone8 = "Isn't that for Childbirth? So A should be the answer, right?"

question9 = "Q9 for $16,000:  In Doctor Who, what was the signature look of the fourth Doctor, as portrayed by Tom Baker?"
answers9 = ["A) Bow-tie, braces and tweed jacket", "B) Wide-brimmed hat and extra long scarf", "C) Pinstripe suit and trainers", "D) Cape, velvet jacket and frilly shirt"]
correct9 = "B"
amount9 = 16000
audience9 = ["A: 38%", "B: 48%", "C: 14%", "D: 0%"]
phone9 = "Im Leaning Towards B, I am not sure though"

question10 = "Q10 for $32,000: Which of these religious observances lasts for the shortest period of time during the calendar year?"
answers10 = ["A) Ramadan", "B) Diwali", "C) Lent", "D) Hanukkah"]
correct10 = "B"
amount10 = 32000
audience10 = ["A: 0%", "B: 69%", "C: 30%", "D: 1%"]
phone10 = "I Know A Hindu And He's Told Me Diwali try B!"

question11 = "Q11 for $64,000:  At the closest point, which island group is only 50 miles south-east of the coast of Florida?"
answers11 = ["A) Bahamas", "B) US Virgin Islands", "C) Turks and Caicos Islands", "D) Bermuda"]
correct11 = "A"
amount11 = 64000
audience11 = ["A: 42%", "B: 17%", "C: 39%", "D: 2%"]
phone11 = "I don't know if it is A or C. Yk What Go for A Trust Me"

question12 = "Q12 for $125,000: Construction of which of these famous landmarks was completed first?"
answers12 = ["A) Empire State Building", "B) Royal Albert Hall", "C) Eiffel Tower", "D) Big Ben Clock Tower"]
correct12 = "D"
amount12 = 125000
audience12 = ["A: 20%", "B: 23%", "C: 20%", "D: 37%"]
phone12 = "I am taking a wild guess D sorry but I have no idea."

question13 = "Q13 for $250,000: Which of these cetaceans is classified as a “toothed whale”?"
answers13 = ["A) Gray whale", "B) Minke whale", "C) Sperm whale", "D) Humpback whale"]
correct13 = "C"
amount13 = 250000
audience13 = ["A: 25%", "B: 25%", "C: 27%", "D: 23%"]
phone13 = "Its C Im Very Sure"

question14 = "Q14 for $500,000: California has alomost the same population as..."
answers14 = ["A) The United Kingdom", "B) Spain", "C) Italy", "D) Poland"]
correct14 = "D"
amount14 = 500000
audience14 = ["A: 9%", "B: 31%", "C: 11%", "D: 49%"]
phone14 = "I have no idea. Which country is the smallest? The smallest one is probably correct."

question15 = "AND NOW: THE FINAL $1,000,000 QUESTION: In 1718, which pirate died in battle off the coast of what is now North Carolina?"
answers15 = ["A) Calico Jack", "B) Blackbeard", "C) Bartholomew Roberts", "D) Captain Kidd"]
correct15 = "B"
amount15 = 1000000
audience15 = ["A: 32%", "B: 29%", "C: 28%", "D: 11%"]
phone15 = "I have absolutely no clue But I find Blackbeard Very Admirable So B"


print("Hello And Welcome TO!")
print(" ")
sleep(1)
print("Another Episode Of")
print(" ")
sleep(0.5)
print("WHO")
sleep(0.5)
print("WANTS")
sleep(0.5)
print("TO")
sleep(0.5)
print("BE")
sleep(0.5)
print("A")
sleep(0.5)
print("MILLIONAIRE!")
name = input ("Enter Your Name: ")
print("OUR FIRST CANDIDATE TONIGHT IS " +name)
sleep(1)
print("Can We Get A Big Round Of Applause for "+name)
print(name+ " Hopefully Your Ready To Become A Millionare")
sleep(3)


print("Just A Quick Remider You have 3 Helplines")
sleep(1.5)
for helpline in helplines:
 print(f"{helpline}--helpline")
sleep(2)
print("Hopefully You're Ready Let's Get Started")
print("")
print("")
print("")
sleep(2.3)

ask_question(question1, answers1, correct1, amount1, audience1, phone1)

if status == "on":
  ask_question(question2, answers2, correct2, amount2, audience2, phone2)

if status == "on":
  ask_question(question3, answers3, correct3, amount3, audience3, phone3)

if status == "on":
  ask_question(question4, answers4, correct4, amount4, audience4, phone4)

if status == "on":
  ask_question(question5, answers5, correct5, amount5, audience5, phone5)

if status == "on":
  ask_question(question6, answers6, correct6, amount6, audience6, phone6)

if status == "on":
  ask_question(question7, answers7, correct7, amount7, audience7, phone7)

if status == "on":
  ask_question(question8, answers8, correct8, amount8, audience8, phone8)

if status == "on":
  ask_question(question9, answers9, correct9, amount9, audience9, phone9)

if status == "on":
  ask_question(question10, answers10, correct10, amount10, audience10, phone10)

if status == "on":
  ask_question(question11, answers11, correct11, amount11, audience11, phone11)

if status == "on":
  ask_question(question12, answers12, correct12, amount12, audience12, phone12)

if status == "on":
  ask_question(question13, answers13, correct13, amount13, audience13, phone13)

if status == "on":
  ask_question(question14, answers14, correct14, amount14, audience14, phone14)

if status == "on":
  ask_question(question15, answers15, correct15, amount15, audience15, phone15)

if status == "on":
  print("CONGRATULATIONS!")
  sleep(2)
  print(" ")
  print("YOU HAVE JUST WON")
  sleep(2)
  print("ONE")
  sleep(1)
  print("MILLION!!")
  sleep(1)
  print("DOLLARS!!!!!!!!!!!!!!!!")
  print(" ")
  print(" ")
  sleep(2)
  print("OUR LATEST MEMBER IN THE ALL TIME HALL OF FAME")
  print(" ")
  sleep(3)
  print("IS...")
  print(" ")
  sleep(1.5)
  print("THE UNFORGETABLE NEW MILLIONAIRE: ")
  print(" ")
  sleep(3)
  print(f"{name.upper()}!!!")
  sleep(1.5)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
