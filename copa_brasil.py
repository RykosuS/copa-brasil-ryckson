# -*- coding: utf-8 -*-
"""
copa_brasil.py
Um pequeno sistema em linha de comando para consultar e editar um
conjunto de dados sobre a participação do Brasil em Copas do Mundo.

Objetivos das mudanças:
- Melhorar legibilidade (nome das funções, mensagens).
- Adicionar comentários úteis e docstrings explicativas.
- Tratar interrupções (Ctrl+C / EOF) com elegância.
- Manter compatibilidade com a lógica original.
"""

from typing import Dict, Optional, Tuple

# ------------------------------------------------------------
# DADOS (registro do desempenho do Brasil nas Copas do Mundo)
# ------------------------------------------------------------
# Estruturas:
# - copas_brasil: map {ano: dados}, onde dados é dict com chaves:
#   'sede', 'resultado', 'jogos', 'vitorias', 'empates', 'derrotas',
#   'gols_pro', 'gols_contra', 'eliminado_na'
# - artilheiros_brasil: map {nome: {'gols_total': int, 'gols_por_copa': {ano: gols}}}
# - partidas_brasil: map {(ano, fase, adversario): {'placar_brasil', 'placar_adversario', 'resultado'}}
#
# Observação: os dados são estáticos aqui (podem ser carregados de arquivo/BD se desejar).

copas_brasil: Dict[int, Dict] = {
    1950: {"sede": "Brasil", "resultado": "Vice-campeao", "jogos": 6, "vitorias": 4,
           "empates": 1, "derrotas": 1, "gols_pro": 14, "gols_contra": 5,
           "eliminado_na": "Final"},
    1958: {"sede": "Suecia", "resultado": "Campeao", "jogos": 6, "vitorias": 5,
           "empates": 1, "derrotas": 0, "gols_pro": 16, "gols_contra": 4,
           "eliminado_na": None},
    1962: {"sede": "Chile", "resultado": "Campeao", "jogos": 6, "vitorias": 5,
           "empates": 1, "derrotas": 0, "gols_pro": 14, "gols_contra": 5,
           "eliminado_na": None},
    1966: {"sede": "Inglaterra", "resultado": "Oitavas de final", "jogos": 3, "vitorias": 1,
           "empates": 1, "derrotas": 1, "gols_pro": 3, "gols_contra": 2,
           "eliminado_na": "Oitavas de final"},
    1970: {"sede": "Mexico", "resultado": "Campeao", "jogos": 6, "vitorias": 6,
           "empates": 0, "derrotas": 0, "gols_pro": 19, "gols_contra": 7,
           "eliminado_na": None},
    1974: {"sede": "Alemanha Ocidental", "resultado": "Terceira fase", "jogos": 6, "vitorias": 3,
           "empates": 2, "derrotas": 1, "gols_pro": 12, "gols_contra": 6,
           "eliminado_na": "Terceira fase"},
    1978: {"sede": "Argentina", "resultado": "Terceira fase", "jogos": 4, "vitorias": 1,
           "empates": 1, "derrotas": 2, "gols_pro": 3, "gols_contra": 4,
           "eliminado_na": "Terceira fase"},
    1982: {"sede": "Espanha", "resultado": "Segunda fase", "jogos": 5, "vitorias": 3,
           "empates": 1, "derrotas": 1, "gols_pro": 10, "gols_contra": 3,
           "eliminado_na": "Segunda fase"},
    1986: {"sede": "Mexico", "resultado": "Quartas de final", "jogos": 5, "vitorias": 4,
           "empates": 0, "derrotas": 1, "gols_pro": 10, "gols_contra": 1,
           "eliminado_na": "Quartas de final"},
    1990: {"sede": "Italia", "resultado": "Oitavas de final", "jogos": 3, "vitorias": 2,
           "empates": 0, "derrotas": 1, "gols_pro": 4, "gols_contra": 2,
           "eliminado_na": "Oitavas de final"},
    1994: {"sede": "Estados Unidos", "resultado": "Campeao", "jogos": 7, "vitorias": 6,
           "empates": 1, "derrotas": 0, "gols_pro": 17, "gols_contra": 3,
           "eliminado_na": None},
    1998: {"sede": "Franca", "resultado": "Vice-campeao", "jogos": 7, "vitorias": 5,
           "empates": 1, "derrotas": 1, "gols_pro": 15, "gols_contra": 10,
           "eliminado_na": "Final"},
    2002: {"sede": "Coreia do Sul e Japao", "resultado": "Campeao", "jogos": 7, "vitorias": 7,
           "empates": 0, "derrotas": 0, "gols_pro": 18, "gols_contra": 4,
           "eliminado_na": None},
    2006: {"sede": "Alemanha", "resultado": "Quartas de final", "jogos": 5, "vitorias": 4,
           "empates": 0, "derrotas": 1, "gols_pro": 10, "gols_contra": 3,
           "eliminado_na": "Quartas de final"},
    2010: {"sede": "Africa do Sul", "resultado": "Quartas de final", "jogos": 5, "vitorias": 3,
           "empates": 1, "derrotas": 1, "gols_pro": 9, "gols_contra": 4,
           "eliminado_na": "Quartas de final"},
    2014: {"sede": "Brasil", "resultado": "4o lugar", "jogos": 7, "vitorias": 4,
           "empates": 1, "derrotas": 2, "gols_pro": 15, "gols_contra": 14,
           "eliminado_na": "Disputa de 3o lugar"},
    2018: {"sede": "Russia", "resultado": "Quartas de final", "jogos": 5, "vitorias": 3,
           "empates": 1, "derrotas": 1, "gols_pro": 8, "gols_contra": 3,
           "eliminado_na": "Quartas de final"},
    2022: {"sede": "Catar", "resultado": "Quartas de final", "jogos": 5, "vitorias": 4,
           "empates": 1, "derrotas": 0, "gols_pro": 12, "gols_contra": 2,
           "eliminado_na": "Quartas de final"},
}

artilheiros_brasil: Dict[str, Dict] = {
    "Pele": {"gols_total": 12, "gols_por_copa": {1958: 6, 1962: 1, 1970: 4, 1966: 1}},
    "Ronaldo": {"gols_total": 15, "gols_por_copa": {1998: 4, 2002: 8, 2006: 3}},
    "Vava": {"gols_total": 9, "gols_por_copa": {1958: 5, 1962: 4}},
    "Rivaldo": {"gols_total": 8, "gols_por_copa": {2002: 5, 1998: 3}},
    "Jairzinho": {"gols_total": 9, "gols_por_copa": {1970: 7, 1974: 2}},
    "Neymar": {"gols_total": 8, "gols_por_copa": {2014: 4, 2018: 2, 2022: 2}},
    "Garrincha": {"gols_total": 5, "gols_por_copa": {1958: 2, 1962: 3}},
    "Tostao": {"gols_total": 5, "gols_por_copa": {1970: 5}},
}

partidas_brasil: Dict[Tuple[int, str, str], Dict] = {
    (1950, "Final", "Uruguai"): {"placar_brasil": 1, "placar_adversario": 2, "resultado": "Derrota"},
    (1958, "Final", "Suecia"): {"placar_brasil": 5, "placar_adversario": 2, "resultado": "Vitoria"},
    (1962, "Final", "Tchecoslovaquia"): {"placar_brasil": 3, "placar_adversario": 1, "resultado": "Vitoria"},
    (1970, "Final", "Italia"): {"placar_brasil": 4, "placar_adversario": 1, "resultado": "Vitoria"},
    (1994, "Final", "Italia"): {"placar_brasil": 0, "placar_adversario": 0, "resultado": "Empate (penaltis)"},
    (1998, "Final", "Franca"): {"placar_brasil": 0, "placar_adversario": 3, "resultado": "Derrota"},
    (2002, "Final", "Alemanha"): {"placar_brasil": 2, "placar_adversario": 0, "resultado": "Vitoria"},
    (2014, "Semifinal", "Alemanha"): {"placar_brasil": 1, "placar_adversario": 7, "resultado": "Derrota"},
    (2022, "Quartas de final", "Croacia"): {"placar_brasil": 1, "placar_adversario": 1, "resultado": "Derrota (penaltis)"},
}

# ------------------------------------------------------------
# FUNÇÕES DE CONSULTA E ANÁLISE
# ------------------------------------------------------------


def listar_copas() -> None:
    """Imprime todas as participações do Brasil em Copas, ordenadas por ano."""
    print("\n--- Participações do Brasil em Copas ---")
    for ano in sorted(copas_brasil):
        dados = copas_brasil[ano]
        print(f"{ano} ({dados['sede']}): {dados['resultado']}")


def detalhes_copa(ano: int) -> None:
    """
    Exibe dados detalhados de uma Copa específica.
    Se o ano não estiver cadastrado, informa ao usuário.
    """
    dados = copas_brasil.get(ano)
    if dados is None:
        print(f"Não há registro do Brasil na Copa de {ano}.")
        return
    print(f"\n--- Copa de {ano} ({dados['sede']}) ---")
    print(f"Resultado final : {dados['resultado']}")
    print(f"Jogos           : {dados['jogos']}")
    print(f"Vitórias         : {dados['vitorias']}")
    print(f"Empates         : {dados['empates']}")
    print(f"Derrotas        : {dados['derrotas']}")
    print(f"Gols pro        : {dados['gols_pro']}")
    print(f"Gols contra     : {dados['gols_contra']}")
    # Se eliminado_na é None, significa que foi campeão naquela edição
    eliminado = dados['eliminado_na'] or 'Não foi eliminado (foi campeão)'
    print(f"Eliminado na    : {eliminado}")


def listar_titulos() -> None:
    """Lista os anos em que o Brasil foi campeão."""
    titulos = [ano for ano, dados in copas_brasil.items() if dados["resultado"] == "Campeao"]
    titulos.sort()
    plural = "títulos" if len(titulos) != 1 else "título"
    print(f"\nO Brasil tem {len(titulos)} {plural} mundial(is): {titulos}")


def listar_eliminacoes() -> None:
    """Lista a fase de eliminação do Brasil em todas as edições que não venceu."""
    print("\n--- Eliminações do Brasil ---")
    for ano in sorted(copas_brasil):
        dados = copas_brasil[ano]
        if dados["eliminado_na"]:
            print(f"{ano}: eliminado na(o) {dados['eliminado_na']}")


def ranking_artilheiros() -> None:
    """
    Gera um ranking simples dos artilheiros do Brasil em Copas,
    ordenando por gols totais (decrescente).
    """
    # Ordenação por gols_total (maior primeiro). Em caso de empate, mantém ordem alfabética.
    ranking = sorted(
        artilheiros_brasil.items(),
        key=lambda item: (-item[1]["gols_total"], item[0])
    )
    print("\n--- Ranking de artilheiros do Brasil em Copas ---")
    for posicao, (nome, dados) in enumerate(ranking, start=1):
        gols = dados.get('gols_total', 0)
        print(f"{posicao}º. {nome} - {gols} gol(s)")


def comparar_copas(ano1: int, ano2: int) -> None:
    """
    Compara lado a lado o desempenho do Brasil em duas edições.
    Exibe valores para campos-chave.
    """
    dados1 = copas_brasil.get(ano1)
    dados2 = copas_brasil.get(ano2)
    if dados1 is None or dados2 is None:
        print("Uma das Copas informadas não está cadastrada.")
        return

    campos = ["resultado", "jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra"]
    print(f"\n{'Item':<18}{ano1:<12}{ano2:<12}")
    for campo in campos:
        v1 = str(dados1.get(campo, 'N/A'))
        v2 = str(dados2.get(campo, 'N/A'))
        print(f"{campo:<18}{v1:<12}{v2:<12}")


def listar_partidas() -> None:
    """Lista todas as partidas cadastradas (chave: ano, fase, adversário)."""
    print("\n--- Partidas cadastradas ---")
    if not partidas_brasil:
        print("Nenhuma partida cadastrada.")
        return
    for (ano, fase, adversario), dados in sorted(partidas_brasil.items()):
        print(f"{ano} | {fase} | Brasil {dados['placar_brasil']} x {dados['placar_adversario']} {adversario} -> {dados['resultado']}")


# ------------------------------------------------------------
# FUNÇÕES DE MODIFICAÇÃO (cadastro/atualização/remoção)
# ------------------------------------------------------------


def cadastrar_copa() -> None:
    """Cadastra uma nova participação do Brasil em uma Copa (interativo)."""
    ano = ler_inteiro("Ano da Copa: ")
    if ano in copas_brasil:
        print("Já existe registro para esse ano. Use a opção de atualizar.")
        return

    sede = safe_input("Sede: ").strip()
    resultado = safe_input("Resultado final (ex.: Campeao, Quartas de final): ").strip()
    jogos = ler_inteiro("Número de jogos: ")
    vitorias = ler_inteiro("Vitórias: ")
    empates = ler_inteiro("Empates: ")
    derrotas = ler_inteiro("Derrotas: ")
    gols_pro = ler_inteiro("Gols pro: ")
    gols_contra = ler_inteiro("Gols contra: ")
    eliminado_na = safe_input("Eliminado na fase (deixe vazio se foi campeao): ").strip() or None

    copas_brasil[ano] = {
        "sede": sede,
        "resultado": resultado,
        "jogos": jogos,
        "vitorias": vitorias,
        "empates": empates,
        "derrotas": derrotas,
        "gols_pro": gols_pro,
        "gols_contra": gols_contra,
        "eliminado_na": eliminado_na,
    }
    print(f"Copa de {ano} cadastrada com sucesso.")


def atualizar_copa() -> None:
    """
    Atualiza um campo de uma Copa já cadastrada.
    O usuário informa o ano, o campo e o novo valor. Campos numéricos são validados.
    """
    ano = ler_inteiro("Ano da Copa a atualizar: ")
    if ano not in copas_brasil:
        print(f"Nao existe registro da Copa de {ano}.")
        return

    campos_disponiveis = list(copas_brasil[ano].keys())
    print("Campos disponíveis para atualizar:", ", ".join(campos_disponiveis))
    campo = safe_input("Campo a atualizar: ").strip()

    if campo not in copas_brasil[ano]:
        print("Campo invalido.")
        return

    novo_valor = safe_input(f"Novo valor para '{campo}': ").strip()
    # Campos que representam inteiros
    inteiros = {"jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra"}

    if campo in inteiros:
        try:
            novo_valor = int(novo_valor)
        except ValueError:
            print("Valor invalido, esperava um numero inteiro.")
            return
    copas_brasil[ano][campo] = novo_valor
    print("Atualizado com sucesso.")


def remover_partida() -> None:
    """Remove uma partida cadastrada a partir da chave composta (ano, fase, adversario)."""
    ano = ler_inteiro("Ano da partida: ")
    fase = safe_input("Fase: ").strip()
    adversario = safe_input("Adversário: ").strip()
    chave = (ano, fase, adversario)
    if chave not in partidas_brasil:
        print("Partida nao encontrada.")
        return
    del partidas_brasil[chave]
    print("Partida removida com sucesso.")


def cadastrar_partida() -> None:
    """Cadastra uma nova partida do Brasil (interativo)."""
    ano = ler_inteiro("Ano: ")
    fase = safe_input("Fase (ex.: Final, Semifinal, Quartas de final): ").strip()
    adversario = safe_input("Adversário: ").strip()
    chave = (ano, fase, adversario)
    if chave in partidas_brasil:
        print("Essa partida já está cadastrada.")
        return

    placar_brasil = ler_inteiro("Gols do Brasil: ")
    placar_adversario = ler_inteiro("Gols do adversário: ")

    if placar_brasil > placar_adversario:
        resultado = "Vitoria"
    elif placar_brasil < placar_adversario:
        resultado = "Derrota"
    else:
        resultado = "Empate"

    partidas_brasil[chave] = {
        "placar_brasil": placar_brasil,
        "placar_adversario": placar_adversario,
        "resultado": resultado,
    }
    print("Partida cadastrada com sucesso.")


# ------------------------------------------------------------
# FUNÇÕES AUXILIARES DE ENTRADA (tratamento e validação)
# ------------------------------------------------------------


def ler_inteiro(mensagem: str) -> int:
    """
    Lê do usuário um inteiro, repetindo até que a entrada seja válida.
    Trata Ctrl+C / EOF via safe_input.
    """
    while True:
        texto = safe_input(mensagem)
        try:
            return int(texto)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def safe_input(prompt: str) -> str:
    """
    Envolve input() tratando KeyboardInterrupt e EOFError.
    Se o usuário interromper a execução, encerra o programa com mensagem amigável.
    """
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nInterrupção recebida. Encerrando o programa.")
        raise SystemExit(0)


# ------------------------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------------------------


def exibir_menu() -> None:
    """Imprime o menu principal de opções."""
    print("\n===== Desempenho do Brasil nas Copas =====")
    print("1. Listar todas as Copas disputadas")
    print("2. Ver detalhes de uma Copa")
    print("3. Listar titulos")
    print("4. Listar eliminacoes")
    print("5. Ranking de artilheiros")
    print("6. Comparar duas Copas")
    print("7. Listar partidas cadastradas")
    print("8. Cadastrar nova Copa")
    print("9. Atualizar dados de uma Copa")
    print("10. Cadastrar partida")
    print("11. Remover partida")
    print("0. Sair")


def main() -> None:
    """
    Loop principal do programa.
    A opção '2' e '6' exigem inputs adicionais, por isso são tratadas separadamente.
    """
    opcoes = {
        "1": listar_copas, "3": listar_titulos, "4": listar_eliminacoes,
        "5": ranking_artilheiros, "7": listar_partidas, "8": cadastrar_copa,
        "9": atualizar_copa, "10": cadastrar_partida, "11": remover_partida,
    }
    
    while True:
        exibir_menu()
        escolha = safe_input("Escolha uma opção: ").strip()

        if escolha == "0":
            print("Encerrando o programa. Até mais!")
            break
        elif escolha == "2":
            ano = ler_inteiro("Digite o ano da Copa: ")
            detalhes_copa(ano)
        elif escolha == "6":
            ano1 = ler_inteiro("Primeiro ano: ")
            ano2 = ler_inteiro("Segundo ano: ")
            comparar_copas(ano1, ano2)
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
