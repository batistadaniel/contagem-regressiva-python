import time # importando a biblioteca time

def iniciarTimer(duracao):
    timer = duracao * 60 # transformando a entrada de minutos pra segundos
    for _ in range(timer, -1, -1): # fim -1 pra aparecer o :00 dos segundos
        horas = timer // 3600 # pega a parte inteira pra evitar o flutuante
        minutos = (timer % 3600) // 60 # pega a parte inteira pra evitar o flutuante
        segundos = timer % 60 # pega o resto apenas
        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}") # formata o display
        time.sleep(1) # timer de 1 segundo
        timer -= 1 # decrementa o timer


iniciarTimer(1) # chama a funcao