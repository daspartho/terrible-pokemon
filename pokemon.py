# Computer's Pokemon choice to be improved
# Error Handling
# Player VS Player improvement req.
# attack variations
# More Pokemons
# Auto assign pokemon when 1 pokemon left
# Decompose code i.e. Remove code branching in 2 copies on the basis of battle type
# not prompting to choose who will be whom in once more in p VS p

import random

print('Welcome To Pokemon Battle')
print()
print('Type 1 for player vs computer')
print('Type 2 for player vs player')
battle_type = input('Enter Choice: ')
print()

if battle_type == '1':

    print('Welcome to this pokemon battle \nYou would be given pokemons randomly\n')
    print()

    computer_score = 0
    player_score = 0
    once_more = '1'
    
    while once_more == '1':

        num_pokemon = int(input('How many pokemons should be there? '))
        print()

        class Pokemon:

            def __init__(self, name, hp, attack, speed, ptype, pstrong, pweak):
                self.name = name
                self.hp = hp
                self.attack = attack
                self.speed = speed
                self.ptype = ptype
                self.pstrong = pstrong
                self.pweak = pweak
              
        venusaur = Pokemon('Venusaur', 302, 82, 80, ['Grass','Poison'], ['Water', 'Electric', 'Grass', 'Fighting', 'Fairy'],  ['Fire', 'Ice', 'Flying', 'Psychic'])
        charizard = Pokemon('Charizard', 281, 84, 100, ['Fire', 'Flying'], ['Grass', 'Fire', 'Ground', 'Bug', 'Steel', 'Fairy', 'Fighting'], ['Water', 'Electric', 'Rock'])
        blastoise = Pokemon('Blastoise', 362, 83, 78, ['Water'], ['Fire', 'Water', 'Ice', 'Steel'], ['Grass', 'Electric'])
        pidgeot = Pokemon('Pidgeot', 278, 80, 101, ['Normal', 'Flying'], ['Grass', 'Ground', 'Bug', 'Ghost'], ['Rock', 'Electric', 'Ice'])
        raichu = Pokemon('Raichu', 178, 90, 110, ['Electric'], ['Electric', 'Flying', 'Steel'], ['Ground'])
        alakazam = Pokemon('Alakazam', 141, 50, 120, ['Psychic'], ['Fighting', 'Psychic'], ['Bug', 'Ghost', 'Dark'])
        machamp = Pokemon('Machamp', 307, 130, 55, ['Fighting'], ['Bug', 'Rock', 'Dark'], ['Fly', 'Psychic', 'Fairy'])
        golem = Pokemon('Golem', 473, 120, 45, ['Rock', 'Ground'], ['Normal', 'Fire', 'Electric', 'Poison', 'Flying', 'Rock'], ['Water', 'Grass', 'Ice', 'Fighting', 'Ground', 'Steel'])
        gengar = Pokemon('Gengar', 194, 65, 110, ['Ghost', 'Poison'], ['Normal', 'Grass', 'Fighting', 'Poison', 'Bug', 'Fairy'], ['Ground', 'Psychic', 'Ghost', 'Dark'])
        gyarados = Pokemon('Gyarados', 311, 125, 81, ['Water', 'Flying'], ['Fire', 'Water', 'Fighting', 'Ground', 'Bug', 'Steel'], ['Electric', 'Rock'])
        snorlax = Pokemon('Snorlax', 373, 110, 30, ['Normal'], ['Fire', 'Ice', 'Ghost'], ['Fighting'])
        dragonite = Pokemon('Dragonite', 367, 134, 80, ['Dragon', 'Flying'], ['Fire', 'Water', 'Grass', 'Fighting', 'Ground', 'Bug'], ['Ice', 'Rock', 'Dragon', 'Fairy'])
        meganium = Pokemon('Meganium', 364, 82, 80, ['Grass'], ['Water', 'Electric', 'Grass', 'Ground'], ['Fire', 'Ice', 'Poison', 'Flying', 'Bug'])
        typhlosion = Pokemon('Typhlosion', 281, 84, 100, ['Fire'], ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy'], ['Water', 'Ground', 'Rock'])
        feraligatr = Pokemon('Feraligatr', 374, 105, 78, ['Water'], ['Fire', 'Water', 'Ice', 'Steel'], ['Electric', 'Grass'])
        steelix = Pokemon('Steelix', 708, 85, 30, ['Steel', 'Ground'], ['Normal', 'Electric', 'Poison', 'Flying', 'Psychic', 'Bug', 'Rock', 'Dragon', 'Steel', 'Fairy'], ['Fire', 'Water', 'Fighting', 'Ground'])
        scizor = Pokemon('Scizor', 344, 130, 65, ['Bug', 'Steel'], ['Normal', 'Grass', 'Ice', 'Poison', 'Psychic', 'Bug', 'Dragon', 'Steel', 'Fairy'], ['Fire'])
        kingdra = Pokemon('Kingdra', 336, 95, 85, ['Water', 'Dragon'], ['Fire', 'Water', 'Steel'], ['Dragon', 'Fairy'])
        tyranitar = Pokemon('Tyranitar', 444, 134, 61, ['Rock', 'Dark'], ['Normal', 'Fire', 'Poison', 'Flying', 'Psychic', 'Ghost', 'Dark'], ['Water', 'Grass', 'Fighting', 'Ground', 'Bug', 'Steel', 'Fairy'])
        sceptile = Pokemon('Sceptile', 224, 85, 120, ['Grass'], ['Water', 'Electric', 'Grass', 'Ground'], ['Fire', 'Ice', 'Poison', 'Flying', 'Bug'])
        blaziken = Pokemon('Blaziken', 255, 120, 80, ['Fire', 'Fighting'], ['Fire', 'Grass', 'Ice', 'Bug', 'Dark', 'Steel'], ['Water', 'Ground', 'Flying', 'Psychic'])
        swampert = Pokemon('Swampert', 364, 110, 60, ['Water', 'Ground'], ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], ['Grass'])
        salamence = Pokemon('Salamence', 315, 135, 100, ['Dragon', 'Flying'], ['Fire', 'Water', 'Grass', 'Fighting', 'Ground', 'Bug'], ['Ice', 'Rock', 'Dragon', 'Fairy'])
        metagross = Pokemon('Metagross', 473, 135, 70, ['Steel', 'Psychic'], ['Normal', 'Grass', 'Ice', 'Poison', 'Flying', 'Psychic', 'Rock', 'Dragon', 'Steel', 'Fairy'], ['Fire', 'Ground', 'Ghost', 'Dark'])

        pokemons = [venusaur, charizard, blastoise, pidgeot, raichu, alakazam, machamp, golem, gengar, gyarados, snorlax, dragonite, meganium, typhlosion, feraligatr, steelix, scizor, kingdra, tyranitar, sceptile, blaziken, swampert, salamence, metagross]

        player_pokemons = []
        computer_pokemons = []

        i = 0
        while i < (num_pokemon):
            j = random.choice(pokemons)
            pokemons.remove(j)
            player_pokemons.append(j)
            k = random.choice(pokemons)
            pokemons.remove(k)
            computer_pokemons.append(k)
            i += 1

        print('Player\'s Pokemons are-')
        for l in player_pokemons:
            print(l.name)
        print()    
        print('And Computer\'s Pokemons are-')
        for m in computer_pokemons:
            print(m.name)
            
        input()
        
        print('Lets start the battle!')

        player_pokemon = None
        computer_pokemon = None

        while player_pokemons != [] and computer_pokemons != []:

            if player_pokemon == None:
                player_choice = input('Choose your pokemon: ')
                print()
                for n in player_pokemons:
                    if n.name == player_choice:
                        player_pokemon = n
                        break

            if computer_pokemon == None:
                computer_pokemon = random.choice(computer_pokemons)
                print('Computer choose', computer_pokemon.name)
                print()

            player_attack_power = 1
            computer_attack_power = 1

            for x in player_pokemon.ptype:
                if x in computer_pokemon.pweak:
                    player_attack_power *= 2
                    break
                    
            for x in computer_pokemon.ptype:
                if x in player_pokemon.pweak:
                    computer_attack_power *= 2
                    break
                    
            for x in player_pokemon.ptype:
                if x in computer_pokemon.pstrong:
                    player_attack_power /= 2
                    break

            for x in computer_pokemon.ptype:
                if x in player_pokemon.pstrong:
                    computer_attack_power /= 2
                    break

            while player_pokemon.hp > 0 and computer_pokemon.hp > 0:

                if player_pokemon.speed >= computer_pokemon.speed:
                    
                    print('Player\'s Attack')
                    print(player_pokemon.name, 'Attacked on', computer_pokemon.name)
                    computer_pokemon.hp -= (player_pokemon.attack * player_attack_power)
                    
                    if computer_pokemon.hp < 0:
                        print(computer_pokemon.name, 'fainted!')
                        print()
                        computer_pokemons.remove(computer_pokemon)
                        print(len(computer_pokemons), 'Pokemon(s) left with Computer-')
                        for x in computer_pokemons:
                            print(x.name)
                        print()
                        computer_pokemon = None
                        break
                    print(computer_pokemon.name, 'HP =', computer_pokemon.hp)
                    input()
                
                    print('Computer\'s Attack')
                    print(computer_pokemon.name, 'Attacked on', player_pokemon.name)
                    player_pokemon.hp -=  (computer_pokemon.attack * computer_attack_power)
                    
                    if player_pokemon.hp < 0:
                        print(player_pokemon.name, 'fainted!')
                        print()
                        player_pokemons.remove(player_pokemon)
                        print(len(player_pokemons), 'Pokemon(s) left with Player-')
                        for l in player_pokemons:
                            print(l.name)
                        print()
                        player_pokemon = None
                        break
                    print(player_pokemon.name, 'HP =', player_pokemon.hp)
                    input()

                else:
                    print('Computer\'s Attack')
                    print(computer_pokemon.name, 'Attacked on', player_pokemon.name)
                    player_pokemon.hp -=  (computer_pokemon.attack * computer_attack_power)
                    
                    if player_pokemon.hp < 0:
                        print(player_pokemon.name, 'fainted!')
                        print()
                        player_pokemons.remove(player_pokemon)
                        print(len(player_pokemons), 'Pokemon(s) left with Player-')
                        for l in player_pokemons:
                            print(l.name)
                        print()
                        player_pokemon = None
                        break
                    print(player_pokemon.name, 'HP =', player_pokemon.hp)
                    input()

                    print('Player\'s Attack')
                    print(player_pokemon.name, 'Attacked on', computer_pokemon.name)
                    computer_pokemon.hp -= (player_pokemon.attack * player_attack_power)
                    
                    if computer_pokemon.hp < 0:
                        print(computer_pokemon.name, 'fainted!')
                        print()
                        computer_pokemons.remove(computer_pokemon)
                        print(len(computer_pokemons), 'Pokemon(s) left with Computer-')
                        for x in computer_pokemons:
                            print(x.name)
                        print()
                        computer_pokemon = None
                        break
                    print(computer_pokemon.name, 'HP =', computer_pokemon.hp)
                    input()

        if player_pokemons == []:
            print('Computer Won!')
            computer_score += 1
            

        else:
            print('Player Won!')
            player_score += 1

        print('Computer -', computer_score, '| Player -', player_score)

        input()

        print('Will you like to play once more')
        once_more = input('If yes type 1: ')
        print()

else:
    
    print('Welcome to this pokemon battle \nYou would be given pokemons randomly\n')
    print()

    computer_score = 0
    player_score = 0
    once_more = '1'

    while once_more == '1':

        num_pokemon = int(input('How many pokemons should be there? '))
        print()

        class Pokemon:

            def __init__(self, name, hp, attack, speed, ptype, pstrong, pweak):
                self.name = name
                self.hp = hp
                self.attack = attack
                self.speed = speed
                self.ptype = ptype
                self.pstrong = pstrong
                self.pweak = pweak
              
        venusaur = Pokemon('Venusaur', 302, 82, 80, ['Grass','Poison'], ['Water', 'Electric', 'Grass', 'Fighting', 'Fairy'],  ['Fire', 'Ice', 'Flying', 'Psychic'])
        charizard = Pokemon('Charizard', 281, 84, 100, ['Fire', 'Flying'], ['Grass', 'Fire', 'Ground', 'Bug', 'Steel', 'Fairy', 'Fighting'], ['Water', 'Electric', 'Rock'])
        blastoise = Pokemon('Blastoise', 362, 83, 78, ['Water'], ['Fire', 'Water', 'Ice', 'Steel'], ['Grass', 'Electric'])
        pidgeot = Pokemon('Pidgeot', 278, 80, 101, ['Normal', 'Flying'], ['Grass', 'Ground', 'Bug', 'Ghost'], ['Rock', 'Electric', 'Ice'])
        raichu = Pokemon('Raichu', 178, 90, 110, ['Electric'], ['Electric', 'Flying', 'Steel'], ['Ground'])
        alakazam = Pokemon('Alakazam', 141, 50, 120, ['Psychic'], ['Fighting', 'Psychic'], ['Bug', 'Ghost', 'Dark'])
        machamp = Pokemon('Machamp', 307, 130, 55, ['Fighting'], ['Bug', 'Rock', 'Dark'], ['Fly', 'Psychic', 'Fairy'])
        golem = Pokemon('Golem', 473, 120, 45, ['Rock', 'Ground'], ['Normal', 'Fire', 'Electric', 'Poison', 'Flying', 'Rock'], ['Water', 'Grass', 'Ice', 'Fighting', 'Ground', 'Steel'])
        gengar = Pokemon('Gengar', 194, 65, 110, ['Ghost', 'Poison'], ['Normal', 'Grass', 'Fighting', 'Poison', 'Bug', 'Fairy'], ['Ground', 'Psychic', 'Ghost', 'Dark'])
        gyarados = Pokemon('Gyarados', 311, 125, 81, ['Water', 'Flying'], ['Fire', 'Water', 'Fighting', 'Ground', 'Bug', 'Steel'], ['Electric', 'Rock'])
        snorlax = Pokemon('Snorlax', 373, 110, 30, ['Normal'], ['Fire', 'Ice', 'Ghost'], ['Fighting'])
        dragonite = Pokemon('Dragonite', 367, 134, 80, ['Dragon', 'Flying'], ['Fire', 'Water', 'Grass', 'Fighting', 'Ground', 'Bug'], ['Ice', 'Rock', 'Dragon', 'Fairy'])
        meganium = Pokemon('Meganium', 364, 82, 80, ['Grass'], ['Water', 'Electric', 'Grass', 'Ground'], ['Fire', 'Ice', 'Poison', 'Flying', 'Bug'])
        typhlosion = Pokemon('Typhlosion', 281, 84, 100, ['Fire'], ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy'], ['Water', 'Ground', 'Rock'])
        feraligatr = Pokemon('Feraligatr', 374, 105, 78, ['Water'], ['Fire', 'Water', 'Ice', 'Steel'], ['Electric', 'Grass'])
        steelix = Pokemon('Steelix', 708, 85, 30, ['Steel', 'Ground'], ['Normal', 'Electric', 'Poison', 'Flying', 'Psychic', 'Bug', 'Rock', 'Dragon', 'Steel', 'Fairy'], ['Fire', 'Water', 'Fighting', 'Ground'])
        scizor = Pokemon('Scizor', 344, 130, 65, ['Bug', 'Steel'], ['Normal', 'Grass', 'Ice', 'Poison', 'Psychic', 'Bug', 'Dragon', 'Steel', 'Fairy'], ['Fire'])
        kingdra = Pokemon('Kingdra', 336, 95, 85, ['Water', 'Dragon'], ['Fire', 'Water', 'Steel'], ['Dragon', 'Fairy'])
        tyranitar = Pokemon('Tyranitar', 444, 134, 61, ['Rock', 'Dark'], ['Normal', 'Fire', 'Poison', 'Flying', 'Psychic', 'Ghost', 'Dark'], ['Water', 'Grass', 'Fighting', 'Ground', 'Bug', 'Steel', 'Fairy'])
        sceptile = Pokemon('Sceptile', 224, 85, 120, ['Grass'], ['Water', 'Electric', 'Grass', 'Ground'], ['Fire', 'Ice', 'Poison', 'Flying', 'Bug'])
        blaziken = Pokemon('Blaziken', 255, 120, 80, ['Fire', 'Fighting'], ['Fire', 'Grass', 'Ice', 'Bug', 'Dark', 'Steel'], ['Water', 'Ground', 'Flying', 'Psychic'])
        swampert = Pokemon('Swampert', 364, 110, 60, ['Water', 'Ground'], ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], ['Grass'])
        salamence = Pokemon('Salamence', 315, 135, 100, ['Dragon', 'Flying'], ['Fire', 'Water', 'Grass', 'Fighting', 'Ground', 'Bug'], ['Ice', 'Rock', 'Dragon', 'Fairy'])
        metagross = Pokemon('Metagross', 473, 135, 70, ['Steel', 'Psychic'], ['Normal', 'Grass', 'Ice', 'Poison', 'Flying', 'Psychic', 'Rock', 'Dragon', 'Steel', 'Fairy'], ['Fire', 'Ground', 'Ghost', 'Dark'])

        pokemons = [venusaur, charizard, blastoise, pidgeot, raichu, alakazam, machamp, golem, gengar, gyarados, snorlax, dragonite, meganium, typhlosion, feraligatr, steelix, scizor, kingdra, tyranitar, sceptile, blaziken, swampert, salamence, metagross]

        print("Choose who will be player and computer")
        input()
        player_pokemons = []
        computer_pokemons = []

        i = 0
        while i < (num_pokemon):
            j = random.choice(pokemons)
            pokemons.remove(j)
            player_pokemons.append(j)
            k = random.choice(pokemons)
            pokemons.remove(k)
            computer_pokemons.append(k)
            i += 1

        print('Player\'s Pokemons are-')
        for l in player_pokemons:
            print(l.name)
        print()    
        print('And Computer\'s Pokemons are-')
        for m in computer_pokemons:
            print(m.name)
            
        input()
        
        print('Lets start the battle!')

        player_pokemon = None
        computer_pokemon = None

        while player_pokemons != [] and computer_pokemons != []:

            if player_pokemon == None:
                player_choice = input('Player Choose your pokemon: ')
                print()
                for n in player_pokemons:
                    if n.name == player_choice:
                        player_pokemon = n
                        break

            if computer_pokemon == None:
                computer_choice = input('Computer Choose your pokemon: ')
                print()
                for n in computer_pokemons:
                    if n.name == computer_choice:
                        computer_pokemon = n
                        break
                print('Computer choose', computer_pokemon.name)
                print()

            player_attack_power = 1
            computer_attack_power = 1

            for x in player_pokemon.ptype:
                if x in computer_pokemon.pweak:
                    player_attack_power *= 2
                    break
                    
            for x in computer_pokemon.ptype:
                if x in player_pokemon.pweak:
                    computer_attack_power *= 2
                    break
                    
            for x in player_pokemon.ptype:
                if x in computer_pokemon.pstrong:
                    player_attack_power /= 2
                    break

            for x in computer_pokemon.ptype:
                if x in player_pokemon.pstrong:
                    computer_attack_power /= 2
                    break

            while player_pokemon.hp > 0 and computer_pokemon.hp > 0:

                if player_pokemon.speed >= computer_pokemon.speed:
                    
                    print('Player\'s Attack')
                    print(player_pokemon.name, 'Attacked on', computer_pokemon.name)
                    computer_pokemon.hp -= (player_pokemon.attack * player_attack_power)
                    
                    if computer_pokemon.hp < 0:
                        print(computer_pokemon.name, 'fainted!')
                        print()
                        computer_pokemons.remove(computer_pokemon)
                        print(len(computer_pokemons), 'Pokemon(s) left with Computer-')
                        for x in computer_pokemons:
                            print(x.name)
                        print()
                        computer_pokemon = None
                        break
                    print(computer_pokemon.name, 'HP =', computer_pokemon.hp)
                    input()
                
                    print('Computer\'s Attack')
                    print(computer_pokemon.name, 'Attacked on', player_pokemon.name)
                    player_pokemon.hp -=  (computer_pokemon.attack * computer_attack_power)
                    
                    if player_pokemon.hp < 0:
                        print(player_pokemon.name, 'fainted!')
                        print()
                        player_pokemons.remove(player_pokemon)
                        print(len(player_pokemons), 'Pokemon(s) left with Player-')
                        for l in player_pokemons:
                            print(l.name)
                        print()
                        player_pokemon = None
                        break
                    print(player_pokemon.name, 'HP =', player_pokemon.hp)
                    input()

                else:
                    print('Computer\'s Attack')
                    print(computer_pokemon.name, 'Attacked on', player_pokemon.name)
                    player_pokemon.hp -=  (computer_pokemon.attack * computer_attack_power)
                    
                    if player_pokemon.hp < 0:
                        print(player_pokemon.name, 'fainted!')
                        print()
                        player_pokemons.remove(player_pokemon)
                        print(len(player_pokemons), 'Pokemon(s) left with Player-')
                        for l in player_pokemons:
                            print(l.name)
                        print()
                        player_pokemon = None
                        break
                    print(player_pokemon.name, 'HP =', player_pokemon.hp)
                    input()

                    print('Player\'s Attack')
                    print(player_pokemon.name, 'Attacked on', computer_pokemon.name)
                    computer_pokemon.hp -= (player_pokemon.attack * player_attack_power)
                    
                    if computer_pokemon.hp < 0:
                        print(computer_pokemon.name, 'fainted!')
                        print()
                        computer_pokemons.remove(computer_pokemon)
                        print(len(computer_pokemons), 'Pokemon(s) left with Computer-')
                        for x in computer_pokemons:
                            print(x.name)
                        print()
                        computer_pokemon = None
                        break
                    print(computer_pokemon.name, 'HP =', computer_pokemon.hp)
                    input()

        if player_pokemons == []:
            print('Computer Won!')
            computer_score += 1

        else:
            print('Player Won!')
            player_score += 1

        print('Computer -', computer_score, '| Player -', player_score)

        input()

        print('Will you like to play once more')
        once_more = input('If yes type 1: ')
        print()

print('Thank You')
