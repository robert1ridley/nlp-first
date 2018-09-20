class Word(object):
  def __init__(self):
    self.baseWord = ''
    self.translations = []

  def setWordAndTranslations(self, inBaseWord, translationArray):
    count = 0
    self.baseWord = inBaseWord
    for item in translationArray:
      if count % 2 == 0 or count == 0:
        translationObject = {}
        translationObject['partOfSpeech'] = item
      else:
        translationObject['chineseTranslation'] = item
        self.translations.append(translationObject)
      count += 1
      
  def getBaseWord(self):
    return self.baseWord

  def getTranslations(self):
    return self.translations

  def setBaseWord(self, newBaseWord):
    self.baseWord = newBaseWord

  def setTranslations(self, newTranslation):
    self.translations = newTranslation