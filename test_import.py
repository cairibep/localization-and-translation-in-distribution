#!/usr/bin/env python3
# Teste de importação após instalar o pacote com: pip install .

from dev_aberto import hello
# import dev_aberto_caiorp

if __name__ == '__main__':
    date, name = hello()
    print(f'Último commit em: {date} por {name}')

