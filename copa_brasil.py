# -*- coding: utf-8 -*-
"""
copa_brasil.py - Sistema de consulta e edição de dados sobre o Brasil em Copas do Mundo.
Uso: python copa_brasil.py
"""

from typing import Dict, Tuple

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


def safe_input(prompt: str) -> str:
    """Lê entrada tratando Ctrl+C e EOF."""
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nInterrupção recebida. Encerrando.")
        raise SystemExit(0)


def ler_inteiro(mensagem: str) -> int:
    """Lê um inteiro com validação."""
    while True:
        try:
            return int(safe_input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def listar_copas() -> None:
    """Imprime todas as Copas do Brasil."""
    print("\n--- Participações do Brasil em Copas ---")
    for ano in sorted(copas_brasil):
        dados = copas_brasil[ano]
        print(f"{ano} ({dados['sede']}): {dados['resultado']}")


def detalhes_copa(ano: int) -> None:
    """Exibe detalhes de uma Copa."""
    dados = copas_brasil.get(ano)
    if not dados:
        print(f"Não há registro da Copa de {ano}.")
        return
    print(f"\n--- Copa de {ano} ({dados['sede']}) ---")
    print(f"Resultado final : {dados['resultado']}")
    print(f"Jogos           : {dados['jogos']}")
    print(f"Vitórias        : {dados['vitorias']}")
    print(f"Empates         : {dados['empates']}")
    print(f"Derrotas        : {dados['derrotas']}")
    print(f"Gols pro        : {dados['gols_pro']}")
    print(f"Gols contra     : {dados['gols_contra']}")
    eliminado = dados['eliminado_na'] or 'Não foi eliminado (foi campeão)'
    print(f"Eliminado na    : {eliminado}")


def listar_titulos() -> None:
    """Lista os títulos mundiais do Brasil."""
    titulos = sorted([ano for ano, dados in copas_brasil.items() if dados["resultado"] == "Campeao"])
    print(f"\nO Brasil tem {len(titulos)} títulos: {titulos}")


def listar_eliminacoes() -> None:
    """Lista as eliminações do Brasil."""
    print("\n--- Eliminações do Brasil ---")
    for ano in sorted(copas_brasil):
        if copas_brasil[ano]["eliminado_na"]:
            print(f"{ano}: eliminado na(o) {copas_brasil[ano]['eliminado_na']}")


def ranking_artilheiros() -> None:
    """Ranking dos artilheiros do Brasil."""
    ranking = sorted(artilheiros_brasil.items(), 
                    key=lambda x: (-x[1]["gols_total"], x[0]))
    print("\n--- Ranking de artilheiros ---")
    for pos, (nome, dados) in enumerate(ranking, 1):
        print(f"{pos}º. {nome} - {dados['gols_total']} gol(s)")


def comparar_copas(ano1: int, ano2: int) -> None:
    """Compara duas Copas lado a lado."""
    d1, d2 = copas_brasil.get(ano1), copas_brasil.get(ano2)
    if not d1 or not d2:
        print("Uma das Copas não está cadastrada.")
        return
    
    campos = ["resultado", "jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra"]
    print(f"\n{'Item':<18}{ano1:<12}{ano2:<12}")
    for campo in campos:
        print(f"{campo:<18}{str(d1[campo]):<12}{str(d2[campo]):<12}")


def listar_partidas() -> None:
    """Lista todas as partidas cadastradas."""
    print("\n--- Partidas cadastradas ---")
    if not partidas_brasil:
        print("Nenhuma partida cadastrada.")
        return
    for (ano, fase, adv), dados in sorted(partidas_brasil.items()):
        print(f"{ano} | {fase} | Brasil {dados['placar_brasil']} x {dados['placar_adversario']} {adv} -> {dados['resultado']}")


def cadastrar_copa() -> None:
    """Cadastra uma nova Copa."""
    ano = ler_inteiro("Ano da Copa: ")
    if ano in copas_brasil:
        print("Já existe registro para esse ano.")
        return

    copas_brasil[ano] = {
        "sede": safe_input("Sede: ").strip(),
        "resultado": safe_input("Resultado final: ").strip(),
        "jogos": ler_inteiro("Número de jogos: "),
        "vitorias": ler_inteiro("Vitórias: "),
        "empates": ler_inteiro("Empates: "),
        "derrotas": ler_inteiro("Derrotas: "),
        "gols_pro": ler_inteiro("Gols pro: "),
        "gols_contra": ler_inteiro("Gols contra: "),
        "eliminado_na": safe_input("Eliminado na fase (vazio se campeão): ").strip() or None,
    }
    print(f"Copa de {ano} cadastrada com sucesso.")


def atualizar_copa() -> None:
    """Atualiza um campo de uma Copa."""
    ano = ler_inteiro("Ano da Copa: ")
    if ano not in copas_brasil:
        print(f"Copa de {ano} não encontrada.")
        return

    print("Campos:", ", ".join(copas_brasil[ano].keys()))
    campo = safe_input("Campo a atualizar: ").strip()
    
    if campo not in copas_brasil[ano]:
        print("Campo inválido.")
        return

    novo_valor = safe_input(f"Novo valor para '{campo}': ").strip()
    
    if campo in {"jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra"}:
        try:
            novo_valor = int(novo_valor)
        except ValueError:
            print("Valor deve ser um número inteiro.")
            return
    
    copas_brasil[ano][campo] = novo_valor
    print("Atualizado com sucesso.")


def cadastrar_partida() -> None:
    """Cadastra uma nova partida."""
    ano = ler_inteiro("Ano: ")
    fase = safe_input("Fase: ").strip()
    adv = safe_input("Adversário: ").strip()
    chave = (ano, fase, adv)
    
    if chave in partidas_brasil:
        print("Essa partida já está cadastrada.")
        return

    gols_br = ler_inteiro("Gols do Brasil: ")
    gols_adv = ler_inteiro("Gols do adversário: ")
    
    if gols_br > gols_adv:
        resultado = "Vitoria"
    elif gols_br < gols_adv:
        resultado = "Derrota"
    else:
        resultado = "Empate"

    partidas_brasil[chave] = {
        "placar_brasil": gols_br,
        "placar_adversario": gols_adv,
        "resultado": resultado,
    }
    print("Partida cadastrada com sucesso.")


def remover_partida() -> None:
    """Remove uma partida cadastrada."""
    ano = ler_inteiro("Ano da partida: ")
    fase = safe_input("Fase: ").strip()
    adv = safe_input("Adversário: ").strip()
    chave = (ano, fase, adv)
    
    if chave not in partidas_brasil:
        print("Partida não encontrada.")
        return
    
    del partidas_brasil[chave]
    print("Partida removida com sucesso.")


def exibir_menu() -> None:
    """Exibe o menu principal."""
    print("\n===== Desempenho do Brasil nas Copas =====")
    print("1. Listar todas as Copas")
    print("2. Ver detalhes de uma Copa")
    print("3. Listar títulos")
    print("4. Listar eliminações")
    print("5. Ranking de artilheiros")
    print("6. Comparar duas Copas")
    print("7. Listar partidas")
    print("8. Cadastrar nova Copa")
    print("9. Atualizar Copa")
    print("10. Cadastrar partida")
    print("11. Remover partida")
    print("0. Sair")


def main() -> None:
    """Loop principal."""
    opcoes = {
        "1": listar_copas, "3": listar_titulos, "4": listar_eliminacoes,
        "5": ranking_artilheiros, "7": listar_partidas, "8": cadastrar_copa,
        "9": atualizar_copa, "10": cadastrar_partida, "11": remover_partida,
    }
    
    while True:
        exibir_menu()
        escolha = safe_input("Escolha uma opção: ").strip()

        if escolha == "0":
            print("Até mais!")
            break
        elif escolha == "2":
            detalhes_copa(ler_inteiro("Digite o ano: "))
        elif escolha == "6":
            comparar_copas(ler_inteiro("Primeiro ano: "), ler_inteiro("Segundo ano: "))
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
