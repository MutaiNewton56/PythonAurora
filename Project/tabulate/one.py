from tabulate import tabulate

# Sample data
data = [
   ["Go \n Collect 200","Baltic \n Avenue","Comunity \n Chest","Jail"],
   ["May Fair","*","*","Pall \n Mall"],
   ["Super Tax","*","*","Chance \n Card"],
   ["Bow Street","*","*","Bond Stret"],
   ["Go To \n Jail","Baltic \n Avenue","Comunity \n Chest","Free \n Parking"],
]


mono_board=[
    {
        'name':"Go \n Collect 200",
        'x':0,
        'y':0,
    },
    {
        'name':"Baltic Avenue",
        'x':0,
        'y':1
    },
    {
        'name':"Jail",
        'x':0,
        'y':3
    },
    {
        'name':"May Fair",
        'x':1,
        'y':0
    }
]

# Display table
print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))
print("Start Game")
print("🐴")

dice=3
cp=mono_board[dice]
print(cp)
print(data[cp['x']][cp['y']])
data[cp['x']][cp['y']]=f"{cp['name']} \n {player1}"
print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))