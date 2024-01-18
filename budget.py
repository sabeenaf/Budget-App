class Category:

  # constructor function
  def __init__(self, category=""):
    self.category = category
    self.ledger = []
    self.balance = 0

  #format for pront
  def __str__(self):
    title = self.category.center(30, "*") + "\n"
    list = ""
    for items in self.ledger:
      desciption_formatted = items["description"][:23].ljust(23)
      amount_formatted = str("{:.2f}".format(items["amount"])).rjust(7)
      list = list + (desciption_formatted + amount_formatted + '\n')
    total = 'Total: ' + str(self.balance)
    return title + list + total

  #deposit amount to account
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount  #add to balance

  #withdraw amount from account
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": (-1) * amount, "description": description})
      self.balance = self.balance - amount  #remove from balance
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def check_funds(self, amount):
    if self.balance >= amount:
      return True
    else:
      return False

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.category)
      category.deposit(amount, "Transfer from " + self.category)
      return True
    else:
      return False


def create_spend_chart(categories):
  spent_total = 0
  spent_per_category = []

  #extract spent values for each category
  for categorie in categories:
    spent = 0
    for item in categorie.ledger:
      if item["amount"] < 0:
        spent += abs(item["amount"])
    spent_per_category.append(spent)  #store sum of spent amount per category
    spent_total += spent  #calculate total spent

  spent_per_category_percent = [
      x / spent_total * 100 for x in spent_per_category
  ]
  spent_per_category_percent = [
      int(x // 10 * 10) for x in spent_per_category_percent
  ]  #rounding down to nearest 10

  #create chart
  title = "Percentage spent by category\n"

  #vertical and bar graph with o
  vertical_bar = 100
  chart = ""
  spent_bar = ["" for x in range(len(spent_per_category_percent))]
  while vertical_bar >= 0:
    for i in range(len(spent_per_category_percent)):
      if spent_per_category_percent[i] >= vertical_bar:
        spent_bar[i] = " o "
      else:
        spent_bar[i] = "   "

    chart = chart + str(vertical_bar).rjust(3) + "|" + "".join(
        spent_bar) + " \n"
    vertical_bar = vertical_bar - 10

  #vertically aligned description text string
  types = []
  longest_string = 0
  #print rotated text
  for categorie in categories:
    #types=types+[categorie.category]
    if len(categorie.category) > longest_string:
      longest_string = len(categorie.category)

  print_str = ""
  for categorie in categories:
    types = types + [categorie.category.ljust(longest_string)]

  for i in range(0, longest_string):
    print_str = print_str + "     "
    for j in range(0, len(types)):
      print_str = print_str + types[j][i] + "  "
    print_str = print_str + "\n"

  #combine title, chart and vertically aligned description
  print_chart = (title + chart + "    " + "-" * (len(categories) * 3 + 1) +
                 "\n" + print_str).rstrip("\n")

  #print(repr(print_chart))
  return print_chart
