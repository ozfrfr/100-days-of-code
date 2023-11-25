import os

print('''
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⠁⡀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⡟⢀⣼⣿⣶⣤⣀⠘⠿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⠟⢀⣾⣿⣿⣿⣿⣿⣷⣦⣄⠉⠻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⠏⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠻⢿⡿⠃⠰⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⢠⣿⣷⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣠⣿⣿⣿⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣦⣄⠙⠻⣿⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣈⠙⠻⣶⠄⠉⠛⠿⣿⡿⠁⣼⣿⣿⣿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠛⢿⣿⣿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣾⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')

print('''
      Welcome to Secret Auction
      ''')


name = input("What is your name? ")
bid = input("What is your bid price? $")
os.system('clear')

auction = [
{
    "Name": name,
    "Bid": int(bid)
}
]

ask = input("Are there other users who want to bid? Type 'Yes' or 'No'. ").lower()
os.system('clear')

while ask not in ['yes', 'no']:
    os.system('clear')
    print("Invalid input. Please enter 'Yes' or 'No'.")
    ask = input("Are there other users who want to bid? Type 'Yes' or 'No'. ").lower()

while ask == "yes":
    os.system('clear')
    new_entry = {}
    new_name = input("What is your name? ")
    new_entry["Name"] = new_name
    new_bid = input("What is your bid price? $")
    new_entry["Bid"] = int(new_bid)
    auction.append(new_entry)
    os.system('clear')
    ask = input("Are there other users who want to bid? 'Yes' or 'No'. ").lower()

if ask == "no":
    os.system('clear') 
    from operator import itemgetter
    winner = max(auction, key=itemgetter('Bid'))

    winner_name = winner['Name']
    winner_bid = winner['Bid']


    print(f"The winner is {winner_name} with bid of ${winner_bid}\n")
