print("Title of program: Onigiri encouragement bot :) :D :P")
print()
while True:
  description = input("How do you feel?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("eat onigiris, they help you feel better :D 🍙")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling, and eat onigiris 🍙")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("onigiris give strength, you should try them :)) 🍙")
      counter += 1
       if each_word == "onigiri":
      feelings_list.append("onigiri")
      encouragement_list.append("congratulations, you have unlocked the final level of onigiris 🍙. Good job, and continue being and feeling like an onigiri :P")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better and remember to eat onigiris :)"

  print()
  print(output)
  print()
