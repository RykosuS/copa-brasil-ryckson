// ============================================
// DADOS BRASILEIROS NAS COPAS DO MUNDO
// ============================================
// Estrutura de armazenamento: dicionários (objetos) com os mesmos dados
// que estão no backend Python, mas aqui representados em JavaScript.

let copasBrasil = {
  1950: { sede: "Brasil", resultado: "Vice-campeao", jogos: 6, vitorias: 4, empates: 1, derrotas: 1, gols_pro: 14, gols_contra: 5, eliminado_na: "Final" },
  1958: { sede: "Suecia", resultado: "Campeao", jogos: 6, vitorias: 5, empates: 1, derrotas: 0, gols_pro: 16, gols_contra: 4, eliminado_na: null },
  1962: { sede: "Chile", resultado: "Campeao", jogos: 6, vitorias: 5, empates: 1, derrotas: 0, gols_pro: 14, gols_contra: 5, eliminado_na: null },
  1966: { sede: "Inglaterra", resultado: "Oitavas de final", jogos: 3, vitorias: 1, empates: 1, derrotas: 1, gols_pro: 3, gols_contra: 2, eliminado_na: "Oitavas de final" },
  1970: { sede: "Mexico", resultado: "Campeao", jogos: 6, vitorias: 6, empates: 0, derrotas: 0, gols_pro: 19, gols_contra: 7, eliminado_na: null },
  1974: { sede: "Alemanha Ocidental", resultado: "Terceira fase", jogos: 6, vitorias: 3, empates: 2, derrotas: 1, gols_pro: 12, gols_contra: 6, eliminado_na: "Terceira fase" },
  1978: { sede: "Argentina", resultado: "Terceira fase", jogos: 4, vitorias: 1, empates: 1, derrotas: 2, gols_pro: 3, gols_contra: 4, eliminado_na: "Terceira fase" },
  1982: { sede: "Espanha", resultado: "Segunda fase", jogos: 5, vitorias: 3, empates: 1, derrotas: 1, gols_pro: 10, gols_contra: 3, eliminado_na: "Segunda fase" },
  1986: { sede: "Mexico", resultado: "Quartas de final", jogos: 5, vitorias: 4, empates: 0, derrotas: 1, gols_pro: 10, gols_contra: 1, eliminado_na: "Quartas de final" },
  1990: { sede: "Italia", resultado: "Oitavas de final", jogos: 3, vitorias: 2, empates: 0, derrotas: 1, gols_pro: 4, gols_contra: 2, eliminado_na: "Oitavas de final" },
  1994: { sede: "Estados Unidos", resultado: "Campeao", jogos: 7, vitorias: 6, empates: 1, derrotas: 0, gols_pro: 17, gols_contra: 3, eliminado_na: null },
  1998: { sede: "Franca", resultado: "Vice-campeao", jogos: 7, vitorias: 5, empates: 1, derrotas: 1, gols_pro: 15, gols_contra: 10, eliminado_na: "Final" },
  2002: { sede: "Coreia do Sul e Japao", resultado: "Campeao", jogos: 7, vitorias: 7, empates: 0, derrotas: 0, gols_pro: 18, gols_contra: 4, eliminado_na: null },
  2006: { sede: "Alemanha", resultado: "Quartas de final", jogos: 5, vitorias: 4, empates: 0, derrotas: 1, gols_pro: 10, gols_contra: 3, eliminado_na: "Quartas de final" },
  2010: { sede: "Africa do Sul", resultado: "Quartas de final", jogos: 5, vitorias: 3, empates: 1, derrotas: 1, gols_pro: 9, gols_contra: 4, eliminado_na: "Quartas de final" },
  2014: { sede: "Brasil", resultado: "4o lugar", jogos: 7, vitorias: 4, empates: 1, derrotas: 2, gols_pro: 15, gols_contra: 14, eliminado_na: "Disputa de 3o lugar" },
  2018: { sede: "Russia", resultado: "Quartas de final", jogos: 5, vitorias: 3, empates: 1, derrotas: 1, gols_pro: 8, gols_contra: 3, eliminado_na: "Quartas de final" },
  2022: { sede: "Catar", resultado: "Quartas de final", jogos: 5, vitorias: 4, empates: 1, derrotas: 0, gols_pro: 12, gols_contra: 2, eliminado_na: "Quartas de final" },
};

// Maiores artilheiros do Brasil em Copas do Mundo
const artilheirosBrasil = {
  "Pele": { gols_total: 12, gols_por_copa: { 1958: 6, 1962: 1, 1970: 4, 1966: 1 } },
  "Ronaldo": { gols_total: 15, gols_por_copa: { 1998: 4, 2002: 8, 2006: 3 } },
  "Vava": { gols_total: 9, gols_por_copa: { 1958: 5, 1962: 4 } },
  "Rivaldo": { gols_total: 8, gols_por_copa: { 2002: 5, 1998: 3 } },
  "Jairzinho": { gols_total: 9, gols_por_copa: { 1970: 7, 1974: 2 } },
  "Neymar": { gols_total: 8, gols_por_copa: { 2014: 4, 2018: 2, 2022: 2 } },
  "Garrincha": { gols_total: 5, gols_por_copa: { 1958: 2, 1962: 3 } },
  "Tostao": { gols_total: 5, gols_por_copa: { 1970: 5 } },
};

// Partidas históricas do Brasil em Copas do Mundo
let partidasBrasil = [
  { ano: 1950, fase: "Final", adversario: "Uruguai", placar_brasil: 1, placar_adversario: 2, resultado: "Derrota" },
  { ano: 1958, fase: "Final", adversario: "Suecia", placar_brasil: 5, placar_adversario: 2, resultado: "Vitoria" },
  { ano: 1962, fase: "Final", adversario: "Tchecoslovaquia", placar_brasil: 3, placar_adversario: 1, resultado: "Vitoria" },
  { ano: 1970, fase: "Final", adversario: "Italia", placar_brasil: 4, placar_adversario: 1, resultado: "Vitoria" },
  { ano: 1994, fase: "Final", adversario: "Italia", placar_brasil: 0, placar_adversario: 0, resultado: "Empate (penaltis)" },
  { ano: 1998, fase: "Final", adversario: "Franca", placar_brasil: 0, placar_adversario: 3, resultado: "Derrota" },
  { ano: 2002, fase: "Final", adversario: "Alemanha", placar_brasil: 2, placar_adversario: 0, resultado: "Vitoria" },
  { ano: 2014, fase: "Semifinal", adversario: "Alemanha", placar_brasil: 1, placar_adversario: 7, resultado: "Derrota" },
  { ano: 2022, fase: "Quartas de final", adversario: "Croacia", placar_brasil: 1, placar_adversario: 1, resultado: "Derrota (penaltis)" },
];

// ============================================
// FUNÇÕES DE CONSULTA E ANÁLISE
// ============================================

// Retorna todos os anos em ordem crescente
function anosOrdenados() {
  return Object.keys(copasBrasil).map(Number).sort((a, b) => a - b);
}

// Conta quantos títulos mundiais o Brasil ganhou
function totalTitulos() {
  return anosOrdenados().filter(ano => copasBrasil[ano].resultado === "Campeao");
}

// Soma total de jogos disputados em todas as Copas
function totalJogos() {
  return anosOrdenados().reduce((soma, ano) => soma + copasBrasil[ano].jogos, 0);
}

// Soma total de gols marcados em todas as Copas
function totalGolsPro() {
  return anosOrdenados().reduce((soma, ano) => soma + copasBrasil[ano].gols_pro, 0);
}

// Gera chave única para identificar uma partida (ano|fase|adversario)
function chavePartida(p) {
  return `${p.ano}|${p.fase}|${p.adversario}`;
}

// ============================================
// FUNÇÕES DE RENDERIZAÇÃO
// ============================================

// Preenche um <select> com opções e formatação opcional
function preencherSelect(select, opcoes, formatador) {
  select.innerHTML = "";
  opcoes.forEach(opcao => {
    const el = document.createElement("option");
    el.value = opcao;
    el.textContent = formatador ? formatador(opcao) : opcao;
    select.appendChild(el);
  });
}

// Atualiza os números do placar no header (títulos, copas, jogos, gols)
function atualizarPlacarHeader() {
  document.getElementById("stat-titulos").textContent = totalTitulos().length;
  document.getElementById("stat-copas").textContent = anosOrdenados().length;
  document.getElementById("stat-jogos").textContent = totalJogos();
  document.getElementById("stat-gols").textContent = totalGolsPro();
}

// Renderiza a lista de todas as participações do Brasil nas Copas
function renderizarListaCopas() {
  const container = document.getElementById("lista-copas");
  container.innerHTML = "";
  anosOrdenados().forEach(ano => {
    const dados = copasBrasil[ano];
    const linha = document.createElement("div");
    linha.className = "linha-copa";
    const ehTitulo = dados.resultado === "Campeao";
    linha.innerHTML = `
      <span class="linha-copa__ano">${ano}</span>
      <span>${dados.sede}</span>
      <span class="linha-copa__resultado ${ehTitulo ? "is-titulo" : ""}">${dados.resultado}</span>
    `;
    container.appendChild(linha);
  });
}

// Renderiza apenas as Copas em que o Brasil foi eliminado
function renderizarEliminacoes() {
  const container = document.getElementById("lista-eliminacoes");
  container.innerHTML = "";
  anosOrdenados().forEach(ano => {
    const dados = copasBrasil[ano];
    if (!dados.eliminado_na) return;
    const linha = document.createElement("div");
    linha.className = "linha-copa";
    linha.innerHTML = `
      <span class="linha-copa__ano">${ano}</span>
      <span>eliminado na(o) ${dados.eliminado_na}</span>
      <span></span>
    `;
    container.appendChild(linha);
  });
}

// Renderiza o ranking dos maiores artilheiros brasileiros em Copas
function renderizarRanking() {
  const lista = document.getElementById("lista-ranking");
  lista.innerHTML = "";
  const ranking = Object.entries(artilheirosBrasil).sort((a, b) => b[1].gols_total - a[1].gols_total);
  ranking.forEach(([nome, dados]) => {
    const item = document.createElement("li");
    item.innerHTML = `<span>${nome}</span><span>${dados.gols_total} gols</span>`;
    lista.appendChild(item);
  });
}

// Renderiza a tabela de partidas cadastradas
function renderizarPartidas() {
  const container = document.getElementById("lista-partidas");
  container.innerHTML = "";
  if (partidasBrasil.length === 0) {
    container.innerHTML = "<p>Nenhuma partida cadastrada.</p>";
  }
  partidasBrasil.forEach(p => {
    const linha = document.createElement("div");
    linha.className = "linha-copa";
    linha.innerHTML = `
      <span class="linha-copa__ano">${p.ano}</span>
      <span>${p.fase} · Brasil ${p.placar_brasil} x ${p.placar_adversario} ${p.adversario}</span>
      <span class="linha-copa__resultado">${p.resultado}</span>
    `;
    container.appendChild(linha);
  });
  preencherSelect(
    document.getElementById("select-remover-partida"),
    partidasBrasil.map(chavePartida),
    chave => chave.replace(/\|/g, " · ")
  );
}

// Atualiza todos os dropdowns com a lista de anos
function atualizarTodosOsSelects() {
  const anos = anosOrdenados();
  preencherSelect(document.getElementById("select-detalhe-ano"), anos);
  preencherSelect(document.getElementById("select-comparar-1"), anos);
  preencherSelect(document.getElementById("select-comparar-2"), anos);
  preencherSelect(document.getElementById("select-atualizar-ano"), anos);
}

// Atualiza todas as visualizações (placar, listas, selects)
function atualizarTudo() {
  atualizarPlacarHeader();
  renderizarListaCopas();
  renderizarEliminacoes();
  renderizarRanking();
  renderizarPartidas();
  atualizarTodosOsSelects();
}

// ============================================
// NAVEGAÇÃO ENTRE ABAS
// ============================================

document.getElementById("tabs").addEventListener("click", (evento) => {
  const botao = evento.target.closest(".ingresso");
  if (!botao) return;
  // Remove a classe "ativo" de todos os botões
  document.querySelectorAll(".ingresso").forEach(b => b.classList.remove("is-ativo"));
  // Esconde todas as abas
  document.querySelectorAll(".aba").forEach(a => a.classList.remove("is-visivel"));
  // Marca o botão clicado como ativo
  botao.classList.add("is-ativo");
  // Mostra a aba correspondente
  document.getElementById(`aba-${botao.dataset.aba}`).classList.add("is-visivel");
});

// ============================================
// CONSULTAS (Ver detalhes, comparar)
// ============================================

// Exibe detalhes completos de uma Copa específica
document.getElementById("btn-detalhe").addEventListener("click", () => {
  const ano = Number(document.getElementById("select-detalhe-ano").value);
  const dados = copasBrasil[ano];
  const saida = document.getElementById("saida-detalhe");
  if (!dados) {
    saida.textContent = `Nao ha registro do Brasil na Copa de ${ano}.`;
    return;
  }
  saida.textContent =
`Copa de ${ano} (${dados.sede})
Resultado final : ${dados.resultado}
Jogos           : ${dados.jogos}
Vitorias        : ${dados.vitorias}
Empates         : ${dados.empates}
Derrotas        : ${dados.derrotas}
Gols pro        : ${dados.gols_pro}
Gols contra     : ${dados.gols_contra}
Eliminado na    : ${dados.eliminado_na || "Nao foi eliminado (foi campeao)"}`;
});

// Compara estatísticas de duas Copas diferentes
document.getElementById("btn-comparar").addEventListener("click", () => {
  const ano1 = Number(document.getElementById("select-comparar-1").value);
  const ano2 = Number(document.getElementById("select-comparar-2").value);
  const d1 = copasBrasil[ano1];
  const d2 = copasBrasil[ano2];
  const saida = document.getElementById("saida-comparar");
  if (!d1 || !d2) {
    saida.textContent = "Uma das Copas informadas nao esta cadastrada.";
    return;
  }
  const campos = [
    ["resultado", "Resultado"], ["jogos", "Jogos"], ["vitorias", "Vitorias"],
    ["empates", "Empates"], ["derrotas", "Derrotas"], ["gols_pro", "Gols pro"], ["gols_contra", "Gols contra"],
  ];
  let texto = `Item            ${ano1}            ${ano2}\n`;
  campos.forEach(([chave, rotulo]) => {
    texto += `${rotulo.padEnd(16)}${String(d1[chave]).padEnd(16)}${String(d2[chave])}\n`;
  });
  saida.textContent = texto;
});

// ============================================
// CADASTRO E ATUALIZAÇÃO DE COPAS
// ============================================

// Cadastra uma nova Copa na base de dados
document.getElementById("form-cadastrar-copa").addEventListener("submit", (evento) => {
  evento.preventDefault();
  const ano = Number(document.getElementById("c-ano").value);
  const saida = document.getElementById("saida-cadastrar-copa");

  if (copasBrasil[ano]) {
    saida.textContent = `Ja existe registro para a Copa de ${ano}. Use a secao de atualizar.`;
    return;
  }

  copasBrasil[ano] = {
    sede: document.getElementById("c-sede").value,
    resultado: document.getElementById("c-resultado").value,
    jogos: Number(document.getElementById("c-jogos").value),
    vitorias: Number(document.getElementById("c-vitorias").value),
    empates: Number(document.getElementById("c-empates").value),
    derrotas: Number(document.getElementById("c-derrotas").value),
    gols_pro: Number(document.getElementById("c-gols-pro").value),
    gols_contra: Number(document.getElementById("c-gols-contra").value),
    eliminado_na: document.getElementById("c-eliminado").value || null,
  };

  saida.textContent = `Copa de ${ano} cadastrada com sucesso.`;
  evento.target.reset();
  atualizarTudo();
});

// Atualiza um campo específico de uma Copa já cadastrada
document.getElementById("btn-atualizar-copa").addEventListener("click", () => {
  const ano = Number(document.getElementById("select-atualizar-ano").value);
  const campo = document.getElementById("select-atualizar-campo").value;
  const valorBruto = document.getElementById("atualizar-valor").value;
  const saida = document.getElementById("saida-atualizar-copa");

  if (!copasBrasil[ano]) {
    saida.textContent = `Nao existe registro da Copa de ${ano}.`;
    return;
  }

  // Campos numéricos devem ser convertidos para número
  const camposNumericos = ["jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra"];
  let valor = valorBruto;
  if (camposNumericos.includes(campo)) {
    if (valorBruto === "" || isNaN(Number(valorBruto))) {
      saida.textContent = "Valor invalido, esperava um numero inteiro.";
      return;
    }
    valor = Number(valorBruto);
  } else if (campo === "eliminado_na" && valorBruto === "") {
    valor = null;
  }

  copasBrasil[ano][campo] = valor;
  saida.textContent = `Campo '${campo}' da Copa de ${ano} atualizado com sucesso.`;
  atualizarTudo();
});

// ============================================
// CADASTRO E REMOÇÃO DE PARTIDAS
// ============================================

// Cadastra uma nova partida no histórico
document.getElementById("form-cadastrar-partida").addEventListener("submit", (evento) => {
  evento.preventDefault();
  const ano = Number(document.getElementById("p-ano").value);
  const fase = document.getElementById("p-fase").value;
  const adversario = document.getElementById("p-adversario").value;
  const placar_brasil = Number(document.getElementById("p-gols-brasil").value);
  const placar_adversario = Number(document.getElementById("p-gols-adversario").value);
  const saida = document.getElementById("saida-cadastrar-partida");

  const chaveNova = `${ano}|${fase}|${adversario}`;
  if (partidasBrasil.some(p => chavePartida(p) === chaveNova)) {
    saida.textContent = "Essa partida ja esta cadastrada.";
    return;
  }

  // Define o resultado baseado no placar
  let resultado = "Empate";
  if (placar_brasil > placar_adversario) resultado = "Vitoria";
  else if (placar_brasil < placar_adversario) resultado = "Derrota";

  partidasBrasil.push({ ano, fase, adversario, placar_brasil, placar_adversario, resultado });
  saida.textContent = "Partida cadastrada com sucesso.";
  evento.target.reset();
  atualizarTudo();
});

// Remove uma partida do histórico
document.getElementById("btn-remover-partida").addEventListener("click", () => {
  const chave = document.getElementById("select-remover-partida").value;
  const saida = document.getElementById("saida-remover-partida");
  const tamanhoAntes = partidasBrasil.length;
  partidasBrasil = partidasBrasil.filter(p => chavePartida(p) !== chave);
  saida.textContent = partidasBrasil.length < tamanhoAntes
    ? "Partida removida com sucesso."
    : "Partida nao encontrada.";
  atualizarTudo();
});

// ============================================
// INICIALIZAÇÃO
// ============================================

// Atualiza todo o conteúdo da página ao carregar
atualizarTudo();
