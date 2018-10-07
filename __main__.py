import models
from helpers import suffixCheck

def createWordInst (englishWord, row):
  word = models.Word()
  word.setWordAndTranslations(englishWord, row)
  return word, englishWord

def searchDictionary(wordDictionary, searchTerm):
  dictSearch = wordDictionary.get(searchTerm, False)
  if dictSearch:
    for entry in dictSearch:
      print ("\nChinese: " + entry['chineseTranslation'] + "\nPart Of Speech: " + entry['partOfSpeech'])
  return dictSearch

def main():
  dataFile = open("./data/dic_ec.txt", "r", encoding='utf-8')
  wordDict = {}

  for row in dataFile:
    row = row.split('\uf8f5')
    englishWord = row[0]
    row.pop(0)
    if row[-1] == '\n':
      row.pop()
    word, englishWord = createWordInst(englishWord, row)
    wordDict[word.getBaseWord()] = word.getTranslations()

  userSearch = input("Enter a term to search: \n")
  founWordInDictionary = searchDictionary(wordDict, userSearch)
  if founWordInDictionary:
    print ("\n")
    main()
  else:
    isSuffixMatched, rootPossibilitiesArray = suffixCheck.testSuffixes(userSearch)
    if isSuffixMatched:
      isMatchFoundForRemovedSuffix = False
      for possibileWord in rootPossibilitiesArray:
        matchFound = searchDictionary(wordDict, possibileWord)
        if matchFound:
          print("THE ABOVE MATCH WAS FOUND AFTER THE SUFFIX WAS REMOVED: " + userSearch + " --> " + possibileWord + "\n")
          isMatchFoundForRemovedSuffix = True
          main()
      if isMatchFoundForRemovedSuffix == False:
        print ("No matches found")
    else:
      print ("No matches found")

if __name__ == "__main__":
  main()