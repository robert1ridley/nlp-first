import re

def isSingularVerb(inWord):
  possibleRootWords = []
  if inWord.endswith('ies'):
    possibleRootWords.append(re.sub('ies$', 'y', inWord))
  elif inWord.endswith('es'):
    possibleRootWords.append(re.sub('es$', '', inWord))
    possibleRootWords.append(re.sub('s$', '', inWord))
  else:
    possibleRootWords.append(re.sub('s$', '', inWord))
  return possibleRootWords

def isContinuousVerb(inWord):
  possibleRootWords = []
  if inWord.endswith('ying'):
    possibleRootWords.append(re.sub('ying$', 'ie', inWord))
    possibleRootWords.append(re.sub('ing$', '', inWord))
  elif inWord.endswith('ing') and inWord[-4] == inWord[-5]:
    removeSuffix = re.sub('ing$', '', inWord)
    removeFinalConst = removeSuffix[:-1]
    possibleRootWords.append(removeFinalConst)
  else:
    possibleRootWords.append(re.sub('ing$', 'e', inWord))
    possibleRootWords.append(re.sub('ing$', '', inWord))
  return possibleRootWords

def isPastTenseVerb(inWord):
  possibleRootWords = []
  if inWord.endswith('ied'):
    possibleRootWords.append(re.sub('ied$', 'y', inWord))
  elif inWord.endswith('ed') and inWord[-3] == inWord[-4]:
    removeSuffix = re.sub('ed$', '', inWord)
    removeFinalConst = removeSuffix[:-1]
    possibleRootWords.append(removeFinalConst)
  else:
    possibleRootWords.append(re.sub('ed$', '', inWord))
    possibleRootWords.append(re.sub('d$', '', inWord))
  return possibleRootWords

def testSuffixes(inWord):
  possibleRootWords = []
  isSuffixMatch = False
  if inWord.endswith('s'):
    possibleRootWords = isSingularVerb(inWord)
    isSuffixMatch = True
  elif inWord.endswith('ing'):
    possibleRootWords = isContinuousVerb(inWord)
    isSuffixMatch = True
  elif inWord.endswith('ed'):
    possibleRootWords = isPastTenseVerb(inWord)
    isSuffixMatch = True
  else:
    possibleRootWords = []
    isSuffixMatch = False

  return isSuffixMatch, possibleRootWords