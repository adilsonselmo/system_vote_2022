# A simple script to calculate BMI
import pywebio
from pywebio.input import *
from pywebio.output import *

def voting():
    put_markdown('# **SISTEMA DE VOTOS - ELEIÇÕES 2022**')
    name = input('Digite seu nome: ', type='text')
    age = input('Digite sua idade: ', type=NUMBER)

    if age >= 18:
        put_text('Verificando seus dados...')

        put_table([
            ['Nome', 'Idade'],
            [name, age]
        ])

        check = checkbox(options = ['Todas os dados estão corretos.'])

        if check:
            selection = radio('Selecione o seu partido', ['MPLA', 'UNITA', 'FNLA', 'Casa Nova'])
            put_text('Obrigado! Seu voto foi enviado.')

            keep_voting = radio('Continuar outro eleitor', ['Sim', 'Não'])

            if keep_voting == 'Sim':
                voting()
            
            
            else:
                return style(put_text('Voto foi finalizado, aguarde os resultados em breve...'), 'color:green')

    else:
        style(put_text('Você não pode votar!'), 'color:orange')

        keep_voting = radio('Continuar outro eleitor', ['Sim', 'Não'])

        if keep_voting == 'Sim':
            voting()

        else:
            return style(put_text('Voto foi finalizado, aguarde os resultados em breve...'), 'color:green')

if __name__ == '__main__':
    pywebio.start_server(voting, port=80)