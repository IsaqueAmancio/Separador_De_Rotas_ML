


def add_saca():
    qtd_pcts = int(input("qtd de pacotes : "))
    for i in range(qtd_pcts + 1):
        if i != 0:
            lista_pct.append(i)
    qtd_recebida = qtd_pcts
    print(qtd_recebida)

def remover_parada():
    parada = int(input("remover parada:"))
    qtd_pct = lista_pct.count(parada)
    for _ in range(qtd_pct):
        lista_pct.remove(parada)

def add_pct_parada():
    parada_e_qtd = str(input("digite a parada e a quantidade de pacotes: "))
    parada_e_qtd = parada_e_qtd.split(',')
    print(parada_e_qtd)
    parada = int(parada_e_qtd[0])
    qtd = int(parada_e_qtd[1])
    lista_pct.remove(parada)
    for _ in range(qtd):
        lista_pct.append(parada)
        lista_pct.sort()
        print(f"--------------------------------- \n Pacotes: {lista_pct}")
        
def verificar_qtd():
    print(f"QTD RECEBIDO: {qtd_recebida}\nQTD ATUAL: {len(lista_pct)}")

def dist_rota():
    entregador = str(input("entregador: "))
    rota = str(input("pacotes: "))
    match entregador:
        case "carlos":
            rota_carlos = []
            n_rota = rota.split('-')
            ini_rota = int(n_rota[0])
            final_rota = int(n_rota[1])
            print(lista_pct)
            print(ini_rota)
            ini_rota = lista_pct.index(ini_rota)
            final_rota = lista_pct.index(final_rota)
            final_rota += 1 
            for i in range(ini_rota,final_rota):
                rota_carlos.append(lista_pct[i])
            print("------------------------")
            print(rota_carlos)
            print(f"PACOTES CARLOS: {rota_carlos.__len__()}")

        case "samuel":
            rota_samuel = []
            n_rota = rota.split('-')
            ini_rota = int(n_rota[0])
            final_rota = int(n_rota[1])
            print(lista_pct)
            print(ini_rota)
            ini_rota = lista_pct.index(ini_rota)
            final_rota = lista_pct.index(final_rota)
            final_rota += 1 
            for i in range(ini_rota,final_rota):
                rota_samuel.append(lista_pct[i])
            print("------------------------")
            print(rota_samuel)
            print(f"PACOTES SAMUEL: {rota_samuel.__len__()}")

        case "gabriel":
            rota_gabriel = []
            n_rota = rota.split('-')
            ini_rota = int(n_rota[0])
            final_rota = int(n_rota[1])
            print(lista_pct)
            print(ini_rota)
            ini_rota = lista_pct.index(ini_rota)
            final_rota = lista_pct.index(final_rota)
            final_rota += 1 
            for i in range(ini_rota,final_rota):
                rota_gabriel.append(lista_pct[i])
            print("------------------------")
            print(rota_gabriel)
            print(f"PACOTES GABRIEL: {rota_gabriel.__len__()}")

        case "davi":
            rota_davi = []
            n_rota = rota.split('-')
            ini_rota = int(n_rota[0])
            final_rota = int(n_rota[1])
            print(lista_pct)
            print(ini_rota)
            ini_rota = lista_pct.index(ini_rota)
            final_rota = lista_pct.index(final_rota)
            final_rota += 1 
            for i in range(ini_rota,final_rota):
                rota_davi.append(lista_pct[i])
            print("------------------------") 
            print(rota_davi)
            print(f"PACOTES DAVI: {rota_davi.__len__()}")
        
lista_pct = []
lista_pct_copia = []
qtd_recebida = 0
while True:
    print(f"--------------------------------------------------------------------------------------------------------------------------------\n                                                                                       QTD_PCTS: ???")
    print("1 - ADICIONAR SACA")
    print("2 - REMOVER PARADA")
    print("3 - ADICONAR PACOTE NA PARADA")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    menu = int(input("escolha uma opção a cima: "))
    match menu : 
        case 1:
             add_saca()
        case 2:
            remover_parada()
        case 3:
            add_pct_parada()
        case 4:
            verificar_qtd()
add_saca(100)
print(lista_pct)
remover_parada(35)
remover_parada(17)
remover_parada(78)
add_pct_parada(9,2)
add_pct_parada(1,3)
verificar_qtd()
dist_rota()