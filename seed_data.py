"""
Seed data for all modules — lesson content with interactive exercises.
Text explanations are OUTSIDE code blocks. Only code examples inside terminal-style blocks.
"""

# ═══════════════════════════════════════════
#  MODULE 01 — SEMANA 1: Fundamentos do Python
# ═══════════════════════════════════════════

def get_m01_s1_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <h3>O que você vai aprender nesta aula</h3>
    <p>Fundamentos absolutos: da instalação ao seu primeiro programa funcional. Ao final você saberá declarar variáveis, usar todos os operadores e escrever condicionais completas.</p>
    <ul>
      <li>Por que Python domina automação e dados no mercado</li>
      <li>Como instalar Python 3 e VS Code no Windows</li>
      <li>Variáveis e os 4 tipos de dados essenciais (str, int, float, bool)</li>
      <li>f-strings: o jeito moderno de formatar textos</li>
      <li>Todos os operadores: aritméticos, de comparação e lógicos</li>
      <li>Estruturas condicionais: if, elif, else e operador ternário</li>
    </ul>
  </div>

  <h2><i data-lucide="zap" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 1. Por que Python?</h2>
  <p>Python é, hoje, a linguagem de programação mais popular do mundo para automação, dados e inteligência artificial. Criada por Guido van Rossum em 1991, ela foi projetada para ser <strong>legível como inglês</strong> — o que a torna ideal para quem está começando e para quem precisa de produtividade no dia a dia.</p>

  <h3>1.1 Vantagens do Python</h3>
  <div class="concept-cards">
    <div class="concept-card">
      <div class="concept-card-header green-accent"><strong>Legibilidade</strong></div>
      <div class="concept-card-body"><p>O código se parece com inglês. Você consegue ler e entender o que ele faz sem decorar sintaxe complicada.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header blue-accent"><strong>Ecossistema enorme</strong></div>
      <div class="concept-card-body"><p>Bibliotecas prontas para tudo: automação (PyAutoGUI), dados (Pandas), IA (TensorFlow), web (Flask) e muito mais.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header purple-accent"><strong>Alta demanda</strong></div>
      <div class="concept-card-body"><p>A linguagem mais pedida em vagas de automação e análise de dados no Brasil. Saber Python abre portas.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header orange-accent"><strong>Multiplataforma</strong></div>
      <div class="concept-card-body"><p>Roda em Windows, Mac e Linux sem alterar uma linha de código. Escreve uma vez, roda em qualquer lugar.</p></div>
    </div>
  </div>

  <h3>1.2 O que você pode fazer com Python</h3>
  <div class="usecase-grid">
    <div class="usecase-card"><div class="uc-icon">🤖</div><div class="uc-title">Automação RPA</div><div class="uc-desc">Clicar, digitar e navegar em sistemas automaticamente</div></div>
    <div class="usecase-card"><div class="uc-icon">📊</div><div class="uc-title">Análise de Dados</div><div class="uc-desc">Processar milhões de linhas com Pandas e gerar relatórios</div></div>
    <div class="usecase-card"><div class="uc-icon">🌐</div><div class="uc-title">Web Scraping</div><div class="uc-desc">Extrair dados de sites automaticamente</div></div>
    <div class="usecase-card"><div class="uc-icon">🧠</div><div class="uc-title">Inteligência Artificial</div><div class="uc-desc">Treinar modelos de ML e integrar com APIs de IA</div></div>
    <div class="usecase-card"><div class="uc-icon">🔌</div><div class="uc-title">APIs e Integração</div><div class="uc-desc">Conectar sistemas via REST APIs e webhooks</div></div>
    <div class="usecase-card"><div class="uc-icon">📈</div><div class="uc-title">Power BI + Python</div><div class="uc-desc">Transformar dados com Python dentro do Power BI</div></div>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="download" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 2. Instalação do Python e VS Code</h2>
  <p>Para começar a programar você precisa de dois softwares: o <strong>interpretador Python</strong> (que executa o código) e um <strong>editor de código</strong>.</p>

  <h3>2.1 Instalando o Python</h3>
  <ol class="step-list">
    <li>Acesse <strong>python.org/downloads</strong> e baixe a versão mais recente (3.12+)</li>
    <li>Na instalação, marque obrigatoriamente a opção <strong>"Add Python to PATH"</strong> antes de clicar em Install</li>
    <li>Abra o terminal (<code>cmd</code> no Windows) e execute: <code>python --version</code></li>
    <li>Se aparecer <code>Python 3.12.x</code>, a instalação funcionou corretamente</li>
  </ol>

  <h3>2.2 Instalando o VS Code</h3>
  <ol class="step-list">
    <li>Baixe o VS Code em <strong>code.visualstudio.com</strong></li>
    <li>Instale com as opções padrão</li>
    <li>Abra o VS Code e vá em <strong>Extensions</strong> (Ctrl+Shift+X)</li>
    <li>Pesquise <strong>"Python"</strong> e instale a extensão da Microsoft</li>
    <li>Pronto! Agora você tem autocomplete, detecção de erros e execução com um clique</li>
  </ol>

  <h3>2.3 Primeiro programa: Hello, World!</h3>
  <p>Por tradição, o primeiro programa em qualquer linguagem exibe a mensagem <em>"Hello, World!"</em>. Em Python é uma única linha:</p>
  <div class="code-block"><div class="code-header">Python — hello.py</div>
    <pre><code>print("Hello, World!")

# Saída: Hello, World!</code></pre>
  </div>
  <p>A função <code>print()</code> exibe qualquer coisa na tela. Qualquer texto entre aspas (simples ou duplas) é chamado de <strong>string</strong>. Você acabou de escrever seu primeiro programa Python.</p>

  <div class="info-box">
    <div class="box-icon"><i data-lucide="info" style="width:18px;height:18px;color:var(--cyan);"></i></div>
    <div><strong>Como executar:</strong> No VS Code, abra o arquivo <code>.py</code> e pressione <strong>F5</strong> ou clique no botão ▶ no canto superior direito. No terminal, use <code>python nome_do_arquivo.py</code>.</div>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="box" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 3. Variáveis e Tipos de Dados</h2>
  <p>Variáveis são <strong>"caixinhas"</strong> que guardam informações na memória do computador. Ao contrário de outras linguagens, em Python você <strong>não precisa declarar o tipo</strong> — ele é detectado automaticamente.</p>

  <div class="code-block"><div class="code-header">Python — declarando variáveis</div>
    <pre><code># Python detecta o tipo automaticamente
nome = "Carlos"        # str — texto
idade = 32             # int — número inteiro
salario = 6500.50      # float — número decimal
ativo = True           # bool — verdadeiro/falso

# Você pode reatribuir qualquer valor
idade = 33             # agora idade vale 33</code></pre>
  </div>

  <p>Existem <strong>4 tipos fundamentais</strong> que você vai usar no dia a dia:</p>

  <h3>3.1 Tipo str — Texto</h3>
  <p>Strings armazenam qualquer sequência de caracteres. Use para nomes, mensagens, caminhos de arquivo, CPFs — tudo que não é número para cálculo.</p>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>nome = "Ana Souza"
cpf = "123.456.789-00"       # CPF é string, não número!
caminho = "C:\\Dados\\relatorio.xlsx"

# Aspas simples ou duplas — tanto faz
mensagem = 'Olá, mundo!'

# String com múltiplas linhas
texto_longo = '''
Primeira linha
Segunda linha
Terceira linha
'''

print(len(nome))   # 9 — quantidade de caracteres
print(nome.upper())  # ANA SOUZA
print(nome.lower())  # ana souza</code></pre>
  </div>

  <h3>3.2 Tipo int — Número Inteiro</h3>
  <p>Inteiros são números sem parte decimal. Use para contagens, IDs, índices, quantidade de itens, anos.</p>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>quantidade = 150
ano = 2024
id_cliente = 10042

# Operações retornam int quando ambos são int
total = 100 + 50    # 150 (int)
dobro = 8 * 2       # 16 (int)

# Cuidado: divisão / sempre retorna float
resultado = 10 / 2  # 5.0 (float!), não 5</code></pre>
  </div>

  <h3>3.3 Tipo float — Número Decimal</h3>
  <p>Floats armazenam números com casas decimais. Use para valores monetários, porcentagens, medições. <strong>Atenção: use ponto como separador decimal</strong>, não vírgula.</p>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>preco = 29.90
taxa_inss = 0.11      # 11%
pi = 3.14159

# Operações com float
desconto = preco * 0.10   # 2.99
preco_final = preco - desconto  # 26.91

# Formatando com 2 casas decimais
print(f"R$ {preco_final:.2f}")  # R$ 26.91</code></pre>
  </div>

  <h3>3.4 Tipo bool — Verdadeiro/Falso</h3>
  <p>Booleanos só aceitam <code>True</code> ou <code>False</code> (com maiúscula inicial). São a base de toda lógica condicional.</p>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>ativo = True
aprovado = False
maior_de_idade = True

# Booleanos vêm de comparações
x = 10
resultado = x > 5   # True
igual = x == 10     # True
diferente = x != 5  # True

# Uso em condicionais
if ativo:
    print("Usuário ativo")  # Saída: Usuário ativo</code></pre>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu entendimento</div>
    <div class="check-question">Qual é o tipo da variável <code>preco = 29.90</code>?</div>
    <input type="text" class="check-input" data-answer="float" placeholder="Digite o tipo...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <h3>3.5 Verificando tipos com type()</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>nome = "Ana"
print(type(nome))     # &lt;class 'str'&gt;

idade = 28
print(type(idade))    # &lt;class 'int'&gt;

salario = 4500.50
print(type(salario))  # &lt;class 'float'&gt;

ativo = True
print(type(ativo))    # &lt;class 'bool'&gt;</code></pre>
  </div>

  <h3>3.6 f-strings — Formatação moderna</h3>
  <p>f-strings são o jeito mais moderno e legível de montar textos com variáveis em Python. Coloque um <code>f</code> antes das aspas e use <code>{}</code> para inserir qualquer variável ou expressão.</p>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>nome = "Ana"
idade = 28
salario = 6500.50

# f-string básica
print(f"Olá, {nome}! Você tem {idade} anos.")
# Saída: Olá, Ana! Você tem 28 anos.

# Com formatação de número
print(f"Salário: R$ {salario:.2f}")
# Saída: Salário: R$ 6500.50

# Com expressão dentro das chaves
print(f"Daqui 5 anos você terá {idade + 5} anos.")
# Saída: Daqui 5 anos você terá 33 anos.

# Alinhamento e largura
print(f"{'Nome':<15} {'Valor':>10}")
print(f"{'Produto A':<15} {150.0:>10.2f}")</code></pre>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="calculator" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 4. Operadores</h2>
  <p>Operadores são os símbolos que usamos para fazer cálculos, comparações e combinar condições. Existem <strong>3 categorias</strong> que você precisa dominar:</p>

  <h3>4.1 Operadores Aritméticos</h3>
  <p>Para cálculos matemáticos. Funcionam como na matemática comum:</p>
  <div class="operator-grid">
    <div class="operator-card"><div class="op-symbol">+</div><div class="op-name">Soma</div><div class="op-example"><code>10 + 3 → 13</code></div></div>
    <div class="operator-card"><div class="op-symbol">-</div><div class="op-name">Subtração</div><div class="op-example"><code>10 - 3 → 7</code></div></div>
    <div class="operator-card"><div class="op-symbol">*</div><div class="op-name">Multiplicação</div><div class="op-example"><code>10 * 3 → 30</code></div></div>
    <div class="operator-card"><div class="op-symbol">/</div><div class="op-name">Divisão</div><div class="op-example"><code>10 / 3 → 3.33</code></div></div>
    <div class="operator-card"><div class="op-symbol">//</div><div class="op-name">Div. Inteira</div><div class="op-example"><code>10 // 3 → 3</code></div></div>
    <div class="operator-card"><div class="op-symbol">%</div><div class="op-name">Resto (mod)</div><div class="op-example"><code>10 % 3 → 1</code></div></div>
    <div class="operator-card"><div class="op-symbol">**</div><div class="op-name">Potência</div><div class="op-example"><code>2 ** 3 → 8</code></div></div>
  </div>

  <div class="code-block"><div class="code-header">Python — operadores em prática</div>
    <pre><code>preco = 150.0
quantidade = 7

total = preco * quantidade      # 1050.0
desconto = total * 0.10         # 105.0
total_com_desconto = total - desconto  # 945.0

# Operador % é muito útil para verificar paridade
numero = 15
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")   # Saída: Ímpar</code></pre>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Mini exercício</div>
    <div class="check-question">Quanto é <code>15 % 4</code> (resto da divisão)?</div>
    <input type="text" class="check-input" data-answer="3" placeholder="Digite o resultado...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <h3>4.2 Operadores de Comparação</h3>
  <p>Sempre retornam <code>True</code> ou <code>False</code>. São a base das condicionais:</p>
  <div class="operator-grid">
    <div class="operator-card"><div class="op-symbol">==</div><div class="op-name">Igual a</div><div class="op-example"><code>5 == 5 → True</code></div></div>
    <div class="operator-card"><div class="op-symbol">!=</div><div class="op-name">Diferente</div><div class="op-example"><code>5 != 3 → True</code></div></div>
    <div class="operator-card"><div class="op-symbol">&gt;</div><div class="op-name">Maior que</div><div class="op-example"><code>5 &gt; 3 → True</code></div></div>
    <div class="operator-card"><div class="op-symbol">&lt;</div><div class="op-name">Menor que</div><div class="op-example"><code>5 &lt; 3 → False</code></div></div>
    <div class="operator-card"><div class="op-symbol">&gt;=</div><div class="op-name">Maior ou igual</div><div class="op-example"><code>5 &gt;= 5 → True</code></div></div>
    <div class="operator-card"><div class="op-symbol">&lt;=</div><div class="op-name">Menor ou igual</div><div class="op-example"><code>3 &lt;= 5 → True</code></div></div>
  </div>

  <div class="danger-box">
    <div class="box-icon"><i data-lucide="alert-triangle" style="width:18px;height:18px;color:#f87171;"></i></div>
    <div><strong>Atenção!</strong> <code>=</code> é atribuição (guardar valor em variável). <code>==</code> é comparação (verificar se são iguais). Confundir os dois é um dos erros mais comuns de iniciantes — Python vai mostrar um erro ou dar resultado errado silenciosamente.</div>
  </div>

  <h3>4.3 Operadores Lógicos</h3>
  <p>Combinam múltiplas condições. Essenciais para lógica mais complexa:</p>
  <div class="operator-grid">
    <div class="operator-card"><div class="op-symbol">and</div><div class="op-name">E (ambos)</div><div class="op-example"><code>True and False → False</code></div></div>
    <div class="operator-card"><div class="op-symbol">or</div><div class="op-name">Ou (algum)</div><div class="op-example"><code>True or False → True</code></div></div>
    <div class="operator-card"><div class="op-symbol">not</div><div class="op-name">Não (inverte)</div><div class="op-example"><code>not True → False</code></div></div>
  </div>

  <div class="code-block"><div class="code-header">Python — operadores lógicos em prática</div>
    <pre><code>idade = 25
renda = 3500.0

# and: ambas as condições precisam ser True
pode_financiar = idade >= 18 and renda >= 2000
print(pode_financiar)   # True

# or: pelo menos uma condição precisa ser True
tem_desconto = idade < 18 or idade >= 65
print(tem_desconto)     # False

# not: inverte o resultado
bloqueado = False
if not bloqueado:
    print("Acesso permitido")   # Saída: Acesso permitido</code></pre>
  </div>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu entendimento</div>
    <div class="check-question">Qual é o resultado de <code>True and False</code>?</div>
    <div class="check-options">
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">False</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">True</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">None</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="git-branch" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 5. Estruturas Condicionais</h2>
  <p>Condicionais permitem que o programa <strong>tome decisões</strong> com base em condições. O Python executa apenas o bloco correspondente à primeira condição verdadeira.</p>

  <h3>5.1 if simples</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>temperatura = 35

if temperatura > 30:
    print("Está muito quente!")
    print("Beba água.")

# Se temperatura for <= 30, nada é impresso</code></pre>
  </div>

  <h3>5.2 if / else</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>saldo = 200.0
valor_saque = 300.0

if saldo >= valor_saque:
    saldo -= valor_saque
    print(f"Saque realizado. Saldo: R$ {saldo:.2f}")
else:
    print("Saldo insuficiente.")</code></pre>
  </div>

  <h3>5.3 if / elif / else — múltiplas condições</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>nota = 7.5

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# Saída: Aprovado</code></pre>
  </div>

  <div class="info-box">
    <div class="box-icon"><i data-lucide="info" style="width:18px;height:18px;color:var(--cyan);"></i></div>
    <div><strong>Indentação é obrigatória em Python!</strong> Os 4 espaços (ou 1 Tab) antes do código dentro de um bloco definem o que pertence àquela condição. Esquecer a indentação causa <code>IndentationError</code>.</div>
  </div>

  <h3>5.4 Condicional em uma linha (ternário)</h3>
  <p>Para condições simples que retornam um valor, Python tem uma forma compacta:</p>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code># Sintaxe: valor_se_true if condicao else valor_se_false
idade = 20
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)   # Maior de idade

# Outro exemplo
preco = 100.0
tipo = "caro" if preco > 50 else "acessível"
print(f"O produto é {tipo}")  # O produto é caro</code></pre>
  </div>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu entendimento</div>
    <div class="check-question">Se <code>nota = 5.5</code>, qual será a saída: <code>if nota >= 9: ... elif nota >= 7: ... elif nota >= 5: ... else: ...</code>?</div>
    <div class="check-options">
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Aprovado</button>
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">Recuperação</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Reprovado</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Excelente!</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <h3>5.5 Exemplo completo — Calculadora de Salário Líquido</h3>
  <p>Vamos combinar todos os conceitos em um exemplo prático real:</p>
  <div class="code-block"><div class="code-header">Python — calculadora_salario.py</div>
    <pre><code>salario_bruto = 5000.0
dependentes = 2

# Calcular desconto INSS (11%)
desconto_inss = salario_bruto * 0.11

# Desconto IR depende do número de dependentes
if dependentes >= 2:
    desconto_ir = 150.0
elif dependentes == 1:
    desconto_ir = 225.0
else:
    desconto_ir = 300.0

salario_liquido = salario_bruto - desconto_inss - desconto_ir

print(f"Salário Bruto:   R$ {salario_bruto:.2f}")
print(f"INSS (11%):      R$ {desconto_inss:.2f}")
print(f"IR:              R$ {desconto_ir:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# Saída:
# Salário Bruto:   R$ 5000.00
# INSS (11%):      R$ 550.00
# IR:              R$ 150.00
# Salário Líquido: R$ 4300.00</code></pre>
  </div>

  <div class="checkpoint-box">
    <div class="cp-title"><i data-lucide="check-circle" style="width:14px;height:14px;display:inline;vertical-align:middle;"></i> Resumo da Aula 1</div>
    <ul>
      <li><strong>Python</strong> é ideal para automação e dados: legível, ecossistema enorme, alta demanda</li>
      <li><strong>Variáveis</strong> guardam dados. Os 4 tipos básicos: str, int, float, bool</li>
      <li><strong>f-strings</strong>: use <code>f"texto {variavel}"</code> para montar textos com variáveis</li>
      <li><strong>Operadores aritméticos</strong>: +, -, *, /, //, %, **</li>
      <li><strong>Operadores de comparação</strong>: ==, !=, >, &lt;, >=, &lt;= (retornam True/False)</li>
      <li><strong>Condicionais</strong>: if / elif / else executam blocos baseados em condições</li>
    </ul>
  </div>
</section>
"""

# ═══════════════════════════════════════════
#  MODULE 01 — SEMANA 2: Estruturas de Dados e Funções
# ═══════════════════════════════════════════

def get_m01_s2_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <h3>O que você vai aprender nesta aula</h3>
    <p>Estruturas de dados e funções são onde Python fica poderoso de verdade. Aqui você aprende a trabalhar com coleções de dados e a criar código reutilizável.</p>
    <ul>
      <li>Listas: indexação, slicing e todos os métodos essenciais</li>
      <li>Tuplas: quando usar imutabilidade a seu favor</li>
      <li>Dicionários: pares chave-valor e o padrão lista de dicts</li>
      <li>Loops for e while com break, continue e enumerate</li>
      <li>Funções: parâmetros, retorno, valores padrão e múltiplos retornos</li>
      <li>Import de bibliotecas: usando o ecossistema Python</li>
    </ul>
  </div>

  <h2><i data-lucide="list" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 5. Listas</h2>
  <p>Listas são coleções <strong>ordenadas e mutáveis</strong> de itens. Pense nelas como uma coluna de planilha: cada linha é um item. Você pode guardar qualquer tipo de dado, inclusive misturar tipos.</p>

  <div class="code-block"><div class="code-header">Python — criando listas</div>
    <pre><code># Lista de strings
frutas = ["maçã", "banana", "laranja", "uva"]

# Lista de números
vendas = [150, 230, 89, 340, 125]

# Lista mista (possível, mas evite em produção)
registro = ["Ana", 28, 6500.0, True]

# Lista vazia (para preencher depois)
resultados = []</code></pre>
  </div>

  <h3>5.1 Indexação e Slicing</h3>
  <p>Cada item tem um índice que começa em 0. Índices negativos contam do final.</p>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# Índices positivos — começa do zero
print(frutas[0])    # maçã (primeiro)
print(frutas[1])    # banana
print(frutas[4])    # manga (quinto)

# Índices negativos — conta do final
print(frutas[-1])   # manga (último)
print(frutas[-2])   # uva (penúltimo)

# Slicing [inicio:fim:passo] — fim é exclusivo
print(frutas[1:3])  # ['banana', 'laranja']
print(frutas[:2])   # ['maçã', 'banana']
print(frutas[2:])   # ['laranja', 'uva', 'manga']
print(frutas[::2])  # ['maçã', 'laranja', 'manga'] (pulando 1)</code></pre>
  </div>

  <h3>5.2 Métodos de Lista</h3>
  <table class="method-table">
    <thead><tr><th>Método</th><th>O que faz</th><th>Exemplo</th></tr></thead>
    <tbody>
      <tr><td>.append(x)</td><td>Adiciona x no final</td><td><code>lista.append("novo")</code></td></tr>
      <tr><td>.insert(i, x)</td><td>Insere x na posição i</td><td><code>lista.insert(0, "início")</code></td></tr>
      <tr><td>.remove(x)</td><td>Remove a 1ª ocorrência de x</td><td><code>lista.remove("banana")</code></td></tr>
      <tr><td>.pop(i)</td><td>Remove e retorna item na posição i</td><td><code>ultimo = lista.pop()</code></td></tr>
      <tr><td>.sort()</td><td>Ordena in-place (modifica a lista)</td><td><code>lista.sort()</code></td></tr>
      <tr><td>.reverse()</td><td>Inverte a ordem in-place</td><td><code>lista.reverse()</code></td></tr>
      <tr><td>.index(x)</td><td>Retorna índice da 1ª ocorrência de x</td><td><code>lista.index("maçã")</code></td></tr>
      <tr><td>.count(x)</td><td>Conta quantas vezes x aparece</td><td><code>lista.count("maçã")</code></td></tr>
      <tr><td>len(lista)</td><td>Quantidade de itens</td><td><code>len(lista)</code></td></tr>
    </tbody>
  </table>

  <div class="code-block"><div class="code-header">Python — métodos em prática</div>
    <pre><code>notas = [8.5, 6.0, 9.2, 7.5, 5.0]

notas.append(8.0)          # adiciona 8.0 no final
notas.sort()               # [5.0, 6.0, 7.5, 8.0, 8.5, 9.2]
media = sum(notas) / len(notas)  # 7.37
print(f"Média: {media:.2f}")     # Média: 7.37
print(f"Maior: {notas[-1]}")     # Maior: 9.2
print(f"Menor: {notas[0]}")      # Menor: 5.0</code></pre>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Mini exercício</div>
    <div class="check-question">Se <code>lista = [10, 20, 30, 40]</code>, qual é o valor de <code>lista[2]</code>?</div>
    <input type="text" class="check-input" data-answer="30" placeholder="Digite o valor...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="lock" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 6. Tuplas</h2>
  <p>Tuplas são como listas, mas <strong>imutáveis</strong> — depois de criadas, não podem ser alteradas. Use para dados que não devem mudar: coordenadas, configurações, constantes.</p>

  <div class="code-block"><div class="code-header">Python</div>
    <pre><code># Coordenadas geográficas — não devem ser alteradas
coordenada = (-23.5505, -46.6333)  # lat, lon de São Paulo
print(coordenada[0])   # -23.5505

# Dias da semana — ordem fixa
dias_uteis = ("seg", "ter", "qua", "qui", "sex")

# Configurações de conexão
DB_CONFIG = ("localhost", 5432, "meu_banco")

# Tuplas são mais rápidas que listas e sinalizam imutabilidade
# coordenada[0] = 10  # ERRO: TypeError!</code></pre>
  </div>

  <div class="info-box">
    <div class="box-icon"><i data-lucide="info" style="width:18px;height:18px;color:var(--cyan);"></i></div>
    <div><strong>Quando usar tupla vs lista?</strong> Use tupla quando os dados NÃO devem mudar (coordenadas, constantes, configs). Use lista quando você vai adicionar, remover ou modificar itens.</div>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="book-open" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 7. Dicionários</h2>
  <p>Dicionários armazenam pares <strong>chave-valor</strong>. Pense neles como uma ficha cadastral — cada campo (chave) tem um valor correspondente. São extremamente úteis para representar objetos do mundo real.</p>

  <div class="code-block"><div class="code-header">Python — criando e acessando dicionários</div>
    <pre><code>funcionario = {
    "nome": "Carlos Silva",
    "cargo": "Analista de Dados",
    "salario": 6500.0,
    "ativo": True
}

# Acessando valores
print(funcionario["nome"])              # Carlos Silva

# .get() — acessa sem erro se chave não existir
print(funcionario.get("setor", "N/A"))  # N/A

# Adicionando e modificando
funcionario["salario"] = 7000.0    # modifica
funcionario["setor"] = "TI"        # adiciona nova chave

# Verificando se chave existe
if "cargo" in funcionario:
    print(f"Cargo: {funcionario['cargo']}")</code></pre>
  </div>

  <h3>7.1 Iterando sobre dicionários</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>produto = {"nome": "Notebook", "preco": 3500.0, "estoque": 15}

# .items() — chave e valor juntos
for chave, valor in produto.items():
    print(f"{chave}: {valor}")

# .keys() — só as chaves
for campo in produto.keys():
    print(campo)

# .values() — só os valores
for v in produto.values():
    print(v)</code></pre>
  </div>

  <h3>7.2 Lista de Dicionários — padrão fundamental</h3>
  <p>O padrão mais usado em automação e dados: uma lista onde cada item é um dicionário representando um registro.</p>
  <div class="code-block"><div class="code-header">Python — lista de dicts (padrão de dados)</div>
    <pre><code>vendas = [
    {"produto": "Notebook",  "vendas": 150, "receita": 375000},
    {"produto": "Mouse",     "vendas": 500, "receita": 44500},
    {"produto": "Teclado",   "vendas": 300, "receita": 45000},
    {"produto": "Monitor",   "vendas": 100, "receita": 120000},
]

# Iterar e imprimir
for item in vendas:
    print(f"{item['produto']}: {item['vendas']} un | R$ {item['receita']:,}")

# Filtrar: só produtos com mais de 200 vendas
top = [v for v in vendas if v["vendas"] > 200]
print(f"Top vendas: {len(top)} produtos")</code></pre>
  </div>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu entendimento</div>
    <div class="check-question">Qual método acessa uma chave de dicionário sem gerar <code>KeyError</code> se ela não existir?</div>
    <div class="check-options">
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">dict["chave"]</button>
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">dict.get("chave", padrão)</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">dict.find("chave")</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="repeat" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 8. Estruturas de Repetição</h2>

  <h3>8.1 Loop for</h3>
  <p>Use o <code>for</code> quando você sabe quantas vezes vai repetir ou quando está percorrendo uma coleção.</p>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code># Iterando sobre lista
nomes = ["Ana", "Bob", "Carla"]
for nome in nomes:
    print(f"Olá, {nome}!")

# range() — sequência de números
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (passo 2)
    print(i)

# enumerate() — índice + valor juntos
for i, nome in enumerate(nomes, start=1):
    print(f"{i}. {nome}")  # 1. Ana, 2. Bob, 3. Carla</code></pre>
  </div>

  <h3>8.2 Loop while</h3>
  <p>Use o <code>while</code> quando não sabe quantas vezes vai repetir — repete enquanto uma condição for verdadeira.</p>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code># Contagem regressiva
contador = 5
while contador > 0:
    print(f"T-{contador}...")
    contador -= 1
print("Lançamento!")

# Loop de tentativas (muito usado em automação)
tentativas = 0
max_tentativas = 3
while tentativas < max_tentativas:
    # simula tentar uma operação
    tentativas += 1
    print(f"Tentativa {tentativas}")
    if tentativas == 2:
        print("Sucesso!")
        break</code></pre>
  </div>

  <h3>8.3 break e continue</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numeros:
    if n % 2 == 0:
        continue    # pula números pares
    if n > 7:
        break       # para quando passa de 7
    print(n)

# Saída: 1, 3, 5, 7</code></pre>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="settings" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 9. Funções</h2>
  <p>Funções são blocos de código reutilizáveis com nome. Em vez de copiar e colar o mesmo código várias vezes, você define uma função uma vez e chama quando precisar.</p>

  <h3>9.1 Definindo e chamando funções</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>def saudar(nome):
    print(f"Olá, {nome}!")

saudar("Ana")    # Olá, Ana!
saudar("Carlos") # Olá, Carlos!

# Parâmetro com valor padrão
def calcular_desconto(preco, percentual=10):
    desconto = preco * (percentual / 100)
    return preco - desconto

print(calcular_desconto(100))      # 90.0 (usa padrão 10%)
print(calcular_desconto(100, 25))  # 75.0 (usa 25%)</code></pre>
  </div>

  <h3>9.2 Funções com retorno</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    return imc, categoria

imc, cat = calcular_imc(70, 1.75)
print(f"IMC: {imc:.1f} — {cat}")
# Saída: IMC: 22.9 — Peso normal</code></pre>
  </div>

  <h3>9.3 Funções práticas para automação</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>from datetime import datetime

def gerar_nome_arquivo(prefixo, extensao="xlsx"):
    # Gera nome de arquivo com data/hora atual
    agora = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefixo}_{agora}.{extensao}"

def formatar_cpf(cpf_numeros):
    # Formata 11 dígitos no padrão 000.000.000-00
    c = cpf_numeros.zfill(11)
    return f"{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}"

print(gerar_nome_arquivo("relatorio"))  # relatorio_20241015_083000.xlsx
print(formatar_cpf("12345678901"))       # 123.456.789-01</code></pre>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Mini exercício</div>
    <div class="check-question">Em <code>def calcular_desconto(preco, percentual=10)</code>, qual é o valor padrão de <code>percentual</code>?</div>
    <input type="text" class="check-input" data-answer="10" placeholder="Digite o valor...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="package" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 10. Import de Bibliotecas</h2>
  <p>Bibliotecas são coleções de funções prontas criadas por outros desenvolvedores. Você não precisa criar tudo do zero — importe e use. Este é o grande poder do ecossistema Python.</p>

  <div class="code-block"><div class="code-header">Python — importando bibliotecas</div>
    <pre><code># Biblioteca padrão (já vem com Python)
import os
import json
from datetime import datetime
from pathlib import Path

# Exemplos de uso
pasta_atual = os.getcwd()
print(f"Pasta: {pasta_atual}")

agora = datetime.now()
print(f"Agora: {agora.strftime('%d/%m/%Y %H:%M')}")

# Verificar se arquivo existe
arquivo = Path("dados.csv")
if arquivo.exists():
    print("Arquivo encontrado!")
else:
    print("Arquivo não encontrado")</code></pre>
  </div>

  <div class="code-block"><div class="code-header">Terminal — instalando bibliotecas externas</div>
    <pre><code># Instalar com pip (uma vez por máquina)
pip install pandas
pip install pyautogui
pip install openpyxl
pip install requests

# Instalar múltiplas de uma vez
pip install pandas openpyxl requests

# Verificar o que está instalado
pip list</code></pre>
  </div>

  <div class="tip-box">
    <div class="tip-icon"><i data-lucide="lightbulb" style="width:18px;height:18px;color:var(--orange);"></i></div>
    <div>
      <strong>Convenção de import:</strong> Para bibliotecas grandes como Pandas e NumPy, use aliases padrão da comunidade: <code>import pandas as pd</code>, <code>import numpy as np</code>. Isso facilita leitura de código de outros devs.
    </div>
  </div>

  <div class="checkpoint-box">
    <div class="cp-title"><i data-lucide="check-circle" style="width:14px;height:14px;display:inline;vertical-align:middle;"></i> Resumo da Aula 2</div>
    <ul>
      <li><strong>Listas</strong>: coleções ordenadas e mutáveis; índices começam em 0; slicing com [inicio:fim]</li>
      <li><strong>Tuplas</strong>: imutáveis; use para dados que não devem mudar</li>
      <li><strong>Dicionários</strong>: chave-valor; <code>.get()</code> é mais seguro que <code>[]</code></li>
      <li><strong>Lista de dicts</strong>: padrão fundamental para trabalhar com dados tabulares</li>
      <li><strong>for/while</strong>: for para coleções e range, while para condições; use break e continue para controle</li>
      <li><strong>Funções</strong>: def, parâmetros, return, valores padrão</li>
      <li><strong>import</strong>: use a biblioteca certa para cada tarefa; instale com pip</li>
    </ul>
  </div>
</section>
"""


# ═══════════════════════════════════════════
#  MODULE 01 — SEMANA 3: Automação com Python
# ═══════════════════════════════════════════

def get_m01_s3_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <h3>O que você vai aprender nesta aula</h3>
    <p>Automação com Python (RPA) é uma das habilidades mais valorizadas e bem pagas do mercado. Nesta aula você aprende a fazer o computador trabalhar por você — sem intervenção humana.</p>
    <ul>
      <li>O que é RPA e onde se aplica no mercado</li>
      <li>PyAutoGUI: controlar mouse, teclado e tirar screenshots</li>
      <li>pywin32: abrir e controlar janelas do Windows</li>
      <li>try/except: automações robustas com logging</li>
      <li>Salvar resultados em CSV e TXT com data automática</li>
    </ul>
  </div>

  <h2><i data-lucide="bot" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 11. O que é Automação de Processos (RPA)?</h2>
  <p>RPA (Robotic Process Automation) é a técnica de usar software para automatizar tarefas repetitivas que humanos fazem manualmente em computadores — clicar em botões, preencher formulários, copiar dados entre sistemas.</p>

  <div class="highlight-grid">
    <div class="highlight-card">
      <i data-lucide="clock" style="width:24px;height:24px;color:var(--orange);"></i>
      <strong>Sem automação:</strong> 30 minutos por dia copiando dados manualmente — 125 horas por ano desperdiçadas
    </div>
    <div class="highlight-card">
      <i data-lucide="zap" style="width:24px;height:24px;color:var(--green);"></i>
      <strong>Com automação:</strong> Script roda em 2 minutos, sem erros, automaticamente toda manhã às 7h
    </div>
  </div>

  <h3>11.1 Onde RPA se aplica</h3>
  <ul>
    <li>Extrair dados de sistemas legados sem API disponível (ERP, sistemas internos)</li>
    <li>Preencher formulários web ou desktop automaticamente</li>
    <li>Copiar informações de um sistema para outro (ERP → planilha, por exemplo)</li>
    <li>Gerar relatórios periódicos sem intervenção manual</li>
    <li>Enviar e-mails em massa com dados personalizados</li>
    <li>Monitorar sites e alertar sobre mudanças de preço ou estoque</li>
  </ul>

  <h3>11.2 Ferramentas que vamos usar</h3>
  <div class="concept-cards">
    <div class="concept-card">
      <div class="concept-card-header green-accent"><strong>PyAutoGUI</strong></div>
      <div class="concept-card-body"><p>Controla mouse e teclado em qualquer programa. Funciona com qualquer aplicação visível na tela.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header blue-accent"><strong>pywin32</strong></div>
      <div class="concept-card-body"><p>Acessa APIs do Windows. Controla janelas, processos e recursos do sistema operacional.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header purple-accent"><strong>subprocess</strong></div>
      <div class="concept-card-body"><p>Abre e controla programas externos diretamente do Python. Biblioteca padrão — sem instalação.</p></div>
    </div>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="mouse-pointer" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 12. PyAutoGUI — Controlando Mouse e Teclado</h2>
  <p>PyAutoGUI simula todas as ações do mouse e teclado. É a forma mais direta de automatizar qualquer programa que tenha interface visual.</p>

  <div class="code-block"><div class="code-header">Terminal — instalação</div>
    <pre><code>pip install pyautogui</code></pre>
  </div>

  <h3>12.1 Controle do Mouse</h3>
  <div class="code-block"><div class="code-header">Python — mouse</div>
    <pre><code>import pyautogui
import time

# Configuração de segurança — SEMPRE inclua!
pyautogui.FAILSAFE = True  # mova mouse ao canto sup-esq para parar
pyautogui.PAUSE = 0.5      # pausa automática de 0.5s entre ações

# Descobrir posição atual do mouse
x, y = pyautogui.position()
print(f"Mouse em: x={x}, y={y}")

# Mover para uma posição
pyautogui.moveTo(500, 300, duration=1.0)  # move suavemente em 1s

# Clicar
pyautogui.click()                    # clique simples
pyautogui.doubleClick()              # clique duplo
pyautogui.rightClick()               # botão direito
pyautogui.click(x=200, y=400)        # clica em coordenada específica

# Arrastar (drag and drop)
pyautogui.dragTo(600, 400, duration=1.0)</code></pre>
  </div>

  <h3>12.2 Controle do Teclado</h3>
  <div class="code-block"><div class="code-header">Python — teclado</div>
    <pre><code>import pyautogui
import time

# Digitar texto
pyautogui.typewrite("relatório mensal 2024", interval=0.05)
pyautogui.press('enter')

# Teclas especiais
pyautogui.press('tab')
pyautogui.press('esc')
pyautogui.press('f5')

# Atalhos de teclado (hotkey)
pyautogui.hotkey('ctrl', 'a')    # selecionar tudo
pyautogui.hotkey('ctrl', 'c')    # copiar
pyautogui.hotkey('ctrl', 'v')    # colar
pyautogui.hotkey('alt', 'f4')    # fechar janela
pyautogui.hotkey('ctrl', 's')    # salvar

# Segurar tecla + clicar
pyautogui.keyDown('shift')
pyautogui.click(800, 400)
pyautogui.keyUp('shift')</code></pre>
  </div>

  <h3>12.3 Screenshots e Detecção de Imagem</h3>
  <p>PyAutoGUI pode tirar screenshots e localizar imagens na tela — ideal para clicar em botões pela aparência, não pela posição fixa.</p>
  <div class="code-block"><div class="code-header">Python — screenshots</div>
    <pre><code>import pyautogui

# Tirar screenshot
screenshot = pyautogui.screenshot()
screenshot.save("tela_atual.png")

# Localizar imagem na tela (busca pela aparência)
# botao.png deve ser uma imagem do botão que você quer clicar
posicao = pyautogui.locateOnScreen("botao_ok.png", confidence=0.9)
if posicao:
    pyautogui.click(posicao)
    print("Botão encontrado e clicado!")
else:
    print("Botão não encontrado na tela")</code></pre>
  </div>

  <div class="danger-box">
    <div class="box-icon"><i data-lucide="alert-triangle" style="width:18px;height:18px;color:#f87171;"></i></div>
    <div><strong>Segurança importante!</strong> Sempre defina <code>pyautogui.FAILSAFE = True</code> no início do script. Se algo der errado, mova o mouse rapidamente para o canto superior esquerdo (posição 0,0) para interromper a automação imediatamente.</div>
  </div>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu entendimento</div>
    <div class="check-question">Por que é importante usar <code>time.sleep()</code> ou <code>pyautogui.PAUSE</code> entre ações de automação?</div>
    <div class="check-options">
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Para o código rodar mais rápido</button>
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">Para dar tempo de o programa carregar antes da próxima ação</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">É exigência do Python para usar PyAutoGUI</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="app-window" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 13. pywin32 — Controlando Janelas Windows</h2>
  <p>O pywin32 permite abrir, fechar, minimizar, maximizar e interagir com janelas de qualquer aplicação Windows, incluindo sistemas legados que não têm API.</p>

  <div class="code-block"><div class="code-header">Terminal — instalação</div>
    <pre><code>pip install pywin32</code></pre>
  </div>

  <div class="code-block"><div class="code-header">Python — controlando janelas</div>
    <pre><code>import win32gui
import win32con
import subprocess
import time

# Abrir o Bloco de Notas
subprocess.Popen(r"C:\Windows\System32\notepad.exe")
time.sleep(1)  # aguardar abrir

# Encontrar a janela pelo título
hwnd = win32gui.FindWindow(None, "Sem título - Bloco de Notas")

if hwnd:
    # Trazer para frente
    win32gui.SetForegroundWindow(hwnd)

    # Maximizar
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    print("Janela maximizada!")

    # Minimizar
    # win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

    # Fechar
    # win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
else:
    print("Janela não encontrada")</code></pre>
  </div>

  <div class="code-block"><div class="code-header">Python — listando todas as janelas abertas</div>
    <pre><code>import win32gui

def listar_janelas():
    janelas = []
    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            titulo = win32gui.GetWindowText(hwnd)
            if titulo:
                janelas.append((hwnd, titulo))
    win32gui.EnumWindows(callback, None)
    return janelas

for hwnd, titulo in listar_janelas():
    print(f"[{hwnd}] {titulo}")</code></pre>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="shield" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 14. Tratamento de Erros com try/except</h2>
  <p>Automações rodam sem supervisão humana. Se o script encontra um erro inesperado e não está preparado, ele para e a tarefa não é concluída. O <code>try/except</code> garante que o script continue mesmo com problemas.</p>

  <div class="code-block"><div class="code-header">Python — estrutura básica</div>
    <pre><code># Sem tratamento — qualquer erro para o script
# arquivo = open("dados.csv")  # FileNotFoundError se não existir

# Com tratamento
try:
    arquivo = open("dados.csv", "r", encoding="utf-8")
    conteudo = arquivo.read()
    arquivo.close()
    print("Arquivo lido com sucesso!")
except FileNotFoundError:
    print("Arquivo não encontrado. Criando novo...")
except PermissionError:
    print("Sem permissão para ler o arquivo.")
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    print("Processo finalizado.")  # executa sempre</code></pre>
  </div>

  <h3>14.1 try/except em automações com logging</h3>
  <div class="code-block"><div class="code-header">Python — automação robusta com log</div>
    <pre><code>import logging
import pyautogui
import time

# Configurar log
logging.basicConfig(
    filename="automacao.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def clicar_botao(x, y, nome="botão"):
    try:
        pyautogui.moveTo(x, y, duration=0.3)
        pyautogui.click()
        logging.info(f"Clique em '{nome}' (x={x}, y={y}) bem-sucedido")
        return True
    except Exception as e:
        logging.error(f"Falha ao clicar em '{nome}': {e}")
        return False

def executar_automacao():
    logging.info("=== Iniciando automação ===")
    try:
        sucesso = clicar_botao(500, 300, "Botão Exportar")
        if sucesso:
            time.sleep(2)
            clicar_botao(700, 400, "Botão Confirmar")
        logging.info("Automação concluída com sucesso")
    except Exception as e:
        logging.critical(f"Falha crítica na automação: {e}")

executar_automacao()</code></pre>
  </div>

  <div class="info-box">
    <div class="box-icon"><i data-lucide="info" style="width:18px;height:18px;color:var(--cyan);"></i></div>
    <div><strong>Boas práticas de logging:</strong> Use <code>logging.info()</code> para eventos normais, <code>logging.warning()</code> para situações inesperadas mas não críticas, <code>logging.error()</code> para erros recuperáveis e <code>logging.critical()</code> para falhas graves.</div>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="save" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 15. Salvar Resultados em CSV e TXT</h2>
  <p>Após extrair os dados, salve em arquivos para análise posterior ou integração com outras ferramentas.</p>

  <h3>15.1 Salvando em CSV</h3>
  <div class="code-block"><div class="code-header">Python — csv module</div>
    <pre><code>import csv
from datetime import datetime

dados = [
    {"nome": "Produto A", "valor": 150.0, "qtd": 10},
    {"nome": "Produto B", "valor": 89.90, "qtd": 25},
    {"nome": "Produto C", "valor": 340.0, "qtd": 5},
]

# Nome com data para não sobrescrever
data_hoje = datetime.now().strftime("%Y-%m-%d")
nome_arquivo = f"relatorio_{data_hoje}.csv"

with open(nome_arquivo, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nome", "valor", "qtd"])
    writer.writeheader()
    writer.writerows(dados)

print(f"Relatório salvo: {nome_arquivo}")</code></pre>
  </div>

  <h3>15.2 Salvando log em TXT</h3>
  <div class="code-block"><div class="code-header">Python — arquivo de log manual</div>
    <pre><code>from datetime import datetime

def registrar_log(mensagem, arquivo="execucao.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{timestamp}] {mensagem}\n"
    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(linha)
    print(linha.strip())

registrar_log("Automação iniciada")
registrar_log("Arquivo exportado: relatorio.xlsx")
registrar_log("Processo finalizado com sucesso")</code></pre>
  </div>

  <div class="tip-box">
    <div class="tip-icon"><i data-lucide="lightbulb" style="width:18px;height:18px;color:var(--orange);"></i></div>
    <div>
      <strong>Dica profissional:</strong> Sempre salve arquivos com a data no nome (<code>relatorio_2024-10-15.csv</code>). Assim você mantém histórico e nunca sobrescreve um arquivo anterior acidentalmente.
    </div>
  </div>

  <div class="checkpoint-box">
    <div class="cp-title"><i data-lucide="check-circle" style="width:14px;height:14px;display:inline;vertical-align:middle;"></i> Resumo da Aula 3</div>
    <ul>
      <li><strong>RPA</strong> automatiza tarefas repetitivas: clicar, digitar, navegar, copiar dados</li>
      <li><strong>PyAutoGUI</strong>: <code>moveTo()</code>, <code>click()</code>, <code>typewrite()</code>, <code>hotkey()</code>, <code>screenshot()</code></li>
      <li><strong>FAILSAFE = True</strong>: mova o mouse ao canto para parar o script em emergência</li>
      <li><strong>pywin32</strong>: encontre e controle janelas com <code>FindWindow()</code> e <code>ShowWindow()</code></li>
      <li><strong>try/except</strong>: proteja o script de erros; use finally para limpeza</li>
      <li><strong>logging</strong>: registre todas as ações para auditoria e diagnóstico</li>
      <li><strong>CSV e TXT</strong>: salve resultados com data no nome do arquivo</li>
    </ul>
  </div>
</section>
"""

# ═══════════════════════════════════════════
#  MODULE 01 — SEMANA 4: Pandas + Agendamento
# ═══════════════════════════════════════════

def get_m01_s4_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <h3>O que você vai aprender nesta aula</h3>
    <p>Pandas é a biblioteca mais poderosa do Python para análise de dados — um Excel turbinado que você controla com código. Nesta aula você vai dominar tudo para transformar dados brutos em relatórios profissionais rodando automaticamente.</p>
    <ul>
      <li>O que é Pandas: DataFrame e Series</li>
      <li>Lendo CSV e Excel com opções avançadas</li>
      <li>Explorando dados: head, info, describe, shape</li>
      <li>Filtrando linhas e acessando colunas</li>
      <li>Criando e transformando colunas</li>
      <li>Tratamento de nulos, duplicatas e agrupamentos</li>
      <li>Exportando para Excel e CSV com data automática</li>
      <li>Agendador de Tarefas do Windows: rodando automaticamente</li>
      <li>Projeto Final: automação completa do início ao fim</li>
    </ul>
  </div>

  <h2><i data-lucide="table" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 16. O que é Pandas?</h2>
  <p>Pandas é a biblioteca mais importante para análise de dados em Python. O nome vem de <em>"panel data"</em>. Pense nela como um Excel dentro do Python — mas com superpoderes: você pode processar milhões de linhas em segundos, encadear operações e automatizar tudo.</p>

  <h3>16.1 Conceitos fundamentais</h3>
  <div class="highlight-grid">
    <div class="highlight-card">
      <i data-lucide="table-2" style="width:24px;height:24px;color:var(--cyan);"></i>
      <strong>DataFrame</strong>: Tabela completa com linhas e colunas — como uma planilha Excel. É o objeto principal do Pandas.
    </div>
    <div class="highlight-card">
      <i data-lucide="bar-chart-3" style="width:24px;height:24px;color:var(--green);"></i>
      <strong>Series</strong>: Uma única coluna ou linha — como uma lista com índice. Cada coluna de um DataFrame é uma Series.
    </div>
  </div>

  <div class="code-block"><div class="code-header">Terminal — instalação</div>
    <pre><code>pip install pandas openpyxl</code></pre>
  </div>

  <div class="code-block"><div class="code-header">Python — criando DataFrame manualmente</div>
    <pre><code>import pandas as pd

# Criar DataFrame a partir de dicionário
df = pd.DataFrame({
    "produto": ["Notebook", "Mouse", "Teclado", "Monitor"],
    "valor":   [2500, 90, 150, 1200],
    "vendas":  [45, 320, 210, 80],
    "ativo":   [True, True, True, False]
})

print(df)
print(f"\nShape: {df.shape}")          # (4, 4)
print(f"Colunas: {list(df.columns)}")  # lista de colunas</code></pre>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="folder-open" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 17. Lendo Arquivos com Pandas</h2>

  <h3>17.1 Lendo CSV</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>import pandas as pd

# CSV com separador ponto e vírgula (padrão BR)
df = pd.read_csv("vendas.csv", sep=";", encoding="utf-8")

# CSV com separador vírgula (padrão internacional)
df = pd.read_csv("data.csv", sep=",", encoding="utf-8")

# Opções úteis
df = pd.read_csv(
    "vendas.csv",
    sep=";",
    encoding="utf-8",
    decimal=",",           # vírgula como decimal (padrão BR)
    thousands=".",         # ponto como milhar
    parse_dates=["data"],  # converte coluna para datetime
    usecols=["produto", "valor", "data"]  # só essas colunas
)</code></pre>
  </div>

  <h3>17.2 Lendo Excel</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>import pandas as pd

# Aba específica
df = pd.read_excel("relatorio.xlsx", sheet_name="Janeiro")

# Primeira aba (padrão)
df = pd.read_excel("relatorio.xlsx")

# Todas as abas (retorna dicionário)
abas = pd.read_excel("relatorio.xlsx", sheet_name=None)
for nome_aba, dados in abas.items():
    print(f"Aba '{nome_aba}': {dados.shape}")</code></pre>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="search" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 18. Explorando e Filtrando Dados</h2>

  <h3>18.1 Funções de exploração</h3>
  <div class="code-block"><div class="code-header">Python — conhecendo seus dados</div>
    <pre><code>import pandas as pd

df = pd.read_csv("vendas.csv", sep=";")

print(df.head(5))       # primeiras 5 linhas
print(df.tail(3))       # últimas 3 linhas
print(df.info())        # tipos de dados e valores nulos
print(df.describe())    # estatísticas: count, mean, std, min, max
print(df.shape)         # (linhas, colunas)
print(df.dtypes)        # tipo de cada coluna
print(df.columns)       # lista de colunas
print(df.isnull().sum())  # quantos nulos por coluna</code></pre>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Mini exercício</div>
    <div class="check-question">Se um DataFrame tem 500 linhas e 8 colunas, qual é o resultado de <code>df.shape</code>?</div>
    <input type="text" class="check-input" data-answer="(500, 8)" placeholder="(linhas, colunas)">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <h3>18.2 Acessando colunas e linhas</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code># Acessar uma coluna
precos = df["valor"]           # retorna uma Series

# Acessar múltiplas colunas
resumo = df[["produto", "valor", "vendas"]]  # retorna DataFrame

# Acessar por posição (iloc)
primeira_linha = df.iloc[0]        # linha 0
primeiras_3 = df.iloc[:3]          # linhas 0, 1, 2
célula = df.iloc[0, 2]             # linha 0, coluna 2

# Acessar por rótulo (loc)
df.loc[0, "produto"]               # linha 0, coluna "produto"
df.loc[df["valor"] > 500, "produto"]  # filtro + coluna</code></pre>
  </div>

  <h3>18.2 Filtros</h3>
  <div class="code-block"><div class="code-header">Python — filtrando dados</div>
    <pre><code>df = pd.DataFrame({
    "produto":   ["Notebook", "Mouse", "Teclado", "Monitor"],
    "valor":     [2500, 90, 150, 1200],
    "categoria": ["Tech", "Periférico", "Periférico", "Tech"]
})

# Filtro simples
caros = df[df["valor"] > 200]
tech = df[df["categoria"] == "Tech"]

# Múltiplos filtros (& = AND, | = OR)
caros_tech = df[(df["valor"] > 200) & (df["categoria"] == "Tech")]

# Filtro com lista de valores (isin)
selecionados = df[df["produto"].isin(["Mouse", "Teclado"])]

# Filtro com texto (str.contains)
notebooks = df[df["produto"].str.contains("Note", case=False)]

print(caros)</code></pre>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="plus-circle" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 19. Criando e Transformando Colunas</h2>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code>import pandas as pd

df = pd.DataFrame({
    "produto": ["Notebook", "Mouse", "Teclado"],
    "preco": [2500.0, 90.0, 150.0],
    "qtd_vendas": [45, 320, 210]
})

# Criar nova coluna calculada
df["receita_total"] = df["preco"] * df["qtd_vendas"]
df["preco_com_taxa"] = df["preco"] * 1.10

# Transformar texto
df["produto_upper"] = df["produto"].str.upper()
df["produto_lower"] = df["produto"].str.lower()

# Categorizar com apply + função
def classificar_preco(preco):
    if preco >= 1000: return "Premium"
    elif preco >= 100: return "Médio"
    else: return "Econômico"

df["categoria_preco"] = df["preco"].apply(classificar_preco)

print(df[["produto", "preco", "receita_total", "categoria_preco"]])</code></pre>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="eraser" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 20. Tratamento de Dados</h2>

  <h3>20.1 Valores nulos</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code># Verificar nulos
print(df.isnull().sum())         # nulos por coluna
print(df.isnull().sum().sum())   # total de nulos

# Preencher nulos com valor fixo
df["valor"].fillna(0, inplace=True)
df["categoria"].fillna("Sem categoria", inplace=True)

# Preencher com a mediana (evita distorção por outliers)
df["valor"].fillna(df["valor"].median(), inplace=True)

# Remover linhas com nulos em colunas obrigatórias
df.dropna(subset=["produto", "valor"], inplace=True)</code></pre>
  </div>

  <h3>20.2 Duplicatas</h3>
  <div class="code-block"><div class="code-header">Python</div>
    <pre><code># Ver duplicatas
print(df.duplicated().sum())  # quantidade de duplicatas

# Remover duplicatas completas
df.drop_duplicates(inplace=True)

# Remover duplicatas por colunas específicas (mantém primeira)
df.drop_duplicates(subset=["produto"], keep="first", inplace=True)</code></pre>
  </div>

  <h3>20.3 Agrupamentos</h3>
  <div class="code-block"><div class="code-header">Python — groupby (como SUMIF do Excel)</div>
    <pre><code>import pandas as pd

df = pd.DataFrame({
    "categoria": ["Tech", "Periférico", "Tech", "Periférico"],
    "produto":   ["Notebook", "Mouse", "Monitor", "Teclado"],
    "valor":     [2500, 90, 1200, 150],
    "vendas":    [45, 320, 80, 210]
})

# Soma por categoria
receita = df.groupby("categoria")["valor"].sum()
print(receita)

# Múltiplas agregações
resumo = df.groupby("categoria").agg(
    total_valor=("valor", "sum"),
    media_valor=("valor", "mean"),
    total_vendas=("vendas", "sum"),
    count=("produto", "count")
).reset_index()
print(resumo)</code></pre>
  </div>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu entendimento</div>
    <div class="check-question">Qual função Pandas equivale ao SUMIF do Excel (somar por grupo)?</div>
    <div class="check-options">
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">df.filter()</button>
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">df.groupby().sum()</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">df.sort_values()</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="download" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 21. Salvando Resultados</h2>
  <div class="code-block"><div class="code-header">Python — exportando dados</div>
    <pre><code>from datetime import datetime

data = datetime.now().strftime("%Y-%m-%d")

# Exportar para Excel (formatado)
df.to_excel(f"relatorio_{data}.xlsx", index=False, sheet_name="Dados")

# Exportar para CSV
df.to_csv(f"relatorio_{data}.csv", index=False, sep=";", encoding="utf-8")

# Exportar múltiplas abas no mesmo Excel
with pd.ExcelWriter(f"relatorio_{data}.xlsx") as writer:
    df.to_excel(writer, sheet_name="Todos", index=False)
    df[df["categoria"] == "Tech"].to_excel(writer, sheet_name="Tech", index=False)
    resumo.to_excel(writer, sheet_name="Resumo", index=False)

print(f"Arquivos salvos com data: {data}")</code></pre>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="clock" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 22. Agendador de Tarefas do Windows</h2>
  <p>Com o Agendador de Tarefas do Windows você executa seu script Python automaticamente em horários definidos — sem precisar abrir o computador e rodar manualmente.</p>

  <h3>22.1 Como agendar um script Python</h3>
  <ol class="step-list">
    <li>Pesquise <strong>"Agendador de Tarefas"</strong> na barra de pesquisa do Windows</li>
    <li>Clique em <strong>"Criar Tarefa Básica..."</strong> no painel direito</li>
    <li>Nome: <strong>Automação Relatório Diário</strong> — clique em Avançar</li>
    <li>Gatilho: <strong>Diariamente</strong> — defina o horário (ex: 07:00) — Avançar</li>
    <li>Ação: <strong>Iniciar um programa</strong> — Avançar</li>
    <li>Programa/script: insira o caminho do <code>python.exe</code> (ex: <code>C:\Python312\python.exe</code>)</li>
    <li>Adicionar argumentos: insira o caminho completo do <code>.py</code> (ex: <code>C:\Scripts\relatorio.py</code>)</li>
    <li>Iniciar em: insira a pasta onde está o script — Concluir</li>
  </ol>

  <h3>22.2 Script com log de execução</h3>
  <div class="code-block"><div class="code-header">Python — relatorio_diario.py</div>
    <pre><code>import pandas as pd
import logging
from datetime import datetime

logging.basicConfig(
    filename="relatorio.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

def gerar_relatorio():
    logging.info("=== Iniciando geração de relatório ===")
    try:
        df = pd.read_csv("dados.csv", sep=";", encoding="utf-8")
        logging.info(f"Dados carregados: {df.shape[0]} linhas")

        # Processar
        df.dropna(subset=["produto", "valor"], inplace=True)
        df["receita"] = df["valor"] * df["qtd"]

        # Salvar
        data = datetime.now().strftime("%Y-%m-%d")
        df.to_excel(f"relatorio_{data}.xlsx", index=False)
        logging.info(f"Relatório salvo: relatorio_{data}.xlsx")

    except Exception as e:
        logging.error(f"Falha: {e}")

gerar_relatorio()</code></pre>
  </div>

  <hr class="section-divider">

  <h2><i data-lucide="trophy" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> 23. Projeto Final do Módulo</h2>
  <p>Você vai construir uma automação completa que engloba tudo que aprendemos nas 4 semanas. Este é o projeto que você apresentará e levará para o seu portfólio.</p>

  <h3>23.1 Etapas do projeto</h3>
  <div class="concept-cards">
    <div class="concept-card">
      <div class="concept-card-header green-accent"><strong>1. Extração</strong></div>
      <div class="concept-card-body"><p>PyAutoGUI/pywin32: abrir o sistema, navegar até o relatório e exportar os dados</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header blue-accent"><strong>2. Processamento</strong></div>
      <div class="concept-card-body"><p>Pandas: ler o arquivo exportado, aplicar filtros e criar colunas calculadas</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header purple-accent"><strong>3. Limpeza</strong></div>
      <div class="concept-card-body"><p>Tratar nulos, remover duplicatas, padronizar textos e converter tipos</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header orange-accent"><strong>4. Saída</strong></div>
      <div class="concept-card-body"><p>Gerar Excel formatado com nome baseado na data atual</p></div>
    </div>
  </div>

  <h3>23.2 Estrutura de código do projeto</h3>
  <div class="code-block"><div class="code-header">Python — projeto_final.py</div>
    <pre><code>import pyautogui
import pandas as pd
import logging
from datetime import datetime
from pathlib import Path

# Configuração
pyautogui.FAILSAFE = True
logging.basicConfig(filename="projeto.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s", encoding="utf-8")

def etapa_extracao():
    # Abre o sistema e exporta os dados
    logging.info("Iniciando extração de dados...")
    # ... suas ações com PyAutoGUI aqui
    logging.info("Extração concluída")

def etapa_processamento(arquivo_csv):
    # Lê, limpa e transforma os dados
    logging.info(f"Processando: {arquivo_csv}")
    df = pd.read_csv(arquivo_csv, sep=";", encoding="utf-8")
    df.dropna(subset=["produto"], inplace=True)
    df.drop_duplicates(inplace=True)
    df["receita"] = df["valor"] * df["qtd"]
    df["categoria"] = df["produto"].apply(
        lambda x: "Premium" if df.loc[df["produto"]==x, "valor"].values[0] > 500 else "Padrão"
    )
    logging.info(f"Processados: {len(df)} registros")
    return df

def etapa_exportacao(df):
    # Salva o resultado final
    data = datetime.now().strftime("%Y-%m-%d")
    saida = f"relatorio_processado_{data}.xlsx"
    df.to_excel(saida, index=False)
    logging.info(f"Exportado: {saida}")
    return saida

def main():
    logging.info("=== INÍCIO DO PROJETO FINAL ===")
    try:
        etapa_extracao()
        df = etapa_processamento("dados_extraidos.csv")
        saida = etapa_exportacao(df)
        logging.info(f"=== CONCLUÍDO: {saida} ===")
    except Exception as e:
        logging.critical(f"FALHA CRÍTICA: {e}")

if __name__ == "__main__":
    main()</code></pre>
  </div>

  <div class="success-box">
    <div class="box-icon"><i data-lucide="check-circle" style="width:18px;height:18px;color:var(--green);"></i></div>
    <div><strong>Parabéns por chegar até aqui!</strong> Com este projeto final você dominou: Python básico, estruturas de dados, automação com PyAutoGUI, análise com Pandas e agendamento automático. Este é o nível que o mercado paga bem. Continue praticando!</div>
  </div>

  <div class="checkpoint-box">
    <div class="cp-title"><i data-lucide="check-circle" style="width:14px;height:14px;display:inline;vertical-align:middle;"></i> Resumo da Aula 4</div>
    <ul>
      <li><strong>Pandas</strong>: DataFrame (tabela) e Series (coluna); instale com <code>pip install pandas openpyxl</code></li>
      <li><strong>Leitura</strong>: <code>read_csv()</code> e <code>read_excel()</code> com parâmetros de encoding, sep, decimal</li>
      <li><strong>Exploração</strong>: <code>head()</code>, <code>info()</code>, <code>describe()</code>, <code>shape</code></li>
      <li><strong>Filtros</strong>: <code>df[condição]</code>, operadores &amp; e |, <code>isin()</code>, <code>str.contains()</code></li>
      <li><strong>Transformação</strong>: colunas calculadas, <code>apply()</code>, <code>str.upper/lower</code></li>
      <li><strong>Limpeza</strong>: <code>fillna()</code>, <code>dropna()</code>, <code>drop_duplicates()</code></li>
      <li><strong>Agrupamento</strong>: <code>groupby().agg()</code> equivale ao SUMIF/tabela dinâmica do Excel</li>
      <li><strong>Exportação</strong>: <code>to_excel()</code>, <code>to_csv()</code>, <code>ExcelWriter</code> para múltiplas abas</li>
      <li><strong>Agendador</strong>: Agendador de Tarefas do Windows executa o script automaticamente</li>
    </ul>
  </div>
</section>
"""

# ═══════════════════════════════════════════
#  MODULE IA — Aula 1
# ═══════════════════════════════════════════

def get_ia_a1_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <p>IA não é mágica — é uma ferramenta. Quem aprende a usá-la bem tem uma vantagem enorme. Nesta aula você vai entender como funcionam os LLMs e como extrair o máximo deles.</p>
  </div>

  <h2><i data-lucide="brain" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> O que são LLMs?</h2>
  <p>LLMs (Large Language Models) são modelos de linguagem treinados em bilhões de textos. Eles aprendem padrões estatísticos da linguagem humana.</p>

  <div class="concept-cards">
    <div class="concept-card">
      <div class="concept-card-header green-accent"><strong>ChatGPT (OpenAI)</strong></div>
      <div class="concept-card-body"><p>Melhor para tarefas gerais, código, criatividade. GPT-4o é excelente.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header blue-accent"><strong>Claude (Anthropic)</strong></div>
      <div class="concept-card-body"><p>Melhor para textos longos, análise de documentos, raciocínio.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header purple-accent"><strong>Gemini (Google)</strong></div>
      <div class="concept-card-body"><p>Integrado ao Google Workspace, bom com multimodal.</p></div>
    </div>
  </div>

  <h2><i data-lucide="pen-tool" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> Prompt Engineering — A Arte de Pedir</h2>
  <p>Um bom prompt tem <strong>4 elementos</strong>. A diferença entre um resultado medíocre e um excelente está em como você pede:</p>

  <div class="operator-grid">
    <div class="operator-card"><div class="op-symbol" style="font-size:1rem;">1</div><div class="op-name">Contexto</div><div class="op-example">Quem é você / cenário</div></div>
    <div class="operator-card"><div class="op-symbol" style="font-size:1rem;">2</div><div class="op-name">Tarefa</div><div class="op-example">O que precisa ser feito</div></div>
    <div class="operator-card"><div class="op-symbol" style="font-size:1rem;">3</div><div class="op-name">Formato</div><div class="op-example">Como quer a resposta</div></div>
    <div class="operator-card"><div class="op-symbol" style="font-size:1rem;">4</div><div class="op-name">Restrições</div><div class="op-example">O que evitar</div></div>
  </div>

  <div class="code-block"><div class="code-header">Prompt Profissional</div>
    <pre><code>[CONTEXTO] Você é um atendente de customer success de SaaS B2B.
[TAREFA] Responda o e-mail de um cliente insatisfeito com suporte.
[FORMATO] Tom empático, máximo 4 parágrafos.
[RESTRIÇÕES] Não prometa prazos específicos. Não culpe outros setores.</code></pre>
  </div>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu entendimento</div>
    <div class="check-question">Qual técnica pede ao modelo para raciocinar passo a passo antes de responder?</div>
    <div class="check-options">
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Few-Shot</button>
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">Chain of Thought</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Role Prompting</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <h2><i data-lucide="list-tree" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> Técnicas Avançadas de Prompt</h2>
  <p>Existem várias técnicas que melhoram drasticamente a qualidade das respostas:</p>

  <div class="concept-cards">
    <div class="concept-card">
      <div class="concept-card-header green-accent"><strong>Few-Shot Learning</strong></div>
      <div class="concept-card-body">
        <p>Dê exemplos antes de pedir a resposta. O modelo aprende o padrão.</p>
        <div class="code-block"><div class="code-header">Exemplo Few-Shot</div>
          <pre><code>Classifique o sentimento:
"Produto excelente!" → Positivo
"Não gostei nada" → Negativo
"O envio atrasou 3 dias" → ?</code></pre>
        </div>
      </div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header blue-accent"><strong>Chain of Thought</strong></div>
      <div class="concept-card-body">
        <p>Peça para o modelo "pensar passo a passo". Melhora raciocínio lógico e matemático.</p>
        <div class="code-block"><div class="code-header">CoT Prompt</div>
          <pre><code>Resolva passo a passo:
Se João tem 3x a idade de Maria, e a
soma das idades é 48, qual a idade
de cada um? Pense antes de responder.</code></pre>
        </div>
      </div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header purple-accent"><strong>Role Prompting</strong></div>
      <div class="concept-card-body">
        <p>Atribua uma persona ao modelo. "Você é um dev sênior com 15 anos de exp em Python."</p>
      </div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header orange-accent"><strong>Self-Consistency</strong></div>
      <div class="concept-card-body">
        <p>Gere 3 respostas diferentes e peça para o modelo escolher a melhor. Reduz erros.</p>
      </div>
    </div>
  </div>

  <h2><i data-lucide="wrench" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> Ferramentas de IA para Desenvolvedores</h2>
  <p>Além de chatbots, existem ferramentas que integram IA diretamente no seu fluxo de trabalho:</p>

  <div class="concept-cards">
    <div class="concept-card">
      <div class="concept-card-header blue-accent"><strong>GitHub Copilot</strong></div>
      <div class="concept-card-body"><p>Autocomplete de código no VS Code. Sugere funções inteiras baseado no contexto. Ideal para boilerplate e padrões comuns.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header green-accent"><strong>Cursor IDE</strong></div>
      <div class="concept-card-body"><p>IDE com IA integrada. Chat com codebase, refatoração automática, geração de testes. O mais avançado atualmente.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header purple-accent"><strong>Windsurf (Cascade)</strong></div>
      <div class="concept-card-body"><p>IDE com assistente agêntico. Executa tarefas complexas autonomamente — edita múltiplos arquivos, roda comandos.</p></div>
    </div>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique</div>
    <div class="check-question">Em Prompt Engineering, qual é o elemento que define COMO você quer a resposta (lista, JSON, parágrafos)?</div>
    <input type="text" class="check-input" data-answer="formato" placeholder="Digite...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <div class="tip-box">
    <div class="tip-icon"><i data-lucide="alert-triangle" style="width:18px;height:18px;color:var(--orange);"></i></div>
    <div>
      <strong>Quando NÃO confiar na IA:</strong> dados precisos (números, datas), eventos recentes, cálculos complexos, decisões legais ou médicas. Sempre verifique informações críticas.
    </div>
  </div>
</section>
"""

# ═══════════════════════════════════════════
#  MODULE IA — Aula 2
# ═══════════════════════════════════════════

def get_ia_a2_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <p>Nesta aula você vai além do ChatGPT e aprende a consumir APIs de IA no seu código Python — abrindo possibilidades ilimitadas de automação inteligente.</p>
  </div>

  <h2><i data-lucide="plug" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> Como funcionam as APIs de IA?</h2>
  <p>Você envia uma requisição HTTP com seu prompt e recebe a resposta do modelo. É exatamente como o ChatGPT funciona por dentro:</p>

  <div class="code-block"><div class="code-header">Python — pip install anthropic</div>
    <pre><code>import anthropic

client = anthropic.Anthropic(api_key="sua-chave-aqui")

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explique pandas em 3 linhas."}
    ]
)
print(message.content[0].text)</code></pre>
  </div>

  <h2><i data-lucide="sliders" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> Parâmetros Importantes</h2>
  <p>Os parâmetros controlam como o modelo se comporta:</p>

  <div class="concept-cards">
    <div class="concept-card">
      <div class="concept-card-header blue-accent"><strong>model</strong></div>
      <div class="concept-card-body"><p>Qual modelo usar. Haiku = rápido/barato. Sonnet = equilibrado.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header green-accent"><strong>max_tokens</strong></div>
      <div class="concept-card-body"><p>Tamanho máximo da resposta. 1 token ≈ 0.75 palavras.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header orange-accent"><strong>temperature</strong></div>
      <div class="concept-card-body"><p>0 = determinístico. 1 = criativo. Use 0.7 para geral.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header purple-accent"><strong>system</strong></div>
      <div class="concept-card-body"><p>Define a persona do modelo. Ex: "Você é um analista de dados sênior."</p></div>
    </div>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Mini exercício</div>
    <div class="check-question">Qual valor de <code>temperature</code> produz respostas mais determinísticas (sempre iguais)?</div>
    <input type="text" class="check-input" data-answer="0" placeholder="Digite o valor...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <h2><i data-lucide="workflow" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> Automação Inteligente com IA</h2>
  <p>O verdadeiro poder está em combinar IA com automação. Exemplos reais:</p>

  <div class="concept-cards">
    <div class="concept-card">
      <div class="concept-card-header green-accent"><strong>Classificação de E-mails</strong></div>
      <div class="concept-card-body"><p>Leia e-mails automaticamente, use IA para classificar (urgente, suporte, vendas) e encaminhe para a fila certa.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header blue-accent"><strong>Extração de Dados</strong></div>
      <div class="concept-card-body"><p>Envie PDFs ou imagens para a API e extraia dados estruturados (nomes, valores, datas) em JSON.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header orange-accent"><strong>Geração de Relatórios</strong></div>
      <div class="concept-card-body"><p>Passe dados brutos e peça para a IA gerar análises, insights e recomendações em linguagem natural.</p></div>
    </div>
  </div>

  <div class="code-block"><div class="code-header">Python — Fluxo de automação com IA</div>
    <pre><code>def processar_documento(texto):
    # Fluxo: le > classifica > extrai > salva
    # 1. Classificar o tipo
    tipo = classificar_com_ia(texto)
    # 2. Extrair dados relevantes
    dados = extrair_dados_com_ia(texto, tipo)
    # 3. Salvar no banco
    salvar_no_banco(dados)
    # 4. Notificar responsável
    enviar_notificacao(tipo, dados)</code></pre>
  </div>

  <div class="tip-box">
    <div class="tip-icon"><i data-lucide="key" style="width:18px;height:18px;color:var(--orange);"></i></div>
    <div>
      <strong>Onde pegar as chaves:</strong> OpenAI → <code>platform.openai.com</code> | Anthropic → <code>console.anthropic.com</code>. Nunca coloque sua chave direto no código — use variáveis de ambiente ou arquivo <code>.env</code>.
    </div>
  </div>
</section>
"""

# ═══════════════════════════════════════════
#  MODULE IA — Aula 3
# ═══════════════════════════════════════════

def get_ia_a3_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <p>Nesta aula você vai aprender a construir aplicações completas com IA — chatbots, pipelines de processamento de dados, e integração com ferramentas do dia a dia.</p>
  </div>

  <h2><i data-lucide="message-square" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> Construindo um Chatbot com Memória</h2>
  <p>Um chatbot real precisa lembrar do contexto da conversa. Isso é feito passando o histórico de mensagens a cada requisição:</p>

  <div class="code-block"><div class="code-header">Python — Chatbot com histórico</div>
    <pre><code>import anthropic

client = anthropic.Anthropic()
historico = []

def chat(mensagem_usuario):
    historico.append({
        "role": "user",
        "content": mensagem_usuario
    })

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system="Você é um assistente de programação Python.",
        messages=historico
    )

    resposta = response.content[0].text
    historico.append({
        "role": "assistant",
        "content": resposta
    })
    return resposta

# Uso:
print(chat("O que é uma list comprehension?"))
print(chat("Me dê 3 exemplos práticos disso"))</code></pre>
  </div>

  <div class="tip-box">
    <div class="tip-icon"><i data-lucide="alert-triangle" style="width:18px;height:18px;color:var(--orange);"></i></div>
    <div><strong>Cuidado com tokens:</strong> O histórico cresce a cada mensagem. Em produção, limite o histórico às últimas N mensagens ou use resumos.</div>
  </div>

  <h2><i data-lucide="file-json" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> Saída Estruturada — JSON Mode</h2>
  <p>Para automação, você precisa que a IA retorne dados em formato estruturado, não texto livre:</p>

  <div class="code-block"><div class="code-header">Python — Forçando JSON</div>
    <pre><code>prompt = (
    "Analise o texto e retorne APENAS um JSON:\\n"
    '{\\n'
    '  "sentimento": "positivo" | "negativo" | "neutro",\\n'
    '  "temas": ["lista", "de", "temas"],\\n'
    '  "urgencia": 1 a 5\\n'
    '}\\n\\n'
    'Texto: "O sistema caiu novamente e perdemos 3h '
    'de trabalho. Precisamos de solucao urgente."'
)

import json
resposta_texto = chat(prompt)
dados = json.loads(resposta_texto)
print(f"Urgencia: {dados['urgencia']}/5")
print(f"Sentimento: {dados['sentimento']}")</code></pre>
  </div>

  <h2><i data-lucide="git-branch" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> Padrão de Pipeline com IA</h2>
  <p>Aplicações reais usam múltiplas chamadas encadeadas. Cada etapa processa o resultado da anterior:</p>

  <div class="concept-cards">
    <div class="concept-card">
      <div class="concept-card-header green-accent"><strong>Etapa 1: Classificar</strong></div>
      <div class="concept-card-body"><p>A IA classifica o input (tipo de documento, sentimento, idioma). Saída: categoria.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header blue-accent"><strong>Etapa 2: Extrair</strong></div>
      <div class="concept-card-body"><p>Com base na categoria, extraia campos específicos em JSON estruturado.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header purple-accent"><strong>Etapa 3: Validar</strong></div>
      <div class="concept-card-body"><p>Python valida o JSON, checa tipos, ranges e completude antes de seguir.</p></div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header orange-accent"><strong>Etapa 4: Agir</strong></div>
      <div class="concept-card-body"><p>Com dados validados: salva no banco, envia e-mail, cria ticket, gera relatório.</p></div>
    </div>
  </div>

  <div class="code-block"><div class="code-header">Python — Pipeline completo</div>
    <pre><code>def pipeline_atendimento(mensagem):
    # Etapa 1: Classificar
    categoria = classificar(mensagem)
    # Possíveis: "suporte_tecnico", "financeiro",
    #            "comercial", "reclamacao"

    # Etapa 2: Extrair dados
    dados = extrair_dados(mensagem, categoria)
    # {"cliente": "...", "problema": "...", "prioridade": 3}

    # Etapa 3: Gerar resposta
    resposta = gerar_resposta(categoria, dados)

    # Etapa 4: Registrar e enviar
    salvar_ticket(categoria, dados, resposta)
    enviar_email(dados["cliente"], resposta)

    return resposta</code></pre>
  </div>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu entendimento</div>
    <div class="check-question">Por que passamos o histórico completo a cada chamada da API?</div>
    <div class="check-options">
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Para gastar mais tokens</button>
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">Porque o modelo não guarda estado entre chamadas</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Porque a API exige no mínimo 10 mensagens</button>
    </div>
    <div class="check-feedback"></div>
  </div>
</section>
"""

# ═══════════════════════════════════════════
#  MODULE IA — Aula 4
# ═══════════════════════════════════════════

def get_ia_a4_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <p>Na última aula do módulo, vamos explorar RAG (Retrieval-Augmented Generation), embeddings, agentes autônomos, e como construir soluções de IA prontas para produção.</p>
  </div>

  <h2><i data-lucide="database" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> RAG — Retrieval-Augmented Generation</h2>
  <p>LLMs têm conhecimento limitado (data de corte, sem dados internos). RAG resolve isso:</p>

  <div class="highlight-grid">
    <div class="highlight-card"><strong>Problema</strong><br>O modelo não conhece seus documentos internos, PDFs, planilhas, base de conhecimento.</div>
    <div class="highlight-card"><strong>Solução (RAG)</strong><br>Busque trechos relevantes dos seus dados e passe como contexto junto com a pergunta.</div>
  </div>

  <div class="code-block"><div class="code-header">Python — RAG simplificado</div>
    <pre><code># 1. Indexar documentos (uma vez)
documentos = [
    "Política de reembolso: até 7 dias...",
    "Horário de atendimento: seg-sex 9h-18h...",
    "Para cancelar, envie e-mail para..."
]

# 2. Buscar trecho relevante (simples)
def buscar_contexto(pergunta, docs):
    # Em produção: use embeddings + banco vetorial
    # Aqui: busca simples por palavras-chave
    scores = []
    for doc in docs:
        palavras = pergunta.lower().split()
        score = sum(1 for p in palavras if p in doc.lower())
        scores.append(score)
    melhor = docs[scores.index(max(scores))]
    return melhor

# 3. Gerar resposta com contexto
def responder_com_rag(pergunta):
    contexto = buscar_contexto(pergunta, documentos)
    prompt = (
        f"Use APENAS o contexto abaixo:\\n"
        f"---\\n{contexto}\\n---\\n"
        f"Pergunta: {pergunta}\\n"
        f"Responda de forma concisa."
    )
    return chamar_ia(prompt)</code></pre>
  </div>

  <h2><i data-lucide="compass" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> Embeddings — Busca Semântica</h2>
  <p>Embeddings transformam texto em vetores numéricos. Textos semelhantes ficam próximos no espaço vetorial:</p>

  <div class="code-block"><div class="code-header">Python — Embeddings com OpenAI</div>
    <pre><code>from openai import OpenAI
import numpy as np

client = OpenAI()

def get_embedding(texto):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texto
    )
    return response.data[0].embedding

def similaridade(vec1, vec2):
    # Cosseno: quanto mais próximo de 1, mais similar
    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )

# Exemplo:
e1 = get_embedding("cachorro feliz")
e2 = get_embedding("cão contente")
e3 = get_embedding("programação Python")

print(similaridade(e1, e2))  # ~0.92 (muito similar)
print(similaridade(e1, e3))  # ~0.15 (bem diferente)</code></pre>
  </div>

  <h2><i data-lucide="bot" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> Agentes Autônomos</h2>
  <p>Agentes são sistemas que usam IA para decidir quais ações tomar. O modelo recebe ferramentas e decide quando/como usá-las:</p>

  <div class="concept-cards">
    <div class="concept-card">
      <div class="concept-card-header green-accent"><strong>Tool Use / Function Calling</strong></div>
      <div class="concept-card-body">
        <p>O modelo recebe uma lista de funções disponíveis e decide qual chamar com quais parâmetros. Ex: buscar_clima("SP"), calcular_frete(cep).</p>
      </div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header blue-accent"><strong>Loop de Agente</strong></div>
      <div class="concept-card-body">
        <p>1) Recebe tarefa → 2) Decide ação → 3) Executa ferramenta → 4) Analisa resultado → 5) Repete ou finaliza.</p>
      </div>
    </div>
    <div class="concept-card">
      <div class="concept-card-header purple-accent"><strong>Frameworks</strong></div>
      <div class="concept-card-body">
        <p><strong>LangChain</strong>: mais popular, muitas integrações. <strong>CrewAI</strong>: múltiplos agentes colaborativos. <strong>AutoGen</strong>: da Microsoft.</p>
      </div>
    </div>
  </div>

  <div class="code-block"><div class="code-header">Python — Agente com Tool Use (conceitual)</div>
    <pre><code>tools = [
    {
        "name": "buscar_preco",
        "description": "Busca o preço de um produto",
        "parameters": {"produto": "string"}
    },
    {
        "name": "calcular_desconto",
        "description": "Calcula desconto percentual",
        "parameters": {"preco": "float", "pct": "float"}
    }
]

# O modelo decide:
# "Preciso buscar o preço do notebook"
# → chama buscar_preco("notebook") → R$ 3500
# "Agora calculo 15% de desconto"
# → chama calcular_desconto(3500, 15) → R$ 2975
# "O notebook com 15% de desconto fica R$ 2975"</code></pre>
  </div>

  <h2><i data-lucide="shield-check" style="width:20px;height:20px;display:inline;vertical-align:middle;"></i> Boas Práticas em Produção</h2>

  <div class="operator-grid">
    <div class="operator-card"><div class="op-symbol" style="font-size:1rem;color:var(--green);">1</div><div class="op-name">Retry</div><div class="op-example">Trate erros de API</div></div>
    <div class="operator-card"><div class="op-symbol" style="font-size:1rem;color:var(--cyan);">2</div><div class="op-name">Cache</div><div class="op-example">Evite chamadas repetidas</div></div>
    <div class="operator-card"><div class="op-symbol" style="font-size:1rem;color:var(--primary-light);">3</div><div class="op-name">Logging</div><div class="op-example">Registre tudo</div></div>
    <div class="operator-card"><div class="op-symbol" style="font-size:1rem;color:var(--orange);">4</div><div class="op-name">Limites</div><div class="op-example">Rate limiting</div></div>
    <div class="operator-card"><div class="op-symbol" style="font-size:1rem;color:var(--red);">5</div><div class="op-name">Validação</div><div class="op-example">Valide output da IA</div></div>
    <div class="operator-card"><div class="op-symbol" style="font-size:1rem;color:var(--green);">6</div><div class="op-name">Custos</div><div class="op-example">Monitore gastos</div></div>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique</div>
    <div class="check-question">Qual técnica permite que um LLM acesse seus documentos internos, passando trechos relevantes como contexto?</div>
    <input type="text" class="check-input" data-answer="RAG" placeholder="Sigla de 3 letras...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <div class="tip-box">
    <div class="tip-icon"><i data-lucide="rocket" style="width:18px;height:18px;color:var(--orange);"></i></div>
    <div><strong>Próximos passos:</strong> Escolha um problema real do seu trabalho. Construa um protótipo simples (script Python + API de IA). Itere e melhore. Em 2 semanas você terá uma ferramenta funcional.</div>
  </div>
</section>
"""


# ═══════════════════════════════════════════
#  ALL MODULES DEFINITION
# ═══════════════════════════════════════════

ALL_MODULES = [
    {
        'name': 'Python Básico + Automação + Pandas',
        'short_name': 'Módulo 01 — Python',
        'description': 'Primeiro contato com programação de verdade. Saia com um script que automatiza uma tarefa real do seu trabalho.',
        'price': 250.0,
        'duration': '4 semanas · 4 calls de 1h',
        'level': 'Iniciante',
        'color': 'green',
        'icon': '🐍',
        'prereqs': 'Nenhum',
        'tools': 'Python, VS Code, PyAutoGUI, pywin32, Pandas',
        'lessons': [
            {
                'title': 'Semana 1 — Fundamentos do Python',
                'subtitle': 'Variáveis, tipos, operadores e condicionais',
                'week': 1, 'order': 1, 'duration': 60,
                'content_func': 'get_m01_s1_content',
                'exercises': [
                    ('Calculadora de IMC', 'Crie um programa que calcula o IMC de uma pessoa com peso=70 e altura=1.75. Imprima o resultado com 2 casas decimais.', 'peso = 70\naltura = 1.75\n\n# Calcule o IMC (peso / altura²)\n# Imprima com 2 casas decimais\n', '22.86', 'IMC = peso / (altura * altura). Use f"{imc:.2f}"', 10),
                    ('Classificador de Temperatura', 'Dado temperatura=35, imprima "Muito quente" se >=35, "Quente" se >=25, "Agradavel" se >=15, ou "Frio" se menor.', 'temperatura = 35\n\n# Use if/elif/else para classificar\n', 'Muito quente', 'if temperatura >= 35: print("Muito quente")', 10),
                    ('Conversor de Moeda', 'Converta R$ 1500 para dólar (taxa=5.0). Imprima exatamente: R$ 1500 = $ 300.00', 'reais = 1500\ntaxa = 5.0\n\n# Calcule e imprima no formato correto\n', 'R$ 1500 = $ 300.00', 'Use f"R$ {reais} = $ {reais/taxa:.2f}"', 10),
                    ('Calculadora de Desconto', 'Dado preco=250.0 e desconto=15 (%), calcule o valor final e imprima "Final: R$ 212.50".', 'preco = 250.0\ndesconto = 15\n\n# Calcule o valor com desconto e imprima\n', 'Final: R$ 212.50', 'valor_final = preco * (1 - desconto/100). Use f"Final: R$ {valor_final:.2f}"', 10),
                    ('Par ou Ímpar', 'Dado numero=47, imprima "47 e impar" se for ímpar ou "47 e par" se for par.', 'numero = 47\n\n# Verifique se é par ou ímpar e imprima\n', '47 e impar', 'Use o operador % (módulo): if numero % 2 == 0: par, else: impar', 10),
                    ('Troca de Variáveis', 'Dadas a=10 e b=25, troque os valores entre elas e imprima "a=25" e "b=10" (cada um em uma linha).', 'a = 10\nb = 25\n\n# Troque os valores de a e b\n# Imprima os resultados\n', 'a=25\nb=10', 'Em Python basta: a, b = b, a', 10),
                    ('Calculadora de Juros', 'Calcule juros simples: capital=1000, taxa=0.05, meses=12. Imprima "Montante: 1600.00".', 'capital = 1000\ntaxa = 0.05\nmeses = 12\n\n# Calcule juros simples: M = C * (1 + taxa * meses)\n', 'Montante: 1600.00', 'montante = capital * (1 + taxa * meses). print(f"Montante: {montante:.2f}")', 10),
                    ('Verificador de Ano Bissexto', 'Dado ano=2024, imprima "2024 e bissexto" se for bissexto, ou "2024 nao e bissexto" caso contrário.', 'ano = 2024\n\n# Verifique se o ano é bissexto e imprima\n', '2024 e bissexto', 'Bissexto: divisível por 4 E (não por 100 OU por 400)', 10),
                ]
            },
            {
                'title': 'Semana 2 — Estruturas de Dados e Funções',
                'subtitle': 'Listas, dicionários, loops e funções',
                'week': 2, 'order': 2, 'duration': 60,
                'content_func': 'get_m01_s2_content',
                'exercises': [
                    ('Média de Notas', 'Calcule a média de [8.5, 7.0, 9.5, 6.0, 10.0] e imprima com 1 casa decimal.', 'notas = [8.5, 7.0, 9.5, 6.0, 10.0]\n\n# Calcule a média e imprima\n', '8.2', 'Use sum(notas) / len(notas) e formate com :.1f', 10),
                    ('Filtrando Dicionário', 'Imprima produtos com preço > 50 no formato "produto: R$ X.XX" (em ordem de inserção, um por linha).', 'produtos = {"caneta": 3.50, "notebook": 2500.00, "mouse": 89.90, "borracha": 1.20, "teclado": 150.00}\n\n# Filtre e imprima os produtos com valor > 50\n', 'notebook: R$ 2500.00\nmouse: R$ 89.90\nteclado: R$ 150.00', 'Use: for chave, valor in produtos.items(): if valor > 50:', 15),
                    ('Fibonacci', 'Crie função fibonacci(n) que retorna o n-ésimo número. Imprima fibonacci(10).', 'def fibonacci(n):\n    # F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)\n    pass\n\nprint(fibonacci(10))\n', '55', 'Use um loop: a, b = 0, 1; for _ in range(n): a, b = b, a+b', 15),
                    ('Inverter Lista', 'Dada a lista numeros=[1,2,3,4,5], inverta-a sem usar .reverse() e imprima o resultado.', 'numeros = [1, 2, 3, 4, 5]\n\n# Inverta a lista sem usar .reverse()\n', '[5, 4, 3, 2, 1]', 'Use slicing: numeros[::-1]', 10),
                    ('Contador de Vogais', 'Crie uma função contar_vogais(texto) que retorna o número de vogais. Imprima contar_vogais("Python e incrivel").', 'def contar_vogais(texto):\n    # Conte as vogais (a, e, i, o, u) no texto\n    pass\n\nprint(contar_vogais("Python e incrivel"))\n', '5', 'Use: sum(1 for c in texto.lower() if c in "aeiou")', 10),
                    ('Dicionário de Frequência', 'Conte quantas vezes cada palavra aparece em "a casa e a casa azul". Imprima no formato "palavra: N" ordenado por palavra.', 'frase = "a casa e a casa azul"\n\n# Conte a frequência de cada palavra e imprima\n', 'a: 2\nazul: 1\ncasa: 2\ne: 1', 'Use um dict para contar. sorted() para ordenar as chaves.', 15),
                    ('Fatorial Recursivo', 'Crie a função fatorial(n) recursiva. Imprima fatorial(6).', 'def fatorial(n):\n    # Caso base e chamada recursiva\n    pass\n\nprint(fatorial(6))\n', '720', 'Base: if n <= 1: return 1. Recursão: return n * fatorial(n-1)', 15),
                    ('Lista de Quadrados', 'Crie uma list comprehension com os quadrados dos números de 1 a 8. Imprima a lista.', 'quadrados = []\n\n# Use list comprehension para gerar quadrados de 1 a 8\n', '[1, 4, 9, 16, 25, 36, 49, 64]', 'quadrados = [x**2 for x in range(1, 9)]', 10),
                ]
            },
            {
                'title': 'Semana 3 — Automação com Python',
                'subtitle': 'RPA, tratamento de erros e salvamento de dados',
                'week': 3, 'order': 3, 'duration': 60,
                'content_func': 'get_m01_s3_content',
                'exercises': [
                    ('Tratamento de Erros', 'Crie dividir(a,b) com try/except. Se b=0, retorne "Erro: divisao por zero". Imprima dividir(10,2) e dividir(5,0).', 'def dividir(a, b):\n    # Use try/except para tratar ZeroDivisionError\n    pass\n\nprint(dividir(10, 2))\nprint(dividir(5, 0))\n', '5.0\nErro: divisao por zero', 'try: return a/b  except ZeroDivisionError: return "Erro: divisao por zero"', 15),
                    ('Gerador de Relatório', 'Dados de vendas: {"Segunda": 1500, "Terca": 2300, "Quarta": 1800}. Calcule e imprima "Total: 5600" e "Media: 1866.67".', 'vendas = {"Segunda": 1500, "Terca": 2300, "Quarta": 1800}\n\n# Calcule total e media\n', 'Total: 5600\nMedia: 1866.67', 'total = sum(vendas.values()); media = total/len(vendas)', 15),
                    ('Validador de Senha', 'Crie validar_senha(s) que retorna True se tem 8+ chars, 1 maiúscula e 1 dígito. Imprima validar_senha("Abc12345") e validar_senha("abc").', 'def validar_senha(s):\n    # Verifique: len >= 8, tem maiúscula, tem dígito\n    pass\n\nprint(validar_senha("Abc12345"))\nprint(validar_senha("abc"))\n', 'True\nFalse', 'len(s)>=8 and any(c.isupper() for c in s) and any(c.isdigit() for c in s)', 15),
                    ('Conversor de CSV', 'Dada a lista de dicts, gere uma string CSV (com header). Imprima a string completa.', 'dados = [\n    {"nome": "Ana", "idade": 25},\n    {"nome": "Bob", "idade": 30},\n    {"nome": "Carla", "idade": 28}\n]\n\n# Gere a string CSV\n', 'nome,idade\nAna,25\nBob,30\nCarla,28', 'header = ",".join(dados[0].keys()). Depois itere cada dict.', 15),
                    ('Log de Operações', 'Crie uma lista "log" e adicione 3 strings de log com horário fixo. Imprima cada linha de log.', 'log = []\n\nlog.append("[08:00] Inicio do processo")\nlog.append("[08:05] Dados carregados: 150 registros")\nlog.append("[08:10] Processo finalizado com sucesso")\n\nfor linha in log:\n    print(linha)\n', '[08:00] Inicio do processo\n[08:05] Dados carregados: 150 registros\n[08:10] Processo finalizado com sucesso', 'Basta usar append para adicionar strings formatadas na lista', 10),
                    ('Retry com Contador', 'Simule 3 tentativas de uma operação que falha nas 2 primeiras. Imprima "Tentativa N: falha" ou "Tentativa N: sucesso".', 'resultados = [False, False, True]\n\nfor i, sucesso in enumerate(resultados, 1):\n    # Imprima o resultado de cada tentativa\n    pass\n', 'Tentativa 1: falha\nTentativa 2: falha\nTentativa 3: sucesso', 'print(f"Tentativa {i}: {\'sucesso\' if sucesso else \'falha\'}")', 10),
                    ('Extrator de Dados', 'Extraia nome e valor de cada string no formato "PRODUTO:VALOR". Imprima "produto -> R$ valor".', 'itens = ["Notebook:2500", "Mouse:89", "Teclado:150"]\n\n# Extraia e imprima nome e valor de cada item\n', 'Notebook -> R$ 2500\nMouse -> R$ 89\nTeclado -> R$ 150', 'Use split(":") para separar nome e valor', 10),
                    ('Backup de Dados', 'Crie uma cópia profunda do dict original, modifique a cópia e mostre que o original não mudou. Imprima original["status"] e copia["status"].', 'original = {"nome": "relatorio", "status": "ativo", "versao": 1}\ncopia = {}\n\n# Faça uma cópia, mude status para "arquivado" na cópia\nfor k, v in original.items():\n    copia[k] = v\ncopia["status"] = "arquivado"\n\nprint(original["status"])\nprint(copia["status"])\n', 'ativo\narquivado', 'Copie com dict() ou {**original}, depois modifique a cópia', 10),
                ]
            },
            {
                'title': 'Semana 4 — Pandas e Análise de Dados',
                'subtitle': 'DataFrames, filtros, limpeza e exportação',
                'week': 4, 'order': 4, 'duration': 60,
                'content_func': 'get_m01_s4_content',
                'exercises': [
                    ('Total por Categoria', 'Calcule o total por categoria e imprima "Tech: 3790" e "Mobilia: 1400" (nessa ordem).', 'vendas = [\n    {"produto": "Notebook", "categoria": "Tech", "valor": 2500},\n    {"produto": "Mouse", "categoria": "Tech", "valor": 90},\n    {"produto": "Cadeira", "categoria": "Mobilia", "valor": 800},\n    {"produto": "Monitor", "categoria": "Tech", "valor": 1200},\n    {"produto": "Mesa", "categoria": "Mobilia", "valor": 600},\n]\n\n# Calcule total por categoria\n', 'Tech: 3790\nMobilia: 1400', 'Use um dict para acumular totais', 20),
                    ('Limpeza de Dados', 'Remova None e duplicatas da lista, ordene e imprima cada número em uma linha.', 'dados = [3, 1, None, 4, 1, 5, None, 9, 2, 6, 5, 3]\n\n# Remova None e duplicatas, ordene e imprima\n', '1\n2\n3\n4\n5\n6\n9', 'limpos = sorted(set(x for x in dados if x is not None))', 15),
                    ('Estatísticas Básicas', 'Calcule e imprima min, max e média da lista. Formato: "Min: X", "Max: X", "Media: X.X" (1 decimal).', 'valores = [45, 78, 23, 91, 56, 34, 67, 82, 12, 95]\n\n# Calcule min, max e média\n', 'Min: 12\nMax: 95\nMedia: 58.3', 'Use min(), max(), sum()/len() e formate com :.1f', 10),
                    ('Tabela Formatada', 'Imprima uma tabela formatada com nome (15 chars) e valor (10 chars, alinhado à direita).', 'produtos = [("Notebook", 2500), ("Mouse", 89), ("Teclado", 150)]\n\n# Imprima a tabela formatada\n', 'Notebook             2500\nMouse                  89\nTeclado               150', 'Use f"{nome:<15}{valor:>10}" para formatar', 10),
                    ('Filtro Múltiplo', 'Filtre funcionários com salário > 3000 E setor=="TI". Imprima nome de cada um.', 'funcionarios = [\n    {"nome": "Ana", "salario": 5000, "setor": "TI"},\n    {"nome": "Bob", "salario": 2500, "setor": "TI"},\n    {"nome": "Carla", "salario": 4000, "setor": "RH"},\n    {"nome": "Dan", "salario": 6000, "setor": "TI"},\n]\n\n# Filtre e imprima os nomes\n', 'Ana\nDan', 'Use: if f["salario"] > 3000 and f["setor"] == "TI"', 15),
                    ('Transpor Dados', 'Dada uma lista de dicts, extraia todas as cidades únicas ordenadas e imprima cada uma.', 'registros = [\n    {"nome": "Ana", "cidade": "SP"},\n    {"nome": "Bob", "cidade": "RJ"},\n    {"nome": "Carla", "cidade": "SP"},\n    {"nome": "Dan", "cidade": "BH"},\n    {"nome": "Eva", "cidade": "RJ"},\n]\n\n# Extraia cidades únicas, ordene e imprima\n', 'BH\nRJ\nSP', 'Use sorted(set(r["cidade"] for r in registros))', 10),
                    ('Top N', 'Encontre os 3 produtos mais caros e imprima "nome: valor" (do mais caro ao mais barato).', 'produtos = [\n    {"nome": "Notebook", "valor": 2500},\n    {"nome": "Mouse", "valor": 89},\n    {"nome": "Teclado", "valor": 150},\n    {"nome": "Monitor", "valor": 1200},\n    {"nome": "Cadeira", "valor": 800},\n]\n\n# Encontre os 3 mais caros e imprima\n', 'Notebook: 2500\nMonitor: 1200\nCadeira: 800', 'Use sorted(produtos, key=lambda x: x["valor"], reverse=True)[:3]', 15),
                    ('Percentual', 'Calcule o percentual de cada categoria sobre o total e imprima "categoria: XX.X%".', 'gastos = {"Alimentacao": 800, "Transporte": 400, "Lazer": 300, "Educacao": 500}\ntotal = sum(gastos.values())\n\n# Calcule e imprima os percentuais\n', 'Alimentacao: 40.0%\nTransporte: 20.0%\nLazer: 15.0%\nEducacao: 25.0%', 'Use f"{cat}: {(val/total)*100:.1f}%" para cada item', 10),
                ]
            },
        ]
    },
    {
        'name': 'Automação Avançada com GUI Scripting',
        'short_name': 'Módulo 02 — Automação Avançada',
        'description': 'Saímos do PyAutoGUI e aprendemos GUI scripting nativo — mais robusto e confiável para produção.',
        'price': 200.0,
        'duration': '3 semanas · 3 calls de 1h',
        'level': 'Básico+',
        'color': 'blue',
        'icon': '⚙️',
        'prereqs': 'Módulo 01',
        'tools': 'Python, win32com, COM Scripting',
        'lessons': [
            {'title': 'Semana 1 — Python Intermediário', 'subtitle': 'Funções avançadas, comprehensions, strings', 'week': 1, 'order': 1, 'duration': 60, 'content_func': None, 'exercises': [
                ('List Comprehension Filtrada', 'Crie uma list comprehension com números pares de 1 a 20. Imprima a lista.', 'pares = []\n\n# List comprehension: pares de 1 a 20\n', '[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]', 'pares = [x for x in range(1, 21) if x % 2 == 0]', 10),
                ('Dict Comprehension', 'Crie um dict com {numero: quadrado} para 1 a 5. Imprima o dict.', 'quadrados = {}\n\n# Dict comprehension\n', '{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}', 'quadrados = {x: x**2 for x in range(1, 6)}', 10),
                ('Lambda e Map', 'Use map() com lambda para dobrar cada número de [1,2,3,4,5]. Imprima a lista resultante.', 'numeros = [1, 2, 3, 4, 5]\n\n# Use map + lambda para dobrar\n', '[2, 4, 6, 8, 10]', 'list(map(lambda x: x*2, numeros))', 10),
                ('Função com *args', 'Crie soma_total(*args) que soma todos os argumentos. Imprima soma_total(1,2,3,4,5).', 'def soma_total(*args):\n    pass\n\nprint(soma_total(1, 2, 3, 4, 5))\n', '15', 'return sum(args)', 10),
                ('String Manipulation', 'Dado texto="  Python É INCRÍVEL  ", normalize: strip, lower, substitua "é" por "e". Imprima resultado.', 'texto = "  Python É INCRÍVEL  "\n\n# Normalize o texto\n', 'python e incrível', 'texto.strip().lower().replace("é", "e")', 10),
                ('Enumerate com Condição', 'Imprima índice e nome de frutas que começam com "m" (minúsculo). Formato: "idx: fruta".', 'frutas = ["maça", "banana", "manga", "uva", "melancia"]\n\n# Use enumerate e filtre\n', '0: maça\n2: manga\n4: melancia', 'for i, f in enumerate(frutas): if f.startswith("m"):', 10),
                ('Zip de Listas', 'Combine nomes e notas usando zip. Imprima "nome: nota" para cada par.', 'nomes = ["Ana", "Bob", "Carla"]\nnotas = [9.5, 7.0, 8.5]\n\n# Use zip para combinar e imprimir\n', 'Ana: 9.5\nBob: 7.0\nCarla: 8.5', 'for nome, nota in zip(nomes, notas): print(f"{nome}: {nota}")', 10),
                ('Decorador Simples', 'Crie um decorador que imprime "Inicio" antes e "Fim" depois de chamar a função. Decore saudacao() que imprime "Ola!".', 'def meu_decorador(func):\n    def wrapper():\n        print("Inicio")\n        func()\n        print("Fim")\n    return wrapper\n\n@meu_decorador\ndef saudacao():\n    print("Ola!")\n\nsaudacao()\n', 'Inicio\nOla!\nFim', 'O decorador já está montado, basta executar', 10),
            ]},
            {'title': 'Semana 2 — GUI Scripting Nativo', 'subtitle': 'win32com, scripting direto, grids e tabelas', 'week': 2, 'order': 2, 'duration': 60, 'content_func': None, 'exercises': [
                ('Simulador de Cliques', 'Crie uma lista de 5 ações simuladas (dicts com tipo e coordenada). Imprima cada ação formatada.', 'acoes = [\n    {"tipo": "click", "x": 100, "y": 200},\n    {"tipo": "click", "x": 300, "y": 400},\n    {"tipo": "double_click", "x": 500, "y": 100},\n    {"tipo": "click", "x": 150, "y": 350},\n    {"tipo": "right_click", "x": 200, "y": 250},\n]\n\nfor i, a in enumerate(acoes, 1):\n    print(f"Acao {i}: {a[\'tipo\']} em ({a[\'x\']}, {a[\'y\']})")\n', 'Acao 1: click em (100, 200)\nAcao 2: click em (300, 400)\nAcao 3: double_click em (500, 100)\nAcao 4: click em (150, 350)\nAcao 5: right_click em (200, 250)', 'Itere a lista com enumerate e formate', 10),
                ('Mapeador de Janelas', 'Crie um dict simulando janelas abertas (nome: PID). Imprima cada janela e seu PID.', 'janelas = {\n    "Bloco de Notas": 1234,\n    "Chrome": 5678,\n    "Excel": 9012,\n    "VS Code": 3456\n}\n\nfor nome, pid in janelas.items():\n    print(f"{nome} (PID: {pid})")\n', 'Bloco de Notas (PID: 1234)\nChrome (PID: 5678)\nExcel (PID: 9012)\nVS Code (PID: 3456)', 'Itere com .items()', 10),
                ('Parser de Coordenadas', 'Extraia x,y de strings "100,200" e calcule a distância de cada ponto à origem. Imprima com 1 decimal.', 'pontos = ["100,200", "300,400", "0,0"]\n\nfor p in pontos:\n    x, y = p.split(",")\n    x, y = int(x), int(y)\n    dist = (x**2 + y**2) ** 0.5\n    print(f"({x},{y}) -> {dist:.1f}")\n', '(100,200) -> 223.6\n(300,400) -> 500.0\n(0,0) -> 0.0', 'Use split(",") e ** 0.5 para raiz quadrada', 10),
                ('Sequência de Teclas', 'Crie uma lista de hotkeys e imprima cada combinação numerada.', 'hotkeys = [\n    ("ctrl", "c", "Copiar"),\n    ("ctrl", "v", "Colar"),\n    ("ctrl", "z", "Desfazer"),\n    ("ctrl", "s", "Salvar"),\n    ("alt", "f4", "Fechar"),\n]\n\nfor i, (k1, k2, desc) in enumerate(hotkeys, 1):\n    print(f"{i}. {k1}+{k2} = {desc}")\n', '1. ctrl+c = Copiar\n2. ctrl+v = Colar\n3. ctrl+z = Desfazer\n4. ctrl+s = Salvar\n5. alt+f4 = Fechar', 'Use desempacotamento de tupla no for', 10),
                ('Config Parser', 'Dado um dict de configuração, valide que todas as chaves obrigatórias existem. Imprima "OK" ou "Faltando: chave".', 'config = {"app_name": "MeuBot", "version": "1.0", "timeout": 30}\nobrigatorias = ["app_name", "version", "timeout", "log_file"]\n\nfaltando = [k for k in obrigatorias if k not in config]\nif faltando:\n    for k in faltando:\n        print(f"Faltando: {k}")\nelse:\n    print("OK")\n', 'Faltando: log_file', 'Verifique cada chave obrigatória se está no dict', 10),
                ('Temporizador', 'Simule um countdown de 5 a 1 e imprima cada número seguido de "Executando!" ao final.', 'for i in range(5, 0, -1):\n    print(i)\nprint("Executando!")\n', '5\n4\n3\n2\n1\nExecutando!', 'Use range(5, 0, -1) para countdown', 10),
                ('Gerador de Script', 'Monte uma lista de comandos de automação e imprima cada um como script numerado.', 'comandos = [\n    "Abrir aplicativo",\n    "Aguardar 2 segundos",\n    "Clicar em Login",\n    "Digitar usuario",\n    "Digitar senha",\n    "Clicar em Entrar",\n    "Aguardar carregamento",\n    "Extrair dados"\n]\n\nfor i, cmd in enumerate(comandos, 1):\n    print(f"Passo {i}: {cmd}")\n', 'Passo 1: Abrir aplicativo\nPasso 2: Aguardar 2 segundos\nPasso 3: Clicar em Login\nPasso 4: Digitar usuario\nPasso 5: Digitar senha\nPasso 6: Clicar em Entrar\nPasso 7: Aguardar carregamento\nPasso 8: Extrair dados', 'Use enumerate para numerar', 10),
                ('Detector de Mudança', 'Compare dois dicts (antes/depois) e imprima quais chaves mudaram de valor.', 'antes = {"status": "ativo", "tentativas": 0, "erro": False}\ndepois = {"status": "concluido", "tentativas": 3, "erro": False}\n\nfor chave in antes:\n    if antes[chave] != depois[chave]:\n        print(f"{chave}: {antes[chave]} -> {depois[chave]}")\n', 'status: ativo -> concluido\ntentativas: 0 -> 3', 'Compare os valores de cada chave nos dois dicts', 10),
            ]},
            {'title': 'Semana 3 — Bots Multi-Tela', 'subtitle': 'Parametrização, múltiplos registros, logs', 'week': 3, 'order': 3, 'duration': 60, 'content_func': None, 'exercises': [
                ('Processador em Lote', 'Processe uma lista de 5 registros (dicts) e imprima "Processando: nome" para cada.', 'registros = [\n    {"id": 1, "nome": "Registro A"},\n    {"id": 2, "nome": "Registro B"},\n    {"id": 3, "nome": "Registro C"},\n    {"id": 4, "nome": "Registro D"},\n    {"id": 5, "nome": "Registro E"},\n]\n\nfor r in registros:\n    print(f"Processando: {r[\'nome\']}")\n', 'Processando: Registro A\nProcessando: Registro B\nProcessando: Registro C\nProcessando: Registro D\nProcessando: Registro E', 'Itere a lista e acesse o campo "nome"', 10),
                ('Log Formatado', 'Crie um sistema de log simples. Imprima msgs com nível: "[INFO] msg" ou "[ERRO] msg".', 'logs = [\n    ("INFO", "Sistema iniciado"),\n    ("INFO", "Conectado ao servidor"),\n    ("ERRO", "Timeout na conexao"),\n    ("INFO", "Reconectando..."),\n    ("INFO", "Conexao restaurada"),\n]\n\nfor nivel, msg in logs:\n    print(f"[{nivel}] {msg}")\n', '[INFO] Sistema iniciado\n[INFO] Conectado ao servidor\n[ERRO] Timeout na conexao\n[INFO] Reconectando...\n[INFO] Conexao restaurada', 'Desempacote a tupla (nivel, msg) no for', 10),
                ('Parametrizador', 'Substitua placeholders em um template com valores de um dict. Imprima resultado.', 'template = "Ola {nome}, seu pedido #{pedido} foi {status}."\nparams = {"nome": "Carlos", "pedido": "1234", "status": "enviado"}\n\nresultado = template\nfor chave, valor in params.items():\n    resultado = resultado.replace("{" + chave + "}", valor)\nprint(resultado)\n', 'Ola Carlos, seu pedido #1234 foi enviado.', 'Use replace() para cada placeholder', 10),
                ('Contador de Erros', 'Conte quantos registros deram erro (status=="erro"). Imprima "Erros: N de M" e "Taxa: X%".', 'resultados = [\n    {"id": 1, "status": "ok"},\n    {"id": 2, "status": "erro"},\n    {"id": 3, "status": "ok"},\n    {"id": 4, "status": "erro"},\n    {"id": 5, "status": "ok"},\n    {"id": 6, "status": "ok"},\n    {"id": 7, "status": "erro"},\n    {"id": 8, "status": "ok"},\n]\n\nerros = sum(1 for r in resultados if r["status"] == "erro")\ntotal = len(resultados)\nprint(f"Erros: {erros} de {total}")\nprint(f"Taxa: {(erros/total)*100:.0f}%")\n', 'Erros: 3 de 8\nTaxa: 38%', 'Use sum() com generator expression para contar', 10),
                ('Gerador de IDs', 'Gere IDs no formato "BOT-001" até "BOT-008". Imprima cada um.', 'for i in range(1, 9):\n    print(f"BOT-{i:03d}")\n', 'BOT-001\nBOT-002\nBOT-003\nBOT-004\nBOT-005\nBOT-006\nBOT-007\nBOT-008', 'Use :03d para pad com zeros', 10),
                ('Filtro de Status', 'Filtre registros com status "pendente" e imprima seus nomes.', 'tarefas = [\n    {"nome": "Tarefa A", "status": "concluida"},\n    {"nome": "Tarefa B", "status": "pendente"},\n    {"nome": "Tarefa C", "status": "pendente"},\n    {"nome": "Tarefa D", "status": "concluida"},\n    {"nome": "Tarefa E", "status": "pendente"},\n]\n\npendentes = [t["nome"] for t in tarefas if t["status"] == "pendente"]\nfor p in pendentes:\n    print(p)\n', 'Tarefa B\nTarefa C\nTarefa E', 'Use list comprehension com filtro', 10),
                ('Merge de Configurações', 'Combine config padrão com config do usuário (usuário sobrescreve). Imprima resultado.', 'padrao = {"timeout": 30, "retries": 3, "verbose": False, "log": True}\nusuario = {"timeout": 60, "verbose": True}\n\nfinal = {**padrao, **usuario}\nfor k, v in sorted(final.items()):\n    print(f"{k}: {v}")\n', 'log: True\nretries: 3\ntimeout: 60\nverbose: True', 'Use {**dict1, **dict2} para mergear', 10),
                ('Resumo de Execução', 'Dado histórico de execuções, calcule total, sucesso e falha. Imprima resumo.', 'execucoes = [True, True, False, True, False, True, True, True, False, True]\n\ntotal = len(execucoes)\nsucesso = sum(execucoes)\nfalha = total - sucesso\nprint(f"Total: {total}")\nprint(f"Sucesso: {sucesso}")\nprint(f"Falha: {falha}")\nprint(f"Taxa: {(sucesso/total)*100:.0f}%")\n', 'Total: 10\nSucesso: 7\nFalha: 3\nTaxa: 70%', 'sum(lista_bool) conta os True', 10),
            ]},
        ]
    },
    {
        'name': 'Excel Profissional com Python',
        'short_name': 'Módulo 03 — Excel + Python',
        'description': 'Gere planilhas formatadas com cores, gráficos e fórmulas — 100% automático pelo Python.',
        'price': 200.0,
        'duration': '3 semanas · 3 calls de 1h',
        'level': 'Intermediário',
        'color': 'blue',
        'icon': '📊',
        'prereqs': 'Módulo 01',
        'tools': 'Python, OpenPyXL, Pandas, XlsxWriter',
        'lessons': [
            {'title': 'Semana 1 — Pandas Avançado', 'subtitle': 'Merge, GroupBy, pivot_table, apply', 'week': 1, 'order': 1, 'duration': 60, 'content_func': None, 'exercises': [
                ('GroupBy Simples', 'Agrupe vendas por região e calcule o total. Imprima "regiao: total".', 'vendas = [\n    {"regiao": "Sul", "valor": 100},\n    {"regiao": "Norte", "valor": 200},\n    {"regiao": "Sul", "valor": 150},\n    {"regiao": "Norte", "valor": 300},\n]\n\ntotais = {}\nfor v in vendas:\n    r = v["regiao"]\n    totais[r] = totais.get(r, 0) + v["valor"]\nfor r in sorted(totais):\n    print(f"{r}: {totais[r]}")\n', 'Norte: 500\nSul: 250', 'Use dict.get(key, 0) para acumular', 10),
                ('Merge de Tabelas', 'Combine duas listas usando ID como chave. Imprima "nome - cidade".', 'pessoas = [{"id": 1, "nome": "Ana"}, {"id": 2, "nome": "Bob"}, {"id": 3, "nome": "Carla"}]\ncidades = [{"id": 1, "cidade": "SP"}, {"id": 2, "cidade": "RJ"}, {"id": 3, "cidade": "BH"}]\n\ncidade_map = {c["id"]: c["cidade"] for c in cidades}\nfor p in pessoas:\n    print(f"{p[\'nome\']} - {cidade_map[p[\'id\']]}")\n', 'Ana - SP\nBob - RJ\nCarla - BH', 'Crie um dict de lookup por ID', 10),
                ('Pivot Simples', 'Calcule média de notas por disciplina. Imprima "disciplina: media" com 1 decimal.', 'notas = [\n    {"disc": "Mat", "nota": 8},\n    {"disc": "Port", "nota": 7},\n    {"disc": "Mat", "nota": 9},\n    {"disc": "Port", "nota": 6},\n    {"disc": "Mat", "nota": 7},\n]\n\nsomas = {}\nconts = {}\nfor n in notas:\n    d = n["disc"]\n    somas[d] = somas.get(d, 0) + n["nota"]\n    conts[d] = conts.get(d, 0) + 1\nfor d in sorted(somas):\n    print(f"{d}: {somas[d]/conts[d]:.1f}")\n', 'Mat: 8.0\nPort: 6.5', 'Acumule somas e contagens separadamente', 10),
                ('Apply Simulado', 'Aplique desconto de 10% se valor > 100. Imprima "produto: valor_final".', 'produtos = [("Notebook", 2500), ("Mouse", 89), ("Teclado", 150), ("Cabo", 25)]\n\nfor nome, valor in produtos:\n    final = valor * 0.9 if valor > 100 else valor\n    print(f"{nome}: {final:.0f}")\n', 'Notebook: 2250\nMouse: 89\nTeclado: 135\nCabo: 25', 'Use operador ternário: x if cond else y', 10),
                ('Ranking', 'Ordene produtos por valor decrescente e imprima com posição.', 'produtos = [("Mouse", 89), ("Notebook", 2500), ("Teclado", 150), ("Monitor", 1200)]\n\nordenados = sorted(produtos, key=lambda x: x[1], reverse=True)\nfor i, (nome, valor) in enumerate(ordenados, 1):\n    print(f"{i}. {nome}: R$ {valor}")\n', '1. Notebook: R$ 2500\n2. Monitor: R$ 1200\n3. Teclado: R$ 150\n4. Mouse: R$ 89', 'Use sorted() com key=lambda', 10),
                ('Acumulador', 'Calcule saldo acumulado a partir de transações. Imprima saldo após cada operação.', 'transacoes = [1000, -200, 500, -150, -300, 800]\nsaldo = 0\n\nfor t in transacoes:\n    saldo += t\n    print(f"Saldo: {saldo}")\n', 'Saldo: 1000\nSaldo: 800\nSaldo: 1300\nSaldo: 1150\nSaldo: 850\nSaldo: 1650', 'Acumule com +=', 10),
                ('Filtro Composto', 'Filtre vendas > 100 da região "Sul". Imprima "produto: valor".', 'vendas = [\n    {"produto": "A", "regiao": "Sul", "valor": 150},\n    {"produto": "B", "regiao": "Norte", "valor": 200},\n    {"produto": "C", "regiao": "Sul", "valor": 80},\n    {"produto": "D", "regiao": "Sul", "valor": 250},\n]\n\nfor v in vendas:\n    if v["regiao"] == "Sul" and v["valor"] > 100:\n        print(f"{v[\'produto\']}: {v[\'valor\']}")\n', 'A: 150\nD: 250', 'Combine condições com and', 10),
                ('Resumo Estatístico', 'Calcule min, max, média e total de uma lista de valores. Imprima tudo formatado.', 'valores = [120, 85, 200, 150, 95, 310, 175]\n\nprint(f"Min: {min(valores)}")\nprint(f"Max: {max(valores)}")\nprint(f"Media: {sum(valores)/len(valores):.1f}")\nprint(f"Total: {sum(valores)}")\n', 'Min: 85\nMax: 310\nMedia: 162.1\nTotal: 1135', 'Use min(), max(), sum(), len()', 10),
            ]},
            {'title': 'Semana 2 — OpenPyXL', 'subtitle': 'Formatação, fórmulas, gráficos, imagens', 'week': 2, 'order': 2, 'duration': 60, 'content_func': None, 'exercises': [
                ('Gerador de Cabeçalho', 'Crie uma lista de cabeçalhos de planilha e imprima numerados.', 'colunas = ["ID", "Nome", "Departamento", "Salario", "Admissao", "Status"]\n\nfor i, col in enumerate(colunas, 1):\n    print(f"Coluna {i}: {col}")\n', 'Coluna 1: ID\nColuna 2: Nome\nColuna 3: Departamento\nColuna 4: Salario\nColuna 5: Admissao\nColuna 6: Status', 'Use enumerate para numerar', 10),
                ('Formatador de Moeda', 'Formate valores como moeda brasileira. Imprima cada um.', 'valores = [1500, 89.9, 2500.55, 0, 12345.6]\n\nfor v in valores:\n    print(f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))\n', 'R$ 1.500,00\nR$ 89,90\nR$ 2.500,55\nR$ 0,00\nR$ 12.345,60', 'Troque . por , e vice-versa para formato BR', 15),
                ('Validador de Dados', 'Valide cada registro e imprima OK ou o erro encontrado.', 'registros = [\n    {"nome": "Ana", "idade": 25},\n    {"nome": "", "idade": 30},\n    {"nome": "Bob", "idade": -5},\n    {"nome": "Carla", "idade": 28},\n]\n\nfor r in registros:\n    if not r["nome"]:\n        print("Erro: nome vazio")\n    elif r["idade"] < 0:\n        print("Erro: idade negativa")\n    else:\n        print(f"OK: {r[\'nome\']}")\n', 'OK: Ana\nErro: nome vazio\nErro: idade negativa\nOK: Carla', 'Verifique cada campo com if/elif/else', 10),
                ('Simulador de Fórmula', 'Simule SOMA, MEDIA, MAX e MIN como funções. Imprima resultado de cada.', 'dados = [10, 20, 30, 40, 50]\n\nprint(f"SOMA: {sum(dados)}")\nprint(f"MEDIA: {sum(dados)/len(dados):.1f}")\nprint(f"MAX: {max(dados)}")\nprint(f"MIN: {min(dados)}")\n', 'SOMA: 150\nMEDIA: 30.0\nMAX: 50\nMIN: 10', 'Use as funções built-in do Python', 10),
                ('Tabela de Cores', 'Associe categorias a cores e imprima "categoria -> cor".', 'cores = {\n    "Receita": "verde",\n    "Despesa": "vermelho",\n    "Investimento": "azul",\n    "Reserva": "amarelo"\n}\n\nfor cat, cor in cores.items():\n    print(f"{cat} -> {cor}")\n', 'Receita -> verde\nDespesa -> vermelho\nInvestimento -> azul\nReserva -> amarelo', 'Itere com .items()', 10),
                ('Gerador de Linhas', 'Gere 5 linhas de uma planilha simulada. Imprima cada linha formatada.', 'funcionarios = [\n    (1, "Ana", "TI", 5000),\n    (2, "Bob", "RH", 4000),\n    (3, "Carla", "TI", 6000),\n    (4, "Dan", "Vendas", 3500),\n    (5, "Eva", "TI", 5500),\n]\n\nfor id, nome, dept, sal in funcionarios:\n    print(f"{id} | {nome:<10} | {dept:<8} | R$ {sal}")\n', '1 | Ana        | TI       | R$ 5000\n2 | Bob        | RH       | R$ 4000\n3 | Carla      | TI       | R$ 6000\n4 | Dan        | Vendas   | R$ 3500\n5 | Eva        | TI       | R$ 5500', 'Use formatação com < para alinhar', 10),
                ('Calculadora de Colunas', 'Calcule nova coluna "lucro" (receita - custo) e imprima.', 'dados = [\n    {"produto": "A", "receita": 500, "custo": 300},\n    {"produto": "B", "receita": 800, "custo": 600},\n    {"produto": "C", "receita": 350, "custo": 400},\n]\n\nfor d in dados:\n    lucro = d["receita"] - d["custo"]\n    print(f"{d[\'produto\']}: lucro = {lucro}")\n', 'A: lucro = 200\nB: lucro = 200\nC: lucro = -50', 'Subtraia receita - custo para cada registro', 10),
                ('Detector de Outliers', 'Identifique valores fora de 2x a média e imprima-os como outliers.', 'dados = [10, 12, 11, 13, 50, 9, 11, 12]\nmedia = sum(dados) / len(dados)\n\nfor d in dados:\n    if d > media * 2:\n        print(f"Outlier: {d} (media: {media:.1f})")\n    else:\n        print(f"Normal: {d}")\n', 'Normal: 10\nNormal: 12\nNormal: 11\nNormal: 13\nOutlier: 50 (media: 16.0)\nNormal: 9\nNormal: 11\nNormal: 12', 'Compare cada valor com media * 2', 10),
            ]},
            {'title': 'Semana 3 — Projeto Final', 'subtitle': 'Código reutilizável, integração, datetime', 'week': 3, 'order': 3, 'duration': 60, 'content_func': None, 'exercises': [
                ('Gerador de Datas', 'Gere datas do mês (dia 1 a 5) no formato DD/MM/AAAA. Use 01/2024.', 'mes = 1\nano = 2024\n\nfor dia in range(1, 6):\n    print(f"{dia:02d}/{mes:02d}/{ano}")\n', '01/01/2024\n02/01/2024\n03/01/2024\n04/01/2024\n05/01/2024', 'Use :02d para pad com zero', 10),
                ('Função Reutilizável', 'Crie formatar_valor(v) que retorna "R$ X.XXX,XX" (formato BR). Teste com 3 valores.', 'def formatar_valor(v):\n    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")\n\nprint(formatar_valor(1500))\nprint(formatar_valor(89.9))\nprint(formatar_valor(25000.5))\n', 'R$ 1.500,00\nR$ 89,90\nR$ 25.000,50', 'Formate e substitua separadores', 15),
                ('Pipeline de Dados', 'Aplique 3 transformações em sequência: filtrar > calcular > formatar. Imprima resultado final.', 'dados = [50, 120, 30, 200, 80, 150]\n\nfiltrados = [x for x in dados if x >= 100]\ndobrados = [x * 2 for x in filtrados]\n\nfor v in dobrados:\n    print(f"R$ {v}")\n', 'R$ 240\nR$ 400\nR$ 300', 'Aplique cada transformação em sequência', 10),
                ('Config de Relatório', 'Monte um dict de configuração de relatório e imprima cada setting.', 'config = {\n    "titulo": "Relatorio Mensal",\n    "autor": "Sistema",\n    "formato": "xlsx",\n    "incluir_graficos": True,\n    "max_linhas": 1000\n}\n\nfor k, v in config.items():\n    print(f"{k}: {v}")\n', 'titulo: Relatorio Mensal\nautor: Sistema\nformato: xlsx\nincluir_graficos: True\nmax_linhas: 1000', 'Itere com .items()', 10),
                ('Tratamento de Exceções', 'Converta strings para float com try/except. Imprima valor ou "Erro".', 'valores = ["10.5", "abc", "20.0", "", "30.5"]\n\nfor v in valores:\n    try:\n        num = float(v)\n        print(f"OK: {num}")\n    except (ValueError, Exception):\n        print(f"Erro: \'{v}\'")\n', "OK: 10.5\nErro: 'abc'\nOK: 20.0\nErro: ''\nOK: 30.5", 'Use try/except ValueError', 10),
                ('Gerador de Nome de Arquivo', 'Gere nomes de arquivo com data e sequência. Imprima 4 nomes.', 'data = "2024-01-15"\n\nfor i in range(1, 5):\n    nome = f"relatorio_{data}_v{i:02d}.xlsx"\n    print(nome)\n', 'relatorio_2024-01-15_v01.xlsx\nrelatorio_2024-01-15_v02.xlsx\nrelatorio_2024-01-15_v03.xlsx\nrelatorio_2024-01-15_v04.xlsx', 'Use f-string com :02d para versão', 10),
                ('Validador de Email', 'Crie validar_email(e) que verifica @ e ".". Teste com 4 emails.', 'def validar_email(e):\n    return "@" in e and "." in e.split("@")[-1]\n\nemails = ["ana@email.com", "bob.com", "carla@", "dan@site.org"]\nfor e in emails:\n    print(f"{e}: {\'valido\' if validar_email(e) else \'invalido\'}")\n', 'ana@email.com: valido\nbob.com: invalido\ncarla@: invalido\ndan@site.org: valido', 'Verifique se tem @ e . após o @', 10),
                ('Resumo Final', 'Calcule e imprima um resumo: total, média, maiores e menores que a média.', 'valores = [100, 250, 80, 300, 150, 90, 200]\n\nmedia = sum(valores) / len(valores)\nacima = [v for v in valores if v > media]\nabaixo = [v for v in valores if v <= media]\n\nprint(f"Total: {sum(valores)}")\nprint(f"Media: {media:.1f}")\nprint(f"Acima da media: {len(acima)}")\nprint(f"Abaixo/igual: {len(abaixo)}")\n', 'Total: 1170\nMedia: 167.1\nAcima da media: 3\nAbaixo/igual: 4', 'Use list comprehension para filtrar', 10),
            ]},
        ]
    },
    {
        'name': 'Banco de Dados com Python',
        'short_name': 'Módulo 04 — Banco de Dados',
        'description': 'O próximo passo além do Excel. Banco de dados para guardar histórico e escalar além da planilha.',
        'price': 250.0,
        'duration': '4 semanas · 4 calls de 1h',
        'level': 'Intermediário',
        'color': 'yellow',
        'icon': '�️',
        'prereqs': 'Módulos 01 e 03',
        'tools': 'Python, SQLite, PostgreSQL, psycopg2, DBeaver',
        'lessons': [
            {'title': 'Semana 1 — SQL Básico', 'subtitle': 'SELECT, WHERE, INSERT, funções de agregação', 'week': 1, 'order': 1, 'duration': 60, 'content_func': None, 'exercises': [
                ('SELECT Simples', 'Filtre registros onde idade > 18. Imprima nome de cada.', 'tabela = [\n    {"nome": "Ana", "idade": 25},\n    {"nome": "Bob", "idade": 16},\n    {"nome": "Carla", "idade": 30},\n    {"nome": "Dan", "idade": 15},\n]\nfor r in tabela:\n    if r["idade"] > 18:\n        print(r["nome"])\n', 'Ana\nCarla', 'Itere e filtre com if', 10),
                ('WHERE com AND', 'Filtre setor=="TI" AND salario > 4000. Imprima "nome: salario".', 'dados = [\n    {"nome": "Ana", "setor": "TI", "salario": 5000},\n    {"nome": "Bob", "setor": "RH", "salario": 4500},\n    {"nome": "Carla", "setor": "TI", "salario": 3500},\n    {"nome": "Dan", "setor": "TI", "salario": 6000},\n]\nfor d in dados:\n    if d["setor"] == "TI" and d["salario"] > 4000:\n        print(f"{d[\'nome\']}: {d[\'salario\']}")\n', 'Ana: 5000\nDan: 6000', 'Combine condições com and', 10),
                ('INSERT Simulado', 'Adicione 3 registros a uma lista e imprima a tabela final.', 'tabela = []\ntabela.append({"id": 1, "produto": "Notebook", "preco": 2500})\ntabela.append({"id": 2, "produto": "Mouse", "preco": 89})\ntabela.append({"id": 3, "produto": "Teclado", "preco": 150})\nfor r in tabela:\n    print(f"ID {r[\'id\']}: {r[\'produto\']} - R$ {r[\'preco\']}")\n', 'ID 1: Notebook - R$ 2500\nID 2: Mouse - R$ 89\nID 3: Teclado - R$ 150', 'Use append()', 10),
                ('COUNT e SUM', 'Calcule COUNT, SUM e AVG de vendas. Imprima resultados.', 'vendas = [100, 250, 80, 300, 150]\nprint(f"COUNT: {len(vendas)}")\nprint(f"SUM: {sum(vendas)}")\nprint(f"AVG: {sum(vendas)/len(vendas):.1f}")\n', 'COUNT: 5\nSUM: 880\nAVG: 176.0', 'Use len(), sum()', 10),
                ('ORDER BY', 'Ordene registros por preço decrescente. Imprima "produto: preco".', 'produtos = [\n    {"produto": "Mouse", "preco": 89},\n    {"produto": "Notebook", "preco": 2500},\n    {"produto": "Teclado", "preco": 150},\n]\nfor p in sorted(produtos, key=lambda x: x["preco"], reverse=True):\n    print(f"{p[\'produto\']}: {p[\'preco\']}")\n', 'Notebook: 2500\nTeclado: 150\nMouse: 89', 'Use sorted() com key=lambda', 10),
                ('DISTINCT', 'Extraia valores únicos da coluna "cidade". Imprima ordenado.', 'registros = [\n    {"nome": "Ana", "cidade": "SP"},\n    {"nome": "Bob", "cidade": "RJ"},\n    {"nome": "Carla", "cidade": "SP"},\n    {"nome": "Dan", "cidade": "BH"},\n]\nfor c in sorted(set(r["cidade"] for r in registros)):\n    print(c)\n', 'BH\nRJ\nSP', 'Use set() para únicos', 10),
                ('UPDATE Simulado', 'Atualize salário de "Ana" para 5500. Imprima tabela.', 'tabela = [\n    {"nome": "Ana", "salario": 5000},\n    {"nome": "Bob", "salario": 4000},\n]\nfor r in tabela:\n    if r["nome"] == "Ana":\n        r["salario"] = 5500\nfor r in tabela:\n    print(f"{r[\'nome\']}: {r[\'salario\']}")\n', 'Ana: 5500\nBob: 4000', 'Itere e modifique o registro', 10),
                ('GROUP BY', 'Calcule total de vendas por vendedor. Imprima "vendedor: total".', 'vendas = [\n    {"vendedor": "Ana", "valor": 100},\n    {"vendedor": "Bob", "valor": 200},\n    {"vendedor": "Ana", "valor": 150},\n    {"vendedor": "Bob", "valor": 300},\n]\ntotais = {}\nfor v in vendas:\n    n = v["vendedor"]\n    totais[n] = totais.get(n, 0) + v["valor"]\nfor n in sorted(totais):\n    print(f"{n}: {totais[n]}")\n', 'Ana: 250\nBob: 500', 'Use dict.get() para acumular', 10),
            ]},
            {'title': 'Semana 2 — SQL Intermediário', 'subtitle': 'JOINs, GROUP BY, subqueries, CTEs', 'week': 2, 'order': 2, 'duration': 60, 'content_func': None, 'exercises': [
                ('INNER JOIN', 'Combine pedidos com clientes pelo ID. Imprima "cliente - produto".', 'clientes = {1: "Ana", 2: "Bob", 3: "Carla"}\npedidos = [{"cliente_id": 1, "produto": "Notebook"}, {"cliente_id": 2, "produto": "Mouse"}, {"cliente_id": 1, "produto": "Teclado"}]\nfor p in pedidos:\n    print(f"{clientes[p[\'cliente_id\']]} - {p[\'produto\']}")\n', 'Ana - Notebook\nBob - Mouse\nAna - Teclado', 'Use dict para lookup', 10),
                ('LEFT JOIN', 'Mostre todos os clientes, mesmo sem pedidos.', 'clientes = ["Ana", "Bob", "Carla"]\npedidos = {"Ana": 3, "Bob": 1}\nfor c in clientes:\n    n = pedidos.get(c, 0)\n    print(f"{c}: {n} pedidos")\n', 'Ana: 3 pedidos\nBob: 1 pedidos\nCarla: 0 pedidos', 'Use dict.get(c, 0)', 10),
                ('GROUP BY + HAVING', 'Agrupe por categoria, filtre total > 500.', 'vendas = [\n    {"cat": "Tech", "val": 300},\n    {"cat": "Casa", "val": 150},\n    {"cat": "Tech", "val": 400},\n    {"cat": "Casa", "val": 200},\n]\ntotais = {}\nfor v in vendas:\n    totais[v["cat"]] = totais.get(v["cat"], 0) + v["val"]\nfor cat, total in sorted(totais.items()):\n    if total > 500:\n        print(f"{cat}: {total}")\n', 'Tech: 700', 'Agrupe primeiro, depois filtre', 10),
                ('Subquery', 'Encontre produtos acima da média de preço.', 'precos = [("Notebook", 2500), ("Mouse", 89), ("Teclado", 150), ("Monitor", 1200)]\nmedia = sum(p for _, p in precos) / len(precos)\nfor nome, preco in precos:\n    if preco > media:\n        print(f"{nome}: {preco} (media: {media:.0f})")\n', 'Notebook: 2500 (media: 985)\nMonitor: 1200 (media: 985)', 'Calcule a média primeiro', 10),
                ('UNION', 'Combine duas listas sem duplicatas. Imprima ordenado.', 'l1 = ["Ana", "Bob", "Carla"]\nl2 = ["Bob", "Dan", "Eva"]\nfor nome in sorted(set(l1 + l2)):\n    print(nome)\n', 'Ana\nBob\nCarla\nDan\nEva', 'Use set() para remover duplicatas', 10),
                ('CTE / Ranking', 'Calcule ranking de vendedores por total.', 'vendas = {"Ana": 1500, "Bob": 2300, "Carla": 1800, "Dan": 900}\nfor i, (nome, total) in enumerate(sorted(vendas.items(), key=lambda x: x[1], reverse=True), 1):\n    print(f"{i}. {nome}: R$ {total}")\n', '1. Bob: R$ 2300\n2. Carla: R$ 1800\n3. Ana: R$ 1500\n4. Dan: R$ 900', 'Ordene por valor decrescente', 10),
                ('Múltiplas Tabelas', 'Combine 3 tabelas: produtos, categorias e estoque.', 'produtos = {1: "Notebook", 2: "Mouse"}\ncategorias = {1: "Tech", 2: "Periferico"}\nestoque = {1: 10, 2: 50}\nfor pid in produtos:\n    print(f"{produtos[pid]} | {categorias[pid]} | Estoque: {estoque[pid]}")\n', 'Notebook | Tech | Estoque: 10\nMouse | Periferico | Estoque: 50', 'Use ID como chave comum', 10),
                ('Análise Cruzada', 'Para cada dept, calcule total de funcs e média salarial.', 'from collections import defaultdict\nfuncs = [\n    {"dept": "TI", "sal": 5000},\n    {"dept": "RH", "sal": 4000},\n    {"dept": "TI", "sal": 6000},\n    {"dept": "RH", "sal": 4500},\n    {"dept": "TI", "sal": 5500},\n]\ndepts = defaultdict(list)\nfor f in funcs:\n    depts[f["dept"]].append(f["sal"])\nfor d in sorted(depts):\n    sals = depts[d]\n    print(f"{d}: {len(sals)} func, media R$ {sum(sals)/len(sals):.0f}")\n', 'RH: 2 func, media R$ 4250\nTI: 3 func, media R$ 5500', 'Agrupe salários por departamento', 10),
            ]},
            {'title': 'Semana 3 — Python + Banco', 'subtitle': 'SQLite, PostgreSQL, Pandas + SQL', 'week': 3, 'order': 3, 'duration': 60, 'content_func': None, 'exercises': [
                ('CRUD Completo', 'Simule Create, Read, Update, Delete. Imprima estado final.', 'db = []\ndb.append({"id": 1, "nome": "Ana"})\ndb.append({"id": 2, "nome": "Bob"})\ndb.append({"id": 3, "nome": "Carla"})\nfor r in db:\n    if r["id"] == 2:\n        r["nome"] = "Roberto"\ndb = [r for r in db if r["id"] != 3]\nfor r in db:\n    print(f"{r[\'id\']}: {r[\'nome\']}")\n', '1: Ana\n2: Roberto', 'Modifique e filtre a lista', 10),
                ('Conversor de Tipos', 'Converta strings para tipos corretos. Imprima resultados.', 'registros = [\n    {"nome": "Ana", "idade": "25", "salario": "5000.50"},\n    {"nome": "Bob", "idade": "30", "salario": "4000.00"},\n]\nfor r in registros:\n    print(f"{r[\'nome\']}: {int(r[\'idade\'])} anos, R$ {float(r[\'salario\']):.2f}")\n', 'Ana: 25 anos, R$ 5000.50\nBob: 30 anos, R$ 4000.00', 'Use int() e float()', 10),
                ('Gerador de SQL', 'Gere comandos INSERT a partir de dados Python.', 'dados = [("Ana", 25, "TI"), ("Bob", 30, "RH")]\nfor nome, idade, dept in dados:\n    print(f"INSERT INTO func (nome, idade, dept) VALUES (\'{nome}\', {idade}, \'{dept}\');")\n', "INSERT INTO func (nome, idade, dept) VALUES ('Ana', 25, 'TI');\nINSERT INTO func (nome, idade, dept) VALUES ('Bob', 30, 'RH');", 'Use f-string para montar o SQL', 10),
                ('Tratamento de Nulos', 'Substitua None por valores padrão e imprima.', 'registros = [\n    {"nome": "Ana", "email": "ana@mail.com", "tel": None},\n    {"nome": "Bob", "email": None, "tel": "11999"},\n]\nfor r in registros:\n    email = r["email"] or "N/A"\n    tel = r["tel"] or "N/A"\n    print(f"{r[\'nome\']}: {email}, {tel}")\n', 'Ana: ana@mail.com, N/A\nBob: N/A, 11999', 'Use or "N/A" para substituir None', 10),
                ('Índice Simulado', 'Crie um dict-índice para busca rápida por nome.', 'registros = [\n    {"id": 1, "nome": "Ana", "dept": "TI"},\n    {"id": 2, "nome": "Bob", "dept": "RH"},\n]\nindice = {r["nome"]: r for r in registros}\nfor busca in ["Ana", "Dan"]:\n    r = indice.get(busca)\n    if r:\n        print(f"Encontrado: {r[\'nome\']} ({r[\'dept\']})")\n    else:\n        print(f"Nao encontrado: {busca}")\n', 'Encontrado: Ana (TI)\nNao encontrado: Dan', 'Use dict comprehension para criar índice', 10),
                ('Migração de Dados', 'Transforme formato antigo para novo formato.', 'antigo = [{"nm": "Ana", "sal": "5000"}, {"nm": "Bob", "sal": "4000"}]\nfor r in antigo:\n    novo = {"nome": r["nm"], "salario": float(r["sal"]), "ativo": True}\n    print(f"{novo[\'nome\']}: R$ {novo[\'salario\']:.2f}, ativo={novo[\'ativo\']}")\n', 'Ana: R$ 5000.00, ativo=True\nBob: R$ 4000.00, ativo=True', 'Mapeie campos antigos para novos', 10),
                ('Transação Simulada', 'Simule transação: se der erro, faça rollback.', 'saldo = 1000\nops = [("deposito", 500), ("saque", 200), ("saque", 2000)]\nfor tipo, valor in ops:\n    if tipo == "deposito":\n        saldo += valor\n        print(f"Deposito: +{valor} = {saldo}")\n    elif valor > saldo:\n        print(f"Erro: saldo insuficiente ({saldo} < {valor})")\n    else:\n        saldo -= valor\n        print(f"Saque: -{valor} = {saldo}")\n', 'Deposito: +500 = 1500\nSaque: -200 = 1300\nErro: saldo insuficiente (1300 < 2000)', 'Verifique saldo antes do saque', 10),
                ('Backup de Tabela', 'Crie cópia de tabela e verifique independência.', 'import copy\noriginal = [{"id": 1, "val": 100}, {"id": 2, "val": 200}]\nbackup = copy.deepcopy(original)\nbackup[0]["val"] = 999\nprint(f"Original: {original[0][\'val\']}")\nprint(f"Backup: {backup[0][\'val\']}")\n', 'Original: 100\nBackup: 999', 'Use copy.deepcopy()', 10),
            ]},
            {'title': 'Semana 4 — Pipeline ETL', 'subtitle': 'Extrair, Transformar, Carregar + agendamento', 'week': 4, 'order': 4, 'duration': 60, 'content_func': None, 'exercises': [
                ('Extração CSV', 'Extraia dados de uma string CSV. Imprima cada registro como dict.', 'csv_text = "nome,idade,cidade\\nAna,25,SP\\nBob,30,RJ"\nlinhas = csv_text.split("\\n")\nheader = linhas[0].split(",")\nfor linha in linhas[1:]:\n    vals = linha.split(",")\n    print(dict(zip(header, vals)))\n', "{'nome': 'Ana', 'idade': '25', 'cidade': 'SP'}\n{'nome': 'Bob', 'idade': '30', 'cidade': 'RJ'}", 'Use split e zip com header', 10),
                ('Transformação', 'Transforme dados: upper no nome, int na idade.', 'dados = [{"nome": "ana", "idade": "25"}, {"nome": "bob", "idade": "30"}]\nfor d in dados:\n    print(f"{d[\'nome\'].upper()}, {int(d[\'idade\'])}")\n', 'ANA, 25\nBOB, 30', 'Use .upper() e int()', 10),
                ('Validação e Carga', 'Valide dados antes de carregar. Imprima resultado.', 'dados = [\n    {"nome": "Ana", "idade": 25},\n    {"nome": "", "idade": 30},\n    {"nome": "Carla", "idade": -5},\n    {"nome": "Dan", "idade": 28},\n]\nok = 0\nfor d in dados:\n    if d["nome"] and d["idade"] > 0:\n        ok += 1\n        print(f"OK: {d[\'nome\']}")\n    else:\n        print(f"Rejeitado: {d}")\nprint(f"Total: {ok}")\n', "OK: Ana\nRejeitado: {'nome': '', 'idade': 30}\nRejeitado: {'nome': 'Carla', 'idade': -5}\nOK: Dan\nTotal: 2", 'Valide cada campo antes de inserir', 10),
                ('Pipeline Completo', 'Execute Extract-Transform-Load em sequência.', 'raw = ["  ana,25 ", " bob,30", "carla,28  "]\nextraidos = [r.strip().split(",") for r in raw]\ntransformados = [{"nome": e[0].title(), "idade": int(e[1])} for e in extraidos]\nprint(f"Extraidos: {len(extraidos)}")\nprint(f"Transformados: {len(transformados)}")\nfor t in transformados:\n    print(f"  {t[\'nome\']}: {t[\'idade\']}")\n', 'Extraidos: 3\nTransformados: 3\n  Ana: 25\n  Bob: 30\n  Carla: 28', 'Divida em 3 etapas sequenciais', 15),
                ('Log de ETL', 'Registre log de cada operação. Imprima log.', 'log = []\nlog.append("[1/3] Extraindo 5 registros...")\nlog.append("[2/3] Transformando: 1 removido")\nlog.append("[3/3] Carregando 4 registros")\nlog.append("Pipeline concluido")\nfor l in log:\n    print(l)\n', '[1/3] Extraindo 5 registros...\n[2/3] Transformando: 1 removido\n[3/3] Carregando 4 registros\nPipeline concluido', 'Use lista para acumular mensagens', 10),
                ('Deduplicação', 'Remova registros duplicados mantendo o mais recente.', 'registros = [\n    {"id": 1, "nome": "Ana", "v": 1},\n    {"id": 2, "nome": "Bob", "v": 1},\n    {"id": 1, "nome": "Ana S", "v": 2},\n]\nultimos = {}\nfor r in registros:\n    if r["id"] not in ultimos or r["v"] > ultimos[r["id"]]["v"]:\n        ultimos[r["id"]] = r\nfor r in sorted(ultimos.values(), key=lambda x: x["id"]):\n    print(f"{r[\'id\']}: {r[\'nome\']} (v{r[\'v\']})")\n', '1: Ana S (v2)\n2: Bob (v1)', 'Mantenha registro com maior versão', 10),
                ('Validação em Lote', 'Valide 5 registros e separe em válidos/inválidos.', 'registros = [\n    {"email": "ana@m.com", "idade": 25},\n    {"email": "bob", "idade": 30},\n    {"email": "c@m.com", "idade": -1},\n    {"email": "d@m.com", "idade": 28},\n    {"email": "", "idade": 22},\n]\nv = sum(1 for r in registros if "@" in r["email"] and r["idade"] > 0)\nprint(f"Validos: {v}")\nprint(f"Invalidos: {len(registros)-v}")\n', 'Validos: 2\nInvalidos: 3', 'Verifique email e idade', 10),
                ('Agendamento', 'Simule execução agendada em horários. Imprima cada.', 'agenda = ["08:00", "12:00", "18:00", "23:00"]\nfor i, h in enumerate(agenda, 1):\n    print(f"Execucao {i} agendada para {h}")\nprint(f"Total: {len(agenda)} execucoes")\n', 'Execucao 1 agendada para 08:00\nExecucao 2 agendada para 12:00\nExecucao 3 agendada para 18:00\nExecucao 4 agendada para 23:00\nTotal: 4 execucoes', 'Use enumerate', 10),
            ]},
        ]
    },
    {
        'name': 'Power BI + SQL + Python',
        'short_name': 'Módulo 05 — Power BI',
        'description': 'Unir Python para preparar dados com Power BI para apresentar resultados visuais.',
        'price': 200.0,
        'duration': '3 semanas · 3 calls de 1h',
        'level': 'Intermediário+',
        'color': 'yellow',
        'icon': '�',
        'prereqs': 'Módulos 01 e 04',
        'tools': 'Power BI Desktop, DAX, Python, SQL, PostgreSQL',
        'lessons': [
            {'title': 'Semana 1 — Python + Power BI', 'subtitle': 'Script Python como fonte, Power Query', 'week': 1, 'order': 1, 'duration': 60, 'content_func': None, 'exercises': [
                ('DataFrame Simples', 'Crie tabela com 4 produtos e imprima formatado.', 'tabela = [\n    {"produto": "Notebook", "vendas": 150, "receita": 375000},\n    {"produto": "Mouse", "vendas": 500, "receita": 44500},\n    {"produto": "Teclado", "vendas": 300, "receita": 45000},\n    {"produto": "Monitor", "vendas": 100, "receita": 120000},\n]\nfor r in tabela:\n    print(f"{r[\'produto\']}: {r[\'vendas\']} un, R$ {r[\'receita\']}")\n', 'Notebook: 150 un, R$ 375000\nMouse: 500 un, R$ 44500\nTeclado: 300 un, R$ 45000\nMonitor: 100 un, R$ 120000', 'Itere e formate cada registro', 10),
                ('KPI Calculado', 'Calcule ticket médio (receita/vendas) para cada produto.', 'dados = [("Notebook", 375000, 150), ("Mouse", 44500, 500), ("Teclado", 45000, 300)]\nfor nome, receita, vendas in dados:\n    ticket = receita / vendas\n    print(f"{nome}: R$ {ticket:.2f}")\n', 'Notebook: R$ 2500.00\nMouse: R$ 89.00\nTeclado: R$ 150.00', 'Divida receita por vendas', 10),
                ('Variação YoY', 'Calcule variação ano a ano (%). Imprima "mes: variacao%".', 'atual = [100, 120, 90, 150]\nanterior = [80, 110, 95, 130]\nmeses = ["Jan", "Fev", "Mar", "Abr"]\nfor m, a, ant in zip(meses, atual, anterior):\n    var = ((a - ant) / ant) * 100\n    print(f"{m}: {var:+.1f}%")\n', 'Jan: +25.0%\nFev: +9.1%\nMar: -5.3%\nAbr: +15.4%', 'Use (atual-anterior)/anterior * 100', 10),
                ('Star Schema', 'Monte tabela fato + dimensão e combine. Imprima resultado.', 'dim_produto = {1: "Notebook", 2: "Mouse"}\nfato = [{"prod_id": 1, "qtd": 10, "valor": 25000}, {"prod_id": 2, "qtd": 50, "valor": 4450}]\nfor f in fato:\n    print(f"{dim_produto[f[\'prod_id\']]}: {f[\'qtd\']} un, R$ {f[\'valor\']}")\n', 'Notebook: 10 un, R$ 25000\nMouse: 50 un, R$ 4450', 'Use dict de dimensão para lookup', 10),
                ('Filtro Calculado', 'Filtre vendas por região e calcule total.', 'vendas = [\n    {"regiao": "Sul", "valor": 1000},\n    {"regiao": "Norte", "valor": 2000},\n    {"regiao": "Sul", "valor": 1500},\n    {"regiao": "Norte", "valor": 800},\n]\nfor reg in ["Sul", "Norte"]:\n    total = sum(v["valor"] for v in vendas if v["regiao"] == reg)\n    print(f"{reg}: R$ {total}")\n', 'Sul: R$ 2500\nNorte: R$ 2800', 'Use sum() com generator filtrado', 10),
                ('Formatação Dashboard', 'Formate números para exibição em dashboard.', 'valor = 1234567.89\nprint(f"Inteiro: {valor:,.0f}")\nprint(f"Decimal: {valor:,.2f}")\nprint(f"Milhares: {valor/1000:,.1f}K")\nprint(f"Milhoes: {valor/1000000:,.2f}M")\n', 'Inteiro: 1,234,568\nDecimal: 1,234,567.89\nMilhares: 1,234.6K\nMilhoes: 1.23M', 'Use :, para separador de milhar', 10),
                ('Ranking Top 5', 'Calcule ranking dos top 5 vendedores.', 'vendedores = {"Ana": 45000, "Bob": 32000, "Carla": 58000, "Dan": 41000, "Eva": 55000, "Fran": 28000}\ntop5 = sorted(vendedores.items(), key=lambda x: x[1], reverse=True)[:5]\nfor i, (nome, valor) in enumerate(top5, 1):\n    print(f"{i}. {nome}: R$ {valor:,}")\n', '1. Carla: R$ 58,000\n2. Eva: R$ 55,000\n3. Ana: R$ 45,000\n4. Dan: R$ 41,000\n5. Bob: R$ 32,000', 'Use sorted() e slice [:5]', 10),
                ('Comparativo', 'Compare vendas de 2 períodos e identifique crescimento/queda.', 'q1 = {"Jan": 100, "Fev": 120, "Mar": 90}\nq2 = {"Jan": 110, "Fev": 105, "Mar": 130}\nfor mes in q1:\n    diff = q2[mes] - q1[mes]\n    status = "crescimento" if diff > 0 else "queda"\n    print(f"{mes}: {status} de {abs(diff)}")\n', 'Jan: crescimento de 10\nFev: queda de 15\nMar: crescimento de 40', 'Compare valores dos mesmos meses', 10),
            ]},
            {'title': 'Semana 2 — Modelagem e DAX', 'subtitle': 'Star schema, medidas, KPIs', 'week': 2, 'order': 2, 'duration': 60, 'content_func': None, 'exercises': [
                ('Medida SUM', 'Some todos os valores e imprima total.', 'valores = [1500, 2300, 800, 4200, 1100]\nprint(f"Total: R$ {sum(valores):,}")\n', 'Total: R$ 9,900', 'Use sum()', 10),
                ('Medida AVERAGE', 'Calcule a média com 2 casas.', 'valores = [1500, 2300, 800, 4200, 1100]\nmedia = sum(valores) / len(valores)\nprint(f"Media: R$ {media:,.2f}")\n', 'Media: R$ 1,980.00', 'Use sum()/len()', 10),
                ('COUNTROWS', 'Conte registros por categoria.', 'dados = [{"cat": "A"}, {"cat": "B"}, {"cat": "A"}, {"cat": "A"}, {"cat": "B"}]\ncontagem = {}\nfor d in dados:\n    c = d["cat"]\n    contagem[c] = contagem.get(c, 0) + 1\nfor cat, n in sorted(contagem.items()):\n    print(f"{cat}: {n} registros")\n', 'A: 3 registros\nB: 2 registros', 'Use dict para contar', 10),
                ('Percentual do Total', 'Calcule % de cada item sobre o total.', 'itens = {"Produto A": 300, "Produto B": 500, "Produto C": 200}\ntotal = sum(itens.values())\nfor nome, val in itens.items():\n    pct = (val / total) * 100\n    print(f"{nome}: {pct:.1f}%")\n', 'Produto A: 30.0%\nProduto B: 50.0%\nProduto C: 20.0%', 'Divida valor pelo total * 100', 10),
                ('Running Total', 'Calcule total acumulado mês a mês.', 'meses = [("Jan", 1000), ("Fev", 1500), ("Mar", 800), ("Abr", 2000)]\nacum = 0\nfor mes, val in meses:\n    acum += val\n    print(f"{mes}: R$ {val} (acum: R$ {acum})")\n', 'Jan: R$ 1000 (acum: R$ 1000)\nFev: R$ 1500 (acum: R$ 2500)\nMar: R$ 800 (acum: R$ 3300)\nAbr: R$ 2000 (acum: R$ 5300)', 'Acumule com +=', 10),
                ('Dimensão Tempo', 'Gere dimensão de tempo com trimestre.', 'meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]\nfor i, mes in enumerate(meses, 1):\n    tri = (i - 1) // 3 + 1\n    print(f"{mes} -> Q{tri}")\n', 'Jan -> Q1\nFev -> Q1\nMar -> Q1\nAbr -> Q2\nMai -> Q2\nJun -> Q2', 'Use (i-1)//3 + 1', 10),
                ('Conditional Format', 'Classifique valores como Bom/Regular/Ruim.', 'vendas = [("Ana", 95), ("Bob", 70), ("Carla", 45), ("Dan", 85)]\nfor nome, pct in vendas:\n    if pct >= 80:\n        status = "Bom"\n    elif pct >= 60:\n        status = "Regular"\n    else:\n        status = "Ruim"\n    print(f"{nome}: {pct}% -> {status}")\n', 'Ana: 95% -> Bom\nBob: 70% -> Regular\nCarla: 45% -> Ruim\nDan: 85% -> Bom', 'Use if/elif/else', 10),
                ('Hierarquia', 'Monte hierarquia País > Estado > Cidade.', 'hierarquia = {\n    "Brasil": {\n        "SP": ["Sao Paulo", "Campinas"],\n        "RJ": ["Rio de Janeiro", "Niteroi"]\n    }\n}\nfor pais, estados in hierarquia.items():\n    print(pais)\n    for estado, cidades in estados.items():\n        print(f"  {estado}")\n        for cidade in cidades:\n            print(f"    {cidade}")\n', 'Brasil\n  SP\n    Sao Paulo\n    Campinas\n  RJ\n    Rio de Janeiro\n    Niteroi', 'Use loops aninhados', 10),
            ]},
            {'title': 'Semana 3 — Publicação', 'subtitle': 'Power BI Service, refresh automático', 'week': 3, 'order': 3, 'duration': 60, 'content_func': None, 'exercises': [
                ('Config de Refresh', 'Monte config de refresh e imprima cada setting.', 'config = {\n    "dataset": "Vendas_2024",\n    "schedule": "diario",\n    "horario": "06:00",\n    "timezone": "America/Sao_Paulo",\n    "notify_failure": True\n}\nfor k, v in config.items():\n    print(f"{k}: {v}")\n', 'dataset: Vendas_2024\nschedule: diario\nhorario: 06:00\ntimezone: America/Sao_Paulo\nnotify_failure: True', 'Itere dict com .items()', 10),
                ('Checklist', 'Verifique checklist antes de publicar.', 'checklist = [\n    ("Dados atualizados", True),\n    ("Filtros configurados", True),\n    ("Permissoes definidas", False),\n    ("Tema aplicado", True),\n    ("Testes realizados", False),\n]\nfor item, ok in checklist:\n    status = "OK" if ok else "PENDENTE"\n    print(f"[{status}] {item}")\n', '[OK] Dados atualizados\n[OK] Filtros configurados\n[PENDENTE] Permissoes definidas\n[OK] Tema aplicado\n[PENDENTE] Testes realizados', 'Use ternário para status', 10),
                ('Gateway Status', 'Monitore gateways. Imprima status de cada.', 'gateways = [\n    {"nome": "GW-Principal", "status": "online", "sync": "08:00"},\n    {"nome": "GW-Backup", "status": "offline", "sync": "07:30"},\n    {"nome": "GW-Dev", "status": "online", "sync": "08:15"},\n]\nfor gw in gateways:\n    print(f"{gw[\'nome\']}: {gw[\'status\']} (sync: {gw[\'sync\']})")\n', 'GW-Principal: online (sync: 08:00)\nGW-Backup: offline (sync: 07:30)\nGW-Dev: online (sync: 08:15)', 'Itere e formate', 10),
                ('Workspace Manager', 'Liste workspaces e dashboards.', 'workspaces = {\n    "Financeiro": ["Receita Mensal", "Fluxo de Caixa"],\n    "Vendas": ["Pipeline", "Metas"],\n    "RH": ["Headcount"]\n}\nfor ws, dashboards in workspaces.items():\n    print(f"Workspace: {ws}")\n    for d in dashboards:\n        print(f"  - {d}")\n', 'Workspace: Financeiro\n  - Receita Mensal\n  - Fluxo de Caixa\nWorkspace: Vendas\n  - Pipeline\n  - Metas\nWorkspace: RH\n  - Headcount', 'Use loops aninhados', 10),
                ('Controle de Acesso', 'Defina permissões por role.', 'permissoes = {\n    "Admin": ["visualizar", "editar", "publicar"],\n    "Editor": ["visualizar", "editar"],\n    "Viewer": ["visualizar"]\n}\nfor role, perms in permissoes.items():\n    print(f"{role}: {\\", \\".join(perms)}")\n', 'Admin: visualizar, editar, publicar\nEditor: visualizar, editar\nViewer: visualizar', 'Use join() para concatenar', 10),
                ('Log de Refresh', 'Simule log de refresh com status.', 'historico = [\n    ("2024-01-15 06:00", "sucesso", "2.3s"),\n    ("2024-01-14 06:00", "sucesso", "2.1s"),\n    ("2024-01-13 06:00", "falha", "timeout"),\n    ("2024-01-12 06:00", "sucesso", "2.5s"),\n]\nfor data, status, info in historico:\n    print(f"{data} | {status} | {info}")\n', '2024-01-15 06:00 | sucesso | 2.3s\n2024-01-14 06:00 | sucesso | 2.1s\n2024-01-13 06:00 | falha | timeout\n2024-01-12 06:00 | sucesso | 2.5s', 'Desempacote tupla no for', 10),
                ('Métricas de Uso', 'Calcule métricas de uso do dashboard.', 'acessos = [45, 52, 38, 61, 55, 42, 48]\nprint(f"Total: {sum(acessos)}")\nprint(f"Media: {sum(acessos)/len(acessos):.1f}")\nprint(f"Pico: {max(acessos)}")\nprint(f"Min: {min(acessos)}")\n', 'Total: 341\nMedia: 48.7\nPico: 61\nMin: 38', 'Use sum, len, max, min', 10),
                ('Alerta de Dados', 'Configure alertas para KPIs fora do limite.', 'kpis = {"Receita": 95000, "Margem": 12, "NPS": 45}\nlimites = {"Receita": 100000, "Margem": 15, "NPS": 50}\nfor kpi, val in kpis.items():\n    lim = limites[kpi]\n    status = "ALERTA" if val < lim else "OK"\n    print(f"{kpi}: {val} (limite: {lim}) -> {status}")\n', 'Receita: 95000 (limite: 100000) -> ALERTA\nMargem: 12 (limite: 15) -> ALERTA\nNPS: 45 (limite: 50) -> ALERTA', 'Compare valor com limite', 10),
            ]},
        ]
    },
    {
        'name': 'APIs e Web Scraping com Python',
        'short_name': 'Módulo 06 — APIs + Scraping',
        'description': 'Buscar e integrar dados de qualquer fonte: APIs públicas, sistemas web e portais.',
        'price': 280.0,
        'duration': '4 semanas · 4 calls de 1h',
        'level': 'Avançado',
        'color': 'red',
        'icon': '🌐',
        'prereqs': 'Módulos 01, 03 e 04',
        'tools': 'Python, requests, BeautifulSoup, Selenium, FastAPI',
        'lessons': [
            {'title': 'Semana 1 — Python Avançado', 'subtitle': 'Decoradores, .env, venv, exceções', 'week': 1, 'order': 1, 'duration': 60, 'content_func': None, 'exercises': [
                ('Decorador Timer', 'Crie decorador que imprime execução. Decore uma função.', 'def timer(func):\n    def wrapper(*args):\n        print(f"Executando {func.__name__}...")\n        result = func(*args)\n        print("Concluido")\n        return result\n    return wrapper\n\n@timer\ndef processar(n):\n    print(f"Processando {n} itens")\n\nprocessar(100)\n', 'Executando processar...\nProcessando 100 itens\nConcluido', 'O decorador envolve a função', 10),
                ('Variáveis de Ambiente', 'Simule leitura de .env com dict.get() e default.', 'env = {"API_KEY": "abc123", "DEBUG": "true"}\napi = env.get("API_KEY", "not-set")\ndb = env.get("DATABASE_URL", "sqlite:///local.db")\nprint(f"API_KEY: {api}")\nprint(f"DATABASE_URL: {db}")\n', 'API_KEY: abc123\nDATABASE_URL: sqlite:///local.db', 'Use dict.get() com valor padrão', 10),
                ('Context Manager', 'Simule context manager com classe.', 'class Conexao:\n    def __init__(self, nome):\n        self.nome = nome\n    def __enter__(self):\n        print(f"Conectando a {self.nome}...")\n        return self\n    def __exit__(self, *args):\n        print(f"Desconectando de {self.nome}")\n\nwith Conexao("banco_prod") as conn:\n    print(f"Usando: {conn.nome}")\n', 'Conectando a banco_prod...\nUsando: banco_prod\nDesconectando de banco_prod', 'Implemente __enter__ e __exit__', 10),
                ('Exception Customizada', 'Crie exceção e trate-a.', 'class SaldoInsuficiente(Exception):\n    pass\n\ndef sacar(saldo, valor):\n    if valor > saldo:\n        raise SaldoInsuficiente(f"Saldo {saldo} < {valor}")\n    return saldo - valor\n\ntry:\n    novo = sacar(100, 50)\n    print(f"Saque OK: saldo = {novo}")\n    novo = sacar(novo, 80)\nexcept SaldoInsuficiente as e:\n    print(f"Erro: {e}")\n', 'Saque OK: saldo = 50\nErro: Saldo 50 < 80', 'Crie classe que herda de Exception', 10),
                ('Generator', 'Crie generator que produz pares até N.', 'def pares(n):\n    for i in range(2, n+1, 2):\n        yield i\n\nfor p in pares(10):\n    print(p)\n', '2\n4\n6\n8\n10', 'Use yield', 10),
                ('Dataclass Simulada', 'Crie factory function para produtos.', 'def criar_produto(nome, preco, estoque=0):\n    return {"nome": nome, "preco": preco, "estoque": estoque}\n\nfor p in [criar_produto("Notebook", 2500, 10), criar_produto("Mouse", 89, 50), criar_produto("Teclado", 150)]:\n    print(f"{p[\'nome\']}: R$ {p[\'preco\']} ({p[\'estoque\']} un)")\n', 'Notebook: R$ 2500 (10 un)\nMouse: R$ 89 (50 un)\nTeclado: R$ 150 (0 un)', 'Use função com valores padrão', 10),
                ('Validação em Cadeia', 'Aplique validações em cadeia e imprima erros.', 'def validar(dado):\n    erros = []\n    if not dado.get("nome"):\n        erros.append("Nome obrigatorio")\n    if not dado.get("email") or "@" not in dado["email"]:\n        erros.append("Email invalido")\n    if dado.get("idade", 0) < 18:\n        erros.append("Menor de idade")\n    return erros\n\nfor t in [{"nome": "Ana", "email": "ana@m.com", "idade": 25}, {"nome": "", "email": "x", "idade": 15}]:\n    e = validar(t)\n    print("OK" if not e else f"Erros: {len(e)}")\n', 'OK\nErros: 3', 'Acumule erros em lista', 10),
                ('Type Checking', 'Valide tipos de argumentos.', 'def processar(nome, idade, ativo):\n    erros = []\n    if not isinstance(nome, str): erros.append("nome: str")\n    if not isinstance(idade, int): erros.append("idade: int")\n    if not isinstance(ativo, bool): erros.append("ativo: bool")\n    return "OK" if not erros else "Erros: " + ", ".join(erros)\n\nprint(processar("Ana", 25, True))\nprint(processar(123, "abc", "sim"))\n', 'OK\nErros: nome: str, idade: int, ativo: bool', 'Use isinstance()', 10),
            ]},
            {'title': 'Semana 2 — APIs REST', 'subtitle': 'HTTP, requests, JSON, autenticação', 'week': 2, 'order': 2, 'duration': 60, 'content_func': None, 'exercises': [
                ('Parse JSON', 'Parse JSON string e extraia dados.', 'import json\nj = \'{"nome": "Ana", "idade": 25, "skills": ["Python", "SQL"]}\'\nd = json.loads(j)\nprint(f"Nome: {d[\'nome\']}")\nprint(f"Idade: {d[\'idade\']}")\nprint(f"Skills: {\\", \\".join(d[\'skills\'])}")\n', 'Nome: Ana\nIdade: 25\nSkills: Python, SQL', 'Use json.loads()', 10),
                ('Construir Request', 'Monte headers e params de uma request.', 'headers = {"Authorization": "Bearer abc123", "Content-Type": "application/json"}\nparams = {"page": 1, "limit": 10}\nprint("Headers:")\nfor k, v in headers.items():\n    print(f"  {k}: {v}")\nprint("Params:")\nfor k, v in params.items():\n    print(f"  {k}={v}")\n', 'Headers:\n  Authorization: Bearer abc123\n  Content-Type: application/json\nParams:\n  page=1\n  limit=10', 'Itere dicts', 10),
                ('Response Handler', 'Trate diferentes status codes.', 'responses = [(200, "OK"), (201, "Created"), (404, "Not Found"), (500, "Server Error")]\nfor code, msg in responses:\n    if code < 300:\n        print(f"Sucesso: {code} {msg}")\n    elif code < 500:\n        print(f"Erro cliente: {code} {msg}")\n    else:\n        print(f"Erro servidor: {code} {msg}")\n', 'Sucesso: 200 OK\nSucesso: 201 Created\nErro cliente: 404 Not Found\nErro servidor: 500 Server Error', 'Classifique por faixa', 10),
                ('Query String', 'Monte URL com query params.', 'base = "https://api.exemplo.com/dados"\nparams = {"cidade": "SP", "ano": 2024, "formato": "json"}\nquery = "&".join(f"{k}={v}" for k, v in params.items())\nprint(f"{base}?{query}")\n', 'https://api.exemplo.com/dados?cidade=SP&ano=2024&formato=json', 'Use join() com f-strings', 10),
                ('Paginação', 'Simule paginação de API.', 'todos = list(range(1, 11))\nps = 3\nfor p in range((len(todos)+ps-1)//ps):\n    items = todos[p*ps:(p+1)*ps]\n    print(f"Pagina {p+1}: {items}")\n', 'Pagina 1: [1, 2, 3]\nPagina 2: [4, 5, 6]\nPagina 3: [7, 8, 9]\nPagina 4: [10]', 'Use slicing com offset', 10),
                ('Rate Limiter', 'Simule rate limiting: máx 3 requests.', 'feitos = 0\nfor i in range(1, 6):\n    if feitos < 3:\n        feitos += 1\n        print(f"Request {i}: OK ({feitos}/3)")\n    else:\n        print(f"Request {i}: BLOQUEADO")\n', 'Request 1: OK (1/3)\nRequest 2: OK (2/3)\nRequest 3: OK (3/3)\nRequest 4: BLOQUEADO\nRequest 5: BLOQUEADO', 'Use contador e compare com limite', 10),
                ('Retry Logic', 'Implemente retry com backoff simulado.', 'resultados = [False, False, True]\nfor t, sucesso in enumerate(resultados, 1):\n    if sucesso:\n        print(f"Tentativa {t}: SUCESSO")\n        break\n    print(f"Tentativa {t}: FALHA (retry em {2**t}s)")\n', 'Tentativa 1: FALHA (retry em 2s)\nTentativa 2: FALHA (retry em 4s)\nTentativa 3: SUCESSO', 'Use 2**t para backoff', 10),
                ('JSON to CSV', 'Converta lista de dicts para CSV.', 'dados = [\n    {"nome": "Ana", "cidade": "SP"},\n    {"nome": "Bob", "cidade": "RJ"},\n]\nheader = ",".join(dados[0].keys())\nprint(header)\nfor d in dados:\n    print(",".join(str(v) for v in d.values()))\n', 'nome,cidade\nAna,SP\nBob,RJ', 'Use keys() para header', 10),
            ]},
            {'title': 'Semana 3 — Web Scraping', 'subtitle': 'BeautifulSoup, Selenium, anti-bloqueio', 'week': 3, 'order': 3, 'duration': 60, 'content_func': None, 'exercises': [
                ('Parse HTML', 'Extraia texto de tags simuladas.', 'html_tags = [\n    ("h1", "Titulo da Pagina"),\n    ("p", "Paragrafo de texto"),\n    ("a", "Link importante"),\n]\nfor tag, content in html_tags:\n    print(f"{tag}: {content}")\n', 'h1: Titulo da Pagina\np: Paragrafo de texto\na: Link importante', 'Itere lista de tuplas', 10),
                ('Extração de Links', 'Extraia URLs de links simulados.', 'links = [\n    {"texto": "Google", "url": "https://google.com"},\n    {"texto": "GitHub", "url": "https://github.com"},\n    {"texto": "Python", "url": "https://python.org"},\n]\nfor l in links:\n    print(f"{l[\'texto\']} -> {l[\'url\']}")\n', 'Google -> https://google.com\nGitHub -> https://github.com\nPython -> https://python.org', 'Acesse campos do dict', 10),
                ('Limpeza HTML', 'Remova tags HTML de strings.', 'import re\ntextos = ["<b>Negrito</b>", "<p>Um <em>paragrafo</em></p>", "<div>Conteudo</div>"]\nfor t in textos:\n    print(re.sub(r"<[^>]+>", "", t))\n', 'Negrito\nUm paragrafo\nConteudo', 'Use regex re.sub()', 10),
                ('Tabela HTML', 'Parse dados de tabela HTML simulada.', 'tabela = [\n    ["Nome", "Idade", "Cidade"],\n    ["Ana", "25", "SP"],\n    ["Bob", "30", "RJ"],\n]\nheader = tabela[0]\nfor linha in tabela[1:]:\n    r = dict(zip(header, linha))\n    print(f"{r[\'Nome\']} ({r[\'Idade\']}) - {r[\'Cidade\']}")\n', 'Ana (25) - SP\nBob (30) - RJ', 'Use zip(header, linha)', 10),
                ('User Agent Rotator', 'Rotacione entre user agents.', 'agents = ["Chrome/120", "Firefox/121", "Safari/17"]\nfor i in range(5):\n    ua = agents[i % len(agents)]\n    print(f"Request {i+1}: {ua}")\n', 'Request 1: Chrome/120\nRequest 2: Firefox/121\nRequest 3: Safari/17\nRequest 4: Chrome/120\nRequest 5: Firefox/121', 'Use i % len()', 10),
                ('CSS Selector', 'Simule extração por seletores CSS.', 'elementos = [\n    {"class": "produto", "text": "Notebook R$ 2500"},\n    {"class": "produto", "text": "Mouse R$ 89"},\n    {"class": "header", "text": "Loja Online"},\n    {"class": "produto", "text": "Teclado R$ 150"},\n]\nfor e in elementos:\n    if e["class"] == "produto":\n        print(e["text"])\n', 'Notebook R$ 2500\nMouse R$ 89\nTeclado R$ 150', 'Filtre por class', 10),
                ('Delay entre Requests', 'Simule delays entre requests.', 'delays = [1.0, 2.5, 1.5, 3.0, 2.0]\nfor i, d in enumerate(delays, 1):\n    print(f"Request {i}: aguardando {d}s")\n', 'Request 1: aguardando 1.0s\nRequest 2: aguardando 2.5s\nRequest 3: aguardando 1.5s\nRequest 4: aguardando 3.0s\nRequest 5: aguardando 2.0s', 'Use enumerate', 10),
                ('Dados Estruturados', 'Extraia dados de texto não-estruturado.', 'textos = [\n    "Produto: Notebook | Preco: R$ 2500",\n    "Produto: Mouse | Preco: R$ 89",\n]\nfor t in textos:\n    partes = dict(p.split(": ", 1) for p in t.split(" | "))\n    print(f"{partes[\'Produto\']}: {partes[\'Preco\']}")\n', 'Notebook: R$ 2500\nMouse: R$ 89', 'Use split() para separar', 10),
            ]},
            {'title': 'Semana 4 — Criando API FastAPI', 'subtitle': 'Endpoints GET/POST, Swagger, deploy', 'week': 4, 'order': 4, 'duration': 60, 'content_func': None, 'exercises': [
                ('Endpoint GET', 'Simule response de GET /produtos.', 'import json\nprodutos = [{"id": 1, "nome": "Notebook"}, {"id": 2, "nome": "Mouse"}]\nresponse = {"status": 200, "data": produtos}\nprint(json.dumps(response, indent=2))\n', '{\n  "status": 200,\n  "data": [\n    {\n      "id": 1,\n      "nome": "Notebook"\n    },\n    {\n      "id": 2,\n      "nome": "Mouse"\n    }\n  ]\n}', 'Use json.dumps com indent', 10),
                ('Endpoint POST', 'Simule criação via POST com validação.', 'def criar(data):\n    if not data.get("nome"):\n        return {"status": 400, "erro": "Nome obrigatorio"}\n    return {"status": 201, "data": {**data, "id": 1}}\n\nprint(criar({"nome": "Notebook", "preco": 2500}))\nprint(criar({"nome": ""}))\n', "{'status': 201, 'data': {'nome': 'Notebook', 'preco': 2500, 'id': 1}}\n{'status': 400, 'erro': 'Nome obrigatorio'}", 'Valide antes de criar', 10),
                ('Path Parameters', 'Simule busca por ID.', 'db = {1: "Notebook", 2: "Mouse", 3: "Teclado"}\nfor bid in [1, 5, 3]:\n    if bid in db:\n        print(f"GET /{bid} -> 200: {db[bid]}")\n    else:\n        print(f"GET /{bid} -> 404: Nao encontrado")\n', 'GET /1 -> 200: Notebook\nGET /5 -> 404: Nao encontrado\nGET /3 -> 200: Teclado', 'Verifique se ID existe', 10),
                ('Query Params', 'Filtre lista por query params.', 'produtos = [\n    {"nome": "Notebook", "cat": "Tech", "preco": 2500},\n    {"nome": "Mouse", "cat": "Tech", "preco": 89},\n    {"nome": "Cadeira", "cat": "Moveis", "preco": 800},\n]\nresult = [p for p in produtos if p["cat"] == "Tech" and p["preco"] >= 100]\nfor r in result:\n    print(f"{r[\'nome\']}: R$ {r[\'preco\']}")\n', 'Notebook: R$ 2500', 'Combine filtros com and', 10),
                ('Middleware Auth', 'Simule middleware de autenticação.', 'def auth(headers):\n    token = headers.get("Authorization", "")\n    if not token:\n        return 401, "Token ausente"\n    if token != "Bearer valid123":\n        return 403, "Token invalido"\n    return 200, "OK"\n\nfor h in [{"Authorization": "Bearer valid123"}, {"Authorization": "Bearer wrong"}, {}]:\n    code, msg = auth(h)\n    print(f"{code}: {msg}")\n', '200: OK\n403: Token invalido\n401: Token ausente', 'Verifique token', 10),
                ('Schema Validation', 'Valide schema de request body.', 'schema = {"nome": str, "idade": int}\ndados = {"nome": "Ana", "idade": "25"}\nerros = []\nfor campo, tipo in schema.items():\n    if not isinstance(dados.get(campo), tipo):\n        erros.append(f"{campo}: esperado {tipo.__name__}")\nfor e in erros:\n    print(e)\n', 'idade: esperado int', 'Use isinstance()', 10),
                ('CRUD Router', 'Simule routing de CRUD.', 'rotas = [\n    ("GET", "/produtos", "listar"),\n    ("POST", "/produtos", "criar"),\n    ("PUT", "/produtos/{id}", "atualizar"),\n    ("DELETE", "/produtos/{id}", "deletar"),\n]\nfor method, path, handler in rotas:\n    print(f"{method:7s} {path:20s} -> {handler}")\n', 'GET     /produtos            -> listar\nPOST    /produtos            -> criar\nPUT     /produtos/{id}       -> atualizar\nDELETE  /produtos/{id}       -> deletar', 'Use formatação com largura fixa', 10),
                ('Error Handler', 'Centralize tratamento de erros.', 'msgs = {400: "Requisicao invalida", 401: "Nao autenticado", 404: "Nao encontrado", 500: "Erro interno"}\nfor code in [200, 404, 500, 401]:\n    if code == 200:\n        print(f"{code}: Sucesso")\n    else:\n        print(f"{code}: {msgs.get(code, \'Desconhecido\')}")\n', '200: Sucesso\n404: Nao encontrado\n500: Erro interno\n401: Nao autenticado', 'Use dict para mapear erros', 10),
            ]},
        ]
    },
    {
        'name': 'Georreferenciamento com Python',
        'short_name': 'Módulo 07 — Geo + Python',
        'description': 'Análise espacial com Python — raríssima no mercado. Ideal para infraestrutura e logística.',
        'price': 320.0,
        'duration': '4 semanas · 4 calls de 1h',
        'level': 'Avançado',
        'color': 'red',
        'icon': '�️',
        'prereqs': 'Módulos 01, 03 e 04',
        'tools': 'Python, GeoPandas, Shapely, Folium, QGIS',
        'lessons': [
            {'title': 'Semana 1 — Fundamentos Geo', 'subtitle': 'Coordenadas, projeções, formatos', 'week': 1, 'order': 1, 'duration': 60, 'content_func': None, 'exercises': [
                ('Coordenadas', 'Formate pontos lat/lon com 4 decimais.', 'pontos = [("SP", -23.5505, -46.6333), ("RJ", -22.9068, -43.1729), ("BSB", -15.7801, -47.9292)]\nfor nome, lat, lon in pontos:\n    print(f"{nome}: {lat:.4f}, {lon:.4f}")\n', 'SP: -23.5505, -46.6333\nRJ: -22.9068, -43.1729\nBSB: -15.7801, -47.9292', 'Use :.4f', 10),
                ('Distância Euclidiana', 'Calcule distância entre 2 pontos.', 'p1 = (0, 0)\np2 = (3, 4)\ndist = ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2) ** 0.5\nprint(f"Distancia: {dist:.1f}")\n', 'Distancia: 5.0', 'Use fórmula euclidiana', 10),
                ('Bounding Box', 'Calcule bounding box de pontos.', 'pontos = [(1,2), (5,8), (3,1), (7,4), (2,6)]\nxs = [p[0] for p in pontos]\nys = [p[1] for p in pontos]\nprint(f"X: {min(xs)} a {max(xs)}")\nprint(f"Y: {min(ys)} a {max(ys)}")\n', 'X: 1 a 7\nY: 1 a 8', 'Use min() e max()', 10),
                ('DMS para Decimal', 'Converta graus/min/seg para decimal.', 'def dms(g, m, s, d):\n    dec = g + m/60 + s/3600\n    return -dec if d in "SW" else dec\n\nprint(f"Lat: {dms(23, 33, 1.8, \'S\'):.4f}")\nprint(f"Lon: {dms(46, 38, 0.0, \'W\'):.4f}")\n', 'Lat: -23.5505\nLon: -46.6333', 'Divida min por 60 e seg por 3600', 10),
                ('Classificar Zona', 'Classifique pontos por hemisférios.', 'pontos = [(10, 20, "A"), (-15, -46, "B"), (40, -74, "C")]\nfor lat, lon, nome in pontos:\n    ns = "N" if lat >= 0 else "S"\n    lo = "L" if lon >= 0 else "O"\n    print(f"{nome}: {ns}/{lo}")\n', 'A: N/L\nB: S/O\nC: N/O', 'Verifique sinal de lat e lon', 10),
                ('Área Retangular', 'Calcule área de retângulo em coords.', 'x1, y1 = 0, 0\nx2, y2 = 10, 5\narea = abs(x2-x1) * abs(y2-y1)\nprint(f"Largura: {abs(x2-x1)}")\nprint(f"Altura: {abs(y2-y1)}")\nprint(f"Area: {area}")\n', 'Largura: 10\nAltura: 5\nArea: 50', 'Use abs()', 10),
                ('Ponto no Retângulo', 'Verifique se pontos estão dentro de um retângulo.', 'bbox = (0, 0, 10, 10)\npontos = [(5,5), (15,5), (0,0), (10,11)]\nfor x, y in pontos:\n    dentro = bbox[0] <= x <= bbox[2] and bbox[1] <= y <= bbox[3]\n    print(f"({x},{y}): {\'dentro\' if dentro else \'fora\'}")\n', '(5,5): dentro\n(15,5): fora\n(0,0): dentro\n(10,11): fora', 'Verifique limites x e y', 10),
                ('GeoJSON', 'Monte estrutura GeoJSON com pontos.', 'features = [\n    {"nome": "SP", "coords": [-46.63, -23.55]},\n    {"nome": "RJ", "coords": [-43.17, -22.91]},\n]\nfor f in features:\n    print(f"{f[\'nome\']}: {f[\'coords\']}")\n', "SP: [-46.63, -23.55]\nRJ: [-43.17, -22.91]", 'Acesse propriedades', 10),
            ]},
            {'title': 'Semana 2 — GeoPandas + Shapely', 'subtitle': 'Buffer, intersect, spatial join', 'week': 2, 'order': 2, 'duration': 60, 'content_func': None, 'exercises': [
                ('Buffer Circular', 'Calcule área de buffer circular.', 'import math\npontos = [("Torre A", 5), ("Torre B", 10), ("Torre C", 3)]\nfor nome, raio in pontos:\n    area = math.pi * raio ** 2\n    print(f"{nome}: raio={raio}, area={area:.1f}")\n', 'Torre A: raio=5, area=78.5\nTorre B: raio=10, area=314.2\nTorre C: raio=3, area=28.3', 'Use pi * r^2', 10),
                ('Intersecção', 'Verifique se 2 retângulos se intersectam.', 'def inter(r1, r2):\n    return not (r1[2]<r2[0] or r2[2]<r1[0] or r1[3]<r2[1] or r2[3]<r1[1])\n\nprint(f"A-B: {inter((0,0,5,5), (3,3,8,8))}")\nprint(f"A-C: {inter((0,0,5,5), (6,6,10,10))}")\n', 'A-B: True\nA-C: False', 'Retângulos NÃO se intersectam se separados', 10),
                ('Centroide', 'Calcule centroide de polígono.', 'vertices = [(0,0), (10,0), (10,5), (0,5)]\ncx = sum(v[0] for v in vertices) / len(vertices)\ncy = sum(v[1] for v in vertices) / len(vertices)\nprint(f"Centroide: ({cx:.1f}, {cy:.1f})")\n', 'Centroide: (5.0, 2.5)', 'Média de x e y', 10),
                ('Spatial Join', 'Associe pontos a zonas.', 'zonas = {"Norte": (0,50,100,100), "Sul": (0,0,100,50)}\npontos = [("A", 30, 70), ("B", 50, 30), ("C", 80, 60)]\nfor nome, x, y in pontos:\n    zona = "N/A"\n    for z, (x1,y1,x2,y2) in zonas.items():\n        if x1<=x<=x2 and y1<=y<=y2:\n            zona = z\n    print(f"{nome}: {zona}")\n', 'A: Norte\nB: Sul\nC: Norte', 'Verifique em qual zona', 10),
                ('Distância Manhattan', 'Calcule distância Manhattan entre pares.', 'pares = [((0,0),(3,4)), ((1,1),(5,5)), ((2,3),(7,1))]\nfor p1, p2 in pares:\n    d = abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])\n    print(f"{p1} -> {p2}: {d}")\n', '(0, 0) -> (3, 4): 7\n(1, 1) -> (5, 5): 8\n(2, 3) -> (7, 1): 7', 'Soma dos abs das diferenças', 10),
                ('Nearest Neighbor', 'Encontre ponto mais próximo de um alvo.', 'alvo = (5, 5)\npontos = [("A",1,1), ("B",4,6), ("C",8,2), ("D",6,4)]\nmelhor = min(pontos, key=lambda p: ((p[1]-alvo[0])**2+(p[2]-alvo[1])**2)**0.5)\nprint(f"Mais proximo: {melhor[0]}")\n', 'Mais proximo: D', 'Use min() com key=distância', 10),
                ('Perímetro', 'Calcule perímetro de um polígono.', 'vertices = [(0,0), (4,0), (4,3), (0,3)]\nperim = 0\nfor i in range(len(vertices)):\n    x1,y1 = vertices[i]\n    x2,y2 = vertices[(i+1) % len(vertices)]\n    perim += ((x2-x1)**2 + (y2-y1)**2) ** 0.5\nprint(f"Perimetro: {perim:.1f}")\n', 'Perimetro: 14.0', 'Some distâncias entre vértices consecutivos', 10),
                ('Converter CRS', 'Simule conversão de coordenadas com fator de escala.', 'pontos = [(-23.55, -46.63), (-22.91, -43.17)]\nfor lat, lon in pontos:\n    x = lon * 111320\n    y = lat * 110540\n    print(f"({lat},{lon}) -> ({x:.0f}, {y:.0f})")\n', '(-23.55,-46.63) -> (-5190082, -2603217)\n(-22.91,-43.17) -> (-4805252, (-2532474)', 'Multiplique por fator de conversão', 10),
            ]},
            {'title': 'Semana 3 — DXF / AutoCAD', 'subtitle': 'ezdxf, converter para GeoDataFrame', 'week': 3, 'order': 3, 'duration': 60, 'content_func': None, 'exercises': [
                ('Layers DXF', 'Liste layers de um DXF simulado.', 'layers = [\n    {"nome": "Lotes", "cor": "amarelo", "elementos": 150},\n    {"nome": "Ruas", "cor": "branco", "elementos": 45},\n    {"nome": "Edificios", "cor": "vermelho", "elementos": 80},\n]\nfor l in layers:\n    print(f"{l[\'nome\']}: {l[\'elementos\']} elementos ({l[\'cor\']})")\n', 'Lotes: 150 elementos (amarelo)\nRuas: 45 elementos (branco)\nEdificios: 80 elementos (vermelho)', 'Itere e formate', 10),
                ('Linhas para Pontos', 'Extraia pontos de linhas simuladas.', 'linhas = [\n    {"id": 1, "inicio": (0,0), "fim": (10,0)},\n    {"id": 2, "inicio": (10,0), "fim": (10,5)},\n    {"id": 3, "inicio": (10,5), "fim": (0,5)},\n]\nfor l in linhas:\n    print(f"Linha {l[\'id\']}: {l[\'inicio\']} -> {l[\'fim\']}")\n', 'Linha 1: (0, 0) -> (10, 0)\nLinha 2: (10, 0) -> (10, 5)\nLinha 3: (10, 5) -> (0, 5)', 'Acesse inicio e fim de cada', 10),
                ('Comprimento Total', 'Calcule comprimento total de linhas.', 'linhas = [((0,0),(10,0)), ((10,0),(10,5)), ((10,5),(0,5))]\ntotal = 0\nfor (x1,y1),(x2,y2) in linhas:\n    comp = ((x2-x1)**2 + (y2-y1)**2) ** 0.5\n    total += comp\n    print(f"Segmento: {comp:.1f}")\nprint(f"Total: {total:.1f}")\n', 'Segmento: 10.0\nSegmento: 5.0\nSegmento: 10.0\nTotal: 25.0', 'Some distâncias de cada segmento', 10),
                ('Filtro por Layer', 'Filtre elementos por layer específico.', 'elementos = [\n    {"layer": "Lotes", "tipo": "polygon", "area": 500},\n    {"layer": "Ruas", "tipo": "line", "area": 0},\n    {"layer": "Lotes", "tipo": "polygon", "area": 800},\n    {"layer": "Edificios", "tipo": "polygon", "area": 200},\n]\nlotes = [e for e in elementos if e["layer"] == "Lotes"]\nfor l in lotes:\n    print(f"Lote: {l[\'area\']}m2")\n', 'Lote: 500m2\nLote: 800m2', 'Filtre com list comprehension', 10),
                ('Escala de Desenho', 'Aplique fator de escala a coordenadas.', 'coords = [(0,0), (100,0), (100,50), (0,50)]\nescala = 0.001\nfor x, y in coords:\n    print(f"({x},{y}) -> ({x*escala:.3f},{y*escala:.3f})")\n', '(0,0) -> (0.000,0.000)\n(100,0) -> (0.100,0.000)\n(100,50) -> (0.100,0.050)\n(0,50) -> (0.000,0.050)', 'Multiplique por fator de escala', 10),
                ('Metadata DXF', 'Extraia metadados de arquivo simulado.', 'meta = {\n    "arquivo": "planta_loteamento.dxf",\n    "versao": "AutoCAD 2024",\n    "unidade": "metros",\n    "layers": 5,\n    "entidades": 1250\n}\nfor k, v in meta.items():\n    print(f"{k}: {v}")\n', 'arquivo: planta_loteamento.dxf\nversao: AutoCAD 2024\nunidade: metros\nlayers: 5\nentidades: 1250', 'Itere dict', 10),
                ('Agrupar por Tipo', 'Agrupe entidades por tipo e conte.', 'entidades = ["line","line","circle","polygon","line","circle","polygon","polygon","line"]\ncontagem = {}\nfor e in entidades:\n    contagem[e] = contagem.get(e, 0) + 1\nfor tipo, n in sorted(contagem.items()):\n    print(f"{tipo}: {n}")\n', 'circle: 2\nline: 4\npolygon: 3', 'Use dict.get()', 10),
                ('Converter Unidades', 'Converta entre metros e pés.', 'metros = [10, 25.5, 100, 3.7]\nfor m in metros:\n    pes = m * 3.28084\n    print(f"{m}m = {pes:.1f}ft")\n', '10m = 32.8ft\n25.5m = 83.7ft\n100m = 328.1ft\n3.7m = 12.1ft', 'Multiplique por 3.28084', 10),
            ]},
            {'title': 'Semana 4 — Mapas Folium', 'subtitle': 'Mapas interativos, choropleth, HTML', 'week': 4, 'order': 4, 'duration': 60, 'content_func': None, 'exercises': [
                ('Config de Mapa', 'Monte config de mapa e imprima settings.', 'config = {\n    "centro": [-23.55, -46.63],\n    "zoom": 12,\n    "tiles": "OpenStreetMap",\n    "width": "100%",\n    "height": "600px"\n}\nfor k, v in config.items():\n    print(f"{k}: {v}")\n', "centro: [-23.55, -46.63]\nzoom: 12\ntiles: OpenStreetMap\nwidth: 100%\nheight: 600px", 'Itere dict', 10),
                ('Marcadores', 'Monte lista de marcadores com popup.', 'marcadores = [\n    {"nome": "Escritorio", "lat": -23.55, "lon": -46.63, "cor": "blue"},\n    {"nome": "Cliente A", "lat": -23.56, "lon": -46.64, "cor": "red"},\n    {"nome": "Cliente B", "lat": -23.54, "lon": -46.62, "cor": "green"},\n]\nfor m in marcadores:\n    print(f"{m[\'nome\']} ({m[\'lat\']},{m[\'lon\']}) - {m[\'cor\']}")\n', 'Escritorio (-23.55,-46.63) - blue\nCliente A (-23.56,-46.64) - red\nCliente B (-23.54,-46.62) - green', 'Acesse campos do dict', 10),
                ('Choropleth Data', 'Prepare dados para mapa choropleth.', 'regioes = {"Norte": 450, "Sul": 680, "Leste": 320, "Oeste": 550}\nmax_val = max(regioes.values())\nfor reg, val in regioes.items():\n    pct = (val/max_val)*100\n    print(f"{reg}: {val} ({pct:.0f}%)")\n', 'Norte: 450 (66%)\nSul: 680 (100%)\nLeste: 320 (47%)\nOeste: 550 (81%)', 'Normalize pelo max', 10),
                ('Legenda', 'Gere legenda de cores para mapa.', 'legenda = [\n    ("0-100", "#fee5d9"),\n    ("100-500", "#fcae91"),\n    ("500-1000", "#fb6a4a"),\n    (">1000", "#cb181d"),\n]\nfor faixa, cor in legenda:\n    print(f"{faixa}: {cor}")\n', '0-100: #fee5d9\n100-500: #fcae91\n500-1000: #fb6a4a\n>1000: #cb181d', 'Itere lista de tuplas', 10),
                ('Popup HTML', 'Gere HTML para popup de marcador.', 'dados = {"nome": "Lote 15", "area": 500, "zona": "Residencial", "valor": 150000}\nhtml = f"<b>{dados[\'nome\']}</b><br>"\nhtml += f"Area: {dados[\'area\']}m2<br>"\nhtml += f"Zona: {dados[\'zona\']}<br>"\nhtml += f"Valor: R$ {dados[\'valor\']:,}"\nprint(html)\n', '<b>Lote 15</b><br>Area: 500m2<br>Zona: Residencial<br>Valor: R$ 150,000', 'Use f-strings para montar HTML', 10),
                ('Classificar por Faixa', 'Classifique valores em faixas de cor.', 'valores = [50, 250, 750, 1200, 400]\nfor v in valores:\n    if v < 100: cor = "verde"\n    elif v < 500: cor = "amarelo"\n    elif v < 1000: cor = "laranja"\n    else: cor = "vermelho"\n    print(f"{v}: {cor}")\n', '50: verde\n250: amarelo\n750: laranja\n1200: vermelho\n400: amarelo', 'Use if/elif/else', 10),
                ('Exportar Coords', 'Exporte coordenadas em formato CSV.', 'pontos = [("SP",-23.55,-46.63), ("RJ",-22.91,-43.17), ("BH",-19.92,-43.94)]\nprint("nome,lat,lon")\nfor nome, lat, lon in pontos:\n    print(f"{nome},{lat},{lon}")\n', 'nome,lat,lon\nSP,-23.55,-46.63\nRJ,-22.91,-43.17\nBH,-19.92,-43.94', 'Formate como CSV', 10),
                ('Resumo Geo', 'Calcule estatísticas de um conjunto de pontos.', 'lats = [-23.55, -22.91, -19.92, -15.78]\nlons = [-46.63, -43.17, -43.94, -47.93]\nprint(f"Lat min: {min(lats)}")\nprint(f"Lat max: {max(lats)}")\nprint(f"Lon min: {min(lons)}")\nprint(f"Lon max: {max(lons)}")\nprint(f"Pontos: {len(lats)}")\n', 'Lat min: -23.55\nLat max: -15.78\nLon min: -47.93\nLon max: -43.17\nPontos: 4', 'Use min, max, len', 10),
            ]},
        ]
    },
    {
        'name': 'Projeto Integrador Final',
        'short_name': 'Módulo 08 — Projeto Final',
        'description': 'Tudo aplicado em um sistema real, construído do zero. Projeto funcional no portfólio.',
        'price': 400.0,
        'duration': '4 semanas · 4 calls de 1h',
        'level': 'Expert',
        'color': 'black',
        'icon': '�',
        'prereqs': 'Módulos 01 a 07 (mínimo 01 a 05)',
        'tools': 'Todas as anteriores + Git, GitHub, Docker',
        'lessons': [
            {'title': 'Semana 1 — Arquitetura', 'subtitle': 'Planejamento, Git, GitHub, documentação', 'week': 1, 'order': 1, 'duration': 60, 'content_func': None, 'exercises': [
                ('Estrutura de Projeto', 'Monte estrutura de pastas de um projeto e imprima como árvore.', 'pastas = [\n    "projeto/",\n    "  src/",\n    "    main.py",\n    "    utils.py",\n    "  tests/",\n    "    test_main.py",\n    "  docs/",\n    "    README.md",\n]\nfor p in pastas:\n    print(p)\n', 'projeto/\n  src/\n    main.py\n    utils.py\n  tests/\n    test_main.py\n  docs/\n    README.md', 'Use indentação para hierarquia', 10),
                ('Git Log', 'Simule log de commits e imprima formatado.', 'commits = [\n    ("abc1234", "feat: adicionar ETL", "2024-01-15"),\n    ("def5678", "fix: corrigir encoding", "2024-01-14"),\n    ("ghi9012", "docs: atualizar README", "2024-01-13"),\n]\nfor hash, msg, data in commits:\n    print(f"{hash[:7]} {data} {msg}")\n', 'abc1234 2024-01-15 feat: adicionar ETL\ndef5678 2024-01-14 fix: corrigir encoding\nghi9012 2024-01-13 docs: atualizar README', 'Formate cada commit', 10),
                ('Gitignore', 'Monte lista de padrões gitignore e imprima.', 'patterns = ["__pycache__/", "*.pyc", ".env", "venv/", "*.db", ".DS_Store", "dist/", "*.log"]\nfor p in patterns:\n    print(p)\n', '__pycache__/\n*.pyc\n.env\nvenv/\n*.db\n.DS_Store\ndist/\n*.log', 'Liste cada padrão', 10),
                ('Requirements', 'Monte requirements.txt simulado.', 'deps = [\n    ("flask", "3.0.0"),\n    ("pandas", "2.1.4"),\n    ("requests", "2.31.0"),\n    ("sqlalchemy", "2.0.23"),\n]\nfor pkg, ver in deps:\n    print(f"{pkg}=={ver}")\n', 'flask==3.0.0\npandas==2.1.4\nrequests==2.31.0\nsqlalchemy==2.0.23', 'Formate como pkg==versão', 10),
                ('README Generator', 'Gere seções de README e imprima.', 'secoes = ["# Projeto ETL", "## Instalacao", "```pip install -r requirements.txt```", "## Uso", "```python main.py```", "## Testes", "```pytest```"]\nfor s in secoes:\n    print(s)\n', '# Projeto ETL\n## Instalacao\n```pip install -r requirements.txt```\n## Uso\n```python main.py```\n## Testes\n```pytest```', 'Imprima cada seção', 10),
                ('Semantic Versioning', 'Incremente versões seguindo semver.', 'versao = [1, 2, 3]\ntipos = ["patch", "minor", "major"]\nfor tipo in tipos:\n    v = versao.copy()\n    if tipo == "patch": v[2] += 1\n    elif tipo == "minor": v[1] += 1; v[2] = 0\n    else: v[0] += 1; v[1] = 0; v[2] = 0\n    print(f"{tipo}: {v[0]}.{v[1]}.{v[2]}")\n', 'patch: 1.2.4\nminor: 1.3.0\nmajor: 2.0.0', 'Patch++, minor++ e zera patch, etc', 10),
                ('Config YAML', 'Monte config de projeto e imprima.', 'config = {\n    "app_name": "meu_projeto",\n    "version": "1.0.0",\n    "database": "postgresql://localhost/db",\n    "debug": False,\n    "workers": 4\n}\nfor k, v in config.items():\n    print(f"{k}: {v}")\n', 'app_name: meu_projeto\nversion: 1.0.0\ndatabase: postgresql://localhost/db\ndebug: False\nworkers: 4', 'Itere dict', 10),
                ('Checklist de Projeto', 'Verifique checklist de início de projeto.', 'checklist = [\n    ("Repo criado", True),\n    ("README escrito", True),\n    (".gitignore", True),\n    ("CI/CD configurado", False),\n    ("Testes iniciais", False),\n]\nfor item, ok in checklist:\n    print(f"[{\'x\' if ok else \' \'}] {item}")\n', '[x] Repo criado\n[x] README escrito\n[x] .gitignore\n[ ] CI/CD configurado\n[ ] Testes iniciais', 'Use ternário para x ou espaço', 10),
            ]},
            {'title': 'Semana 2 — Docker', 'subtitle': 'Dockerfile, Compose, agendamento', 'week': 2, 'order': 2, 'duration': 60, 'content_func': None, 'exercises': [
                ('Dockerfile', 'Monte instruções de Dockerfile e imprima.', 'instrucoes = [\n    "FROM python:3.11-slim",\n    "WORKDIR /app",\n    "COPY requirements.txt .",\n    "RUN pip install -r requirements.txt",\n    "COPY . .",\n    "CMD [\\"python\\", \\"main.py\\"]",\n]\nfor inst in instrucoes:\n    print(inst)\n', 'FROM python:3.11-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY . .\nCMD ["python", "main.py"]', 'Imprima cada instrução', 10),
                ('Docker Compose', 'Monte serviços de compose e imprima.', 'servicos = {\n    "web": {"image": "python:3.11", "ports": "5000:5000"},\n    "db": {"image": "postgres:15", "ports": "5432:5432"},\n    "redis": {"image": "redis:7", "ports": "6379:6379"},\n}\nfor nome, cfg in servicos.items():\n    print(f"{nome}: {cfg[\'image\']} ({cfg[\'ports\']})")\n', 'web: python:3.11 (5000:5000)\ndb: postgres:15 (5432:5432)\nredis: redis:7 (6379:6379)', 'Itere dict de serviços', 10),
                ('Env Variables', 'Monte .env e imprima variáveis.', 'env_vars = [\n    ("DATABASE_URL", "postgresql://user:pass@db:5432/app"),\n    ("SECRET_KEY", "minha-chave-secreta"),\n    ("DEBUG", "false"),\n    ("WORKERS", "4"),\n]\nfor key, val in env_vars:\n    print(f"{key}={val}")\n', 'DATABASE_URL=postgresql://user:pass@db:5432/app\nSECRET_KEY=minha-chave-secreta\nDEBUG=false\nWORKERS=4', 'Formate como KEY=VALUE', 10),
                ('Container Status', 'Simule docker ps e imprima.', 'containers = [\n    ("web-1", "running", "5000:5000", "2h"),\n    ("db-1", "running", "5432:5432", "2h"),\n    ("redis-1", "exited", "6379:6379", "1h"),\n]\nfor nome, status, ports, uptime in containers:\n    print(f"{nome:12s} {status:10s} {ports:15s} {uptime}")\n', 'web-1        running    5000:5000       2h\ndb-1         running    5432:5432       2h\nredis-1      exited     6379:6379       1h', 'Use formatação com largura fixa', 10),
                ('Build Steps', 'Simule etapas de build e imprima status.', 'steps = [\n    ("Install deps", True, "3.2s"),\n    ("Run tests", True, "5.1s"),\n    ("Build image", True, "12.4s"),\n    ("Push registry", False, "timeout"),\n]\nfor step, ok, info in steps:\n    status = "OK" if ok else "FAIL"\n    print(f"[{status}] {step} ({info})")\n', '[OK] Install deps (3.2s)\n[OK] Run tests (5.1s)\n[OK] Build image (12.4s)\n[FAIL] Push registry (timeout)', 'Use ternário para status', 10),
                ('Volumes', 'Monte mapeamento de volumes e imprima.', 'volumes = [\n    ("./data", "/app/data", "rw"),\n    ("./logs", "/app/logs", "rw"),\n    ("./config", "/app/config", "ro"),\n]\nfor host, container, mode in volumes:\n    print(f"{host} -> {container} ({mode})")\n', './data -> /app/data (rw)\n./logs -> /app/logs (rw)\n./config -> /app/config (ro)', 'Formate cada volume', 10),
                ('Health Check', 'Simule health check de serviços.', 'servicos = [\n    ("API", "http://localhost:5000/health", 200),\n    ("DB", "postgresql://localhost:5432", 200),\n    ("Cache", "redis://localhost:6379", 0),\n]\nfor nome, url, code in servicos:\n    status = "healthy" if code == 200 else "unhealthy"\n    print(f"{nome}: {status} ({url})")\n', 'API: healthy (http://localhost:5000/health)\nDB: healthy (postgresql://localhost:5432)\nCache: unhealthy (redis://localhost:6379)', 'Verifique status code', 10),
                ('Cron Schedule', 'Monte agenda de tarefas cron e imprima.', 'tarefas = [\n    ("0 6 * * *", "ETL diario"),\n    ("0 */4 * * *", "Backup a cada 4h"),\n    ("0 0 * * 0", "Limpeza semanal"),\n    ("0 0 1 * *", "Relatorio mensal"),\n]\nfor cron, desc in tarefas:\n    print(f"{cron:15s} {desc}")\n', '0 6 * * *       ETL diario\n0 */4 * * *     Backup a cada 4h\n0 0 * * 0       Limpeza semanal\n0 0 1 * *       Relatorio mensal', 'Use formatação com largura', 10),
            ]},
            {'title': 'Semana 3 — Projeto (Parte 1)', 'subtitle': 'Extração + ETL + georref', 'week': 3, 'order': 3, 'duration': 60, 'content_func': None, 'exercises': [
                ('Pipeline Config', 'Monte config de pipeline ETL.', 'config = {\n    "source": "api.dados.gov.br",\n    "format": "json",\n    "destination": "postgresql://db/geo",\n    "schedule": "diario 06:00",\n    "retry": 3\n}\nfor k, v in config.items():\n    print(f"{k}: {v}")\n', 'source: api.dados.gov.br\nformat: json\ndestination: postgresql://db/geo\nschedule: diario 06:00\nretry: 3', 'Itere config', 10),
                ('Extrator Multi-Fonte', 'Simule extração de múltiplas fontes.', 'fontes = [\n    {"nome": "API IBGE", "tipo": "rest", "registros": 5000},\n    {"nome": "CSV Prefeitura", "tipo": "file", "registros": 1200},\n    {"nome": "Shapefile", "tipo": "geo", "registros": 800},\n]\ntotal = 0\nfor f in fontes:\n    total += f["registros"]\n    print(f"{f[\'nome\']} ({f[\'tipo\']}): {f[\'registros\']} registros")\nprint(f"Total: {total}")\n', 'API IBGE (rest): 5000 registros\nCSV Prefeitura (file): 1200 registros\nShapefile (geo): 800 registros\nTotal: 7000', 'Acumule total', 10),
                ('Transformador', 'Aplique transformações e imprima resultado.', 'dados = [{"nome": "  ana silva  ", "cpf": "123.456.789-00"}]\nfor d in dados:\n    d["nome"] = d["nome"].strip().title()\n    d["cpf"] = d["cpf"].replace(".", "").replace("-", "")\n    print(f"{d[\'nome\']}: {d[\'cpf\']}")\n', 'Ana Silva: 12345678900', 'Use strip(), title(), replace()', 10),
                ('Validador Geo', 'Valide coordenadas geográficas.', 'pontos = [(-23.55, -46.63), (91, 0), (0, 181), (-15.78, -47.93)]\nfor lat, lon in pontos:\n    ok = -90 <= lat <= 90 and -180 <= lon <= 180\n    print(f"({lat},{lon}): {\'valido\' if ok else \'invalido\'}")\n', '(-23.55,-46.63): valido\n(91,0): invalido\n(0,181): invalido\n(-15.78,-47.93): valido', 'Lat: -90 a 90, Lon: -180 a 180', 10),
                ('Merge de Fontes', 'Combine dados de duas fontes pelo ID.', 'fonte_a = {1: {"nome": "Lote A", "area": 500}, 2: {"nome": "Lote B", "area": 800}}\nfonte_b = {1: {"zona": "Residencial"}, 2: {"zona": "Comercial"}}\nfor id in fonte_a:\n    merged = {**fonte_a[id], **fonte_b.get(id, {})}\n    print(f"{id}: {merged}")\n', "1: {'nome': 'Lote A', 'area': 500, 'zona': 'Residencial'}\n2: {'nome': 'Lote B', 'area': 800, 'zona': 'Comercial'}", 'Use {**dict1, **dict2}', 10),
                ('Relatório de ETL', 'Gere relatório de execução ETL.', 'etapas = [\n    ("Extracao", 1000, 1000, 0),\n    ("Limpeza", 1000, 950, 50),\n    ("Carga", 950, 950, 0),\n]\nfor etapa, entrada, saida, erros in etapas:\n    print(f"{etapa}: {entrada} -> {saida} ({erros} erros)")\n', 'Extracao: 1000 -> 1000 (0 erros)\nLimpeza: 1000 -> 950 (50 erros)\nCarga: 950 -> 950 (0 erros)', 'Formate cada etapa', 10),
                ('Checkpoint', 'Salve e carregue checkpoints do pipeline.', 'checkpoint = {"etapa": "transformacao", "processados": 750, "total": 1000, "erros": 12}\nprint("=== CHECKPOINT ===")\nfor k, v in checkpoint.items():\n    print(f"  {k}: {v}")\nprogresso = (checkpoint["processados"]/checkpoint["total"])*100\nprint(f"Progresso: {progresso:.0f}%")\n', '=== CHECKPOINT ===\n  etapa: transformacao\n  processados: 750\n  total: 1000\n  erros: 12\nProgresso: 75%', 'Calcule progresso percentual', 10),
                ('Qualidade de Dados', 'Avalie qualidade dos dados processados.', 'metricas = {\n    "completude": 95.5,\n    "unicidade": 99.2,\n    "validade": 87.3,\n    "consistencia": 92.1\n}\nfor m, v in metricas.items():\n    status = "OK" if v >= 90 else "ATENCAO"\n    print(f"{m}: {v}% [{status}]")\n', 'completude: 95.5% [OK]\nunicidade: 99.2% [OK]\nvalidade: 87.3% [ATENCAO]\nconsistencia: 92.1% [OK]', 'Compare com threshold de 90%', 10),
            ]},
            {'title': 'Semana 4 — Projeto (Parte 2)', 'subtitle': 'Dashboard, API, testes, deploy', 'week': 4, 'order': 4, 'duration': 60, 'content_func': None, 'exercises': [
                ('Dashboard KPIs', 'Monte KPIs do dashboard e imprima.', 'kpis = {\n    "Total Registros": 15000,\n    "Cobertura Geo": "87%",\n    "Ultima Atualizacao": "2024-01-15",\n    "Uptime API": "99.9%"\n}\nfor nome, val in kpis.items():\n    print(f"{nome}: {val}")\n', 'Total Registros: 15000\nCobertura Geo: 87%\nUltima Atualizacao: 2024-01-15\nUptime API: 99.9%', 'Itere dict', 10),
                ('API Endpoints', 'Liste endpoints da API do projeto.', 'endpoints = [\n    ("GET", "/api/lotes", "Listar lotes"),\n    ("GET", "/api/lotes/{id}", "Detalhe do lote"),\n    ("POST", "/api/lotes", "Criar lote"),\n    ("GET", "/api/mapa", "Gerar mapa"),\n]\nfor method, path, desc in endpoints:\n    print(f"{method:6s} {path:20s} {desc}")\n', 'GET    /api/lotes           Listar lotes\nGET    /api/lotes/{id}      Detalhe do lote\nPOST   /api/lotes           Criar lote\nGET    /api/mapa            Gerar mapa', 'Use formatação com largura', 10),
                ('Test Runner', 'Simule execução de testes e imprima resultados.', 'testes = [\n    ("test_conexao_db", True),\n    ("test_etl_pipeline", True),\n    ("test_api_lotes", True),\n    ("test_exportar_mapa", False),\n    ("test_autenticacao", True),\n]\npassed = sum(1 for _, ok in testes if ok)\nfor nome, ok in testes:\n    print(f"  {\'PASS\' if ok else \'FAIL\'} {nome}")\nprint(f"\\n{passed}/{len(testes)} passed")\n', '  PASS test_conexao_db\n  PASS test_etl_pipeline\n  PASS test_api_lotes\n  FAIL test_exportar_mapa\n  PASS test_autenticacao\n\n4/5 passed', 'Conte passados com sum()', 10),
                ('Deploy Checklist', 'Verifique checklist de deploy.', 'checklist = [\n    ("Testes passando", True),\n    ("Migrations rodaram", True),\n    ("Variáveis .env", True),\n    ("Docker build OK", True),\n    ("Monitoramento ativo", False),\n]\nfor item, ok in checklist:\n    print(f"[{\'OK\' if ok else \'  \'}] {item}")\n', '[OK] Testes passando\n[OK] Migrations rodaram\n[OK] Variáveis .env\n[OK] Docker build OK\n[  ] Monitoramento ativo', 'Use ternário', 10),
                ('Monitoramento', 'Monte painel de monitoramento.', 'servicos = [\n    ("API", "online", 23, 0.1),\n    ("DB", "online", 45, 0.5),\n    ("ETL", "running", 78, 2.3),\n    ("Cache", "offline", 0, 0),\n]\nfor nome, status, cpu, mem in servicos:\n    print(f"{nome:6s} {status:10s} CPU:{cpu:3d}% MEM:{mem}GB")\n', 'API    online     CPU: 23% MEM:0.1GB\nDB     online     CPU: 45% MEM:0.5GB\nETL    running    CPU: 78% MEM:2.3GB\nCache  offline    CPU:  0% MEM:0GB', 'Formate com largura fixa', 10),
                ('Documentação API', 'Gere docs de endpoint da API.', 'doc = {\n    "endpoint": "/api/lotes",\n    "method": "GET",\n    "params": ["page", "limit", "zona"],\n    "response": "200 JSON array"\n}\nfor k, v in doc.items():\n    if isinstance(v, list):\n        print(f"{k}: {\\", \\".join(v)}")\n    else:\n        print(f"{k}: {v}")\n', 'endpoint: /api/lotes\nmethod: GET\nparams: page, limit, zona\nresponse: 200 JSON array', 'Trate listas com join()', 10),
                ('Release Notes', 'Monte release notes e imprima.', 'changes = [\n    ("feat", "Pipeline ETL automatizado"),\n    ("feat", "API REST com autenticacao"),\n    ("fix", "Corrigir projecao CRS"),\n    ("docs", "Documentacao completa"),\n]\nfor tipo, desc in changes:\n    print(f"- [{tipo}] {desc}")\n', '- [feat] Pipeline ETL automatizado\n- [feat] API REST com autenticacao\n- [fix] Corrigir projecao CRS\n- [docs] Documentacao completa', 'Formate tipo entre colchetes', 10),
                ('Métricas Finais', 'Calcule e imprima métricas do projeto.', 'metricas = {\n    "Linhas de codigo": 2500,\n    "Testes": 45,\n    "Cobertura": 87,\n    "Endpoints": 12,\n    "Tempo deploy": "3min"\n}\nfor m, v in metricas.items():\n    print(f"{m}: {v}")\n', 'Linhas de codigo: 2500\nTestes: 45\nCobertura: 87\nEndpoints: 12\nTempo deploy: 3min', 'Itere e imprima', 10),
            ]},
        ]
    },
    {
        'name': 'Inteligência Artificial na Prática',
        'short_name': 'Módulo IA',
        'description': 'Use IA como ferramenta de trabalho real. Prompt engineering, APIs, chatbots, RAG e agentes autônomos.',
        'price': 150.0,
        'duration': '4 semanas · 4 calls de 1h',
        'level': 'Todos os níveis',
        'color': 'purple',
        'icon': '🤖',
        'prereqs': 'Nenhum (Aulas 1-2) · Módulo 01 recomendado (Aulas 3-4)',
        'tools': 'ChatGPT, Claude, Cursor, GitHub Copilot, API OpenAI/Anthropic, LangChain',
        'lessons': [
            {
                'title': 'Aula 1 — IA como Ferramenta de Trabalho',
                'subtitle': 'LLMs, Prompt Engineering, técnicas avançadas e ferramentas',
                'week': 1, 'order': 1, 'duration': 60,
                'content_func': 'get_ia_a1_content',
                'exercises': [
                    ('Prompt de 4 Partes', 'Monte um prompt com as 4 partes: contexto, tarefa, formato e restricoes. Imprima cada variável.', 'contexto = ""\ntarefa = ""\nformato = ""\nrestricoes = ""\n\nprint(contexto)\nprint(tarefa)\nprint(formato)\nprint(restricoes)\n', None, 'Preencha cada variável com texto relevante para um cenário profissional', 20),
                    ('Técnicas de Prompt', 'Crie uma lista chamada "tecnicas" com 4 técnicas de prompt engineering. Imprima cada uma numerada.', 'tecnicas = []\n\n# Adicione 4 técnicas e imprima\n', None, 'As técnicas são: Few-Shot, Chain of Thought, Role Prompting, Self-Consistency', 15),
                    ('Comparar Modelos', 'Monte dict de modelos com suas características. Imprima tabela comparativa.', 'modelos = {\n    "GPT-4": {"empresa": "OpenAI", "contexto": "128K", "preco": "alto"},\n    "Claude 3.5": {"empresa": "Anthropic", "contexto": "200K", "preco": "medio"},\n    "Gemini": {"empresa": "Google", "contexto": "1M", "preco": "medio"},\n}\nfor nome, info in modelos.items():\n    print(f"{nome} ({info[\'empresa\']}): ctx={info[\'contexto\']}, preco={info[\'preco\']}")\n', 'GPT-4 (OpenAI): ctx=128K, preco=alto\nClaude 3.5 (Anthropic): ctx=200K, preco=medio\nGemini (Google): ctx=1M, preco=medio', 'Itere dict aninhado', 10),
                    ('Role Prompting', 'Crie 3 system prompts para diferentes roles. Imprima cada.', 'roles = [\n    ("Analista de Dados", "Voce e um analista de dados senior. Responda com foco em metricas."),\n    ("Dev Python", "Voce e um desenvolvedor Python expert. Forneça codigo limpo."),\n    ("Revisor", "Voce e um revisor de texto. Corrija gramatica e clareza."),\n]\nfor role, prompt in roles:\n    print(f"[{role}] {prompt}")\n', '[Analista de Dados] Voce e um analista de dados senior. Responda com foco em metricas.\n[Dev Python] Voce e um desenvolvedor Python expert. Forneça codigo limpo.\n[Revisor] Voce e um revisor de texto. Corrija gramatica e clareza.', 'Crie prompts específicos por role', 10),
                    ('Few-Shot Template', 'Monte template few-shot com exemplos. Imprima o prompt completo.', 'exemplos = [\n    ("Adorei o produto!", "positivo"),\n    ("Pessimo atendimento", "negativo"),\n    ("O produto e ok", "neutro"),\n]\nprint("Classifique o sentimento:")\nfor texto, sent in exemplos:\n    print(f"Texto: {texto} -> {sent}")\nprint("Texto: Entrega rapida e produto bom -> ???")\n', 'Classifique o sentimento:\nTexto: Adorei o produto! -> positivo\nTexto: Pessimo atendimento -> negativo\nTexto: O produto e ok -> neutro\nTexto: Entrega rapida e produto bom -> ???', 'Monte exemplos antes da pergunta', 10),
                    ('Token Counter', 'Estime tokens de um texto (1 token ~ 4 chars). Imprima contagem.', 'textos = [\n    "Ola, como voce esta?",\n    "Python e uma linguagem de programacao muito utilizada para automacao e analise de dados.",\n    "IA",\n]\nfor t in textos:\n    chars = len(t)\n    tokens = chars // 4\n    print(f"{chars} chars ~ {tokens} tokens: {t[:30]}...")\n', '21 chars ~ 5 tokens: Ola, como voce esta?...\n89 chars ~ 22 tokens: Python e uma linguagem de prog...\n2 chars ~ 0 tokens: IA...', 'Divida chars por 4', 10),
                    ('Custo de API', 'Calcule custo estimado de chamadas à API. Imprima resumo.', 'chamadas = [\n    {"modelo": "GPT-4", "tokens_in": 500, "tokens_out": 200, "preco_in": 0.03, "preco_out": 0.06},\n    {"modelo": "Claude", "tokens_in": 800, "tokens_out": 300, "preco_in": 0.015, "preco_out": 0.075},\n]\nfor c in chamadas:\n    custo = (c["tokens_in"]/1000)*c["preco_in"] + (c["tokens_out"]/1000)*c["preco_out"]\n    print(f"{c[\'modelo\']}: ${custo:.4f}")\n', 'GPT-4: $0.0270\nClaude: $0.0345', 'Custo = (tokens/1000) * preço por 1K', 10),
                    ('Temperatura', 'Simule efeito da temperatura na criatividade. Imprima resultado para cada valor.', 'temps = [\n    (0.0, "resposta exata e deterministica"),\n    (0.5, "balanco entre precisao e criatividade"),\n    (1.0, "alta criatividade e variacao"),\n]\nfor temp, desc in temps:\n    print(f"temp={temp}: {desc}")\n', 'temp=0.0: resposta exata e deterministica\ntemp=0.5: balanco entre precisao e criatividade\ntemp=1.0: alta criatividade e variacao', 'Itere lista de tuplas', 10),
                ]
            },
            {
                'title': 'Aula 2 — APIs de IA com Python',
                'subtitle': 'API OpenAI/Anthropic, parâmetros e automação inteligente',
                'week': 2, 'order': 2, 'duration': 60,
                'content_func': 'get_ia_a2_content',
                'exercises': [
                    ('Estrutura de Request', 'Monte um dict request_body com: model, max_tokens, temperature, system com valores preenchidos. Imprima "chave: valor" para cada.', 'request_body = {\n    "model": "",\n    "max_tokens": 0,\n    "temperature": 0.0,\n    "system": ""\n}\n\nfor chave, valor in request_body.items():\n    print(f"{chave}: {valor}")\n', None, 'Use: model="claude-3-5-sonnet", max_tokens=1024, temperature=0.7, system="Assistente Python"', 20),
                    ('Pipeline Simples', 'Crie um dict com 3 etapas de um pipeline de automação com IA. Imprima "etapa: descricao" para cada.', 'pipeline = {}\n\n# Adicione 3 etapas e imprima\n', None, 'Exemplo: {"classificar": "Classificar tipo do documento", "extrair": "Extrair dados em JSON", "salvar": "Salvar no banco"}', 15),
                    ('Headers de API', 'Monte headers para chamada à API. Imprima cada header.', 'headers = {\n    "Authorization": "Bearer sk-xxx",\n    "Content-Type": "application/json",\n    "X-API-Version": "2024-01-01",\n    "Accept": "application/json"\n}\nfor k, v in headers.items():\n    print(f"{k}: {v}")\n', 'Authorization: Bearer sk-xxx\nContent-Type: application/json\nX-API-Version: 2024-01-01\nAccept: application/json', 'Itere dict', 10),
                    ('Retry com Backoff', 'Simule retry de chamada à API com backoff exponencial.', 'respostas = [429, 429, 200]\nfor i, code in enumerate(respostas, 1):\n    if code == 200:\n        print(f"Tentativa {i}: Sucesso!")\n    else:\n        wait = 2 ** i\n        print(f"Tentativa {i}: Rate limit (429), aguardando {wait}s")\n', 'Tentativa 1: Rate limit (429), aguardando 2s\nTentativa 2: Rate limit (429), aguardando 4s\nTentativa 3: Sucesso!', 'Use 2**i para backoff', 10),
                    ('Batch Processing', 'Processe múltiplos textos em lote. Imprima status de cada.', 'textos = ["Texto curto", "Um texto um pouco mais longo para processar", "Outro texto", "Texto final do lote"]\nfor i, t in enumerate(textos, 1):\n    tokens = len(t) // 4\n    print(f"[{i}/{len(textos)}] {tokens} tokens: {t[:20]}")\nprint(f"Total processado: {len(textos)} textos")\n', '[1/4] 2 tokens: Texto curto\n[2/4] 10 tokens: Um texto um pouco ma\n[3/4] 2 tokens: Outro texto\n[4/4] 5 tokens: Texto final do lote\nTotal processado: 4 textos', 'Use enumerate e len()//4', 10),
                    ('Error Handling API', 'Trate diferentes erros de API. Imprima ação para cada.', 'erros = [\n    (400, "Bad Request", "Verificar formato do request"),\n    (401, "Unauthorized", "Verificar API key"),\n    (429, "Rate Limited", "Aguardar e tentar novamente"),\n    (500, "Server Error", "Tentar novamente em 30s"),\n]\nfor code, msg, acao in erros:\n    print(f"{code} {msg}: {acao}")\n', '400 Bad Request: Verificar formato do request\n401 Unauthorized: Verificar API key\n429 Rate Limited: Aguardar e tentar novamente\n500 Server Error: Tentar novamente em 30s', 'Formate cada erro com ação', 10),
                    ('Streaming Simulado', 'Simule streaming de resposta da IA palavra por palavra.', 'resposta = "Python e uma linguagem versátil para automação"\npalavras = resposta.split()\nacumulado = ""\nfor p in palavras:\n    acumulado += p + " "\n    print(acumulado.strip())\n', 'Python\nPython e\nPython e uma\nPython e uma linguagem\nPython e uma linguagem versátil\nPython e uma linguagem versátil para\nPython e uma linguagem versátil para automação', 'Acumule palavras uma a uma', 10),
                    ('Custo por Modelo', 'Compare custos de diferentes modelos para mesma tarefa.', 'modelos = [\n    ("GPT-4", 0.03, 0.06),\n    ("GPT-3.5", 0.001, 0.002),\n    ("Claude 3.5", 0.015, 0.075),\n]\ntokens_in, tokens_out = 1000, 500\nfor nome, pin, pout in modelos:\n    custo = (tokens_in/1000)*pin + (tokens_out/1000)*pout\n    print(f"{nome}: ${custo:.3f}")\n', 'GPT-4: $0.060\nGPT-3.5: $0.002\nClaude 3.5: $0.052', 'Calcule custo = in*preço_in + out*preço_out', 10),
                ]
            },
            {
                'title': 'Aula 3 — Chatbots e Aplicações com IA',
                'subtitle': 'Chatbot com memória, JSON mode e pipelines de dados',
                'week': 3, 'order': 3, 'duration': 60,
                'content_func': 'get_ia_a3_content',
                'exercises': [
                    ('Histórico de Chat', 'Crie uma lista "historico" com 4 dicts simulando uma conversa (alternando role user/assistant). Imprima cada mensagem formatada.', 'historico = []\n\n# Adicione 4 mensagens e imprima\n', None, 'Formato: {"role": "user", "content": "..."} e {"role": "assistant", "content": "..."}', 20),
                    ('Validação de JSON', 'Dado o dict "resposta_ia", valide se tem as chaves "sentimento", "temas" e "urgencia". Imprima "OK" se todas existem, ou "Faltando: chave" para cada ausente.', 'import json\n\nresposta_ia = {"sentimento": "negativo", "temas": ["suporte", "bug"], "urgencia": 4}\nchaves_esperadas = ["sentimento", "temas", "urgencia"]\n\n# Valide e imprima\n', 'OK', 'Verifique: all(k in resposta_ia for k in chaves_esperadas)', 15),
                    ('Gerenciar Memória', 'Simule memória de chatbot com limite. Mantenha últimas 3 mensagens.', 'memoria = []\nmsgs = ["Oi", "Qual seu nome?", "Me ajude com Python", "Como fazer um loop?", "E um dict?"]\nfor m in msgs:\n    memoria.append(m)\n    if len(memoria) > 3:\n        memoria.pop(0)\n    print(f"Memoria ({len(memoria)}): {memoria}")\n', "Memoria (1): ['Oi']\nMemoria (2): ['Oi', 'Qual seu nome?']\nMemoria (3): ['Oi', 'Qual seu nome?', 'Me ajude com Python']\nMemoria (3): ['Qual seu nome?', 'Me ajude com Python', 'Como fazer um loop?']\nMemoria (3): ['Me ajude com Python', 'Como fazer um loop?', 'E um dict?']", 'Use pop(0) quando exceder limite', 10),
                    ('JSON Mode', 'Parse resposta da IA em JSON e extraia campos.', 'import json\nresposta = \'{"produto": "Notebook", "sentimento": "positivo", "nota": 4.5, "tags": ["qualidade", "preco"]}\'\ndados = json.loads(resposta)\nprint(f"Produto: {dados[\'produto\']}")\nprint(f"Sentimento: {dados[\'sentimento\']}")\nprint(f"Nota: {dados[\'nota\']}")\nprint(f"Tags: {\\", \\".join(dados[\'tags\'])}")\n', 'Produto: Notebook\nSentimento: positivo\nNota: 4.5\nTags: qualidade, preco', 'Use json.loads() para parse', 10),
                    ('Classificador', 'Simule classificação de textos. Imprima categoria de cada.', 'textos = [\n    ("Quero cancelar minha assinatura", "cancelamento"),\n    ("Nao consigo fazer login", "suporte_tecnico"),\n    ("Quanto custa o plano pro?", "vendas"),\n    ("Obrigado pelo atendimento!", "feedback"),\n]\nfor texto, cat in textos:\n    print(f"[{cat}] {texto}")\n', '[cancelamento] Quero cancelar minha assinatura\n[suporte_tecnico] Nao consigo fazer login\n[vendas] Quanto custa o plano pro?\n[feedback] Obrigado pelo atendimento!', 'Formate cada classificação', 10),
                    ('Token Window', 'Simule janela de contexto: truncar msgs se exceder limite.', 'msgs = ["Msg curta", "Uma mensagem um pouco maior", "Outra msg", "Mensagem final"]\nlimite = 50\ntotal = 0\nfor m in msgs:\n    chars = len(m)\n    if total + chars <= limite:\n        total += chars\n        print(f"Incluida: {m} (total: {total})")\n    else:\n        print(f"Truncada: {m} (excede {limite})")\n', 'Incluida: Msg curta (total: 9)\nIncluida: Uma mensagem um pouco maior (total: 35)\nIncluida: Outra msg (total: 44)\nTruncada: Mensagem final (excede 50)', 'Acumule chars e verifique limite', 10),
                    ('Extrator de Entidades', 'Simule extração de entidades de texto. Imprima entidades encontradas.', 'texto = "Ana trabalha na Google em Sao Paulo desde 2020"\nentidades = {\n    "pessoa": "Ana",\n    "empresa": "Google",\n    "cidade": "Sao Paulo",\n    "ano": "2020"\n}\nfor tipo, valor in entidades.items():\n    print(f"{tipo}: {valor}")\n', 'pessoa: Ana\nempresa: Google\ncidade: Sao Paulo\nano: 2020', 'Monte dict com entidades extraídas', 10),
                    ('Sumarização', 'Simule sumarização contando palavras. Imprima resumo.', 'texto = "Python e uma linguagem de programacao criada em 1991 por Guido van Rossum"\npalavras = texto.split()\nresumo = " ".join(palavras[:5]) + "..."\nprint(f"Original: {len(palavras)} palavras")\nprint(f"Resumo: {resumo}")\n', 'Original: 12 palavras\nResumo: Python e uma linguagem de...', 'Use split() e join() com slice', 10),
                ]
            },
            {
                'title': 'Aula 4 — RAG, Embeddings e Agentes',
                'subtitle': 'Busca semântica, agentes autônomos e produção',
                'week': 4, 'order': 4, 'duration': 60,
                'content_func': 'get_ia_a4_content',
                'exercises': [
                    ('Busca por Relevância', 'Dada uma lista de documentos e uma pergunta, encontre o doc mais relevante contando palavras em comum. Imprima o documento.', 'docs = [\n    "Politica de reembolso: ate 7 dias uteis",\n    "Horario de atendimento: segunda a sexta 9h as 18h",\n    "Para cancelar envie email para cancelamento@empresa.com"\n]\npergunta = "qual horario de atendimento"\n\n# Encontre o doc mais relevante\n', 'Horario de atendimento: segunda a sexta 9h as 18h', 'Conte palavras da pergunta que aparecem em cada doc. Use lower() e split().', 20),
                    ('Definindo Tools', 'Crie uma lista "tools" com 2 dicts representando ferramentas (name, description). Imprima nome e descrição de cada.', 'tools = []\n\n# Adicione 2 ferramentas e imprima\n', None, 'Exemplo: {"name": "buscar_preco", "description": "Busca preço de produto"}', 15),
                    ('Chunk de Documento', 'Divida um texto longo em chunks de N palavras. Imprima cada chunk.', 'texto = "Python e otimo para automacao analise de dados web scraping APIs inteligencia artificial e muito mais"\npalavras = texto.split()\nchunk_size = 4\nfor i in range(0, len(palavras), chunk_size):\n    chunk = " ".join(palavras[i:i+chunk_size])\n    print(f"Chunk {i//chunk_size + 1}: {chunk}")\n', 'Chunk 1: Python e otimo para\nChunk 2: automacao analise de dados\nChunk 3: web scraping APIs inteligencia\nChunk 4: artificial e muito mais', 'Use range com step e slicing', 10),
                    ('Similaridade Simples', 'Calcule similaridade entre textos contando palavras em comum.', 'def similaridade(t1, t2):\n    s1 = set(t1.lower().split())\n    s2 = set(t2.lower().split())\n    comum = s1 & s2\n    return len(comum) / max(len(s1), len(s2))\n\npares = [\n    ("Python para automacao", "Automacao com Python"),\n    ("Python para automacao", "Java para web"),\n]\nfor a, b in pares:\n    sim = similaridade(a, b)\n    print(f"Sim({a[:20]}, {b[:20]}): {sim:.2f}")\n', 'Sim(Python para automa, Automacao com Python): 0.67\nSim(Python para automa, Java para web): 0.33', 'Use intersecção de sets', 10),
                    ('Agente Decisor', 'Simule agente que decide qual tool usar baseado na pergunta.', 'tools = {"buscar": "busca na base", "calcular": "faz contas", "enviar": "envia email"}\nperguntas = [\n    ("Quanto e 5+3?", "calcular"),\n    ("Onde fica o arquivo?", "buscar"),\n    ("Mande pro cliente", "enviar"),\n]\nfor pergunta, tool in perguntas:\n    print(f"Q: {pergunta}")\n    print(f"Tool: {tool} -> {tools[tool]}")\n', 'Q: Quanto e 5+3?\nTool: calcular -> faz contas\nQ: Onde fica o arquivo?\nTool: buscar -> busca na base\nQ: Mande pro cliente\nTool: enviar -> envia email', 'Mapeie perguntas para tools', 10),
                    ('RAG Pipeline', 'Simule pipeline RAG: buscar, contextualizar, responder.', 'base = ["Doc sobre Python", "Doc sobre SQL", "Doc sobre Docker"]\npergunta = "Como usar Docker?"\nprint(f"1. Busca: \\"{pergunta}\\"")\nrelevante = [d for d in base if any(p in d.lower() for p in pergunta.lower().split())]\nprint(f"2. Encontrado: {relevante}")\nprint(f"3. Resposta: Baseado em {len(relevante)} doc(s)")\n', '1. Busca: "Como usar Docker?"\n2. Encontrado: [\'Doc sobre Docker\']\n3. Resposta: Baseado em 1 doc(s)', 'Busque docs com palavras em comum', 10),
                    ('Guardrails', 'Simule verificação de segurança na resposta da IA.', 'respostas = [\n    ("Python e otimo para dados", True),\n    ("Vou hackear o sistema", False),\n    ("Aqui esta o codigo", True),\n    ("Informacoes confidenciais: senha=123", False),\n]\nfor resp, seguro in respostas:\n    status = "APROVADA" if seguro else "BLOQUEADA"\n    print(f"[{status}] {resp[:30]}")\n', '[APROVADA] Python e otimo para dados\n[BLOQUEADA] Vou hackear o sistema\n[APROVADA] Aqui esta o codigo\n[BLOQUEADA] Informacoes confidenciais:', 'Verifique flag de segurança', 10),
                    ('Métricas de Avaliação', 'Calcule métricas de qualidade de respostas da IA.', 'avaliacoes = [4, 5, 3, 5, 4, 2, 5, 4]\nmedia = sum(avaliacoes) / len(avaliacoes)\nboas = sum(1 for a in avaliacoes if a >= 4)\nprint(f"Media: {media:.1f}/5")\nprint(f"Boas (>=4): {boas}/{len(avaliacoes)}")\nprint(f"Taxa: {(boas/len(avaliacoes))*100:.0f}%")\n', 'Media: 4.0/5\nBoas (>=4): 5/8\nTaxa: 62%', 'Use sum, len e list comprehension', 10),
                ]
            },
        ]
    },
]

CONTENT_FUNCTIONS = {
    'get_m01_s1_content': get_m01_s1_content,
    'get_m01_s2_content': get_m01_s2_content,
    'get_m01_s3_content': get_m01_s3_content,
    'get_m01_s4_content': get_m01_s4_content,
    'get_ia_a1_content': get_ia_a1_content,
    'get_ia_a2_content': get_ia_a2_content,
    'get_ia_a3_content': get_ia_a3_content,
    'get_ia_a4_content': get_ia_a4_content,
}
