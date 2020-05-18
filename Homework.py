

import random
print('Начало великой RPG-игры "Гейрой и Чудовища"')
name = input('Введите имя рыцаря : ')
base_hp = 10
base_attack = 10
monster_dead = 0
while monster_dead != 10 or base_hp > 0:
    monetka = random.randint(1,4)
    if monetka == 1 :
        '''Битва с монстром'''
        monst_hp = random.randint(1,11)
        monst_attack = random.randint(1,11)
        print('Вы встретили монстра со здоровьем {0} и атакой {1}'.format(monst_hp, monst_attack))
        print('Выберите действие : 1 - атаковать монстра , 2 - убежать')
        while True:
            choice = input('Введите 1, чтобы драться или 2, чтобы убежать : ')
            print('Вы ввели {0}'.format(choice))
            if choice == '1':
                while True:
                    monst_hp = monst_hp - base_attack
                    if monst_hp <= 0 :
                        monster_dead += 1
                        break
                    base_hp = base_hp - monst_attack
                    if base_hp <= 0 :
                        print('Вы умерли')
                        break
                break
            elif choice == '2':
                print('Вы сбежали')
                break
            else:
                print('Вы ввели неверное значение. Введите 1 или 2')

    elif monetka == 2:
        sword_power = random.randint(1,20)
        print('Вы обнаружили меч с силой - {}'.format(sword_power))
        while True:
            choice_2 = input('Введите 1 , чтобы поднять меч или 2, чтобы пройти мимо : ')
            if choice_2 == '1':
                base_attack = sword_power
                break
            elif choice_2 == '2':
                print('Вы прошли мимо')
                break
            else:
                print('Вы ввели неверное значение. Введите 1 или 2')

    else:
        print('По дороге вы нашли яблоко')
        apple_hp = random.randint(1,20)
        base_hp = base_hp + apple_hp
        print('Яблоко восстановило - {} здоровья'.format(apple_hp))

    print('Сила меча - {}'.format(base_attack))
    print('Общее количество жизней - {}'.format(base_hp))
    print('Монстров убито - {}'.format(monster_dead))
print('Поздравляем. Вы победили')


