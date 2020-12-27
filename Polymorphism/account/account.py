class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if isinstance(amount, int):
            self._transactions.append(amount)
            return
        raise ValueError('please use int for amount')

    @property  ## acc.balance shte go vezemem a ne da go vikame s acc.balance()
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.amount + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")

        account.add_transaction(amount_to_add)
        return f"New Balance: {account.amount}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner, self.amount})"

    def __len__(self):
        return len(self._transactions)

    # def __iter__(self):
    #     pass

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):    ## reversed vrushta obj koito nqma repr a go slagame v __list__ toi ima repr
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        acc = Account(owner=f"{self.owner}&{other.owner}", amount=self.amount+other.amount)
        acc._transactions.extend(self._transactions + other._transactions)
        ## append she mi sloji v lista trransactions [[list ot other]]
        ## extend shte mi veme stoinostite ot dr list i shte gi dobavi
        return acc


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:  ## __iter__
    print(transaction)
print(acc[1])               ## __getitem__
print(list(reversed(acc))) ## __reverse__
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2  ## __add__
print(acc3)
print(acc3._transactions)













