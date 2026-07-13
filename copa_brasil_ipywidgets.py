"""
Desempenho do Brasil nas Copas do Mundo
Trabalho Final - Estrutura de Dados (dicionarios)
Interface grafica com ipywidgets, para uso no Google Colab.

Como usar no Colab:
1. Cole este arquivo inteiro em UMA celula do notebook.
2. Rode a celula. A interface com abas vai aparecer logo abaixo.
"""

get_ipython().system('pip install ipywidgets -q')

import ipywidgets as widgets
from IPython.display import display, clear_output

# ---------------------------------------------------------------------------
# DADOS
# ---------------------------------------------------------------------------

copas_brasil = {
    1958: {"sede": "Suecia", "resultado": "Campeao", "jogos": 6, "vitorias": 5,
           "empates": 1, "derrotas": 0, "gols_pro": 16, "gols_contra": 4,
           "eliminado_na": None},
    1962: {"sede": "Chile", "resultado": "Campeao", "jogos": 6, "vitorias": 4,
           "empates": 2, "derrotas": 0, "gols_pro": 14, "gols_contra": 5,
           "eliminado_na": None},
    1970: {"sede": "Mexico", "resultado": "Campeao", "jogos": 6, "vitorias": 6,
           "empates": 0, "derrotas": 0, "gols_pro": 19, "gols_contra": 7,
           "eliminado_na": None},
    1982: {"sede": "Espanha", "resultado": "Segunda fase", "jogos": 5,
           "vitorias": 4, "empates": 0, "derrotas": 1, "gols_pro": 15,
           "gols_contra": 6, "eliminado_na": "Segunda fase"},
    1986: {"sede": "Mexico", "resultado": "Quartas de final", "jogos": 5,
           "vitorias": 3, "empates": 1, "derrotas": 1, "gols_pro": 10,
           "gols_contra": 4, "eliminado_na": "Quartas de final"},
    1994: {"sede": "Estados Unidos", "resultado": "Campeao", "jogos": 7,
           "vitorias": 5, "empates": 2, "derrotas": 0, "gols_pro": 11,
           "gols_contra": 3, "eliminado_na": None},
    1998: {"sede": "Franca", "resultado": "Vice-campeao", "jogos": 7,
           "vitorias": 5, "empates": 0, "derrotas": 2, "gols_pro": 14,
           "gols_contra": 10, "eliminado_na": "Final"},
    2002: {"sede": "Coreia do Sul e Japao", "resultado": "Campeao", "jogos": 7,
           "vitorias": 7, "empates": 0, "derrotas": 0, "gols_pro": 18,
           "gols_contra": 4, "eliminado_na": None},
    2006: {"sede": "Alemanha", "resultado": "Quartas de final", "jogos": 5,
           "vitorias": 4, "empates": 0, "derrotas": 1, "gols_pro": 10,
           "gols_contra": 3, "eliminado_na": "Quartas de final"},
    2014: {"sede": "Brasil", "resultado": "4o lugar", "jogos": 7,
           "vitorias": 3, "empates": 2, "derrotas": 2, "gols_pro": 11,
           "gols_contra": 14, "eliminado_na": "Disputa de 3o lugar"},
    2018: {"sede": "Russia", "resultado": "Quartas de final", "jogos": 5,
           "vitorias": 3, "empates": 1, "derrotas": 1, "gols_pro": 8,
           "gols_contra": 3, "eliminado_na": "Quartas de final"},
    2022: {"sede": "Catar", "resultado": "Quartas de final", "jogos": 5,
           "vitorias": 3, "empates": 1, "derrotas": 1, "gols_pro": 8,
           "gols_contra": 4, "eliminado_na": "Quartas de final"},
}

artilheiros_brasil = {
    "Pele": {"gols_total": 12, "gols_por_copa": {1958: 6, 1962: 1, 1970: 4, 1966: 1}},
    "Ronaldo": {"gols_total": 15, "gols_por_copa": {1998: 4, 2002: 8, 2006: 3}},
    "Vava": {"gols_total": 9, "gols_por_copa": {1958: 5, 1962: 4}},
    "Rivaldo": {"gols_total": 8, "gols_por_copa": {2002: 5, 1998: 3}},
    "Jairzinho": {"gols_total": 9, "gols_por_copa": {1970: 7, 1974: 2}},
    "Neymar": {"gols_total": 8, "gols_por_copa": {2014: 4, 2018: 2, 2022: 2}},
}

partidas_brasil = {
    (1958, "Final", "Suecia"): {"placar_brasil": 5, "placar_adversario": 2, "resultado": "Vitoria"},
    (1970, "Final", "Italia"): {"placar_brasil": 4, "placar_adversario": 1, "resultado": "Vitoria"},
    (1994, "Final", "Italia"): {"placar_brasil": 0, "placar_adversario": 0, "resultado": "Empate (penaltis)"},
    (1998, "Final", "Franca"): {"placar_brasil": 0, "placar_adversario": 3, "resultado": "Derrota"},
    (2002, "Final", "Alemanha"): {"placar_brasil": 2, "placar_adversario": 0, "resultado": "Vitoria"},
    (2014, "Semifinal", "Alemanha"): {"placar_brasil": 1, "placar_adversario": 7, "resultado": "Derrota"},
    (2022, "Quartas de final", "Croacia"): {"placar_brasil": 1, "placar_adversario": 1, "resultado": "Derrota (penaltis)"},
}


# ---------------------------------------------------------------------------
# LOGICA (mesmas funcoes da versao terminal, retornando texto em vez de
# usar print/input diretamente, para poderem ser exibidas em widgets.Output)
# ---------------------------------------------------------------------------

def texto_listar_copas():
    linhas = ["Participacoes do Brasil em Copas:\n"]
    for ano in sorted(copas_brasil):
        dados = copas_brasil[ano]
        linhas.append(f"{ano} ({dados['sede']}): {dados['resultado']}")
    return "\n".join(linhas)


def texto_detalhes_copa(ano):
    dados = copas_brasil.get(ano)
    if dados is None:
        return f"Nao ha registro do Brasil na Copa de {ano}."
    linhas = [
        f"Copa de {ano} ({dados['sede']})",
        f"Resultado final : {dados['resultado']}",
        f"Jogos           : {dados['jogos']}",
        f"Vitorias        : {dados['vitorias']}",
        f"Empates         : {dados['empates']}",
        f"Derrotas        : {dados['derrotas']}",
        f"Gols pro        : {dados['gols_pro']}",
        f"Gols contra     : {dados['gols_contra']}",
        f"Eliminado na    : {dados['eliminado_na'] or 'Nao foi eliminado (foi campeao)'}",
    ]
    return "\n".join(linhas)


def texto_listar_titulos():
    titulos = sorted(ano for ano, dados in copas_brasil.items() if dados["resultado"] == "Campeao")
    return f"O Brasil tem {len(titulos)} titulos mundiais: {titulos}"


def texto_listar_eliminacoes():
    linhas = ["Eliminacoes do Brasil:\n"]
    for ano in sorted(copas_brasil):
        dados = copas_brasil[ano]
        if dados["eliminado_na"]:
            linhas.append(f"{ano}: eliminado na(o) {dados['eliminado_na']}")
    return "\n".join(linhas)


def texto_ranking_artilheiros():
    ranking = sorted(artilheiros_brasil.items(), key=lambda item: item[1]["gols_total"], reverse=True)
    linhas = ["Ranking de artilheiros do Brasil em Copas:\n"]
    for posicao, (nome, dados) in enumerate(ranking, start=1):
        linhas.append(f"{posicao}o. {nome} - {dados['gols_total']} gols")
    return "\n".join(linhas)


def texto_comparar_copas(ano1, ano2):
    dados1 = copas_brasil.get(ano1)
    dados2 = copas_brasil.get(ano2)
    if dados1 is None or dados2 is None:
        return "Uma das Copas informadas nao esta cadastrada."
    linhas = [f"{'Item':<15}{ano1:<15}{ano2:<15}"]
    for campo in ["resultado", "jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra"]:
        linhas.append(f"{campo:<15}{str(dados1[campo]):<15}{str(dados2[campo]):<15}")
    return "\n".join(linhas)


def texto_listar_partidas():
    if not partidas_brasil:
        return "Nenhuma partida cadastrada."
    linhas = ["Partidas cadastradas:\n"]
    for (ano, fase, adversario), dados in sorted(partidas_brasil.items()):
        linhas.append(f"{ano} | {fase} | Brasil {dados['placar_brasil']} x "
                       f"{dados['placar_adversario']} {adversario} -> {dados['resultado']}")
    return "\n".join(linhas)


def cadastrar_copa(ano, sede, resultado, jogos, vitorias, empates, derrotas,
                    gols_pro, gols_contra, eliminado_na):
    if ano in copas_brasil:
        return f"Ja existe registro para a Copa de {ano}. Use a aba de atualizar."
    copas_brasil[ano] = {
        "sede": sede, "resultado": resultado, "jogos": jogos, "vitorias": vitorias,
        "empates": empates, "derrotas": derrotas, "gols_pro": gols_pro,
        "gols_contra": gols_contra, "eliminado_na": eliminado_na or None,
    }
    return f"Copa de {ano} cadastrada com sucesso."


def atualizar_copa(ano, campo, novo_valor):
    if ano not in copas_brasil:
        return f"Nao existe registro da Copa de {ano}."
    if campo in ("jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra"):
        try:
            novo_valor = int(novo_valor)
        except ValueError:
            return "Valor invalido, esperava um numero inteiro."
    copas_brasil[ano][campo] = novo_valor if novo_valor != "" else None
    return f"Campo '{campo}' da Copa de {ano} atualizado com sucesso."


def cadastrar_partida(ano, fase, adversario, placar_brasil, placar_adversario):
    chave = (ano, fase, adversario)
    if chave in partidas_brasil:
        return "Essa partida ja esta cadastrada."
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
    return "Partida cadastrada com sucesso."


def remover_partida(chave):
    if chave not in partidas_brasil:
        return "Partida nao encontrada."
    del partidas_brasil[chave]
    return "Partida removida com sucesso."


# ---------------------------------------------------------------------------
# INTERFACE (ipywidgets)
# ---------------------------------------------------------------------------

estilo = {"description_width": "140px"}
layout_campo = widgets.Layout(width="380px")


def anos_disponiveis():
    return sorted(copas_brasil.keys())


def chaves_partidas():
    return sorted(partidas_brasil.keys())


# --- Aba 1: Consultas -------------------------------------------------------

saida_consultas = widgets.Output()
dd_ano_detalhe = widgets.Dropdown(options=anos_disponiveis(), description="Ano:", style=estilo)
btn_detalhes = widgets.Button(description="Ver detalhes da Copa", button_style="info")
btn_listar_copas = widgets.Button(description="Listar todas as Copas")
btn_listar_eliminacoes = widgets.Button(description="Listar eliminacoes")
btn_listar_partidas = widgets.Button(description="Listar partidas")


def ao_clicar_detalhes(_):
    with saida_consultas:
        clear_output()
        print(texto_detalhes_copa(dd_ano_detalhe.value))


def ao_clicar_listar_copas(_):
    with saida_consultas:
        clear_output()
        print(texto_listar_copas())


def ao_clicar_listar_eliminacoes(_):
    with saida_consultas:
        clear_output()
        print(texto_listar_eliminacoes())


def ao_clicar_listar_partidas(_):
    with saida_consultas:
        clear_output()
        print(texto_listar_partidas())


btn_detalhes.on_click(ao_clicar_detalhes)
btn_listar_copas.on_click(ao_clicar_listar_copas)
btn_listar_eliminacoes.on_click(ao_clicar_listar_eliminacoes)
btn_listar_partidas.on_click(ao_clicar_listar_partidas)

aba_consultas = widgets.VBox([
    widgets.HBox([dd_ano_detalhe, btn_detalhes]),
    widgets.HBox([btn_listar_copas, btn_listar_eliminacoes, btn_listar_partidas]),
    saida_consultas,
])

# --- Aba 2: Analises ---------------------------------------------------------

saida_analises = widgets.Output()
btn_titulos = widgets.Button(description="Listar titulos")
btn_ranking = widgets.Button(description="Ranking de artilheiros")
dd_ano1 = widgets.Dropdown(options=anos_disponiveis(), description="Copa 1:", style=estilo)
dd_ano2 = widgets.Dropdown(options=anos_disponiveis(), description="Copa 2:", style=estilo)
btn_comparar = widgets.Button(description="Comparar", button_style="info")


def ao_clicar_titulos(_):
    with saida_analises:
        clear_output()
        print(texto_listar_titulos())


def ao_clicar_ranking(_):
    with saida_analises:
        clear_output()
        print(texto_ranking_artilheiros())


def ao_clicar_comparar(_):
    with saida_analises:
        clear_output()
        print(texto_comparar_copas(dd_ano1.value, dd_ano2.value))


btn_titulos.on_click(ao_clicar_titulos)
btn_ranking.on_click(ao_clicar_ranking)
btn_comparar.on_click(ao_clicar_comparar)

aba_analises = widgets.VBox([
    widgets.HBox([btn_titulos, btn_ranking]),
    widgets.HBox([dd_ano1, dd_ano2, btn_comparar]),
    saida_analises,
])

# --- Aba 3: Cadastrar / atualizar Copa --------------------------------------

saida_copa = widgets.Output()

tx_ano_novo = widgets.IntText(description="Ano:", style=estilo, layout=layout_campo)
tx_sede = widgets.Text(description="Sede:", style=estilo, layout=layout_campo)
tx_resultado = widgets.Text(description="Resultado:", style=estilo, layout=layout_campo)
tx_jogos = widgets.IntText(description="Jogos:", style=estilo, layout=layout_campo)
tx_vitorias = widgets.IntText(description="Vitorias:", style=estilo, layout=layout_campo)
tx_empates = widgets.IntText(description="Empates:", style=estilo, layout=layout_campo)
tx_derrotas = widgets.IntText(description="Derrotas:", style=estilo, layout=layout_campo)
tx_gols_pro = widgets.IntText(description="Gols pro:", style=estilo, layout=layout_campo)
tx_gols_contra = widgets.IntText(description="Gols contra:", style=estilo, layout=layout_campo)
tx_eliminado_na = widgets.Text(description="Eliminado na:", style=estilo, layout=layout_campo)
btn_cadastrar_copa = widgets.Button(description="Cadastrar Copa", button_style="success")

dd_ano_atualizar = widgets.Dropdown(options=anos_disponiveis(), description="Ano:", style=estilo)
dd_campo_atualizar = widgets.Dropdown(
    options=["sede", "resultado", "jogos", "vitorias", "empates", "derrotas",
             "gols_pro", "gols_contra", "eliminado_na"],
    description="Campo:", style=estilo)
tx_novo_valor = widgets.Text(description="Novo valor:", style=estilo, layout=layout_campo)
btn_atualizar_copa = widgets.Button(description="Atualizar Copa", button_style="warning")


def atualizar_dropdowns_de_ano():
    """Mantem os dropdowns de ano sincronizados apos um cadastro novo."""
    opcoes = anos_disponiveis()
    for dd in (dd_ano_detalhe, dd_ano1, dd_ano2, dd_ano_atualizar):
        dd.options = opcoes


def ao_clicar_cadastrar_copa(_):
    with saida_copa:
        clear_output()
        msg = cadastrar_copa(
            tx_ano_novo.value, tx_sede.value, tx_resultado.value, tx_jogos.value,
            tx_vitorias.value, tx_empates.value, tx_derrotas.value,
            tx_gols_pro.value, tx_gols_contra.value, tx_eliminado_na.value,
        )
        print(msg)
        atualizar_dropdowns_de_ano()


def ao_clicar_atualizar_copa(_):
    with saida_copa:
        clear_output()
        print(atualizar_copa(dd_ano_atualizar.value, dd_campo_atualizar.value, tx_novo_valor.value))


btn_cadastrar_copa.on_click(ao_clicar_cadastrar_copa)
btn_atualizar_copa.on_click(ao_clicar_atualizar_copa)

aba_copa = widgets.VBox([
    widgets.HTML("<b>Cadastrar nova Copa</b>"),
    tx_ano_novo, tx_sede, tx_resultado, tx_jogos, tx_vitorias, tx_empates,
    tx_derrotas, tx_gols_pro, tx_gols_contra, tx_eliminado_na, btn_cadastrar_copa,
    widgets.HTML("<hr><b>Atualizar Copa existente</b>"),
    dd_ano_atualizar, dd_campo_atualizar, tx_novo_valor, btn_atualizar_copa,
    saida_copa,
])

# --- Aba 4: Partidas (cadastrar / remover) ----------------------------------

saida_partida = widgets.Output()

tx_ano_partida = widgets.IntText(description="Ano:", style=estilo, layout=layout_campo)
tx_fase_partida = widgets.Text(description="Fase:", style=estilo, layout=layout_campo)
tx_adversario = widgets.Text(description="Adversario:", style=estilo, layout=layout_campo)
tx_placar_brasil = widgets.IntText(description="Gols Brasil:", style=estilo, layout=layout_campo)
tx_placar_adversario = widgets.IntText(description="Gols adversario:", style=estilo, layout=layout_campo)
btn_cadastrar_partida = widgets.Button(description="Cadastrar partida", button_style="success")

dd_partida_remover = widgets.Dropdown(options=chaves_partidas(), description="Partida:", style=estilo)
btn_remover_partida = widgets.Button(description="Remover partida", button_style="danger")


def atualizar_dropdown_partidas():
    dd_partida_remover.options = chaves_partidas()


def ao_clicar_cadastrar_partida(_):
    with saida_partida:
        clear_output()
        msg = cadastrar_partida(
            tx_ano_partida.value, tx_fase_partida.value, tx_adversario.value,
            tx_placar_brasil.value, tx_placar_adversario.value,
        )
        print(msg)
        atualizar_dropdown_partidas()


def ao_clicar_remover_partida(_):
    with saida_partida:
        clear_output()
        if dd_partida_remover.value is None:
            print("Nao ha partidas cadastradas para remover.")
            return
        print(remover_partida(dd_partida_remover.value))
        atualizar_dropdown_partidas()


btn_cadastrar_partida.on_click(ao_clicar_cadastrar_partida)
btn_remover_partida.on_click(ao_clicar_remover_partida)

aba_partidas = widgets.VBox([
    widgets.HTML("<b>Cadastrar partida</b>"),
    tx_ano_partida, tx_fase_partida, tx_adversario, tx_placar_brasil,
    tx_placar_adversario, btn_cadastrar_partida,
    widgets.HTML("<hr><b>Remover partida</b>"),
    dd_partida_remover, btn_remover_partida,
    saida_partida,
])

# --- Monta as abas -----------------------------------------------------------

abas = widgets.Tab(children=[aba_consultas, aba_analises, aba_copa, aba_partidas])
abas.set_title(0, "Consultas")
abas.set_title(1, "Analises")
abas.set_title(2, "Copas")
abas.set_title(3, "Partidas")

display(widgets.HTML("<h2>Desempenho do Brasil nas Copas do Mundo</h2>"))
display(abas)
