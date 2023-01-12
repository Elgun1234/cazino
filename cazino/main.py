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


test = Outcome("test",5)
test1 = Outcome("test",5)
print(test.__eq__(test1))
print(test.__ne__(test1))

print(test.__hash__())
print(test1.__hash__())


