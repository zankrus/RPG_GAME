from colorama import Fore
import random

from termcolor import colored
print(Fore.GREEN + 'Начало великой RPG-игры "Гейрой и Чудовища"', 'green')
print('Ваша задача убить 10 монстров и не умереть', 'green')
name = input('Введите имя рыцаря : ')
base_hp = 30
base_attack = 10
print('Ваши стартовые характеристики : Здоровье - {} , атака меча - {}'.format(base_hp, base_attack))
monster_dead = 0
while monster_dead != 10 :
    monetka = random.randint(1,3)
    if monetka == 1 :
        '''Битва с монстром'''
        monst_hp = random.randint(5,30)
        monst_attack = random.randint(1,20)
        print(Fore.RED + 'Вы встретили монстра со здоровьем {0} и атакой {1}'.format(monst_hp, monst_attack))
        print('Выберите действие : 1 - атаковать монстра , 2 - убежать')
        while True:
            choice = input('Введите 1, чтобы драться или 2, чтобы убежать : ')
            print('Вы ввели {0}'.format(choice))
            if choice == '1':
                print('Началась драка')
                count = 1
                while True:
                    print('Начался {} раунд боя'.format(count))
                    monst_hp = monst_hp - base_attack
                    print('У монстра осталось - {} жизней'.format(monst_hp))
                    if monst_hp <= 0 :
                        print('Монстр побежден', 'green')
                        monster_dead += 1
                        break
                    base_hp = base_hp - monst_attack
                    print('У вас осталось - {} жизней'.format(base_hp))
                    if base_hp <= 0 :
                        print('Вы умерли.Игра окончена', 'red')
                        quit()
                    count += 1
                break
            elif choice == '2':
                print('Вы сбежали')
                break
            else:
                print('Вы ввели неверное значение. Введите 1 или 2')

    elif monetka == 2:
        sword_power = random.randint(1,20)
        print(Fore.BLUE + 'Вы обнаружили меч с силой - {}'.format(sword_power))
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
        print(Fore.CYAN + 'По дороге вы нашли яблоко', 'green')
        apple_hp = random.randint(1,10)
        base_hp = base_hp + apple_hp
        print('Яблоко восстановило - {} здоровья'.format(apple_hp))

    print(Fore.YELLOW + 'Вечереет. Итог дня:')
    print('Сила меча - {}'.format(base_attack))
    print('Общее количество жизней - {}'.format(base_hp))
    print('Монстров убито - {}'.format(monster_dead))
    input('Конец игрового дня Нажмите ENTER чтобы начать новый ход')


print('Поздравляем. Вы победили')

