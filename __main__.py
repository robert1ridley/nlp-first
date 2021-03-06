import models
from helpers import suffixCheck
import sys

def createWordInst (englishWord, row):
  word = models.Word()
  word.setWordAndTranslations(englishWord, row)
  return word, englishWord

def searchDictionary(wordDictionary, searchTerm):
  dictSearch = wordDictionary.get(searchTerm, False)
  if dictSearch:
    for entry in dictSearch:
      print ("\n英语单词：" + searchTerm + "\n中文翻译：" +
             entry['chineseTranslation'] + "\n词性：" + entry['partOfSpeech'])
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

  userSearch = input("\n输入一个英文单词（停止程序，输入 '1'）：\n")
  if userSearch == '1':
    sys.exit()
  isMatchFound = False
  founWordInDictionary = searchDictionary(wordDict, userSearch)
  
  # Check whether user-entered word is in dictionary
  # isMatchFound if there is a match in dict
  if founWordInDictionary:
    isMatchFound = True
  
  # Check whether suffix removal finds dict match
  isSuffixMatched, rootPossibilitiesArray = suffixCheck.testSuffixes(userSearch)
  if isSuffixMatched:
    for possibileWord in rootPossibilitiesArray:
      matchFound = searchDictionary(wordDict, possibileWord)
      if matchFound:
        isMatchFound = True
  if isMatchFound == False:
    print ("\n没有匹配的中文单词")

if __name__ == "__main__":
  while True:
    main()