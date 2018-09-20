class Word(object):
  def __init__(self):
    self.baseWord = ''
    self.translations = []

  def setWordAndTranslations(self, inBaseWord, translationArray):
    count = 0
    translationObject = {}
    self.baseWord = inBaseWord
    for item in translationArray:
      if count % 2 == 0 or count == 0:
        translationObject['partOfSpeech'] = item
      else:
        translationObject['chineseTranslation'] = item
      count += 1
    self.translations.append(translationObject)
      
  def getBaseWord(self):
    return self.baseWord

  def getTranslations(self):
    return self.translations

  def setBaseWord(self, newBaseWord):
    self.baseWord = newBaseWord

  def setTranslations(self, newTranslation):
    self.translations = newTranslation