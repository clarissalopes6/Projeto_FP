import os
os.system("cls")

treinos = {}
competicao = {}
meta_distancia = 0
meta_tempo = 0

def salvar_arquivo():
    with open('treinos.txt', 'a') as arquivo:
        for numero, dados in treinos.items():
            arquivo.write(f"{numero},{dados['data']},{dados['distancia']},{dados['tempo']},{dados['localizacao']},{dados['clima']}\n")

    with open('competicao.txt', 'a') as arquivo:
        for numero, dados in competicao.items():
            arquivo.write(f"{numero},{dados['data']},{dados['distancia']},{dados['tempo']},{dados['localizacao']},{dados['clima']}\n")

def carrega_dados_treinos():
    treinos = {}

    try:
        with open('treinos.txt', 'r') as arquivo:
            for linha in arquivo:
                if not linha.strip():
                    continue
                dados = linha.strip().split(',')
                try:
                    numero = int(dados[0])
                except ValueError:
                    print(f"Valor inválido ignorado: {dados[0]}")
                    continue

                treinos[numero] = {
                    'data': dados[1],
                    'distancia': float(dados[2]),
                    'tempo': float(dados[3]),
                    'localizacao': dados[4],
                    'clima': dados[5]
                }

        for numero, dados in treinos.items():
            print(f"Treino {numero}:")
            for k, v in dados.items():
                print(f"{k}: {v}", end=" | ")
            print()

    except FileNotFoundError:
        pass


def carrega_dados_competicao():
    competicao = {}  

    try:
        with open('competicao.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                numero = int(dados[0])
                competicao[numero] = {
                    'data': dados[1],
                    'distancia': float(dados[2]),
                    'tempo': float(dados[3]),
                    'localizacao': dados[4],
                    'clima': dados[5]
                }

            for numero, dados in competicao.items():
                print(f"Competição {numero}:")
                for k, v in dados.items():
                    print(f"{k}: {v}", end=" | ")
                print()  

    except FileNotFoundError:
        pass


import random
def treino_aleatorio():
    try:
        with open("treinos.txt", "r",encoding="utf8") as arquivo:
            treinos_lista = arquivo.readlines()
            treino_aleatorio = random.choice(treinos_lista)
            print(f"\nSugestão de treino: \n{treino_aleatorio}")
    except FileNotFoundError:
        print("Arquivo 'treinos.txt' não encontrado.")
   
def excluir_treino():
    nu = int(input("\nDigite o número do treino que deseja excluir:"))
    if nu in treinos:
        treinos.pop(nu)
        print(f"\nTreino {nu} excluído com sucesso!")
        with open('treinos.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        with open('treinos.txt', 'w') as arquivo:
            for linha in linhas:
                dados = linha.strip().split(',')
                numero = int(dados[0])
                if numero != nu:  
                    arquivo.write(linha)
        print(f"\nArquivo 'treinos.txt' foi atualizado sem o treino {nu}.")
    else:
        print("\nTreino não encontrado.")

def excluir_competicao():
    nu = int(input("\nDigite o número da competição que deseja excluir:"))
    if nu in competicao:
        competicao.pop(nu)
        print(f"\nCompetição {nu} excluída com sucesso.")
        with open('competicao.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        with open('competicao.txt', 'w') as arquivo:
            for linha in linhas:
                dados = linha.strip().split(',')
                numero = int(dados[0])
                if numero != nu:  
                    arquivo.write(linha)
        print(f"\nArquivo 'competicao.txt' foi atualizado sem a competição {nu}.")
    else:
        print("\nCompetição não encontrada.")

def filtro_treinos_comp(tipo):
    filtro = input("\nDeseja filtrar por 'distância' ou 'tempo'? ").lower()
   
   
    if filtro not in ['distancia', 'tempo']:
        print("\nOpção de filtro inválida!")
        return

    try:
        valor = float(input(f"\nDigite o valor para filtrar por {filtro}: "))
    except ValueError:
        print("\nValor inválido para comparação!")
        return

    treinos = {}
    competicao = {}

    try:
        with open('competicao.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                numero = int(dados[0])
                competicao[numero] = {
                    'data': dados[1],
                    'distancia': float(dados[2]),
                    'tempo': float(dados[3]),
                    'localizacao': dados[4],
                    'clima': dados[5]
                }
    except FileNotFoundError:
        print("\nArquivo 'competicao.txt' não encontrado.")

    try:
        with open('treinos.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                numero = int(dados[0])
                treinos[numero] = {
                    'data': dados[1],
                    'distancia': float(dados[2]),
                    'tempo': float(dados[3]),
                    'localizacao': dados[4],
                    'clima': dados[5]
                }
    except FileNotFoundError:
        print("\nArquivo 'treinos.txt' não encontrado.")

    if tipo == "treino":
        lista = treinos
    elif tipo == "competição":
        lista = competicao
    else:
        print("\nTipo inválido! Use 'treino' ou 'competição'.")
        return

    cont=0
    print(f"\n{tipo} filtrados:")
    for numero, dados in lista.items():
        if filtro == 'distancia' and dados['distancia'] == valor:
            print(f"\nNúmero: {numero}, Data: {dados['data']}, Distância: {dados['distancia']} km, Tempo: {dados['tempo']} minutos, Localização: {dados['localizacao']}, Clima: {dados['clima']}")
            cont+=1
        elif filtro == 'tempo' and dados['tempo'] == valor:
            print(f"\nNúmero: {numero}, Data: {dados['data']}, Distância: {dados['distancia']} km, Tempo: {dados['tempo']} minutos, Localização: {dados['localizacao']}, Clima: {dados['clima']}")
            cont+=1
    if cont==0:
        print("\nNenhum item encontrado com o valor especificado.")
   
def def_metas():
    global meta_distancia, meta_tempo
    meta_distancia = float(input("\nDigite a distância total que deseja correr (em km): "))
    meta_tempo = float(input("\nDigite o tempo total que deseja correr (em minutos): "))
    print(f"\nSua meta é correr {meta_distancia} km em {meta_tempo} minutos.")
   
    with open('metas.txt', 'a') as arquivo:
     arquivo.write(f"{meta_distancia},{meta_tempo}\n")


def carrega_metas():
    metas = []
    try:
        with open('metas.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                distancia = float(dados[0])
                tempo = float(dados[1])
                metas.append({'distancia': distancia, 'tempo': tempo})
    except FileNotFoundError:
        pass
    return metas    
   
def comparar_com_metas(treino, metas):
     meta_atingida = False
   
     for meta in metas:
        if treino['distancia'] >= meta['distancia'] and treino['tempo'] <= meta['tempo']:
            if not meta_atingida:
                print(f"\nParabéns! Você atingiu a(s) seguinte(s) meta(s):")
                meta_atingida = True
            print(f"\nMeta: Correr {meta['distancia']} km em até {meta['tempo']} minutos. Você fez {treino['distancia']} km em {treino['tempo']} minutos.")
   
     if not meta_atingida:
        print(f"\nTreino não atingiu nenhuma das metas.")


def calculo_calorico():
   if len(treinos) == 0:
       print("\nNão há treinos salvos para calcular o seu gasto calórico. Por favor, registre o(s) treino(s) primeiro. \n")
       return
   else:
       print("\nTreinos Registrados: \n")
       for numero, dados in treinos.items():
           print(f"Nº{numero} \nData: {dados['data']} - Distância: {dados['distancia']} km - Tempo{dados['tempo']} minutos\n")
           try:
               num_treino = int(input("\nDigite o número do treino que deseja calcular: \n"))
               if num_treino not in treinos:
                   print("\nTreino não encontrado. \n")
                   return
           except ValueError:
               print("\nEntrada inválida.\n")
               return
       treino_escolhido = treinos[num_treino]
       peso = float(input("\nDigite o seu peso [kg]: "))
       horas_treino = treino_escolhido['tempo']/60
       velocidade = treino_escolhido['distancia']/horas_treino
       if velocidade < 6:
           MET = 3.6
       elif 6 <= velocidade <=10:
           MET = 7
       else:
           MET = 12
       calorias = MET*peso*horas_treino
       print(f"\nGasto Calórico estimado: {calorias} kcal\n")
       input("\nPressione enter para voltar para o menu\n")


while True:
    opcao = int(input("\n1-Treino \n2-Competição \n3-Sugestão de Treino \n4-Filtro \n5-Metas \n6-Gasto calórico\n \nDigite o número da opção desejada:"))
    if opcao not in [1, 2, 3, 4, 5,6]:
        print("\nOpção inválida")
        continue

    if opcao == 1:
        opcao2 = int(input("\n1-Adicionar \n2-Visualizar \n3-Atualizar \n4-Excluir\n \nDigite o número da opção desejada:"))
        if opcao2 not in [1, 2, 3, 4]:
            print("\nOpção inválida")
            continue

        if opcao2 ==1:
            numero = int(input("\nDigite o número do treino:"))
            data = input("Digite a data do treino:")
            distancia = float(input("Digite a distância percorrida em Km:"))
            tempo = float(input("Digite o tempo do treino em minutos:"))
            localizacao = input("Digite a localização do treino:")
            clima = input("Digite as condições climáticas do treino:")
            treinos[numero] = {'data': data,'distancia': distancia,'tempo': tempo,'localizacao': localizacao,'clima': clima}
            metas = carrega_metas()  
            comparar_com_metas(treinos[numero], metas)  
            salvar_arquivo()

        elif opcao2 == 2:
            carrega_dados_treinos()

        elif opcao2==3:
            n = int(input("\nDigite o número do treino que deseja atualizar:"))
            atualizar = int(input("\n1-Data \n2-Distância \n3-Tempo \n4-Localização \n5-Clima \nDigite o número da opção que deseja atualizar:"))
            if n in treinos:
                if atualizar == 1:
                    novadata = input("\nDigite a data atualizada:")
                    treinos[n]['data'] = novadata
                elif atualizar ==2:
                    novadistancia = float(input("\nDigite a distância atualizada:"))
                    treinos[n]['distancia']= novadistancia
                elif atualizar == 3:
                    novotempo = float(input("\nDigite o tempo atualizado:"))
                    treinos[n]['tempo'] = novotempo
                elif atualizar ==4:
                    novalocalizacao = input("\nDigite a localização atualizada:")
                    treinos[n]['localizacao'] = novalocalizacao
                elif atualizar ==5:
                    novoclima = input("\nDigite o clima atualizado:")
                    treinos[n]['clima'] = novoclima
                comparar_com_metas(treinos[numero])
                salvar_arquivo()

        elif opcao2 == 4:
            excluir_treino()

    elif opcao == 2:
        opcao3 = int(input("\n1-Adicionar \n2-Visualizar \n3-Atualizar \n4-Excluir\n \nDigite o número da opção desejada:"))

        if opcao3 not in [1, 2, 3, 4]:
            print("\nOpção inválida")
            continue

        if opcao3 ==1:
            numero = int(input("\nDigite o número da competição:"))
            data = input("\nDigite a data da competição:")
            distancia = float(input("\nDigite a distância percorrida em Km:"))
            tempo =float(input("\nDigite o tempo da competição em minutos:"))
            localizacao = input("\nDigite a localização da competição:")
            clima = input("\nDigite as condições climáticas da competição:")
            competicao[numero] = {'data': data,'distancia': distancia,'tempo': tempo,'localizacao': localizacao,'clima': clima}
            salvar_arquivo()
        elif opcao3 == 2:
            carrega_dados_competicao()
        elif opcao3==3:
            n = int(input("\nDigite o número da competição que deseja atualizar:"))
            atualizar = int(input("1-Data \n2-Distância \n3-Tempo \n4-Localização \n5-Clima \nDigite o número da opção que deseja atualizar:"))
            if n in competicao:
                if atualizar == 1:
                    novadata = input("\nDigite a data atualizada:")
                    competicao[n]['data'] = novadata
                elif atualizar ==2:
                    novadistancia = float(input("\nDigite a distância atualizada:"))
                    competicao[n]['distancia']= novadistancia
                elif atualizar == 3:
                    novotempo = float(input("\nDigite o tempo atualizado:"))
                    competicao[n]['tempo'] = novotempo
                elif atualizar ==4:
                    novalocalizacao = input("\nDigite a localização atualizada:")
                    competicao[n] ['localizacao']= novalocalizacao
                elif atualizar ==5:
                    novoclima = input("\nDigite o clima atualizado:")
                    competicao[n]['clima'] = novoclima
                salvar_arquivo()
        elif opcao3 == 4:  
            excluir_competicao()

    elif opcao == 3:
        treino_aleatorio()
        
    elif opcao == 4:
        tipo = input("\ntreino \ncompetição \nDigite a opção desejada:").lower()
        if tipo == "treino" or tipo=="competição":
            filtro_treinos_comp(tipo)
        else:
            print("\nOpção inválida")
    elif opcao == 5:
        def_metas()
    elif opcao == 6:
        calculo_calorico()