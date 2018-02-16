class Draw:
    completion=0
    tree=[]
    mode=(str)

    def __init__(self, mode):
        if mode!="Artist" and mode !="Standard":
            return 0
        self.mode=mode
        if self.mode== "Artist":
            self.ArtistDrawingInit()
        if self.mode=="Standard":
            self.StandardDrawingInit()

    def Drawing(self,mistakes):
        if self.mode=="Standard":
            tree=[]
            for i in range(0,len(self.tree)):
                tree.append("")

            if (mistakes>0):
                tree[6]="/|\\"
            if (mistakes>1):
                tree[5]=" |"
                tree[4]=" |"
                tree[3]=" |"
                tree[2]=" |"
            if (mistakes>2):
                tree[0]=" __"
                tree[1]=" |/"
            if (mistakes>3):
                tree[0]=" _____"
            if (mistakes>4):
                tree[1]=" |/  |"
            if (mistakes>5):
                tree[1]=" |/  |"
                tree[2]=" |   0"
                tree[3]=" |  /|\\"
                tree[4]=" |  /'\\"
            for i in tree:
                print(i)


        if self.mode=="Artist":
            for i in range(0,len(self.tree)):
                if mistakes-1<i:
                    print("")
                    continue
                print(self.tree.__getitem__(i))

    def StandardDrawingInit(self):
        self.tree.append(" _____")
        self.tree.append(" |/  |")
        self.tree.append(" |   0")
        self.tree.append(" |  /|\\")
        self.tree.append(" |  /'\\")
        self.tree.append(" |")
        self.tree.append("/|\\")
        self.maxDrawn=6

    def ArtistDrawingInit(self):
        #http://ascii.co.uk/art/hangman
        self.tree.append("  ___________.._______")
        self.tree.append("| .__________))______|")
        self.tree.append("| | / /      ||")
        self.tree.append("| |/ /       ||")
        self.tree.append("| | /        ||.-''.")
        self.tree.append("| |/         |/  _  \\")
        self.tree.append("| |          ||  `/,|")
        self.tree.append("| |          (\\\\`_.'")
        self.tree.append("| |         .-`--'.")
        self.tree.append("| |        /Y . . Y\\")
        self.tree.append("| |       // |   | \\\\")
        self.tree.append("| |      //  | . |  \\\\")
        self.tree.append("| |     ')   |   |   (`")
        self.tree.append("| |          ||'||")
        self.tree.append("| |          || ||")
        self.tree.append("| |          || ||")
        self.tree.append("| |          || ||")
        self.tree.append("| |         / | | \\")
        self.tree.append("\"\"\"\"\"\"\"\"\"\"|_`-' `-' |\"\"\"|")
        self.tree.append("|\"|\"\"\"\"\"\"\"\ \       '\"|\"|")
        self.tree.append("| |        \ \        | |")
        self.tree.append(": :         \ \       : :")
        self.tree.append(". .          `'       . .")
        self.maxDrawn=23

    def DrawShow(self):
        self.Drawing(self.maxDrawn)

    def GetMaxMistakes(self):
        return self.maxDrawn