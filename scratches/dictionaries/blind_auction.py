import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
\n'''

bids = {}

print(logo)

more_bystanders = True
while more_bystanders:
    name = input("Name of the bystander: ")
    bid = float(input("Bid price: $"))

    bids[name] = bid

    if input("Are there more bystanders? (y/n)").lower() != 'y':
        more_bystanders = False
    else: 
        cls()

winner_name = ""
winner_value = 0
for b_name in bids:
    if bids[b_name] > winner_value:
        winner_name = b_name
        winner_value = bids[b_name]

print(f"Awarded to {winner_name} for ${round(winner_value)}")