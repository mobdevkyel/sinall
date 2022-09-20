from flask import Flask
import requests
from time import time, sleep
from datetime import datetime, timedelta
import os, time, sys, json, re, configparser


app = Flask(__name__)

url = 'https://api.fbtips.com.br/v1/speedway/'

@app.route('/buscar')
def buscar():
    
    # DADOS DA API
    def dados():
        global url
        resp = requests.get(url=url)
        data = resp.json()
        return data
    # ==========================================
    
    # HORARIO DO SITE
    data = dados()
    DataHoraSite = data['lastUpdated']
    d = DataHoraSite.split(' ')
    dd = d[1].split(':')
    HaraSite = f'{dd[0]}:{dd[1]}'
    #===========================================
    
    # FUNÇOES
    def pegar_coluna(minuto):
        coluna = 0
        if minuto == 1:
            coluna = 0
        elif minuto == 4:
            coluna = 1 
        elif minuto == 7:
            coluna = 2   
        elif minuto == 10:
            coluna = 3    
        elif minuto == 13:
            coluna = 4    
        elif minuto == 16:
            coluna = 5
        elif minuto == 19:
            coluna = 6    
        elif minuto == 22:
            coluna = 7    
        elif minuto == 25:
            coluna = 8    
        elif minuto == 28:
            coluna = 9    
        elif minuto == 31:
            coluna = 10    
        elif minuto == 34:
            coluna = 11
        elif minuto == 37:
            coluna = 12    
        elif minuto == 40:
            coluna = 13    
        elif minuto == 43:
            coluna = 14    
        elif minuto == 46:
            coluna = 15    
        elif minuto == 49:
            coluna = 16    
        elif minuto == 52:
            coluna = 17    
        elif minuto == 55:
            coluna = 18   
        elif minuto == 58:
            coluna = 19     
        return coluna
    
    def verifica_cor(p1, p2, p3, p4):
        verde = False
        amarelo = False
        vermelho = False
        roxo = False
        
        if p1 == 'verde':
            verde = True
        if p2 == 'verde':
            verde = True
        if p3 == 'verde':
            verde = True
        if p4 == 'verde':
            verde = True
            
        if p1 == 'amarelo':
            amarelo = True
        if p2 == 'amarelo':
            amarelo = True
        if p3 == 'amarelo':
            amarelo = True
        if p4 == 'amarelo':
            amarelo = True 
            
        if p1 == 'vermelho': 
            vermelho = True
        if p2 == 'vermelho': 
            vermelho = True
        if p3 == 'vermelho': 
            vermelho = True
        if p4 == 'vermelho':
            vermelho = True
            
        if p1 == 'roxo': 
            roxo = True
        if p2 == 'roxo': 
            roxo = True
        if p3 == 'roxo': 
            roxo = True
        if p4 == 'roxo':
            roxo = True
        
        if verde == False:
            return 'verde'
        elif amarelo == False:
            return 'amarelo'
        elif vermelho == False:
            return 'vermelho'
        elif roxo == False:
            return 'roxo'

    def verifica_cor2(p1, p2, p3, p4):
        verde = False
        amarelo = False
        vermelho = False
        roxo = False
        cores = []
        
        if p1 == 'verde':
            verde = True
        if p2 == 'verde':
            verde = True
        if p3 == 'verde':
            verde = True
        if p4 == 'verde':
            verde = True
            
        if p1 == 'amarelo':
            amarelo = True
        if p2 == 'amarelo':
            amarelo = True
        if p3 == 'amarelo':
            amarelo = True
        if p4 == 'amarelo':
            amarelo = True 
            
        if p1 == 'vermelho': 
            vermelho = True
        if p2 == 'vermelho': 
            vermelho = True
        if p3 == 'vermelho': 
            vermelho = True
        if p4 == 'vermelho':
            vermelho = True
            
        if p1 == 'roxo': 
            roxo = True
        if p2 == 'roxo': 
            roxo = True
        if p3 == 'roxo': 
            roxo = True
        if p4 == 'roxo':
            roxo = True
        
        if verde == False:
            cores.append('verde')
        elif amarelo == False:
            cores.append('amarelo')
        elif vermelho == False:
            cores.append('vermelho')
        elif roxo == False:
            cores.append('roxo')
        
        return cores[0], cores[1]

    def verifica_cor3(p01, p02, p03):
        verde = False
        amarelo = False
        vermelho = False
        roxo = False
        
        
        if p01 == 'verde':
            verde = True
        if p02 == 'verde':
            verde = True
        if p03 == 'verde':
            verde = True
                    
        if p01 == 'amarelo':
            amarelo = True
        if p02 == 'amarelo':
            amarelo = True
        if p03 == 'amarelo':
            amarelo = True
                    
        if p01 == 'vermelho': 
            vermelho = True
        if p02 == 'vermelho': 
            vermelho = True
        if p03 == 'vermelho': 
            vermelho = True
                    
        if p01 == 'roxo': 
            roxo = True
        if p02 == 'roxo': 
            roxo = True
        if p03 == 'roxo': 
            roxo = True
                
        if verde == False:
            return 'verde'
        elif amarelo == False:
            return 'amarelo'
        elif vermelho == False:
            return 'vermelho'
        elif roxo == False:
            return 'roxo'
    
    def verifivar_padrao(lista_linha1, lista_linha2, lista_linha3, Entrada_coluna):
        
        try:
            linha = False
            
            p1 = lista_linha2[Entrada_coluna]
            p2 = lista_linha2[(Entrada_coluna+1)]
            p3 = lista_linha3[Entrada_coluna]
            p4 = lista_linha3[(Entrada_coluna+1)]
            p04 = lista_linha1[(Entrada_coluna)-1]
            p03 = lista_linha1[(Entrada_coluna)-2]
            p02 = lista_linha1[(Entrada_coluna-3)]
            p01 = lista_linha1[(Entrada_coluna-4)]
            
            if p1 == p2 and p3 != p1 and p4 != p2 and p3 != p4:
                padrao = 'Par Alto'
                entrada = p3,p4
            elif p3 == p4 and p3 != p1 and p4 != p2 and p1 != p2:
                padrao = 'Par Baixo'
                entrada = p2,p1
            elif p1 == p3 and p1 != p2 and p3 != p4 and p2 != p4:
                padrao = 'Par Esquerdo'
                entrada = p2,p4
            elif p2 == p4 and p2 != p1 and p4 != p3 and p1 != p3:
                padrao = 'Par Direito'
                entrada = p3,p1
            elif p2 == p3 and p2 != p1 and p3 != p4 and p1 != p4:
                padrao = 'Diagonal Direita'
                cor_falta = verifica_cor(p1, p2, p3, p4)
                entrada = p1,p2,cor_falta
            elif p1 == p4 and p1 != p2 and p4 != p3 and p2 != p3:
                padrao = 'Diagonal Esquerda'
                cor_falta = verifica_cor(p1, p2, p3, p4)
                entrada = p1,p2,cor_falta
            elif p1 == p4 and p2 == p3:
                padrao = 'Diagonal dupla'
                p1, p2 = verifica_cor2(p1, p2, p3, p4)
                entrada = p1,p2
            elif p01 != p02 and p02 != p03 and p03 != p01:
                padrao = 'Linha'
                linha = True
                corfalta = verifica_cor3(p01, p02, p03)
                atuais_minutos = p04
                entrada = p02, corfalta

            return padrao, entrada, linha
        except:
            return '', '', ''
    
    def pegarhora():
            url = 'https://api.fbtips.com.br/v1/speedway/'
            resp = requests.get(url=url)
            data = resp.json()

            hora = data['lastUpdated'].split(' ')
            hora2 = hora[1].split(':')
            horaanalise = f'{hora2[0]}:{hora2[1]}'

            return horaanalise, hora2[1]
    
    def telegram(padrao, pilotosEntradas, minutosEntradas, totalPilotos, totalMinutos, tipo, lista_linha1):
        
                
        #"-1001491918280" arb key:1354435258:AAFHjsNdiIXAa6mjqn_b5WvrWEIGNBqzMVw
        # -1001660958039 5779647627:AAHiu073fuTOJ36UOjvxiUOFws_b4_N__gI
                    
        chat_id = "-1001660958039"
        token = '5779647627:AAHiu073fuTOJ36UOjvxiUOFws_b4_N__gI'
        pilotos = []
        minut01 = ''
        minut02 = ''
        minut03 = ''
        
        if tipo == 'entrada':
            if totalMinutos == 3:
                if totalPilotos == 2:
                    msg = f'⚠️ ATENÇÃO VAMOS ENTRAR ⚠️\n{padrao}\n\n➡️ PILOTOS  🏍  =  {pilotosEntradas[0]} {pilotosEntradas[1]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]} e {minutosEntradas[2]}\n\nLink Corrida: https://bit.ly/Bet365_SpeeDway'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                    maismin = int(minutosEntradas[0]) + 1
                    maismin2 = int(minutosEntradas[1]) + 1
                    maismin3 = int(minutosEntradas[2]) + 1
                    
                    if int(maismin) <= 9:
                        mi1 = f'0{maismin}'
                        minut01 = str(mi1)
                    else:
                        minut01 = str(maismin)
                    
                    if int(maismin2) <= 9:
                        mi2 = f'0{maismin2}'
                        minut02 = str(mi2)
                    else:
                        minut02 = str(maismin2)
                    
                    if int(maismin3) <= 9:
                        mi3 = f'0{maismin3}'
                        minut03 = str(mi3)
                    else:
                        minut03 = str(maismin3)
                                    
                else:
                    msg = f'⚠️ ATENÇÃO VAMOS ENTRAR ⚠️\n{padrao}\n\n➡️ ENTRADA  🏍 = {pilotosEntradas[0]} {pilotosEntradas[1]} {pilotosEntradas[2]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]} e {minutosEntradas[2]}\n\nLink Corrida: https://bit.ly/Bet365_SpeeDway'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                    maismin = int(minutosEntradas[0]) + 1
                    maismin2 = int(minutosEntradas[1]) + 1
                    maismin3 = int(minutosEntradas[2]) + 1
                    
                    if int(maismin) <= 9:
                        mi1 = f'0{maismin}'
                        minut01 = str(mi1)
                    else:
                        minut01 = str(maismin)
                    
                    if int(maismin2) <= 9:
                        mi2 = f'0{maismin2}'
                        minut02 = str(mi2)
                    else:
                        minut02 = str(maismin2)
                    
                    if int(maismin3) <= 9:
                        mi3 = f'0{maismin3}'
                        minut03 = str(mi3)
                    else:
                        minut02 = str(maismin3)                
            else:
                if totalPilotos == 2:
                    msg = f'⚠️ ATENÇÃO VAMOS ENTRAR ⚠️\n{padrao}\n\n➡️ PILOTOS  🏍  =  {pilotosEntradas[0]} {pilotosEntradas[1]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]}\n\nLink Corrida: https://bit.ly/Bet365_SpeeDway'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                    maismin = int(minutosEntradas[0]) + 1
                    maismin2 = int(minutosEntradas[1]) + 1
                    
                    
                    if int(maismin) <= 9:
                        mi1 = f'0{maismin}'
                        minut01 = str(mi1)
                    else:
                        minut01 = str(maismin)
                    
                    if int(maismin2) <= 9:
                        mi2 = f'0{maismin2}'
                        minut02 = str(mi2)
                    else:
                        minut02 = str(maismin2)
                    
                    
                                
                else:
                    msg = f'⚠️ ATENÇÃO VAMOS ENTRAR ⚠️\n{padrao}\n\n➡️ ENTRADA  🏍 = {pilotosEntradas[0]} {pilotosEntradas[1]} {pilotosEntradas[2]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]}\n\nLink Corrida: https://bit.ly/Bet365_SpeeDway'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                    maismin = int(minutosEntradas[0]) + 1
                    maismin2 = int(minutosEntradas[1]) + 1
                    
                    
                    if int(maismin) <= 9:
                        mi1 = f'0{maismin}'
                        minut01 = str(mi1)
                    else:
                        minut01 = str(maismin)
                    
                    if int(maismin2) <= 9:
                        mi2 = f'0{maismin2}'
                        minut02 = str(mi2)
                    else:
                        minut02 = str(maismin2)         
                    
            def send_message(chat_id, msg):
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage', {'chat_id': chat_id, 'text': str(msg)})
            
            
            send_message(chat_id, msg)
            time.sleep(70)
            
        elif tipo == 'win':
            if totalMinutos == 3:
                if totalPilotos == 2:
                    msg = f'✅ PAGA ✅\n\n➡️ PILOTOS   🏍  =  {pilotosEntradas[0]} {pilotosEntradas[1]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]} e {minutosEntradas[2]}\n\nLink Bet365: https://bit.ly/Bet365_SpeeDway\n\n✅✅✅✅✅✅✅✅✅✅✅✅\n\n🏆 {NomePiloto} ✅ Odd: {odd} 🔮: {oddPrevisao} 🤑'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                                    
                else:
                    msg = f'✅ PAGA ✅\n\n➡️ PILOTOS   🏍 = {pilotosEntradas[0]} {pilotosEntradas[1]} {pilotosEntradas[2]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]} e {minutosEntradas[2]}\n\nLink Bet365: https://bit.ly/Bet365_SpeeDway\n\n✅✅✅✅✅✅✅✅✅✅✅✅\n\n🏆 {NomePiloto} ✅ Odd: {odd} 🔮: {oddPrevisao} 🤑'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                                    
            else:
                if totalPilotos == 2:
                    msg = f'✅ PAGA ✅\n\n➡️ PILOTOS   🏍  =  {pilotosEntradas[0]} {pilotosEntradas[1]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]}\n\nLink Bet365: https://bit.ly/Bet365_SpeeDway\n\n✅✅✅✅✅✅✅✅✅✅✅✅\n\n🏆 {NomePiloto} ✅ Odd: {odd} 🔮: {oddPrevisao} 🤑'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                                    
                else:
                    msg = f'✅ PAGA ✅\n\n➡️ PILOTOS   🏍 = {pilotosEntradas[0]} {pilotosEntradas[1]} {pilotosEntradas[2]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]}\n\nLink Bet365: https://bit.ly/Bet365_SpeeDway\n\n✅✅✅✅✅✅✅✅✅✅✅✅\n\n🏆 {NomePiloto} ✅ Odd: {odd} 🔮: {oddPrevisao} 🤑'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                                
            def send_message(chat_id, msg):
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage', {'chat_id': chat_id, 'text': str(msg)})
            send_message(chat_id, msg)
            inicio()
        
        elif tipo == 'loss':
            if totalMinutos == 3:
                if totalPilotos == 2:
                    msg = f'❌ DERROTA ❌\n\n➡️ PILOTOS   🏍  =  {pilotosEntradas[0]} {pilotosEntradas[1]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]} e {minutosEntradas[2]}\n\nLink Bet365: https://bit.ly/Bet365_SpeeDway\n\n❌❌❌\n'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                                    
                else:
                    msg = f'❌ DERROTA ❌\n\n➡️ PILOTOS   🏍 = {pilotosEntradas[0]} {pilotosEntradas[1]} {pilotosEntradas[2]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]} e {minutosEntradas[2]}\n\nLink Bet365: https://bit.ly/Bet365_SpeeDway\n\n❌❌❌\n'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                                    
            else:
                if totalPilotos == 2:
                    msg = f'❌ DERROTA ❌\n\n➡️ PILOTOS   🏍  =  {pilotosEntradas[0]} {pilotosEntradas[1]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]}\n\nLink Bet365: https://bit.ly/Bet365_SpeeDway\n\n❌❌❌\n'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                                    
                else:
                    msg = f'❌ DERROTA ❌\n\n➡️ PILOTOS   🏍 = {pilotosEntradas[0]} {pilotosEntradas[1]} {pilotosEntradas[2]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]}\n\nLink Bet365: https://bit.ly/Bet365_SpeeDway\n\n❌❌❌\n'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                                
            def send_message(chat_id, msg):
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage', {'chat_id': chat_id, 'text': str(msg)})
            send_message(chat_id, msg)
            inicio()
        
        min1 = ''
        min2 = ''
        min3 = ''
        
        corVencedor = ''
        minutos = ''
        oddPrevisao = ''
        previsao = ''
        nomePiloto = ''
        NomePiloto = ''
        odd = ''
        horas = ''
        
        def pegarVencedor():
            
            corVencedor = ''
        
            url = 'https://api.fbtips.com.br/v1/speedway/'

            resp = requests.get(url=url)
            data = resp.json()

            lista_linha1 = []
            ctl1 = -1
            for l1 in data['linhas'][0]['colunas']:
                ctl1 += 1
                try:
                    linha1 = data['linhas'][0]['colunas'][ctl1]['corVencedor']
                except:
                    linha1 = int(data['linhas'][0]['colunas'][ctl1]['minutos'])
                lista_linha1.append(linha1)

            ct = 0
            for c in lista_linha1:
                if type(c) == int:
                    ct += 1
                    if ct == 1:
                        minutoAtual = c    
                            
            coluna = 0
            for l1 in lista_linha1:
                if type(l1) != int:   
                    corVencedor = l1
            return corVencedor        
                                
            
        con = 0
        pilotos = [] 
        coluna = 0
        while True:
            horaSite, minutos = pegarhora()
            now = datetime.now() + timedelta(minutes=1)
            hora = now.strftime('%H:%M')
            horaH = now.strftime('%H')
            horaSinal = f'{horaH}'
            #corVencedor = pegarVencedor()
            
            min1 = f'{str(horaSinal)}:{minut01}'
            min2 = f'{str(horaSinal)}:{minut02}' 
            min3 = f'{str(horaSinal)}:{minut03}'    
            
            print(f'Aguardando resultado: {horaSite} - Hora verificar: {min1}, {min2}, {min3}', end='\r')
            if horaSite == min1 or horaSite == min2 or horaSite == min3:
            
                for i in pilotosEntradas:
                    ct += 1
                    pilotos.append(i)

                for i in data['linhas'][1]['colunas']:
                    coluna += 1
                    try:
                        corVencedor = data['linhas'][0]['colunas'][coluna]['corVencedor']
                        minutos = data['linhas'][0]['colunas'][coluna]['minutos']
                        oddPrevisao = data['linhas'][0]['colunas'][coluna]['oddPrevisao']
                        previsao = data['linhas'][0]['colunas'][coluna]['previsao']
                        nomePiloto = data['linhas'][0]['colunas'][coluna]['nomePiloto']
                        NomePiloto = data['linhas'][0]['colunas'][coluna]['nomePiloto']
                        odd = data['linhas'][0]['colunas'][coluna]['odd']
                        previsaoTricast = data['linhas'][0]['colunas'][coluna]['previsaoTricast']
                        
                        if str(minutos) == str(minut01) or str(minutos) == str(minut02) or str(minutos) == str(minut03):
                            at = corVencedor
                            print(f'Minuto: {minutos}\ncorVencedor: {corVencedor}\noddPrevisao: {oddPrevisao}\nprevisao: {previsao}\nNomePiloto: {nomePiloto}\n\n')
                            
                            for c in pilotos:
                                                                    
                                if at == c:
                                    if ct == 2:
                                        msg = f'✅ PAGA ✅\n\n➡️ PILOTOS  🏍  =  {pilotos[0]} {pilotos[1]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]} e {minutosEntradas[2]}\n\nLink Bet365: https://bit.ly/Bet365_SpeeDway\n\n✅✅✅✅✅✅✅✅✅✅✅✅\n\n🏆 {NomePiloto} ✅ Odd: {odd} 🔮: {oddPrevisao} 🤑'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                                    else:
                                        msg = f'✅ PAGA ✅\n\n➡️ PILOTOS  🏍  =  {pilotos[0]} {pilotos[1]} {pilotos[2]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]} e {minutosEntradas[2]}\n\nLink Bet365: https://bit.ly/Bet365_SpeeDway\n\n✅✅✅✅✅✅✅✅✅✅✅✅\n\n🏆 {NomePiloto} ✅ Odd: {odd} 🔮: {oddPrevisao} 🤑'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                                    
                                    EN = False
                                    
                                    def send_message(chat_id, msg):
                                        requests.post(f'https://api.telegram.org/bot{token}/sendMessage', {'chat_id': chat_id, 'text': str(msg)})
                                    send_message(chat_id, msg)
                                    inicio()
                                    break

                            
                                    
                                        
                    except:
                        corVencedor = data['linhas'][0]['colunas'][coluna]['minutos']
                            
            
                
    # ===========================================
    # LINHA 01
    lista_linha1 = []
    ctl1 = -1
    for l1 in data['linhas'][0]['colunas']:
        ctl1 += 1
        try:
            linha1 = data['linhas'][0]['colunas'][ctl1]['corVencedor']
        except:
            linha1 = int(data['linhas'][0]['colunas'][ctl1]['minutos'])
        lista_linha1.append(linha1)
    # ==========================================
    # LINHA 02
    lista_linha2 = []
    ctl2 = -1
    for l2 in data['linhas'][1]['colunas']:
        ctl2 += 1
        try:
            linha2 = data['linhas'][1]['colunas'][ctl2]['corVencedor']
        except:
            linha2 = int(data['linhas'][1]['colunas'][ctl2]['minutos'])
        lista_linha2.append(linha2)
    # ==========================================
    # LINHA 03
    lista_linha3 = []
    ctl3 = -1
    for l3 in data['linhas'][2]['colunas']:
        ctl3 += 1
        try:
            linha3 = data['linhas'][2]['colunas'][ctl3]['corVencedor']
        except:
            linha3 = int(data['linhas'][2]['colunas'][ctl3]['minutos'])
        lista_linha3.append(linha3)
    # =========================================
    
    # SABER MINUTO ATUAL
    ct = 0
    minutoAtual = 0
    for c in lista_linha1:
        if type(c) == int:
            ct += 1
            if ct == 1:
                minutoAtual = c
    if minutoAtual >= 52 and minutoAtual <= 58:
        minutoAtual = 55    
    # ========================================
    
    # PEGAR COLUNA ATUAL E PULAR MAIS UMA
    proxima_coluna = pegar_coluna(minutoAtual)+1
    EntradaInicial_minuto = minutoAtual+3
    Entrada_coluna = proxima_coluna
    # =======================================
    
    # OBTER PADRAO, ENTRADA E DEFINIR PILOTOS
    padrao, entrada, linha = verifivar_padrao(lista_linha1, lista_linha2, lista_linha3, Entrada_coluna)
    minutosEntradas = []
    pilotosEntradas = []
    totalPilotos = 0
    totalMinutos = 0
    tipo = 'entrada' 
    coluna = 0
    print(data['linhas'][0]['colunas'][0])
    
        
        
    if padrao != '' and entrada != '' and linha != '':
        if linha:
            if minutoAtual == 55:
                minutosEntradas.append(minutoAtual)
                minutosEntradas.append(minutoAtual+3)
            else:
                minutosEntradas.append(minutoAtual)
                minutosEntradas.append(minutoAtual+3)
                minutosEntradas.append(minutoAtual+6)
        else:
            if minutoAtual == 55:
                minutosEntradas.append(EntradaInicial_minuto)
                minutosEntradas.append(EntradaInicial_minuto+3)
            else:
                minutosEntradas.append(EntradaInicial_minuto)
                minutosEntradas.append(EntradaInicial_minuto+3)
                minutosEntradas.append(EntradaInicial_minuto+6)   
        
        for piloto in entrada:
            totalPilotos += 1
            pilotosEntradas.append(piloto)
        for min in minutosEntradas:
            totalMinutos += 1
                
        # FAZENDO A ENTRADA / SINAL
        #telegram(padrao, pilotosEntradas, minutosEntradas, totalPilotos, totalMinutos, tipo, lista_linha1)
        res = {'padrao':padrao,'pilotosEntradas':pilotosEntradas, 'minutosEntradas':minutosEntradas, 'totalPilotos':totalPilotos, 'totalMinutos':totalMinutos}
        return res
            
    else:
        res = {'padrao':'Sem dados, no momento. Tente novamente na proxima corrida','pilotosEntradas':'', 'minutosEntradas':'', 'totalPilotos':'', 'totalMinutos':''}
        return res

    

if __name__ == '__main__':
    app.run(debug=True)
