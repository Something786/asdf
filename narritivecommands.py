import math

def text(dialog=""):
  print("-\n"+dialog+"\n-")

def options(dialog, *choices):
  choiceischosen = False
  optionstext = ""
  for choice in choices:
    optionstext=optionstext+choice[1]+" - "+choice[0]+", "
  while(not(choiceischosen)):
    chosen = input(dialog+"\n("+optionstext[0:-2]+")\n-")
    for choice in choices:
      if(choice[1]==chosen or choice[0]==chosen):
        choice[2]()
        choiceischosen = True
        return 1
    text('"'+chosen+'" does not exist, Try again.')