from Draw import Draw
from random import randint
import os

class Hangman:
    drawn=(Draw)
    mode=(str)      #zmienia wygląd hangman'a, ilość dopuszczalnych błędów oraz czy są wyświetlane podpowiedzi
    questionID=(int)
    wordList=[(str)]
    defList=[(str)]
    alreadyChosen=[(int)]
    alreadyChosen=[(bool)]
    usedLetters=[str]
    

#     def __init__(self):
#         modeInt=input("Wybierz tryb:\n1-Standardowy\n2-Artystyczny\n")
#         #modeInt=1
#         if modeInt==2:
#             self.mode="Artist"
#         else:
#             self.mode="Standard"
#         self.drawn=Draw(self.mode)
#         try:
#             self.LoadDataFromFile()
#         except FileNotFoundError:
#             return
#         self.MainGameLoop()

    def __init__(self,mode):
        modeInt=mode
        if modeInt==2:
            self.mode="Artist"
        else:
            self.mode="Standard"
        self.drawn=Draw(self.mode)
        try:
            self.LoadDataFromFile()
        except FileNotFoundError:
            return
        self.MainGameLoop()


    def MainGameLoop(self):
        mistakes=(int)
        while True:
            while True:         #losowy wybór bez powtórzeń słowa z listy
                isAll=True
                try:
                    for b in self.alreadyChosen:
                        if b == False:
                            isAll = False
                            break
                    if isAll:
                        print("skończyły się słowa")
                        return
                    self.questionID = randint(0, len(self.wordList))
                    if self.alreadyChosen[self.questionID]:
                        continue
                    self.alreadyChosen[self.questionID] = True
                except IndexError:
                    continue
                break
            hiddenVals=[(int)]
            mistakes=0
            try:
                hiddenWord = self.wordList[self.questionID]
                for i in range(0,len(hiddenWord)-1):
                    hiddenVals.append(0)
                hiddenVals[0]=0
                for i in range(0,len(hiddenWord)-1):
                    if hiddenWord[i]==" ":
                        hiddenVals[i]=1
            except IndexError:
                continue
            except TypeError:
                continue
            self.usedLetters.clear()
            while True:
                #print('\n' * 80)  # prints 80 line breaks      #taki clrscr z tym że dla konsoli wewnątrz kompilatora
                os.system('cls')
                self.drawn.Drawing(mistakes)
                if self.mode=="Standard":
                    print(self.defList[self.questionID])
                if mistakes>=self.drawn.GetMaxMistakes():
                    if phrase==self.wordList[self.questionID]:
                        for i in range(0,len(hiddenVals)):
                            hiddenVals[i]=1
                if mistakes>=self.drawn.GetMaxMistakes():
                    for i in range(0,len(hiddenVals)):
                        hiddenVals[i]=True
                    print("Gratulacje, przegrałeś\n")
                    self.PrintHiddenWord(hiddenWord,hiddenVals)
                    input("Press enter to cont\n")
                    break;
                self.PrintHiddenWord(hiddenWord,hiddenVals)
                self.PrintUsedLetters()
                if self.IfUnhidden(hiddenVals):
                        print("Gratulacje, wygrałeś\n")
                        input("Press enter to cont\n")
                        break;
                phrase = input("podaj literę/słowo\n")
                if phrase=="0":
                    return
                if phrase=="1":
                    break
                if len(phrase)!=1:
                    if phrase==self.wordList[self.questionID]:
                        for i in range(0,len(hiddenVals)):
                            hiddenVals[i]=1
                        continue
                    else:
                        print("złe słowo")
                        mistakes+=1
                        continue
                x=self.CompareString(phrase,hiddenWord,hiddenVals)
                if x==[]:
                    print("brak litery")
                    self.usedLetters.append(phrase)
                    mistakes+=1
                    continue
                hiddenVals=x
                self.PrintHiddenWord(hiddenWord,hiddenVals)

    def CompareString(self,phrase,hiddenWord,hiddenVals):
        word=self.wordList[self.questionID]
        if hiddenWord.__contains__(phrase)==0:
            return []
        for i in range(0,len(hiddenWord)):
            if hiddenWord[i]==phrase:
                hiddenVals[i]=1
        return hiddenVals

    def LoadDataFromFile(self):
        #file = open('Hangman-Data.txt', 'w+')
        file=open("Hangman-Data.txt")
        for line in file:
            if line.find(";")==0:
                continue
            self.wordList.append(line.split(";")[0].lower())
            self.defList.append(line.split(";")[1])
            self.alreadyChosen.append(False)

    def PrintWordAndDefList(self):
        for i in range(0,len(self.defList)):
            print(self.wordList[i],"-",self.defList[i])

    def PrintHiddenWord(self,hiddenWord,hiddenVals):
        string=""
        for i in range(0,len(hiddenVals)):
            if hiddenVals[i]==1:
                string+=hiddenWord[i]+" "
                if hiddenWord[i]==" ":
                    string+="  "
            else:
                string+="_ "
        print(string)

    def IfUnhidden(self,hiddenVals):
        for i in hiddenVals:
            if i==0:
                return False
        return True

    def PrintUsedLetters(self):
        string="Użyte litery: "
        for i in self.usedLetters:
            string+=i+" "
        print(string)
