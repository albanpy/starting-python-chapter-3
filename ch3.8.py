#Hot Dog Cookout Calculator
people=int(input("Enter the number of people attending the cookout:"))
hot_dog_given=int(input("Enter the number of hot dogs each person will be given:"))
total_hot_dog=people*hot_dog_given
if total_hot_dog>=10:
    hot_dog_pack=total_hot_dog//10
    hot_dog_buns_pack=total_hot_dog//8
    hot_dog_leftover=total_hot_dog%10
    hot_dog_buns_leftover=total_hot_dog%8
    ################################
    print(f'The minimum number of packages of hot dogs required={hot_dog_pack:,}')
    print(f'The minimum number of packages of hot dog buns required={hot_dog_buns_pack:,}')
    print(f'The number of hot dogs that will be left over={hot_dog_leftover:,}')
    print(f'The number of hot dog buns that will be left over={hot_dog_buns_leftover:,}')
else:
    print("There is no packet of hot dog")
