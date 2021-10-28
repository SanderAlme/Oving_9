class Quiz:
    def __init__(self, sporsmal, alternativer, svar):
        self.sporsmal = sporsmal
        self.alternativer = alternativer
        self.svar = svar
    
    def sjekk_svar(self):
        gjett = int(input(self))
        if self.svar == gjett:
            print("Riktig svar!")
            return 1
        else:
            print("Feil svar!")
            return 0
        
    def __str__(self):
        return (self.sporsmal
                + self.alternativer[0]
                + self.alternativer[1]
                + self.alternativer[2]
                + self.alternativer[3]
                + "\n\nSvaret ditt: ")

sporsmal = ["Hvor ligger UIS?\n",
            "Hvilket år er vi i?\n",
            "Hva fag er dette?\n",
            "Hva er 2+2?\n"]

alternativer = [["1) Stavanger ", "2) Oslo ", "3) Trondheim ", "4) Bergen "], 
           ["1) 2002 ", "2) 2069 ", "3) 2021 ", "4) 2016 "],
           ["1) Data ", "2) Kunst ", "3) Fysikk ", "4) Historie "],
           ["1) 5 ", "2) 3 ", "3) 1 ", "4) 4 "]]

svar = [1, 3, 1, 4]

if __name__ == "__main__":
    Quiz1 = Quiz(sporsmal[0], alternativer[0], svar[0])
    Quiz2 = Quiz(sporsmal[1], alternativer[1], svar[1])
    Quiz3 = Quiz(sporsmal[2], alternativer[2], svar[2])
    Quiz4 = Quiz(sporsmal[3], alternativer[3], svar[3])
    Quiz1.sjekk_svar()
    Quiz2.sjekk_svar()
    Quiz3.sjekk_svar()
    Quiz4.sjekk_svar()
