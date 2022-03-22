from random import randint as randomNum

def calculateGeneration(males, females, birthChance, genderList, deathChanse):

  malesBorn = 0

  femalesBorn = 0

  malesDied = 0

  femalesDied = 0
  
  if females == males:
    for x in range(females):
      if randomNum(1, birthChance) == 1:
        if genderList[randomNum(0,(len(genderList) - 1))] == 1:
          malesBorn += 1
        else:
          femalesBorn += 1
  elif females > males:
    for x in range(males):
      if randomNum(1, birthChance) == 1:
        if genderList[randomNum(0,(len(genderList) - 1))] == 1:
          malesBorn += 1
        else:
          femalesBorn += 1
  elif males > females:
    for x in range(females):
      if randomNum(1, birthChance) == 1:
        if genderList[randomNum(0,(len(genderList) - 1))] == 1:
          malesBorn += 1
        else:
          femalesBorn += 1

  for x in range(males + females):
    if randomNum(1, deathChanse) == 1:
      if randomNum(1,2) == 1:
        malesDied += 1
      else:
        femalesDied += 1

  return {
    "death": {
      "male": malesDied,
      "female": femalesDied
    },
    "birth": {
      "male": malesBorn,
      "female": femalesBorn
    },
    "newNum": {
      "male": ( males + malesBorn - malesDied),
      "female": ( females + femalesBorn - femalesDied)
    }
  }

def displayDat(males, females, bornMale, bornFemale, genNum, deadMale, deadFemale):
  print('Gen Data')
  print(f"Generation: {genNum}")
  print(f'Males: {males}')
  print(f'Females: {females}')
  print(f'Death: { deadMale + deadFemale }')
  print(f'Birth: { bornMale + bornFemale }')