class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        balance = 0

        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        output = "*" * ((30 - len(self.name)) // 2)
        output += self.name
        output += "*" * (30 - len(output))

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"

            output += "\n"
            output += description.ljust(23) + amount.rjust(7)

        output += f"\nTotal: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    total_spent = 0
    spent = []

    for category in categories:
        category_spent = 0

        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += -item["amount"]

        spent.append(category_spent)
        total_spent += category_spent
    percentages = []
    for amount in spent:
        percentage = int((amount / total_spent) * 100)
        percentage = (percentage // 10) * 10
        percentages.append(percentage)

    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        chart += str(level).rjust(3) + "|"

        for percentage in percentages:
            if percentage >= level:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1)

    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        chart += "\n     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

    return chart
