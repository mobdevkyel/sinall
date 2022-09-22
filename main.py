from flask import Flask, render_template, request, jsonify
import requests
import json
from time import time, sleep
from datetime import datetime, timedelta
import os, time, sys, json, re
import string
from random import choice

app = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    #return "meu primeiro site"
    return ("homepage.html")

@app.route("/speedway")
def geral():
    now = datetime.now() + timedelta(hours=3)
    now2 = datetime.now() - timedelta(hours=3)
    data_final = now2.strftime("%d/%m/%Y")
    hor = now.strftime('%M') 
    hor2 = now.strftime('%H:%M:%S')    
    if int(hor) <= 4 and int(hor) > 49:
        res = {'retorno':'Sem dados no momento'}
        return res
    else:
        def dados():
            url = 'https://api.fbtips.com.br/v1/speedway/'
            resp = requests.get(url=url)
            data = resp.json()
            return jsonify(data)
            return data
        # ==========================================
        
        # HORARIO DO SITE
        data = dados()
        #DataHoraSite = data['lastUpdated']
        #d = DataHoraSite.split(' ')
        #dd = d[1].split(':')
        #HaraSite = f'{dd[0]}:{dd[1]}'
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
        
        def checagem():
            
            try:
                url = 'https://api.fbtips.com.br/v1/speedway/'

                resp = requests.get(url=url)
                data = resp.json()

                lista_linha1 = []
                lista = []
                ctl1 = -1
                cores = []
                minutos = []
                ProximoMinuto = 0
                MinutoAnterior = 0
                UltimaCor = ''
                
                for l1 in data['linhas'][0]['colunas']:
                    ctl1 += 1
                    try:
                        linha1 = data['linhas'][0]['colunas'][ctl1]['corVencedor']
                        lista_linha1.append(linha1)
                    except:
                        linha1 = int(data['linhas'][0]['colunas'][ctl1]['minutos'])
                        lista_linha1.append(linha1)
                
                        
                for item in lista_linha1:
                    if type(item) == int:
                        minutos.append(item)     
                    elif type(item) != int:
                        cores.append(item)    
                    else:
                        cores = []
                        minutos = []    
                
                if  cores != [] and minutos != []:
                    ProximoMinuto = int(minutos[0])
                    MinutoAnterior = int(minutos[0]-3)
                    UltimaCor = str(cores[-1])
                    if ProximoMinuto == 1:
                        MinutoAnterior = 58
                    
                    return MinutoAnterior, UltimaCor, ProximoMinuto 
                else:
                    return 0, '', 0            
            except:
                time.sleep(2)
                MinutoAnterior, UltimaCor, ProximoMinuto = checagem()
                return MinutoAnterior, UltimaCor, ProximoMinuto
                
        def resultados():
            url = 'https://api.fbtips.com.br/v1/speedway/'
            resp = requests.get(url=url)
            data = resp.json()
            listageral = []
            coluna = 0
            lista_linha1 = []
            for i in data['linhas'][0]['colunas']:
                coluna += 1
                listageral.append(i)
                
            MinutoAnterior, UltimaCor, ProximoMinuto = checagem()
            cool = pegar_coluna(int(MinutoAnterior))
            
            corVencedor = listageral[cool]['corVencedor']
            minutos = listageral[cool]['minutos']
            oddPrevisao = listageral[cool]['oddPrevisao']
            previsao = listageral[cool]['previsao']
            nomePiloto = listageral[cool]['nomePiloto']
            odd = listageral[cool]['odd']
            #previsaoTricast = listageral[cool]['previsaoTricast']


            return str(corVencedor), str(odd), str(minutos), str(oddPrevisao), str(previsao), str(nomePiloto), str(odd)
        
        def telegram(padrao, pilotosEntradas, minutosEntradas, totalPilotos, totalMinutos, tipo, lista_linha1):
            global totalApostas
            global Par_Alto
            global Par_AltoD
            global Par_Baixo
            global Par_BaixoD
            global Par_Esquerdo
            global Par_EsquerdoD
            global Par_Direito
            global Par_DireitoD
            global Diagonal_Direita
            global Diagonal_DireitaD
            global Diagonal_Esquerda
            global Diagonal_EsquerdaD
            global Diagonal_dupla
            global Diagonal_duplaD
            global Linha
            global LinhaD
            global hora
            global win
            global loss
            global acertos
            global erros
            global maxwin
            global maxloss
            global ultimowin
            global ultimoloss
            global wing1
            global wing2
            global wing3
            global listagales
            
            os.system('cls' if os.name == 'nt' else 'clear')
                
            #"-1001491918280" arb key:1354435258:AAFHjsNdiIXAa6mjqn_b5WvrWEIGNBqzMVw
            # -1001660958039 5779647627:AAHiu073fuTOJ36UOjvxiUOFws_b4_N__gI
                        
            chat_id = "-1001660958039"
            token = '5779647627:AAHiu073fuTOJ36UOjvxiUOFws_b4_N__gI'
            pilotos = []
            minut01 = ''
            minut02 = ''
            minut03 = ''
            mi1 = ''
            mi2 = ''
            mi3 = ''
            par = 0
            parD = 0
            
            if padrao == 'Par Alto':
                par = Par_Alto
                parD = Par_AltoD
            elif padrao == 'Par Baixo':
                par = Par_Baixo
                parD = Par_BaixoD
            elif padrao == 'Par Esquerdo':
                par = Par_Esquerdo
                parD = Par_EsquerdoD
            elif padrao == 'Par Direito':
                par = Par_Direito
                parD = Par_DireitoD
            elif padrao == 'Diagonal Direita':
                par = Diagonal_Direita
                parD = Diagonal_DireitaD
            elif padrao == 'Diagonal Esquerda':
                par = Diagonal_Esquerda
                parD = Diagonal_EsquerdaD
            elif padrao == 'Diagonal dupla':
                par = Diagonal_dupla
                parD = Diagonal_duplaD
            elif padrao == 'Linha':
                par = Linha
                parD = LinhaD
                
            contagemgale = len(listaMinutos)
            contagemgale = int(contagemgale)     
            
            
            if tipo == 'entrada':
                if totalMinutos == 3:
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
                        
                    if totalPilotos == 2:
                                            
                        msg = f'🚨 ATENÇÃO NOVA ENTRADA 🚨\n🕰 Ultimo win foi as: {ultimowin}\n🕰 Ultimo loss foi as: {ultimoloss}\n\n🎲 {padrao} - (Total de {par} win e {parD} loss.)\n\n➡️ Pilotos  🏍 🏍  =  {pilotosEntradas[0]} {pilotosEntradas[1]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]} e {minutosEntradas[2]}\n\nLink Corrida: https://bit.ly/Bet365_SpeeDway'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                                    
                    else:
                        
                        msg = f'🚨 ATENÇÃO NOVA ENTRADA 🚨\n🕰 Ultimo win foi as: {ultimowin}\n🕰 Ultimo loss foi as: {ultimoloss}\n\n🎲 {padrao} - (Total de {par} win e {parD} loss.)\n\n➡️ Pilotos  🏍 🏍 🏍 = {pilotosEntradas[0]} {pilotosEntradas[1]} {pilotosEntradas[2]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]} e {minutosEntradas[2]}\n\nLink Corrida: https://bit.ly/Bet365_SpeeDway'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                    
                                    
                else:
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
                        
                    if totalPilotos == 2:
                                            
                        msg = f'⚠️ ATENÇÃO VAMOS ENTRAR ⚠️\n\n🎲 {padrao}\n\n➡️ Pilotos  🏍 🏍  =  {pilotosEntradas[0]} {pilotosEntradas[1]}\n\n⏰ Minutos: {minutosEntradas[0]}, {minutosEntradas[1]}\n\nLink Corrida: https://bit.ly/Bet365_SpeeDway'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                    
                    else:
                                            
                        msg = f'⚠️ ATENÇÃO VAMOS ENTRAR ⚠️\n\n🎲 {padrao}\n\n➡️ Pilotos  🏍 🏍 🏍 = {pilotosEntradas[0]} {pilotosEntradas[1]} {pilotosEntradas[2]}\n\n⏰ Minutos: {mi1} e {mi2}\n\nLink Corrida: https://bit.ly/Bet365_SpeeDway'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                            
                        
                def send_message(chat_id, msg):
                    requests.post(f'https://api.telegram.org/bot{token}/sendMessage', {'chat_id': chat_id, 'text': str(msg)})
                
                
                send_message(chat_id, msg)
                #send_message(chat_id, '🔅 DICA: ANTES DE APOSTAR AVALIEM SE AS ODDS SÃO JUSTAS, DEPENDENDO DAS ODDS PODE NAO COMPENSAR FAZER GALE!\nhttps://calculadoradedutching.com/')
                            
            elif tipo == 'win':
                corVencedor, odd, minutos, oddPrevisao, previsao, NomePiloto, odd = resultados()
                totalApostas += 1
                win += 1
                acertos += 1
                erros = 0
                
                if padrao == 'Par Alto': 
                    Par_Alto += 1
                elif padrao == 'Par Baixo':
                    Par_Baixo += 1
                elif padrao == 'Par Esquerdo':
                    Par_Esquerdo += 1
                elif padrao == 'Par Direito':
                    Par_Direito += 1
                elif padrao == 'Diagonal Direita':
                    Diagonal_Direita += 1
                elif padrao == 'Diagonal Esquerda':
                    Diagonal_Esquerda += 1
                elif padrao == 'Diagonal dupla':
                    Diagonal_dupla += 1
                elif padrao == 'Linha':
                    Linha += 1
                    
                
                #total_padroes = (Par_Alto+Par_Baixo+Par_Esquerdo+Par_Direito+Diagonal_Direita+Diagonal_Esquerda+Diagonal_dupla+Linha+Par_AltoD+Par_BaixoD+Par_EsquerdoD+Par_DireitoD+Diagonal_DireitaD+Diagonal_EsquerdaD+Diagonal_duplaD+LinhaD)
                now = datetime.now() - timedelta(hours=3)
                data_final = now.strftime("%d/%m/%Y")
                hor = now.strftime('%M') 
                hor2 = now.strftime('%H:%M')
                ultimowin = hor2 
                
                taxa = (100 *win) / totalApostas
                taxa = round(taxa, 2)
                tatawin = f'{taxa}%'
                maxwin = 0
                maxloss += 1
                
                            
                
                msg = f'✅ PAGA ✅ 👆👆👆👉👉 {corVencedor}\n\n🤑 Sequencia de {acertos} acertos seguidos\n\n🏆 Piloto: {corVencedor} {NomePiloto}\n⏰ Minuto: {minutos}\n✅ Odd: {odd}\n🔮 Odd Previsão: {oddPrevisao}\n\n🏁 Entradas realizadas: {totalApostas}\n🏁 Wins: {win}\n🏁 Loss: {loss}\n➗ Percentual: {tatawin} de vitorias\n\n🚴 PADRÕES WIN/LOSS 🚴\nPar Alto =  {Par_Alto}/{Par_AltoD}\nPar Baixo =  {Par_Baixo}/{Par_BaixoD}\nPar Esquerdo =  {Par_Esquerdo}/{Par_EsquerdoD}\nPar Direito =  {Par_Direito}/{Par_DireitoD}\nDiagonal Direita =  {Diagonal_Direita}/{Diagonal_DireitaD}\nDiagonal Esquerda =  {Diagonal_Esquerda}/{Diagonal_EsquerdaD}\nDiagonal dupla =  {Diagonal_dupla}/{Diagonal_duplaD}\nLinha =  {Linha}/{LinhaD}\n\nLink Bet365: https://bit.ly/Bet365_SpeeDway\nGrupo chat: https://t.me/+OJvL-drMgT00ZmUx\n\n✅✅✅✅✅✅✅✅✅✅✅✅'.replace('verde','🟢').replace('amarelo','🟡').replace('vermelho','🔴').replace('roxo','🟣')
                img = open('paga.png', 'rb')
                def send_message(chat_id, msg):
                    requests.post(f'https://api.telegram.org/bot{token}/sendMessage', {'chat_id': chat_id, 'text': str(msg)})
                    #requests.post(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo=https://raw.githubusercontent.com/mobdevkyel/sinall/main/paga.png')
                
                send_message(chat_id, msg)
                inicio()
            
            elif tipo == 'loss':
                totalApostas += 1
                loss += 1
                acertos = 0
                erros += 1
                maxwin += 1
                maxloss = 0
                
                if padrao == 'Par Alto':
                    Par_AltoD += 1
                elif padrao == 'Par Baixo':
                    Par_BaixoD += 1
                elif padrao == 'Par Esquerdo':
                    Par_EsquerdoD += 1
                elif padrao == 'Par Direito':
                    Par_DireitoD += 1
                elif padrao == 'Diagonal Direita':
                    Diagonal_DireitaD += 1
                elif padrao == 'Diagonal Esquerda':
                    Diagonal_EsquerdaD += 1
                elif padrao == 'Diagonal dupla':
                    Diagonal_duplaD += 1
                elif padrao == 'Linha':
                    LinhaD += 1
                    
                
                now = datetime.now() - timedelta(hours=3)
                data_final = now.strftime("%d/%m/%Y")
                hor = now.strftime('%M') 
                hor2 = now.strftime('%H:%M')
                ultimoloss = hor2 
                
                taxa = (100 *loss) / totalApostas
                taxa = round(taxa, 2)
                tataloss = f'{taxa}%'
                msg = f'❌ DERROTA ❌ 👆👆👆\n😩 Sequencia de {erros} derrotas seguidas\n\nEntradas realizadas: {totalApostas}\n🏁 Wins: {win}\n🏁 Loss: {loss}\n➗ Percentual: {tataloss}  de derrotas'
                                
                def send_message(chat_id, msg):
                    requests.post(f'https://api.telegram.org/bot{token}/sendMessage', {'chat_id': chat_id, 'text': str(msg)})
                
                            
                send_message(chat_id, msg)
                inicio()
            
            now = datetime.now() + timedelta(minutes=1)
            hora = now.strftime('%H:%M')    
            hora = f'{hora}:00'
            listaMinutos = minutosEntradas
            qtminutos = 0
            MinutoAnterior = ''
            UltimaCor = ''
            ProximoMinuto = ''
            MinutoAnterior, UltimaCor, ProximoMinuto = checagem() 
            while True:
                now = datetime.now() + timedelta(minutes=1)
                now2 = datetime.now() + timedelta(minutes=0)
                horaChecagem = now.strftime('%H:%M') 
                horaChecagem2 = now2.strftime('%H:%M:%S')   
                if len(listaMinutos) == 0:
                    telegram(padrao, pilotosEntradas, minutosEntradas, totalPilotos, totalMinutos, 'loss', lista_linha1)
                    break
                else:
                    print(f'Utimo vencedor: {UltimaCor}, do minuto: {MinutoAnterior}, entradas: {listaMinutos} - {horaChecagem2}', end='\r')
                    #print(f'Aguardando resultado: {horaChecagem2} - nova chacagem as: {hora}', end='\r')
                    #MinutoAnterior, UltimaCor, ProximoMinuto = checagem()
                    if int(MinutoAnterior) == int(listaMinutos[0]):
                            
                        listaMinutos.remove(listaMinutos[0])
                        
                        for p in pilotosEntradas:
                            if str(p) == str(UltimaCor):
                                listagales = listaMinutos
                                telegram(padrao, pilotosEntradas, MinutoAnterior, totalPilotos, totalMinutos, 'win', lista_linha1)
                                break
                            else:
                                hora = horaChecagem 
                                MinutoAnterior, UltimaCor, ProximoMinuto = checagem()
                    else:
                        hora = horaChecagem
                        MinutoAnterior, UltimaCor, ProximoMinuto = checagem()
                        pass
                        
                time.sleep(1)
                    
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
        if minutoAtual > 52 and minutoAtual <= 58:
            res = {'retorno':'Sem dados no momento'}
            return res
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
                
            if 3 in minutosEntradas: 
                res = {'retorno':'Sem dados no momento'}
                return res          
            else:
                # FAZENDO A ENTRADA
                telegram(padrao, pilotosEntradas, minutosEntradas, totalPilotos, totalMinutos, tipo, lista_linha1)
                res = {'Padrao':padrao, 'retorno':'ok'}
                return(res)
        

# colocar o site no ar
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

    # servidor do heroku
