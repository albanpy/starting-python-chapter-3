#Book Club Points
books=int(input("Enter number of books that he or she purchased this month:"))
if books>=0 and books<2:
    print(f'You earns 0 points for purchased {books} books')
elif books>=2 and books<4:
    print(f'You earns 5 points for purchased {books} books')
elif books>=4 and books<6:
    print(f'You earns 15 points for purchased {books} books')
elif books>=6 and books<8:
    print(f'You earns 30 points for purchased {books} books')
elif books>=8:
    print(f'You earns 60 points for purchased {books} books')
