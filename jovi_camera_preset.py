# jovi camera preset
# projeto academico: sistema inteligente de presets de camera


# lista para guardar os presets criados
presets_salvos = []


def exibir_voltar():
    print(f"\n  [ 0 ] voltar")
    print(f"  " + "." * 15)


def exibir_separador():
    print("=" * 55)


def exibir_cabecalho(titulo):
    exibir_separador()
    print(f"  {titulo}")
    exibir_separador()


def ler_opcao(pergunta, opcoes):
    # pede para o usuario escolher uma opcao valida
    # aceita 0 para voltar ao menu principal
    while True:
        exibir_voltar()
        texto = " / ".join(opcoes)
        resposta = input(f"  {pergunta} ({texto}): ")
        resposta = resposta.strip().lower()

        if resposta == "0":
            return "0"

        if resposta in opcoes:
            return resposta

        print(f"  opcao invalida! escolha entre: {texto}")


def ler_numero(pergunta, minimo, maximo):
    # pede para o usuario digitar um numero
    # digite 0 para voltar ao menu principal
    while True:
        exibir_voltar()
        entrada = input(f"  {pergunta} ({minimo}-{maximo}): ")
        entrada = entrada.strip()

        if entrada == "0":
            return 0

        try:
            valor = int(entrada)
            if valor >= minimo and valor <= maximo:
                return valor
            else:
                print(f"  digite um numero entre {minimo} e {maximo}.")
        except ValueError:
            print("  entrada invalida! digite apenas numeros.")


def ler_numero_menu(pergunta, minimo, maximo):
    # pede um numero para o menu principal
    while True:
        try:
            valor = int(input(f"  {pergunta} ({minimo}-{maximo}): "))
            if valor >= minimo and valor <= maximo:
                return valor
            else:
                print(f"  digite um numero entre {minimo} e {maximo}.")
        except ValueError:
            print("  entrada invalida! digite apenas numeros.")


def gerar_configuracoes(ambiente, objetivo, experiencia, visual):
    # cria as configuracoes da camera com base nas respostas do questionario

    # valores iniciais
    brilho = 50
    contraste = 50
    saturacao = 50
    hdr = "Desligado"
    modo_noturno = "Desligado"
    estabilizacao = "Desligada"

    # ajustes pelo ambiente
    if ambiente == "interno":
        brilho = 65
        contraste = 55
    elif ambiente == "externo":
        brilho = 45
        contraste = 50
        hdr = "Ligado"
    elif ambiente == "noturno":
        brilho = 80
        contraste = 40
        modo_noturno = "Ligado"
        hdr = "Ligado"

    # ajustes pelo objetivo
    if objetivo == "selfie":
        saturacao = 60
        estabilizacao = "Ligada"
    elif objetivo == "paisagem":
        saturacao = 70
        hdr = "Ligado"
    elif objetivo == "retrato":
        saturacao = 50
        contraste = 60
    elif objetivo == "movimento":
        estabilizacao = "Ligada"
        brilho = brilho + 10

    # ajustes pela experiencia
    if experiencia == "intermediario":
        brilho = brilho + 5
        contraste = contraste + 5
    elif experiencia == "avancado":
        brilho = brilho + 10
        contraste = contraste + 10
        saturacao = saturacao + 5

    # ajustes pela preferencia visual
    if visual == "cores vivas":
        saturacao = saturacao + 15
        contraste = contraste + 5
    elif visual == "profissional":
        saturacao = saturacao - 5
        contraste = contraste + 10

    # limita os valores
    if brilho > 100:
        brilho = 100
    if brilho < 0:
        brilho = 0
    if contraste > 100:
        contraste = 100
    if contraste < 0:
        contraste = 0
    if saturacao > 100:
        saturacao = 100
    if saturacao < 0:
        saturacao = 0

    # organiza as configuracoes
    configuracoes = {
        "brilho": brilho,
        "contraste": contraste,
        "saturacao": saturacao,
        "hdr": hdr,
        "modo_noturno": modo_noturno,
        "estabilizacao": estabilizacao
    }

    return configuracoes


def exibir_preset(preset):
    # mostra os dados do preset
    print("")
    print(f"  nome: {preset['nome']}")
    print("  respostas do questionario:")
    print(f"     ambiente ......... {preset['ambiente']}")
    print(f"     objetivo ......... {preset['objetivo']}")
    print(f"     experiencia ...... {preset['experiencia']}")
    print(f"     visual ........... {preset['visual']}")
    print("  configuracoes geradas:")
    print(f"     brilho ........... {preset['config']['brilho']}%")
    print(f"     contraste ........ {preset['config']['contraste']}%")
    print(f"     saturacao ........ {preset['config']['saturacao']}%")
    print(f"     hdr .............. {preset['config']['hdr']}")
    print(f"     modo noturno ..... {preset['config']['modo_noturno']}")
    print(f"     estabilizacao .... {preset['config']['estabilizacao']}")


def responder_questionario():
    # faz o questionario e gera o preset automaticamente

    exibir_cabecalho("QUESTIONARIO: GERAR NOVO PRESET")
    print("")

    # pergunta 1: ambiente
    ambiente = ler_opcao("qual e o ambiente da foto?", ["interno", "externo", "noturno"])
    if ambiente == "0":
        print("  voltando ao menu principal...")
        return

    # pergunta 2: objetivo
    objetivo = ler_opcao("qual e o objetivo da foto?", ["selfie", "paisagem", "retrato", "movimento"])
    if objetivo == "0":
        print("  voltando ao menu principal...")
        return

    # pergunta 3: experiencia
    experiencia = ler_opcao("qual seu nivel de experiencia?", ["iniciante", "intermediario", "avancado"])
    if experiencia == "0":
        print("  voltando ao menu principal...")
        return

    # pergunta 4: preferencia visual
    visual = ler_opcao("qual sua preferencia visual?", ["cores vivas", "natural", "profissional"])
    if visual == "0":
        print("  voltando ao menu principal...")
        return

    # gera as configuracoes
    config = gerar_configuracoes(ambiente, objetivo, experiencia, visual)

    # pede um nome para o preset
    exibir_voltar()
    nome = input("  de um nome para este preset: ").strip()
    if nome == "0":
        print("  voltando ao menu principal...")
        return
    if nome == "":
        nome = f"Preset {len(presets_salvos) + 1}"

    # monta o preset
    preset = {
        "nome": nome,
        "ambiente": ambiente,
        "objetivo": objetivo,
        "experiencia": experiencia,
        "visual": visual,
        "config": config
    }

    # salva na lista
    presets_salvos.append(preset)

    # mostra o resultado
    print("")
    exibir_separador()
    print("  preset gerado e salvo com sucesso!")
    exibir_preset(preset)
    exibir_separador()


def criar_preset_manual():
    # permite criar um preset definindo cada valor manualmente

    exibir_cabecalho("CRIAR PRESET MANUALMENTE")
    print("")

    # pede o nome
    exibir_voltar()
    nome = input("  de um nome para este preset: ").strip()
    if nome == "0":
        print("  voltando ao menu principal...")
        return
    if nome == "":
        nome = "Preset " + str(len(presets_salvos) + 1)

    print("")
    print("  defina cada configuracao da camera:")
    print("")

    # pede os valores numericos
    brilho = ler_numero("brilho", 1, 100)
    if brilho == 0:
        print("  voltando ao menu principal...")
        return

    contraste = ler_numero("contraste", 1, 100)
    if contraste == 0:
        print("  voltando ao menu principal...")
        return

    saturacao = ler_numero("saturacao", 1, 100)
    if saturacao == 0:
        print("  voltando ao menu principal...")
        return

    # pede as opcoes
    hdr = ler_opcao("hdr", ["ligado", "desligado"])
    if hdr == "0":
        print("  voltando ao menu principal...")
        return

    modo_noturno = ler_opcao("modo noturno", ["ligado", "desligado"])
    if modo_noturno == "0":
        print("  voltando ao menu principal...")
        return

    estabilizacao = ler_opcao("estabilizacao", ["ligada", "desligada"])
    if estabilizacao == "0":
        print("  voltando ao menu principal...")
        return

    # monta as configuracoes
    config = {
        "brilho": brilho,
        "contraste": contraste,
        "saturacao": saturacao,
        "hdr": hdr.capitalize(),
        "modo_noturno": modo_noturno.capitalize(),
        "estabilizacao": estabilizacao.capitalize()
    }

    # monta o preset
    preset = {
        "nome": nome,
        "ambiente": "manual",
        "objetivo": "manual",
        "experiencia": "manual",
        "visual": "manual",
        "config": config
    }

    # salva na lista
    presets_salvos.append(preset)

    # mostra o resultado
    print("")
    exibir_separador()
    print("  preset manual criado e salvo com sucesso!")
    exibir_preset(preset)
    exibir_separador()


def editar_preset():
    # permite editar as configuracoes de um preset salvo

    exibir_cabecalho("EDITAR PRESET")

    # verifica se tem presets salvos
    if len(presets_salvos) == 0:
        print("")
        print("  nenhum preset salvo para editar.")
        print("  use a opcao 1 do menu para criar um preset.")
        print("")
        exibir_separador()
        return

    # mostra os presets disponiveis
    print("")
    print("    0. voltar ao menu principal")
    print("  presets disponiveis:")
    for i in range(len(presets_salvos)):
        print(f"    {i + 1}. {presets_salvos[i]['nome']}")

    # pede qual preset quer editar
    indice = ler_numero_menu("escolha o numero do preset", 0, len(presets_salvos))

    # verifica se quer voltar
    if indice == 0:
        print("  voltando ao menu principal...")
        return

    # pega o preset escolhido
    preset = presets_salvos[indice - 1]

    print("")
    print(f"  editando: {preset['nome']}")
    print("  (valores atuais mostrados entre colchetes)")
    print("")

    # loop do menu de edicao
    while True:
        print("  o que deseja editar?")
        print("    0. voltar ao menu principal")
        print(f"    1. brilho ........... [{preset['config']['brilho']}%]")
        print(f"    2. contraste ........ [{preset['config']['contraste']}%]")
        print(f"    3. saturacao ........ [{preset['config']['saturacao']}%]")
        print(f"    4. hdr .............. [{preset['config']['hdr']}]")
        print(f"    5. modo noturno ..... [{preset['config']['modo_noturno']}]")
        print(f"    6. estabilizacao .... [{preset['config']['estabilizacao']}]")
        print("")

        opcao = ler_numero_menu("escolha uma opcao", 0, 6)

        if opcao == 1:
            novo = ler_numero_menu("novo valor de brilho", 0, 100)
            preset["config"]["brilho"] = novo
            print(f"  brilho alterado para {novo}%")
            print("")

        elif opcao == 2:
            novo = ler_numero_menu("novo valor de contraste", 0, 100)
            preset["config"]["contraste"] = novo
            print(f"  contraste alterado para {novo}%")
            print("")

        elif opcao == 3:
            novo = ler_numero_menu("novo valor de saturacao", 0, 100)
            preset["config"]["saturacao"] = novo
            print(f"  saturacao alterada para {novo}%")
            print("")

        elif opcao == 4:
            valor = ler_opcao("hdr", ["ligado", "desligado"])
            if valor != "0":
                preset["config"]["hdr"] = valor.capitalize()
                print(f"  hdr alterado para {valor.capitalize()}")
                print("")

        elif opcao == 5:
            valor = ler_opcao("modo noturno", ["ligado", "desligado"])
            if valor != "0":
                preset["config"]["modo_noturno"] = valor.capitalize()
                print(f"  modo noturno alterado para {valor.capitalize()}")
                print("")

        elif opcao == 6:
            valor = ler_opcao("estabilizacao", ["ligada", "desligada"])
            if valor != "0":
                preset["config"]["estabilizacao"] = valor.capitalize()
                print(f"  estabilizacao alterada para {valor.capitalize()}")
                print("")

        elif opcao == 0:
            break

    # mostra o preset atualizado
    print("")
    exibir_separador()
    print("  preset atualizado:")
    exibir_preset(preset)
    exibir_separador()


def exibir_menu():
    # mostra o menu principal na tela
    print("")
    exibir_separador()
    print("  JOVI CAMERA:  PRESET")
    exibir_separador()
    print("  0. sair do programa")
    print("  1. responder questionario e gerar preset")
    print("  2. criar preset manualmente")
    print("  3. editar preset salvo")
    exibir_separador()


def main():
    # funcao principal do programa

    # mensagem de boas vindas
    print("")
    exibir_separador()
    print("  bem vindo ao jovi camera  preset!")
    print("  configure sua camera de forma inteligente.")
    exibir_separador()

    # loop principal
    while True:
        exibir_menu()
        opcao = ler_numero_menu("escolha uma opcao", 0, 3)

        if opcao == 1:
            responder_questionario()

        elif opcao == 2:
            criar_preset_manual()

        elif opcao == 3:
            editar_preset()

        elif opcao == 0:
            print("")
            exibir_separador()
            print("  obrigado por usar o jovi camera  preset!")
            print("  ate a proxima!")
            exibir_separador()
            print("")
            break


if __name__ == "__main__":
    main()
