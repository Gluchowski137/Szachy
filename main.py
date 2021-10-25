import pygame

pygame.init()
rozmiarokna = (600, 400)
okno = pygame.display.set_mode(rozmiarokna)
klik = False
miejsca = {"a8": (0, 0), "b8": (50, 0), "c8": (100, 0), "d8": (150, 0), "e8": (200, 0), "f8": (250, 0), "g8": (300, 0),
           "h8": (350, 0), "a7": (0, 50), "b7": (50, 50), "c7": (100, 50), "d7": (150, 50), "e7": (200, 50),
           "f7": (250, 50),
           "g7": (300, 50), "h7": (350, 50), "a6": (0, 100), "b6": (50, 100), "c6": (100, 100), "d6": (150, 100),
           "e6": (200, 100), "f6": (250, 100), "g6": (300, 100),
           "h6": (350, 100), "a5": (0, 150), "b5": (50, 150), "c5": (100, 150), "d5": (150, 150), "e5": (200, 150),
           "f5": (250, 150),
           "g5": (300, 150), "h5": (350, 150), "a4": (0, 200), "b4": (50, 200), "c4": (100, 200), "d4": (150, 200),
           "e4": (200, 200), "f4": (250, 200), "g4": (300, 200),
           "h4": (350, 200), "a3": (0, 250), "b3": (50, 250), "c3": (100, 250), "d3": (150, 250), "e3": (200, 250),
           "f3": (250, 250),
           "g3": (300, 250), "h3": (350, 250), "a2": (0, 300), "b2": (50, 300), "c2": (100, 300), "d2": (150, 300),
           "e2": (200, 300), "f2": (250, 300), "g2": (300, 300),
           "h2": (350, 300), "a1": (0, 350), "b1": (50, 350), "c1": (100, 350), "d1": (150, 350), "e1": (200, 350),
           "f1": (250, 350),
           "g1": (300, 350), "h1": (350, 350)}
dupl = []
ckrol = pygame.image.load('cking.png')
cskoczek = pygame.image.load('cknight.png')
cwieza = pygame.image.load('crok.png')
ckrolowa = pygame.image.load('cqueen.png')
cgoniec = pygame.image.load('cbishop.png')
cpionek = pygame.image.load('cpawn.png')
bkrol = pygame.image.load('chess-king.png')
bskoczek = pygame.image.load('chess-knight.png')
bwieza = pygame.image.load('chess-rok.png')
bkrolowa = pygame.image.load('chess-queen.png')
bgoniec = pygame.image.load('bishop.png')
bpionek = pygame.image.load('chess-pawn.png')
runda = 0
ileb = 0
ilec = 0
yb = 0
yc = 350
def papa(px, py):
    global ileb,ilec,yb,yc
    if ileb == 4:
        yb += 50
        ileb = 0
    if ilec == 4:
        yc -= 50
        ilec = 0

    for x in pionki:
        if px == x.x and py == x.y:
            if x.kolor == "bialy":
                x.x = 400 + (50 * ileb)
                x.y = yb
                ileb +=1
                if x.id == "krol":
                    print("czarny wygrał")
            else:
                x.x = 400 + (50 * ilec)
                x.y = yc
                ilec += 1
                if x.id == "krol":
                    print("Biały wygrał")




class Pionki():
    def __init__(self, x, y, w, s, kolor, id, zdj, miejsce="z", klikniety=False):
        self.x = x
        self.y = y
        self.w = w
        self.s = s
        self.kolor = kolor
        self.id = id
        self.klikniety = klikniety
        self.miejsce = miejsce
        self.zdj = zdj

    def aktualizacja_miejsca(self):
        for x in miejsca.items():
            if x[1][0] == self.x and x[1][1] == self.y:
                self.miejsce = x[0]

    def ruch(self, mx, my):
        stare = (self.x,self.y)
        dupl.clear()
        for x in pionki:
            dupl.append((x.x, x.y))
        mozna = 0
        global klik, ile,runda
        gdziekliknieto = (int(mx - (mx % 50)), int(my - (my % 50)))
        if self.id == "pionek":
            if self.kolor == "czarny":
                if self.x < mx < self.x + 49 and self.y > my > self.y - 49:
                    klik = False
                    self.klikniety = False
                    for x in pionki:
                        if self.y - 50 == x.y and self.x == x.x:
                            mozna += 1
                    if mozna == 0:
                        self.y -= 50
                elif self.x - 49 < mx < self.x and self.y > my > self.y - 49:
                    for x in pionki:
                        if self.y - 50 == x.y and self.x - 50 == x.x:
                            if self.kolor != x.kolor:
                                papa(self.x - 50, self.y - 50)
                                klik = False
                                self.klikniety = False
                                self.y -= 50
                                self.x -= 50

                        else:
                            klik = False
                            self.klikniety = False
                elif self.x + 49 < mx < self.x + 99 and self.y > my > self.y - 49:
                    for x in pionki:
                        if self.y - 50 == x.y and self.x + 50 == x.x:
                            if self.kolor != x.kolor:
                                papa(self.x + 50, self.y - 50)
                                klik = False
                                self.klikniety = False
                                self.y -= 50
                                self.x += 50

                        else:
                            klik = False
                            self.klikniety = False

            elif self.kolor == "bialy":
                if self.x < mx < self.x + 49 and self.y + 49 < my < self.y + 99:
                    klik = False
                    self.klikniety = False
                    for x in pionki:
                        if self.y + 50 == x.y and self.x == x.x:
                            mozna += 1
                    if mozna == 0:
                        self.y += 50
                elif self.x + 49 < mx < self.x + 99 and self.y + 49 < my < self.y + 99:
                    for x in pionki:
                        if self.y + 50 == x.y and self.x + 50 == x.x:
                            if self.kolor != x.kolor:
                                papa(self.x + 50, self.y + 50)
                                self.y += 50
                                self.x += 50
                                klik = False
                                self.klikniety = False
                        else:
                            klik = False
                            self.klikniety = False

                elif self.x - 49 < mx < self.x and self.y + 49 < my < self.y + 99:
                    for x in pionki:
                        if self.y + 50 == x.y and self.x - 50 == x.x:
                            if self.kolor != x.kolor:
                                papa(self.x - 50, self.y + 50)
                                klik = False
                                self.klikniety = False
                                self.y += 50
                                self.x -= 50

                        else:
                            klik = False
                            self.klikniety = False
        elif self.id == "wieza":
            if self.x < mx < self.x + 49 and 0 < my < 400:
                if my < self.y:
                    ile = (self.y - my) / 50
                    ile = int(ile) + 1
                elif my > self.y:
                    ile = (my - self.y) / 50
                    ile = int(ile)
                for k in range(ile):
                    if my < self.y:
                        for x in pionki:
                            if self.y - 50 == x.y and self.x == x.x:
                                if mozna == 0:
                                    if self.kolor == x.kolor:
                                        mozna += 1
                                    elif self.kolor != x.kolor:
                                        papa(self.x, self.y - 50)
                                        mozna += 1
                                        if mozna == 1:
                                            self.y -= 50
                                            continue

                        if mozna == 0:
                            self.y -= 50
                    elif my > self.y:
                        for x in pionki:
                            if self.y + 50 == x.y and self.x == x.x:
                                if mozna == 0:
                                    if self.kolor == x.kolor:
                                        mozna += 1
                                    elif self.kolor != x.kolor:
                                        papa(self.x, self.y + 50)
                                        mozna += 1
                                        if mozna == 1:
                                            self.y += 50
                                            continue

                        if mozna == 0:
                            self.y += 50
                klik = False
                self.klikniety = False
            elif 0 < mx < 400 and self.y < my < self.y + 49:
                if mx < self.x:
                    ile = (self.x - mx) / 50
                    ile = int(ile) + 1
                elif mx > self.x:
                    ile = (mx - self.x) / 50
                    ile = int(ile)
                for k in range(ile):
                    if mx < self.x:
                        for x in pionki:
                            if self.x - 50 == x.x and self.y == x.y:
                                if mozna == 0:
                                    if self.kolor == x.kolor:
                                        mozna += 1
                                    elif self.kolor != x.kolor:
                                        papa(self.x - 50, self.y)
                                        mozna += 1
                                        if mozna == 1:
                                            self.x -= 50
                                            continue

                        if mozna == 0:
                            self.x -= 50
                    elif mx > self.x:
                        for x in pionki:
                            if self.x + 50 == x.x and self.y == x.y:
                                if mozna == 0:
                                    if self.kolor == x.kolor:
                                        mozna += 1
                                    elif self.kolor != x.kolor:
                                        papa(self.x + 50, self.y)
                                        mozna += 1
                                        if mozna == 1:
                                            self.x += 50
                                            continue
                        if mozna == 0:
                            self.x += 50
                klik = False
                self.klikniety = False
        elif self.id == "goniec":
            if mx < self.x:
                ile = (self.x - mx) / 50
                ile = int(ile) + 1
            elif mx > self.x:
                ile = (mx - self.x) / 50
                ile = int(ile)
            if mx < self.x and my < self.y:
                for k in range(ile):
                    for x in pionki:
                        if self.x - 50 == x.x and self.y - 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x - 50, self.y - 50)
                                    self.x -= 50
                                    self.y -= 50
                                    mozna = 1
                                    continue
                                else:
                                    mozna = 1
                    if mozna == 0:
                        self.x -= 50
                        self.y -= 50
            elif mx > self.x and my < self.y:
                for k in range(ile):
                    for x in pionki:
                        if self.x + 50 == x.x and self.y - 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x + 50, self.y - 50)
                                    self.x += 50
                                    self.y -= 50
                                    mozna = 1
                                    continue
                                else:
                                    mozna = 1
                    if mozna == 0:
                        self.x += 50
                        self.y -= 50
            elif mx > self.x and my > self.y + 49:
                for k in range(ile):
                    for x in pionki:
                        if self.x + 50 == x.x and self.y + 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x + 50, self.y + 50)
                                    self.x += 50
                                    self.y += 50
                                    mozna = 1
                                    continue
                                else:
                                    mozna = 1
                    if mozna == 0:
                        self.x += 50
                        self.y += 50
            elif mx < self.x and my > self.y + 49:
                for k in range(ile):
                    for x in pionki:
                        if self.x - 50 == x.x and self.y + 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x - 50, self.y + 50)
                                    self.x -= 50
                                    self.y += 50
                                    mozna = 1
                                    continue
                                else:
                                    mozna = 1
                    if mozna == 0:
                        self.x -= 50
                        self.y += 50
            klik = False
            self.klikniety = False
        elif self.id == "kon":
            if self.x + 99 < mx < self.x + 149:
                if self.y > my > self.y - 49:
                    for x in pionki:
                        if self.x + 100 == x.x and self.y - 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x + 100, self.y - 50)
                                    self.x += 100
                                    self.y -= 50
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x += 100
                        self.y -= 50
                elif self.y + 49 < my < self.y + 99:
                    for x in pionki:
                        if self.x + 100 == x.x and self.y + 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x + 100, self.y + 50)
                                    self.x += 100
                                    self.y += 50
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x += 100
                        self.y += 50
            if self.x - 99 < mx < self.x - 49:
                if self.y > my > self.y - 49:
                    for x in pionki:
                        if self.x - 100 == x.x and self.y - 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x - 100, self.y - 50)
                                    self.x -= 100
                                    self.y -= 50
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x -= 100
                        self.y -= 50
                elif self.y + 49 < my < self.y + 99:
                    for x in pionki:
                        if self.x - 100 == x.x and self.y + 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x - 100, self.y + 50)
                                    self.x -= 100
                                    self.y += 50
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x -= 100
                        self.y += 50
            elif self.y - 99 < my < self.y - 49:
                if self.x + 49 < mx < self.x + 99:
                    for x in pionki:
                        if self.x + 50 == x.x and self.y - 100 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x + 50, self.y - 100)
                                    self.x += 50
                                    self.y -= 100
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x += 50
                        self.y -= 100
                elif self.x - 49 < mx < self.x:
                    for x in pionki:
                        if self.x - 50 == x.x and self.y - 100 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x - 50, self.y - 100)
                                    self.x -= 50
                                    self.y -= 100
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x -= 50
                        self.y -= 100
            elif self.y + 99 < my < self.y + 149:
                if self.x + 49 < mx < self.x + 99:
                    for x in pionki:
                        if self.x + 50 == x.x and self.y + 100 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x + 50, self.y + 100)
                                    self.x += 50
                                    self.y += 100
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x += 50
                        self.y += 100
                elif self.x - 49 < mx < self.x:
                    for x in pionki:
                        if self.x - 50 == x.x and self.y + 100 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x - 50, self.y + 100)
                                    self.x -= 50
                                    self.y += 100
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x -= 50
                        self.y += 100
            klik = False
            self.klikniety = False
        elif self.id == "krol":
            # GORA
            if self.x < mx < self.x + 49 and self.y > my > self.y - 49:
                for x in pionki:
                    if self.y - 50 == x.y and self.x == x.x:
                        if mozna == 0:
                            if self.kolor != x.kolor:
                                papa(self.x, self.y - 50)
                                self.y -= 50
                                mozna += 1
                            else:
                                mozna += 1
                if mozna == 0:
                    self.y -= 50
            # dol
            elif self.x < mx < self.x + 49 and self.y + 49 < my < self.y + 99:
                for x in pionki:
                    if self.y + 50 == x.y and self.x == x.x:
                        if mozna == 0:
                            if self.kolor != x.kolor:
                                papa(self.x, self.y + 50)
                                self.y += 50
                                mozna += 1
                            else:
                                mozna += 1
                if mozna == 0:
                    self.y += 50
            # lewo
            elif self.x - 49 < mx < self.x and self.y < my < self.y + 49:
                for x in pionki:
                    if self.y == x.y and self.x - 50 == x.x:
                        if mozna == 0:
                            if self.kolor != x.kolor:
                                papa(self.x - 50, self.y)
                                self.x -= 50
                                mozna += 1
                            else:
                                mozna += 1
                if mozna == 0:
                    self.x -= 50
            # prawo
            elif self.x + 49 < mx < self.x + 99 and self.y < my < self.y + 49:
                for x in pionki:
                    if self.y == x.y and self.x + 50 == x.x:
                        if mozna == 0:
                            if self.kolor != x.kolor:
                                papa(self.x + 50, self.y)
                                self.x += 50
                                mozna += 1
                            else:
                                mozna += 1
                if mozna == 0:
                    self.x += 50
            # prawogora
            elif self.x + 49 < mx < self.x + 99 and self.y > my > self.y - 49:
                for x in pionki:
                    if self.y - 50 == x.y and self.x + 50 == x.x:
                        if self.kolor != x.kolor:
                            papa(self.x + 50, self.y - 50)
                            self.x += 50
                            self.y -= 50
                            mozna += 1
                        else:
                            mozna += 1
                if mozna == 0:
                    self.x += 50
                    self.y -= 50
            # prawodol
            elif self.x + 49 < mx < self.x + 99 and self.y + 49 < my < self.y + 99:
                for x in pionki:
                    if self.y + 50 == x.y and self.x + 50 == x.x:
                        if self.kolor != x.kolor:
                            papa(self.x + 50, self.y + 50)
                            self.x += 50
                            self.y += 50
                            mozna += 1
                        else:
                            mozna += 1
                if mozna == 0:
                    self.x += 50
                    self.y += 50
            # lewogora
            elif self.x - 49 < mx < self.x and self.y > my > self.y - 49:
                for x in pionki:
                    if self.y - 50 == x.y and self.x - 50 == x.x:
                        if self.kolor != x.kolor:
                            papa(self.x - 50, self.y - 50)
                            self.x -= 50
                            self.y -= 50
                            mozna += 1
                        else:
                            mozna += 1
                if mozna == 0:
                    self.x -= 50
                    self.y -= 50
            # lewodol
            elif self.x - 49 < mx < self.x and self.y + 49 < my < self.y + 99:
                for x in pionki:
                    if self.y + 50 == x.y and self.x - 50 == x.x:
                        if self.kolor != x.kolor:
                            papa(self.x - 50, self.y + 50)
                            self.x -= 50
                            self.y += 50
                            mozna += 1
                        else:
                            mozna += 1
                if mozna == 0:
                    self.x -= 50
                    self.y += 50
            klik = False
            self.klikniety = False
        elif self.id == "hetman":
            mabycx = mx - int(mx % 50)
            mabycy = my - int(my % 50)
            if self.x < mx < self.x + 49 and 0 < my < 400:
                if my < self.y:
                    ile = (self.y - my) / 50
                    ile = int(ile) + 1
                elif my > self.y:
                    ile = (my - self.y) / 50
                    ile = int(ile)
                for k in range(ile):
                    if my < self.y:
                        for x in pionki:
                            if self.y - 50 == x.y and self.x == x.x:
                                if mozna == 0:
                                    if self.kolor == x.kolor:
                                        mozna += 1
                                    elif self.kolor != x.kolor:
                                        papa(self.x, self.y - 50)
                                        mozna += 1
                                        if mozna == 1:
                                            self.y -= 50
                                            continue

                        if mozna == 0:
                            self.y -= 50
                    elif my > self.y:
                        for x in pionki:
                            if self.y + 50 == x.y and self.x == x.x:
                                if mozna == 0:
                                    if self.kolor == x.kolor:
                                        mozna += 1
                                    elif self.kolor != x.kolor:
                                        papa(self.x, self.y + 50)
                                        mozna += 1
                                        if mozna == 1:
                                            self.y += 50
                                            continue

                        if mozna == 0:
                            self.y += 50
            elif 0 < mx < 400 and self.y < my < self.y + 49:
                if mx < self.x:
                    ile = (self.x - mx) / 50
                    ile = int(ile) + 1
                elif mx > self.x:
                    ile = (mx - self.x) / 50
                    ile = int(ile)
                for k in range(ile):
                    if mx < self.x:
                        for x in pionki:
                            if self.x - 50 == x.x and self.y == x.y:
                                if mozna == 0:
                                    if self.kolor == x.kolor:
                                        mozna += 1
                                    elif self.kolor != x.kolor:
                                        papa(self.x - 50, self.y)
                                        mozna += 1
                                        if mozna == 1:
                                            self.x -= 50
                                            continue

                        if mozna == 0:
                            self.x -= 50
                    elif mx > self.x:
                        for x in pionki:
                            if self.x + 50 == x.x and self.y == x.y:
                                if mozna == 0:
                                    if self.kolor == x.kolor:
                                        mozna += 1
                                    elif self.kolor != x.kolor:
                                        papa(self.x + 50, self.y)
                                        mozna += 1
                                        if mozna == 1:
                                            self.x += 50
                                            continue
                        if mozna == 0:
                            self.x += 50

            if mx < self.x:
                ile = (self.x - mx) / 50
                ile = int(ile) + 1
            elif mx > self.x:
                ile = (mx - self.x) / 50
                ile = int(ile)
            if mx < self.x and my < self.y:
                for k in range(ile):
                    for x in pionki:
                        if self.x - 50 == x.x and self.y - 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x - 50, self.y - 50)
                                    self.x -= 50
                                    self.y -= 50
                                    mozna = 1
                                    k = 0
                                    continue
                                else:
                                    mozna = 1
                    if mozna == 0:
                        self.x -= 50
                        self.y -= 50
            elif mx > self.x and my < self.y:
                for k in range(ile):
                    for x in pionki:
                        if self.x + 50 == x.x and self.y - 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x + 50, self.y - 50)
                                    self.x += 50
                                    self.y -= 50
                                    mozna = 1
                                    k = 0
                                    continue
                                else:
                                    mozna = 1
                    if mozna == 0:
                        self.x += 50
                        self.y -= 50
            elif mx > self.x and my > self.y + 49:
                for k in range(ile):
                    for x in pionki:
                        if self.x + 50 == x.x and self.y + 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x + 50, self.y + 50)
                                    self.x += 50
                                    self.y += 50
                                    mozna = 1
                                    k = 0
                                    continue
                                else:
                                    mozna = 1
                    if mozna == 0:
                        self.x += 50
                        self.y += 50
            elif mx < self.x and my > self.y + 49:
                for k in range(ile):
                    for x in pionki:
                        if self.x - 50 == x.x and self.y + 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x - 50, self.y + 50)
                                    self.x -= 50
                                    self.y += 50
                                    mozna = 1
                                    k = 0
                                    continue
                                else:
                                    mozna = 1
                    if mozna == 0:
                        self.x -= 50
                        self.y += 50
            klik = False
            self.klikniety = False
        elif self.id == "kon":
            if self.x + 99 < mx < self.x + 149:
                if self.y > my > self.y - 49:
                    for x in pionki:
                        if self.x + 100 == x.x and self.y - 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x + 100, self.y - 50)
                                    self.x += 100
                                    self.y -= 50
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x += 100
                        self.y -= 50
                elif self.y + 49 < my < self.y + 99:
                    for x in pionki:
                        if self.x + 100 == x.x and self.y + 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x + 100, self.y + 50)
                                    self.x += 100
                                    self.y += 50
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x += 100
                        self.y += 50
            if self.x - 99 < mx < self.x - 49:
                if self.y > my > self.y - 49:
                    for x in pionki:
                        if self.x - 100 == x.x and self.y - 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x - 100, self.y - 50)
                                    self.x -= 100
                                    self.y -= 50
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x -= 100
                        self.y -= 50
                elif self.y + 49 < my < self.y + 99:
                    for x in pionki:
                        if self.x - 100 == x.x and self.y + 50 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x - 100, self.y + 50)
                                    self.x -= 100
                                    self.y += 50
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x -= 100
                        self.y += 50
            elif self.y - 99 < my < self.y - 49:
                if self.x + 49 < mx < self.x + 99:
                    for x in pionki:
                        if self.x + 50 == x.x and self.y - 100 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x + 50, self.y - 100)
                                    self.x += 50
                                    self.y -= 100
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x += 50
                        self.y -= 100
                elif self.x - 49 < mx < self.x:
                    for x in pionki:
                        if self.x - 50 == x.x and self.y - 100 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x - 50, self.y - 100)
                                    self.x -= 50
                                    self.y -= 100
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x -= 50
                        self.y -= 100
            elif self.y + 99 < my < self.y + 149:
                if self.x + 49 < mx < self.x + 99:
                    for x in pionki:
                        if self.x + 50 == x.x and self.y + 100 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x + 50, self.y + 100)
                                    self.x += 50
                                    self.y += 100
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x += 50
                        self.y += 100
                elif self.x - 49 < mx < self.x:
                    for x in pionki:
                        if self.x - 50 == x.x and self.y + 100 == x.y:
                            if mozna == 0:
                                if self.kolor != x.kolor:
                                    papa(self.x - 50, self.y + 100)
                                    self.x -= 50
                                    self.y += 100
                                    mozna += 1
                                else:
                                    mozna += 1
                    if mozna == 0:
                        self.x -= 50
                        self.y += 100

        if self.x != gdziekliknieto[0] or self.y != gdziekliknieto[1]:
            k = 0
            for x in pionki:
                x.x = dupl[k][0]
                x.y = dupl[k][1]
                k += 1
                klik = False
                self.klikniety = False
        else:
            dupl.clear()
            for x in pionki:
                dupl.append((x.x, x.y))
            klik = False
            self.klikniety = False
            runda += 1
        if gdziekliknieto[0] == stare[0] and gdziekliknieto[1] == stare[1]:
            runda -=1

    def rys(self):
        okno.blit(self.zdj, (self.x + 8, self.y + 8))

    def klik(self, mx, my):
        global znakx, znaky, klik
        if runda%2 == 0:
            if self.kolor == "bialy":
                if self.x < mx < self.x + 49 and self.y < my < self.y + 49:
                    znakx = self.x + 5
                    znaky = self.y + 5
                    self.klikniety = True
                    klik = True
        elif runda%2 == 1:
            if self.kolor == "czarny":
                if self.x < mx < self.x + 49 and self.y < my < self.y + 49:
                    znakx = self.x + 5
                    znaky = self.y + 5
                    self.klikniety = True
                    klik = True


pionki = [
    Pionki(0, 0, 40, 40, "bialy", "wieza", bwieza), Pionki(50, 0, 40, 40, "bialy", "kon", bskoczek),
    Pionki(100, 0, 40, 40, "bialy", "goniec", bgoniec),
    Pionki(150, 0, 40, 40, "bialy", "krol", bkrol), Pionki(200, 0, 40, 40, "bialy", "hetman", bkrolowa),
    Pionki(250, 0, 40, 40, "bialy", "goniec", bgoniec), Pionki(300, 0, 40, 40, "bialy", "kon", bskoczek),
    Pionki(350, 0, 40, 40, "bialy", "wieza", bwieza), Pionki(0, 350, 40, 40, "czarny", "wieza", cwieza),
    Pionki(50, 350, 40, 40, "czarny", "kon", cskoczek),
    Pionki(100, 350, 40, 40, "czarny", "goniec", cgoniec),
    Pionki(150, 350, 40, 40, "czarny", "krol", ckrol), Pionki(200, 350, 40, 40, "czarny", "hetman", ckrolowa),
    Pionki(250, 350, 40, 40, "czarny", "goniec", cgoniec), Pionki(300, 350, 40, 40, "czarny", "kon", cskoczek),
    Pionki(350, 350, 40, 40, "czarny", "wieza", cwieza)]

for x in range(0, 400, 50):
    pionki.append(Pionki(x, 50, 40, 40, "bialy", "pionek", bpionek))
    pionki.append(Pionki(x, 300, 40, 40, "czarny", "pionek", cpionek))


def mapa():
    kol = 0
    for x in range(0, 400, 50):
        kol += 1
        for y in range(0, 400, 50):
            if kol % 2 == 0:
                kolor = (255, 204, 153)
            else:
                kolor = (144, 96, 48)
            pygame.draw.rect(okno, kolor, (x, y, 50, 50))
            kol += 1


def redraw():
    okno.fill((100,100,100))
    mapa()
    for x in pionki:
        Pionki.aktualizacja_miejsca(x)
        Pionki.rys(x)
    if klik == True:
        pygame.draw.rect(okno, (255, 0, 0), (znakx, znaky, 40, 40), 3)
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx < 400:
                if klik == False:
                    for x in pionki:
                        Pionki.klik(x, mx, my)
                elif klik == True:
                    for x in pionki:
                        if x.klikniety == True:
                            Pionki.ruch(x, mx, my)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                klik = False
                for x in pionki:
                    x.klikniety = False

    redraw()
