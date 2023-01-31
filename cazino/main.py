import random

class Outcome:
    def __init__(self, name:str, odds:int):
        self.name = str(name)
        self.odds = int(odds)

    def winAmount(self,amount:float) -> float:
        return amount*self.odds

    def __eq__(self,other) -> bool:
        return self.name == other.name

    def __ne__(self,other) -> bool:
        return self.name != other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return f"{self.odds}:1"

    def __repr__(self) -> str:
        return f"Outcome({self.name},{self.odds})"
class Bin(frozenset):
    '''
    Each bin will have 12-14 Outcomes
    Frozenset means a unique values, fixed once created
    Extended (inherits all methods from frozenset e.g. .add()
    Chapter 6, pages 45-48
    '''
    pass

class Wheel:
    '''
    Contains 38 bins
    Responsible for Random Number Generation (RNG)
    Chapter 7, pages 49-52
    '''

    def __init__(self):
        self.bins = list(Bin() for _ in range(38))
        self.rng = random.Random()
        self.rng.seed(4)

    def addOutcome(self, number, outcome):
        self.bins[number] = Bin(self.bins[number] | Bin([outcome]))

    def next(self):
        return self.rng.randint(0,37) # todo want bin not number

    def get(self, bin):
        return self.bins[bin]


class BinBuilder:
    """
    Creates all of the winning Outcomes and adds them to each bin on the wheel
    Each bin has 12-14 different ways that it can be a winner e.g. 1 can be straight, street, corner...
    Chapter 8, pages 53-58
    """

    def buildBins(self, wheel):
        pass

    def straightBets(self):
        """
        Bet on a single number paying at 35:1
        38 bets / 38 outcomes
        """
        outcomes = []
        for i in range(38):
            if i == 37:
                bin = Outcome("00",35)
                x = (i,bin.__repr__())
                outcomes.append(x)
            else:
                bin = Outcome(str(i), 35)
                x = (i, bin.__repr__())
                outcomes.append(x)

        return outcomes

    def splitBets(self):
        """
        Adjacent pair of numbers (column or row) paying at 17:1
        114 bets / 114 outcomes
        """
        outcomes = []
        odds = 17
        for rows in range(3):
            for i in range(1+rows,32+rows,3):
                bin = Outcome(f"{i}-{i+3}",odds)
                x = (i,bin)
                outcomes.append(x)
        for i in range(2,36,3):
            bin = Outcome(f"{i}-{i-1}",odds)
            bin_alt = Outcome(f"{i}-{i+1}",odds)
            x = (i,bin)
            outcomes.append(x)
            x = (i,bin_alt)
            outcomes.append(x)

        return outcomes

    def streetBets(self):
        """
        3 numbers in a single row paying at 11:1
        12 possible bets / 36 outcomes
        """
        outcomes = []
        return outcomes

    def lineBets(self):
        """
        A 6 number block (2 street bets) paying at 5:1
        11 possible bets
        """
        outcomes = []
        return outcomes

    def dozenBets(self):
        """
        Each number is member of one of three dozens paying at 2:1
        3 possible bets
        """
        outcomes = []
        return outcomes

    def cornerBets(self):
        """
        A square of 4 numbers paying at 8:1
        22 possible bets / 88 outcomes
        """
        outcomes = []
        return outcomes

    def outsideBets(self):
        """
        All other bets e.g. Red/Black, Low/High, Even/Odd
        """
        outcomes = []
        return outcomes

b = BinBuilder()
print(b.splitBets())
print(len(b.splitBets()))




