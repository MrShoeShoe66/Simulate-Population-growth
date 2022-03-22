import func
import time

print("Population growth Simulator")

print('----------------------------')

maleCount = input("How manny males will be born in a litter?\n> ")

print('----------------------------')

femaleCount = input("How manny females will be born in a litter\n> ")

try:
  maleCount = int(maleCount)
  femaleCount = int(femaleCount)
except:
  print('Unable to export your numbers from txt to int')
  exit(3)

genderList = []

for x in range(maleCount):
  genderList.append(1)

for x in range(femaleCount):
  genderList.append(2)

print('----------------------------')

print("STARTING POP:")

totalPop = 200

print(f'Total: {totalPop}')

maleCount = 100

print(f'Male: {maleCount}')

femaleCount = 100

print(f'Female: {femaleCount}')

print('----------------------------')

babyChanse = input('What will be the chanse of a sucsesful birth?\n> 1/')

try:
  babyChanse = int(babyChanse)
except:
  print('Unable to export your numbers from txt to int')
  exit(3)

print('----------------------------')

birthChance = input('What will be the chanse of an attempted birth?\n> 1/')

try:
  birthChance = int(birthChance)
except:
  print('Unable to export your numbers from txt to int')
  exit(3)

print('----------------------------')

deathChance = input('What will be the chanse of a death?\n> 1/')

try:
  deathChance = int(deathChance)
except:
  print('Unable to export your numbers from txt to int')
  exit(3)

print('----------------------------')

delayCount = input("Should there be a delay?\n> (0) ")

if delayCount == '':
  delayCount = '0'

try:
  delayCount = int(delayCount)
except:
  print('Unable to export your numbers from txt to int')
  exit(3)

print('----------------------------')

genCount = input("How manny generations sould be calulated?\n> (inf) ")

if genCount == '':
  genCount = 'inf'
  infGen = True
else:
  infGen = False

try:
  if not infGen:
    genCount = int(genCount)
except:
  print('Unable to export your numbers from txt to int')
  exit(3)

print('----------------------------')

start = input("Hit enter to start\n> [START]")

print('----------------------------')

genNum = 0

continueLoop = True

while continueLoop:
  if infGen:
    if femaleCount <= 0 or maleCount <= 0:
      continueLoop = False
    else:  
  
      genRaw = func.calculateGeneration(maleCount, femaleCount, birthChance, genderList, deathChance)
      
      maleCount = genRaw['newNum']['male']
      femaleCount = genRaw['newNum']['female']
      
      deadMale = genRaw['death']['male']
      deadFemale = genRaw['death']['female']
  
      bornMale = genRaw['birth']['male']
      bornFemale = genRaw['birth']['female']
  
      maleCount = genRaw['newNum']['male']
      femaleCount = genRaw['newNum']['female']
      
      genNum += 1
      func.displayDat(maleCount, femaleCount, bornMale, bornFemale, genNum, deadMale, deadFemale)
      print('----------------------------')
      
      time.sleep(delayCount)
  else:
      for x in range(genCount):
        if femaleCount <= 0 or maleCount <= 0:
          continueLoop = False
        else:  
      
          genRaw = func.calculateGeneration(maleCount, femaleCount, birthChance, genderList, deathChance)
          
          maleCount = genRaw['newNum']['male']
          femaleCount = genRaw['newNum']['female']
          
          deadMale = genRaw['death']['male']
          deadFemale = genRaw['death']['female']
      
          bornMale = genRaw['birth']['male']
          bornFemale = genRaw['birth']['female']
      
          genNum += 1
      
          func.displayDat(maleCount, femaleCount, bornMale, bornFemale, genNum, deadMale, deadFemale)
          print('----------------------------')
          
          time.sleep(delayCount)

if femaleCount <= 0 or maleCount <= 0:
  print('Species Eradicated')
  print('Try tweeking some numbers to change this!')
else:
  print('Species Surrvived')