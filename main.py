import json
import math
from narritivecommands import text, options



restarts = 0
debugging = 0
inventory = []
items = {}

def loadjson(file):
  f = open(file+'.json')
  dictionary = json.load(f)
  f.close()
  return dictionary

items = loadjson("items")

def give(item,number='1'):
  number = int(number)
  if number<1:
    return 0
  stackSize = items[item].get("StackableTo")
  for itemindex,currentitem in enumerate(inventory):
    if(currentitem[0].get("name")==items[item].get("name") and currentitem[1]!=stackSize):
      if(stackSize==0):
          currentitem[1]+=number
      elif(stackSize>1):
        for i in range(
          math.floor(float(number-(stackSize-currentitem[1]))/stackSize)
          ):
          inventory.append([items[item],stackSize])
        if((number-(stackSize-currentitem[1]))%stackSize>0):
          inventory.append([items[item],(number-(stackSize-currentitem[1]))%stackSize])
        currentitem[1]+=number
      else:
        for itemnum in range(number):
          inventory.append([items[item],1])
      return 1
  if(stackSize==0):
    inventory.append([items[item],number])
  elif(stackSize>1):
    for i in range(math.floor(float(number)/stackSize)):
      inventory.append([items[item],stackSize])
    if(number%stackSize>0):
      inventory.append([items[item],number%stackSize])
  else:
    for itemnum in range(number):
      inventory.append([items[item],1])

def viewinventory():
  global inventory
  message="Inventory:"
  for item in inventory:
    if(item[0].get("StackableTo")==0 or item[0].get("StackableTo")>1):
      message+='\n {}: {:^20}'.format(item[0].get("name"),str(item[1]))
    else:
      message+="\n "+item[0].get("name")
  text(message)

def checkitem(item,number='1'):
  number=int(number)
  global inventory
  for currentitem in inventory:
    if(currentitem[0].get("name")==items[item].get("name") and currentitem[1]>=number):
      return True
  return False

def resetinventory():
  global inventory
  inventory = []

def askhelp():
  global commands
  helpmessage = '{:^100}'.format('[Help]')
  for com in commands:
    helpmessage+='\n {:^10} {} {:^30} {} {:^50}'.format(com,'-',commands[com][1],'-',commands[com][2])
  text(helpmessage)


commands = {
  "text":[text,"prints stuff","text>[input]"],
  "give":[give,"gives items","give>[item],(numberofitems)"],
  "inv":[viewinventory,"view inventory","inv"],
  "clear":[resetinventory,"clears the inventory","clear"],
  "help":[askhelp,"ask for help","help"]
}

def runcommand(command, args=[]):
  if(len(args)==0):
    command()
  else:
    command(*args)

def debug():
  text("-Debug mode is on-")
  resetinventory()
  inputcommand=""
  while(inputcommand!="q"):
    inputcommand = input("c:")
    if(inputcommand=="q"):
      break
    commandparts = inputcommand.split(">")
    inputcommand = commandparts[0]
    inputargs = ''
    if(len(commandparts)>1):
      inputargs = commandparts[1]
    if(len(inputargs)==0):
      args = []
    else:
      args = inputargs.split(",")
    #runcommand(commands[inputcommand],args)
    try:
      runcommand(commands[inputcommand][0],args)
    except Exception as e:
      text("command failed. try again.\n["+str(e)+"]\nuse 'help' to get more info")

def end():
  text("The End.")
  options("Would you like to restart?",("Yes","y",start),("No","n",print))

def start(restart=True):
  global restarts
  if(not(restart)):
    name = input("What is your name?\n")
    text("Hello "+name)
  else:
    restarts+=1
  resetinventory()
  give("money",100)
  text("Welcome to our game!")
  text("There are three doors. Door 1, Door 2, and Door 3.")
  options("Which door do you choose?",("Door 1","d1",door1),("Door 2","d2",door2),("Door 3","d3",door3))


def door1():
  #
  text("")







# door 2

def door2():
  #
  text("")







# door 3

def door3():
  #
  text("")

if(not(debugging)):
  start(False)
else:
  debug()