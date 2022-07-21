from random import randint
from colorama import Fore
from time import sleep
from rich import print
import os
import colorama
colorama.init(autoreset=True)

os.system('cls')
del_file = open('data_player.txt', 'r+')
del_file.truncate(0)

print('\n\n\n\n\n\n\n\n\n\n\n\n')
print('[bold white]Escolha sua dificuldade de jogo:[/]\n\n[[bold yellow]1[/]] [bold yellow]Fácil[/][bold white] (0 a 100)[/]\n[[bold red]2[/]] [bold red]Díficil[/][bold white] (0 a 1.000)[/]')
choice = int(input('\n>> '))
easy = 1
hard = 2
if choice       == easy:
    number      = randint(0, 100)
    dificulty   = '[bold white]Dificuldade:[/] [bold yellow]Fácil[/]'
    easy_num    = '[bold cyan]0 [bold white]a[/] 100[/]'
elif choice     == hard:
    number      = randint(0, 1000)
    dificulty   = '[bold white]Dificuldade:[/] [bold red]Difícil[/]'
    hard_num    = '[bold cyan]0 [bold white]a[/] 1.000[/]'

try:
    os.system('cls')
    print(f'\n\n\n\n\n\n\n\n\n\n\n\n{dificulty}\n')
    print(f'[bold white]Tenho um desafio para você! Te desafio acertar um número entre {easy_num}.[/]')

except:
    os.system('cls')
    print(f'\n\n\n\n\n\n\n\n\n\n\n\n{dificulty}\n')
    print(f'[bold white]Tenho um desafio para você! Te desafio acertar um número entre {hard_num}.[/]')


sleep(0.8)
print('[bold white]Será se você consegue?[/]\n')
sleep(1)
times = 0
accept = False
while not accept:
    print('Escolha um número, tente a sorte:')
    answer = input(f'{Fore.LIGHTCYAN_EX}>>{Fore.WHITE} ')
    os.system('cls')
    print('\n\n\n\n\n\n\n\n\n\n\n\n')
    print('[bold white]Seu histórico de tentativas:[/]')
    tip = int(answer)

    archive = open('data_player.txt', 'a')
    archive.write('• ' + answer + "\n")
    archive.close()

    archive = open('data_player.txt', 'r')
    for linha in archive:
        linha = linha.rstrip()
        print(linha)
    archive.close()

    times += 1

    if tip == number:
        accept = True
        continue
    else:
        if tip < number:
            print(
                f'\nÉ {Fore.LIGHTRED_EX}MAIOR {Fore.WHITE}que {answer}, tente mais uma vez.\n')
        elif tip > number:
            print(
                f'\nÉ {Fore.GREEN}menor {Fore.WHITE}que {answer}, tente mais um vez.\n')

print('\n\n\n[green][bold]:white_check_mark: Escolha certa!!![/]\n')
sleep(1.2)
print(dificulty)
print(f'Número: {answer}')
print(f'Você acertou com {times} tentativas!\n\n')

print('Deseja continuar jogando? [bold][white](S/N)[/]')
choice = input(f'{Fore.LIGHTCYAN_EX}>>{Fore.WHITE} ').upper()
if choice == 'S':
    print('\n\n\n\n[bold][white]Uma boa sorte e um bom jogo novamente![/]')
    sleep(2)
    os.system('python main.py')

else:
    if choice != 'S':
        os.system('cls')
        print(
            '\n\n\n\n\n\n\n\n\n\n\n\n[bold][red]Jogo finalizado.[/]\n\n\n\n\n\n\n\n\n\n\n\n\n\n')