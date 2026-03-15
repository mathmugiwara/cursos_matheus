"""
Execute: python reseed.py
Atualiza o conteudo das aulas sem apagar usuarios ou modulos.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app import app, db, Module, Lesson, Exercise, LessonProgress, ExerciseSubmission

# ─────────────────────────── HELPERS ───────────────────────────

def add_lesson(module_id, title, subtitle, content, week, order, duration=60):
    l = Lesson(module_id=module_id, title=title, subtitle=subtitle,
               content=content, week_number=week, order=order, duration_minutes=duration)
    db.session.add(l); db.session.flush(); return l

def add_ex(lesson_id, order, title, desc, starter, expected, hint, points=10):
    db.session.add(Exercise(lesson_id=lesson_id, order=order, title=title,
        description=desc, starter_code=starter, expected_output=expected,
        hint=hint, points=points))

# ─────────────────────────── SEMANA 1 CONTENT ───────────────────────────

def s1_content():
    return """<section class="lesson-section">
  <div class="lesson-intro-box">
    <p><strong>Objetivo da semana:</strong> Sair do absoluto zero e criar seus primeiros programas Python reais. Ao final, você vai entender como o computador processa informações e vai escrever código que já resolve problemas do dia a dia.</p>
  </div>

  <h2>🐍 Por que Python?</h2>
  <p>Python foi criado em 1991 pelo holandês Guido van Rossum com uma filosofia simples: código deve ser tão legível quanto texto em inglês. Essa decisão mudou tudo. Diferente de outras linguagens onde você precisa decorar uma sintaxe cheia de símbolos, em Python o código lê quase como uma frase. Você consegue entender o que um programa faz mesmo antes de saber programar.</p>
  <p>Hoje Python é a linguagem mais popular do mundo para automação, análise de dados e inteligência artificial. No Brasil, a demanda por quem domina Python cresce todos os anos. Scripts que automatizam relatórios, robôs que preenchem formulários, dashboards que atualizam sozinhos — tudo isso começa pelo mesmo ponto de partida que você está agora.</p>
  <div class="highlight-grid">
    <div class="highlight-card"><span>📖</span><strong>Legibilidade</strong><br>Você lê o código e entende o que faz, mesmo sem saber programar ainda.</div>
    <div class="highlight-card"><span>📦</span><strong>Ecossistema gigante</strong><br>Pandas para dados, PyAutoGUI para automação, TensorFlow para IA — tudo pronto para usar.</div>
    <div class="highlight-card"><span>💼</span><strong>Alta demanda</strong><br>Linguagem mais pedida em vagas de automação e análise de dados no Brasil.</div>
    <div class="highlight-card"><span>⚡</span><strong>Produtividade</strong><br>Em horas você cria algo funcional. O que leva semanas em outras linguagens, leva dias em Python.</div>
  </div>

  <h2>🛠️ Configurando seu Ambiente</h2>
  <p>Para escrever e executar Python, você precisa de dois programas: o <strong>interpretador Python</strong>, que é o motor que entende e roda seu código, e um <strong>editor de código</strong>, onde você escreve. O VS Code é hoje o editor mais usado no mundo justamente pela sua integração perfeita com Python e pelo ecossistema de extensões gratuitas.</p>
  <p>Siga os passos abaixo exatamente nessa ordem. O detalhe mais importante é marcar a opção "Add Python to PATH" durante a instalação — sem isso, o terminal não reconhece o comando <code>python</code>.</p>
  <div class="code-block">
    <div class="code-header">Terminal — Verificando a instalação</div>
    <pre><code">python --version
pip --version</code></pre>
  </div>
  <p>Se ambos os comandos retornarem um número de versão, a instalação foi concluída com sucesso. Agora crie um arquivo <code>teste.py</code>, escreva <code>print("Olá, mundo!")</code> e execute com <code>python teste.py</code> no terminal. Se aparecer a mensagem, está tudo pronto.</p>

  <h2>📦 Variáveis e Tipos de Dados</h2>
  <p>Uma variável é um nome que você dá a um valor armazenado na memória do computador. Pense como uma etiqueta colada numa caixa — a etiqueta é o nome, o conteúdo da caixa é o valor. Em Python, você não precisa declarar o tipo da variável antecipadamente: a linguagem descobre sozinha com base no valor atribuído. Isso se chama <strong>tipagem dinâmica</strong>.</p>
  <p>Existem quatro tipos fundamentais que você vai usar em praticamente todo script. O tipo <strong>int</strong> armazena números inteiros como contadores e idades. O tipo <strong>float</strong> armazena números com casas decimais como preços e percentuais. O tipo <strong>str</strong> armazena qualquer texto entre aspas. O tipo <strong>bool</strong> armazena apenas dois valores possíveis: <code>True</code> ou <code>False</code>, e é a base de toda lógica condicional.</p>
  <div class="code-block">
    <div class="code-header">Python — Os 4 tipos fundamentais</div>
    <pre><code">idade = 28
salario = 4_500.50
nome = "Ana Silva"
ativo = True

print(type(idade))    # &lt;class 'int'&gt;
print(type(salario))  # &lt;class 'float'&gt;
print(type(nome))     # &lt;class 'str'&gt;
print(type(ativo))    # &lt;class 'bool'&gt;</code></pre>
  </div>
  <p>O underline em <code>4_500.50</code> é apenas um separador visual — facilita a leitura de números grandes sem afetar o valor calculado. Você pode usar em qualquer número: <code>1_000_000</code> é exatamente o mesmo que <code>1000000</code>.</p>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Qual o resultado de <code>int('42') + 8</code>?</div>
    <input type="text" class="check-input" data-answer="50" placeholder="Digite o resultado...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <h2>🔄 Conversão entre Tipos</h2>
  <p>Na prática real de automação, você vai constantemente receber dados em um tipo e precisar trabalhar com eles em outro. O caso mais comum acontece ao ler arquivos CSV ou formulários: todos os valores chegam como <strong>string</strong>, mesmo que sejam números. Sem converter, você não consegue fazer cálculos — somar duas strings em Python não dá um número, dá uma concatenação.</p>
  <p>Python oferece três funções de conversão principais: <code>int()</code> converte para inteiro, <code>float()</code> para decimal e <code>str()</code> para texto. A conversão só funciona se o valor for compatível — tentar converter <code>"R$ 150"</code> diretamente para número vai gerar um <code>ValueError</code>. O hábito correto é sempre limpar o dado antes de converter.</p>
  <div class="code-block">
    <div class="code-header">Python — Convertendo tipos na prática</div>
    <pre><code">texto = "1500"
numero = int(texto)
decimal = float(texto)

valor = "R$ 150"
valor_limpo = valor.replace("R$", "").strip()
numero = float(valor_limpo)

entrada = "42"
if entrada.isnumeric():
    print(int(entrada))
else:
    print("Valor inválido")</code></pre>
  </div>
  <p>O método <code>.strip()</code> remove espaços nas bordas do texto — muito útil depois de um <code>.replace()</code>. O método <code>.isnumeric()</code> retorna <code>True</code> se a string contém apenas dígitos, permitindo uma verificação segura antes de converter.</p>

  <h2>✍️ f-strings e Formatação</h2>
  <p>Montar mensagens com variáveis é uma das tarefas mais frequentes em qualquer script. Antes das f-strings existia a concatenação com <code>+</code>, que funcionava mas tornava o código verboso e propenso a erros de espaçamento. As f-strings, introduzidas no Python 3.6, resolveram isso com uma sintaxe elegante: coloque a letra <code>f</code> antes das aspas e use <code>{variavel}</code> dentro do texto.</p>
  <p>A parte mais poderosa é o sistema de formatação dentro das chaves. Dois pontos seguidos de um código de formato permitem controlar casas decimais, porcentagens, alinhamento e separadores de milhar — tudo em uma única expressão, sem funções extras.</p>
  <div class="code-block">
    <div class="code-header">Python — f-strings e formatação de números</div>
    <pre><code">nome = "Carlos"
salario = 6_750.5
bonus = 0.15
liquido = salario * (1 + bonus)

print(f"Funcionário: {nome}")
print(f"Salário base: R$ {salario:.2f}")
print(f"Com bônus de {bonus:.0%}: R$ {liquido:.2f}")

total = 1_234_567.89
print(f"Total: R$ {total:,.2f}")

print(f"{'Produto':<15} {'Valor':>10}")
print(f"{'Notebook':<15} {2500.00:>10.2f}")
print(f"{'Mouse':<15} {90.00:>10.2f}")</code></pre>
  </div>
  <p>Na formatação, <code>:.2f</code> significa "duas casas decimais", <code>:.0%</code> converte um decimal em porcentagem sem casas, <code>:,</code> adiciona separador de milhar e <code>:&lt;15</code> alinha o texto à esquerda em um campo de 15 caracteres. Esses modificadores são essenciais para gerar relatórios com visual profissional.</p>

  <h2>🔢 Operadores</h2>
  <p>Operadores são os símbolos que realizam operações sobre valores. Os aritméticos funcionam como na matemática, com duas particularidades importantes do Python. Primeiro, o operador <code>/</code> sempre retorna um número float, mesmo que a divisão seja exata — <code>10 / 2</code> retorna <code>5.0</code>, não <code>5</code>. Segundo, o operador <code>//</code> faz a divisão inteira descartando o resto, e o operador <code>%</code> (módulo) retorna apenas esse resto.</p>
  <p>O operador módulo merece atenção especial porque aparece com frequência. Verificar se um número é par ou ímpar, identificar múltiplos, distribuir itens em grupos — tudo usa módulo. Os operadores de atribuição composta como <code>+=</code> e <code>-=</code> são atalhos muito usados em loops para acumular valores.</p>
  <div class="code-block">
    <div class="code-header">Python — Operadores aritméticos e lógicos</div>
    <pre><code">print(10 / 3)    # 3.3333...
print(10 // 3)   # 3
print(10 % 3)    # 1
print(2 ** 10)   # 1024

x = 10
x += 5    # x = 15
x *= 2    # x = 30

print(5 > 3)            # True
print(5 == 5)           # True
print(5 != 3)           # True
print(True and False)   # False
print(True or False)    # True
print("a" in "python")  # True</code></pre>
  </div>
  <p>Atenção para um erro clássico: <code>=</code> é atribuição (coloca um valor na variável) e <code>==</code> é comparação (verifica se dois valores são iguais). Usar <code>=</code> dentro de um <code>if</code> gera um erro de sintaxe imediatamente — Python não permite isso justamente para evitar bugs silenciosos.</p>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Qual o resultado de <code>10 % 3</code>? (operador módulo — resto da divisão)</div>
    <input type="text" class="check-input" data-answer="1" placeholder="Digite o resultado...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <h2>🔀 Condicionais: if / elif / else</h2>
  <p>Condicionais permitem que seu código tome decisões com base em condições. Elas avaliam uma expressão que resulta em <code>True</code> ou <code>False</code> e executam blocos diferentes dependendo do resultado. Em Python, a <strong>indentação</strong> — o recuo de 4 espaços — não é uma convenção estética: ela é a própria sintaxe que define quais linhas pertencem a qual bloco. Esquecer ou usar indentação errada é um dos erros mais comuns de iniciantes.</p>
  <p>A estrutura completa usa <code>if</code> para a primeira condição, <code>elif</code> (abreviação de "else if") para condições alternativas — você pode ter quantos <code>elif</code> quiser — e <code>else</code> como bloco padrão quando nenhuma condição anterior foi verdadeira. Apenas um dos blocos será executado a cada vez.</p>
  <div class="code-block">
    <div class="code-header">Python — Condicionais e operador ternário</div>
    <pre><code">nota = 7.5

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

temperatura = 28
chovendo = False

if temperatura >= 25 and not chovendo:
    print("Dia perfeito para sair!")
elif temperatura >= 25 and chovendo:
    print("Quente mas chuvoso")
else:
    print("Fique em casa")

status = "Aprovado" if nota >= 7 else "Reprovado"

imc = 22.5
if 18.5 <= imc < 25:
    print("Peso normal")</code></pre>
  </div>
  <p>A última linha mostra uma característica única do Python: você pode encadear comparações como <code>18.5 &lt;= imc &lt; 25</code>, que lê exatamente como uma notação matemática. O operador ternário na penúltima linha (<code>X if condição else Y</code>) é ótimo para atribuições simples em uma linha, mas use com moderação — condições complexas ficam mais claras em um <code>if</code> normal.</p>
  <div class="code-block">
    <div class="code-header">Exemplo real — Calculadora de frete com múltiplas regras</div>
    <pre><code">peso_kg = 3.5
distancia_km = 450
valor_produto = 250.0

if valor_produto >= 300:
    frete = 0.0
    motivo = "frete grátis"
elif distancia_km <= 100:
    frete = peso_kg * 3.50
    motivo = "entrega local"
elif distancia_km <= 500:
    frete = peso_kg * 7.00
    motivo = "entrega regional"
else:
    frete = peso_kg * 12.00
    motivo = "entrega nacional"

print(f"Frete ({motivo}): R$ {frete:.2f}")
print(f"Total: R$ {valor_produto + frete:.2f}")</code></pre>
  </div>
  <p>Perceba como o código lê quase como uma tabela de regras de negócio escrita em português. Essa legibilidade é uma das maiores forças do Python — a lógica fica clara até para quem não é programador, facilitando revisões e manutenção futura.</p>

  <div class="tip-box">
    <span class="tip-icon">⚠️</span>
    <div><strong>Erro mais comum:</strong> usar <code>=</code> ao invés de <code>==</code> na comparação. <code>if x = 5</code> é erro de sintaxe. A comparação correta é sempre <code>if x == 5</code>.</div>
  </div>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Qual bloco é executado quando a condição do <code>if</code> é <strong>False</strong> e nenhum <code>elif</code> se aplica?</div>
    <div class="check-options">
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">O bloco <code>else</code></button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">O bloco <code>elif</code></button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">O código repete do início</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Desafio rápido</div>
    <div class="check-question">Qual o resultado de <code>2 ** 8</code>?</div>
    <input type="text" class="check-input" data-answer="256" placeholder="Digite o resultado...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>
</section>"""

# ─────────────────────────── SEMANA 1 EXERCISES ───────────────────────────

def s1_exercises():
    return [
        ("Calculadora de IMC",
         "Calcule o IMC de uma pessoa com peso=70kg e altura=1.75m. Fórmula: IMC = peso / (altura²). Imprima apenas o resultado com 2 casas decimais.",
         "peso = 70\naltura = 1.75\n\n# Calcule o IMC\n# Imprima com 2 casas decimais (ex: 22.86)\n",
         "22.86",
         "imc = peso / (altura ** 2)  depois  print(f'{imc:.2f}')", 10),

        ("Classificador de Nota",
         "Dado nota=7.5, imprima a classificação: 'Excelente' (>=9), 'Aprovado' (>=7), 'Recuperacao' (>=5) ou 'Reprovado' (abaixo de 5).",
         "nota = 7.5\n\n# Use if/elif/else para classificar\n# Imprima exatamente uma das opções acima\n",
         "Aprovado",
         "if nota >= 9: ... elif nota >= 7: print('Aprovado') ...", 10),

        ("Conversor de Temperatura",
         "Converta celsius=100 para Fahrenheit. Fórmula: F = C * 9/5 + 32. Imprima com 1 casa decimal.",
         "celsius = 100\n\n# Converta para Fahrenheit\n# Imprima com 1 casa decimal (ex: 212.0)\n",
         "212.0",
         "fahrenheit = celsius * 9/5 + 32  depois  print(f'{fahrenheit:.1f}')", 10),

        ("Calculadora de Desconto",
         "Um produto custa R$ 200.00 com 15% de desconto. Calcule e imprima o valor final no formato exato: 'R$ 170.00'",
         "preco = 200.0\ndesconto = 0.15\n\n# Calcule o valor com desconto\n# Imprima no formato: R$ 170.00\n",
         "R$ 170.00",
         "final = preco * (1 - desconto)  depois  print(f'R$ {final:.2f}')", 10),

        ("Par ou Impar",
         "Dado n=17, imprima 'Par' se o número for par ou 'Impar' se for ímpar. Use o operador módulo (%).",
         "n = 17\n\n# Use o operador % para verificar\n# Imprima: 'Par' ou 'Impar'\n",
         "Impar",
         "if n % 2 == 0: print('Par') else: print('Impar')", 10),

        ("Salario Liquido",
         "Calcule o salário líquido: bruto=5000, desconto INSS=11%. Imprima no formato exato: 'R$ 4450.00'",
         "bruto = 5000.0\ninss = 0.11\n\n# Calcule o liquido (bruto - desconto)\n# Imprima: R$ 4450.00\n",
         "R$ 4450.00",
         "liquido = bruto - (bruto * inss)  depois  print(f'R$ {liquido:.2f}')", 10),

        ("Faixa Etaria",
         "Dado idade=25, classifique: 'Crianca' (0-12), 'Adolescente' (13-17), 'Jovem adulto' (18-25), 'Adulto' (26-59), 'Idoso' (60+). Imprima a classificação.",
         "idade = 25\n\n# Classifique a faixa etaria\n# Use if/elif/else com os intervalos corretos\n",
         "Jovem adulto",
         "if 18 <= idade <= 25: print('Jovem adulto')", 15),

        ("Troco no Caixa",
         "Produto custa R$ 7.50, cliente pagou R$ 10.00. Imprima o troco no formato: 'Troco: R$ 2.50'",
         "preco = 7.50\npago = 10.00\n\n# Calcule o troco\n# Imprima: Troco: R$ 2.50\n",
         "Troco: R$ 2.50",
         "troco = pago - preco  depois  print(f'Troco: R$ {troco:.2f}')", 10),
    ]

# ─────────────────────────── SEMANA 2 CONTENT ───────────────────────────

def s2_content():
    return """<section class="lesson-section">
  <div class="lesson-intro-box">
    <p><strong>Objetivo da semana:</strong> Aprender as estruturas que permitem trabalhar com conjuntos de dados — listas, dicionários — e criar código reutilizável com funções. Esses são os blocos fundamentais de qualquer script de automação.</p>
  </div>

  <h2>📋 Listas</h2>
  <p>Uma lista é uma coleção <strong>ordenada e mutável</strong> de itens. Ordenada significa que cada elemento tem uma posição fixa, chamada de índice, e você acessa qualquer item pela sua posição. Mutável significa que você pode adicionar, remover ou alterar itens depois de criar a lista. Listas são a estrutura mais usada em Python — praticamente todo script as utiliza.</p>
  <p>O índice começa sempre em zero, não em um. Portanto, o primeiro elemento está na posição 0, o segundo na posição 1, e assim por diante. Python também suporta índices negativos: <code>-1</code> acessa o último elemento, <code>-2</code> o penúltimo. O <strong>slicing</strong> permite extrair fatias da lista usando a notação <code>[início:fim]</code>, onde o índice final é sempre exclusivo.</p>
  <div class="code-block">
    <div class="code-header">Python — Criação, acesso e slicing</div>
    <pre><code">nomes = ["Ana", "Bob", "Carla", "Diego"]

print(nomes[0])    # Ana
print(nomes[-1])   # Diego
print(nomes[1:3])  # ['Bob', 'Carla']
print(nomes[::-1]) # ['Diego', 'Carla', 'Bob', 'Ana']</code></pre>
  </div>
  <p>O slicing <code>[::-1]</code> é uma forma idiomática de inverter qualquer lista ou string. O terceiro parâmetro é o passo — <code>-1</code> percorre de trás para frente. Esse truque é muito útil em algoritmos de processamento de texto e dados.</p>
  <div class="code-block">
    <div class="code-header">Python — Métodos essenciais de listas</div>
    <pre><code">frutas = ["maçã", "banana", "laranja"]

frutas.append("uva")
frutas.insert(1, "manga")
frutas.remove("banana")
removido = frutas.pop()
removido2 = frutas.pop(0)

print(len(frutas))
print("uva" in frutas)

numeros = [3, 1, 4, 1, 5, 9]
numeros.sort()
numeros.sort(reverse=True)

ordenada = sorted(numeros)

quadrados = [x**2 for x in range(1, 6)]
pares = [x for x in range(20) if x % 2 == 0]</code></pre>
  </div>
  <p>Uma distinção importante: <code>.sort()</code> modifica a lista original sem retornar nada, enquanto <code>sorted()</code> retorna uma nova lista ordenada sem alterar a original. Use <code>sorted()</code> quando precisar preservar a ordem original. As <strong>list comprehensions</strong> na última parte são uma das sintaxes mais elegantes do Python — permitem criar listas filtradas e transformadas em uma única linha.</p>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Qual método adiciona um item no <strong>final</strong> de uma lista?</div>
    <input type="text" class="check-input" data-answer="append" placeholder="ex: lista.___('item')">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Desafio rápido</div>
    <div class="check-question">Qual o resultado de <code>len([10, 20, 30, 40, 50])</code>?</div>
    <input type="text" class="check-input" data-answer="5" placeholder="Digite o resultado...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <h2>🔒 Tuplas</h2>
  <p>Tuplas são estruturas idênticas às listas em termos de acesso, mas com uma diferença fundamental: são <strong>imutáveis</strong>. Uma vez criada, você não pode adicionar, remover ou alterar itens. Essa característica não é uma limitação — é uma garantia. Quando você vê uma tupla no código, sabe imediatamente que aquele dado não vai mudar, o que facilita o raciocínio sobre o programa.</p>
  <p>O uso mais prático das tuplas é o <strong>desempacotamento</strong>: você pode atribuir cada elemento a uma variável diferente em uma única linha. Isso é extremamente útil quando uma função precisa retornar múltiplos valores — tecnicamente ela retorna uma tupla, que o chamador desempacota imediatamente.</p>
  <div class="code-block">
    <div class="code-header">Python — Tuplas e desempacotamento</div>
    <pre><code">coordenadas = (23.5, -46.6)
rgb_vermelho = (255, 0, 0)

lat, lon = coordenadas
print(f"Latitude: {lat}, Longitude: {lon}")

r, g, b = rgb_vermelho
print(f"R={r}, G={g}, B={b}")</code></pre>
  </div>
  <p>Use tuplas quando os dados representam um registro fixo — coordenadas geográficas, configurações de conexão (host, porta), cores RGB, ou qualquer conjunto de valores que sempre andam juntos e não devem ser modificados acidentalmente.</p>

  <h2>📚 Dicionários</h2>
  <p>Dicionários armazenam pares de <strong>chave: valor</strong>. Se a lista é como uma fila numerada, o dicionário é como um armário com etiquetas — você busca um item pelo nome, não pela posição. Essa estrutura mapeia perfeitamente dados do mundo real: um cadastro de funcionário, uma nota fiscal, uma resposta de API. É a estrutura mais importante para manipular dados em Python.</p>
  <p>Acessar uma chave inexistente com colchetes (<code>dicionario["chave"]</code>) gera um <code>KeyError</code> e quebra o programa. O método <code>.get()</code> resolve isso: ele retorna <code>None</code> se a chave não existir, ou um valor padrão que você define. Em automações que processam dados variáveis, sempre prefira <code>.get()</code> aos colchetes diretos.</p>
  <div class="code-block">
    <div class="code-header">Python — Dicionários: acesso, modificação e iteração</div>
    <pre><code">funcionario = {
    "nome": "Carlos Silva",
    "cargo": "Analista",
    "salario": 6_500.0,
    "habilidades": ["Python", "SQL", "Excel"]
}

print(funcionario["nome"])
print(funcionario.get("setor", "N/A"))

funcionario["salario"] = 7_000.0
funcionario["setor"] = "Tecnologia"
del funcionario["cargo"]

for chave, valor in funcionario.items():
    print(f"{chave}: {valor}")

if "nome" in funcionario:
    print("Cadastro válido")</code></pre>
  </div>
  <p>A iteração com <code>.items()</code> é a forma mais usada — ela entrega uma tupla <code>(chave, valor)</code> a cada passo do loop, que você desempacota diretamente na assinatura do <code>for</code>. Isso elimina a necessidade de acessar o dicionário dentro do loop.</p>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">O que <code>dicionario.get('chave', 'N/A')</code> retorna se a chave <strong>não existir</strong>?</div>
    <input type="text" class="check-input" data-answer="N/A" placeholder="Digite a resposta...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Qual a diferença principal entre <strong>Lista</strong> e <strong>Tupla</strong>?</div>
    <div class="check-options">
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">Lista é mutável (pode mudar); Tupla é imutável (não muda)</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Tupla pode ter mais elementos que lista</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Lista usa chaves <code>{}</code>; Tupla usa colchetes <code>[]</code></button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <h2>🔄 Loops: for e while</h2>
  <p>Loops executam um bloco de código repetidamente. O <code>for</code> é usado quando você sabe antecipadamente sobre o que vai iterar: os elementos de uma lista, um intervalo de números, as chaves de um dicionário. Ele percorre cada item automaticamente, sem que você precise gerenciar o índice manualmente.</p>
  <p>A função <code>range(início, fim, passo)</code> gera uma sequência de inteiros. <code>enumerate()</code> adiciona um contador automático à iteração — muito útil para numerar itens em relatórios. <code>zip()</code> combina duas listas em paralelo, permitindo percorrer ambas ao mesmo tempo sem lidar com índices.</p>
  <div class="code-block">
    <div class="code-header">Python — for com range, enumerate e zip</div>
    <pre><code">produtos = ["Notebook", "Mouse", "Teclado"]
for produto in produtos:
    print(f"- {produto}")

for i in range(1, 11):
    print(i)

nomes = ["Ana", "Bob", "Carla"]
for i, nome in enumerate(nomes, start=1):
    print(f"{i}. {nome}")

precos = [2500, 90, 150]
for produto, preco in zip(produtos, precos):
    print(f"{produto}: R$ {preco:.2f}")</code></pre>
  </div>
  <p>O <code>while</code> é diferente: ele repete enquanto uma condição for verdadeira, sem saber de antemão quantas vezes vai rodar. É o loop certo para situações onde o número de repetições depende de algo que acontece durante a execução, como aguardar uma resposta de sistema ou processar dados até encontrar um marcador de fim.</p>
  <div class="code-block">
    <div class="code-header">Python — while, break e continue</div>
    <pre><code">tentativas = 0
while tentativas < 3:
    tentativas += 1
    print(f"Tentativa {tentativas}")

for n in range(100):
    if n == 5:
        break
    print(n)

for n in range(10):
    if n % 2 == 0:
        continue
    print(n)

contador = 0
while True:
    contador += 1
    if contador >= 5:
        break
print(f"Parou no {contador}")</code></pre>
  </div>
  <p>O padrão <code>while True: ... break</code> é muito comum em automações: você inicia um loop infinito e usa <code>break</code> para sair quando uma condição específica for atingida. O <code>continue</code> pula para a próxima iteração sem executar o restante do bloco, útil para ignorar itens inválidos em um conjunto de dados.</p>

  <h2>⚙️ Funções</h2>
  <p>Uma função é um bloco de código nomeado que realiza uma tarefa específica. Você a define uma vez com <code>def</code> e pode chamá-la quantas vezes quiser em qualquer parte do programa. O princípio por trás disso tem um nome: DRY — <em>Don't Repeat Yourself</em>. Se você escreveu o mesmo trecho de código em dois lugares, provavelmente deveria ser uma função.</p>
  <p>Parâmetros com <strong>valor padrão</strong> tornam as funções mais flexíveis: o chamador pode omitir o argumento e o padrão é usado. Uma função pode retornar múltiplos valores separados por vírgula — tecnicamente ela retorna uma tupla, que o chamador desempacota. Isso é muito mais limpo do que criar variáveis globais para "passar resultados para fora".</p>
  <div class="code-block">
    <div class="code-header">Python — Funções com parâmetros e retornos</div>
    <pre><code">def saudar(nome):
    return f"Olá, {nome}!"

print(saudar("Ana"))

def calcular_imposto(valor, aliquota=0.15):
    return valor * aliquota

print(calcular_imposto(1000))
print(calcular_imposto(1000, 0.27))

def analisar(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

minimo, maximo, media = analisar([4, 7, 2, 9, 1])
print(f"Min: {minimo}, Max: {maximo}, Média: {media:.1f}")

def somar_tudo(*numeros):
    return sum(numeros)

print(somar_tudo(1, 2, 3, 4, 5))</code></pre>
  </div>
  <p>O parâmetro <code>*numeros</code> com asterisco coleta todos os argumentos extras em uma tupla. Isso é útil quando o número de argumentos varia. Variáveis criadas dentro de uma função existem apenas dentro dela — esse conceito se chama <strong>escopo local</strong>. Tentar acessar uma variável local fora da função gera um <code>NameError</code>.</p>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Qual palavra-chave é usada para <strong>retornar</strong> um valor de uma função?</div>
    <input type="text" class="check-input" data-answer="return" placeholder="Digite a resposta...">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Desafio rápido</div>
    <div class="check-question">O que acontece quando um <code>for</code> encontra um <code>break</code>?</div>
    <div class="check-options">
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">Sai imediatamente do loop</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Pula para a próxima iteração</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Reinicia o loop do zero</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <h2>📦 Importando Bibliotecas</h2>
  <p>Python vem com uma biblioteca padrão enorme — centenas de módulos para matemática, datas, arquivos, redes e muito mais. Além disso, um repositório público chamado PyPI tem mais de 400 mil pacotes de terceiros que você instala com um único comando <code>pip install nome</code>. É esse ecossistema que torna Python tão poderoso.</p>
  <p>Existem três formas de importar. A importação completa traz o módulo inteiro e você acessa funções com <code>modulo.funcao()</code>. A importação com alias (<code>import pandas as pd</code>) cria um apelido mais curto — pd, np, dt são convenções tão estabelecidas que você vai vê-las em praticamente todo código Python profissional. A importação seletiva (<code>from modulo import funcao</code>) traz apenas o que você precisa, sem carregar o resto.</p>
  <div class="code-block">
    <div class="code-header">Python — Importando módulos e instalando pacotes</div>
    <pre><code">import math
print(math.sqrt(16))
print(math.pi)

import datetime as dt
hoje = dt.datetime.now()
print(hoje.strftime("%d/%m/%Y"))

from datetime import datetime, timedelta
amanha = datetime.now() + timedelta(days=1)</code></pre>
  </div>
  <p>Para instalar pacotes externos, use o terminal: <code>pip install pandas</code>, <code>pip install pyautogui</code>. Nunca instale dentro do arquivo Python com <code>os.system()</code> — sempre use o terminal diretamente. Para descobrir o que um módulo oferece, use <code>help(modulo)</code> no Python ou acesse a documentação oficial em <strong>docs.python.org</strong>.</p>

  <div class="tip-box">
    <span class="tip-icon">💡</span>
    <div><strong>Convenção de nomes:</strong> Funções com verbos no infinitivo: <code>calcular_salario()</code>, <code>enviar_email()</code>. Variáveis com substantivos: <code>lista_nomes</code>, <code>total_vendas</code>. Constantes em maiúsculas: <code>TAXA_JUROS = 0.15</code>. Seguir essas convenções faz seu código se parecer profissional desde o início.</div>
  </div>
</section>"""

def s2_exercises():
    return [
        ("Media das Notas",
         "Calcule a media da lista [8.5, 7.0, 9.5, 6.0, 10.0] usando sum() e len(). Imprima com 1 casa decimal.",
         "notas = [8.5, 7.0, 9.5, 6.0, 10.0]\n\n# Calcule usando sum() e len()\n# Imprima com 1 casa decimal\n",
         "8.2",
         "media = sum(notas) / len(notas)  depois  print(f'{media:.1f}')", 10),

        ("Maior e Menor",
         "Dada a lista [5, 2, 8, 1, 9, 3], imprima o maior e o menor em linhas separadas. Formato: 'Maior: 9' e 'Menor: 1'",
         "numeros = [5, 2, 8, 1, 9, 3]\n\n# Use max() e min()\n# Imprima em duas linhas\n",
         "Maior: 9\nMenor: 1",
         "print(f'Maior: {max(numeros)}')  print(f'Menor: {min(numeros)}')", 10),

        ("Numeros Pares",
         "Crie uma lista com todos os números pares de 1 a 20 usando list comprehension e imprima a lista.",
         "# Crie a lista com list comprehension\n# Use range(1, 21) e filtre os pares com % 2 == 0\npares = []\nprint(pares)\n",
         "[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]",
         "pares = [n for n in range(1, 21) if n % 2 == 0]", 10),

        ("Frequencia de Palavras",
         "Conte quantas vezes cada palavra aparece. Imprima em ordem alfabetica no formato 'palavra: count' (uma por linha).",
         'palavras = ["python", "java", "python", "c", "java", "python"]\n\n# Crie um dicionario de frequencias\n# Imprima em ordem alfabetica\n',
         "c: 1\njava: 2\npython: 3",
         "freq = {}; for p in palavras: freq[p] = freq.get(p,0)+1; for k in sorted(freq): print(f'{k}: {freq[k]}')", 15),

        ("Verificador de Palindromo",
         "Verifique se a palavra 'arara' e um palindromo (igual ao contrario). Imprima 'Palindromo' ou 'Nao palindromo'.",
         "palavra = 'arara'\n\n# Compare a palavra com ela mesma invertida\n# Use slicing [::-1] para inverter\n",
         "Palindromo",
         "if palavra == palavra[::-1]: print('Palindromo')", 15),

        ("Sequencia Fibonacci",
         "Crie uma funcao fibonacci(n) que retorna o n-esimo numero. F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2). Imprima fibonacci(10).",
         "def fibonacci(n):\n    # Use loop: comece com a=0, b=1\n    # A cada passo: a, b = b, a+b\n    pass\n\nprint(fibonacci(10))\n",
         "55",
         "a, b = 0, 1; for _ in range(n): a, b = b, a+b; return a", 15),

        ("Fatorial",
         "Crie uma funcao fatorial(n) que calcula n! (ex: 5! = 5*4*3*2*1 = 120). Imprima fatorial(5).",
         "def fatorial(n):\n    # Comece com resultado = 1\n    # Multiplique por cada numero de 1 ate n\n    pass\n\nprint(fatorial(5))\n",
         "120",
         "resultado = 1; for i in range(1, n+1): resultado *= i; return resultado", 15),

        ("Palavra mais Frequente",
         "Encontre a palavra que mais aparece no texto e imprima a palavra e sua frequencia em linhas separadas.",
         'texto = "python java python python java c python"\npalavras = texto.split()\n\n# Crie um dicionario de frequencias\n# Encontre a de maior contagem com max()\nfreq = {}\n# complete aqui\n',
         "python\n4",
         "freq = {}; for p in palavras: freq[p] = freq.get(p,0)+1; mais = max(freq, key=freq.get); print(mais); print(freq[mais])", 20),
    ]

# ─────────────────────────── SEMANA 3 CONTENT ───────────────────────────

def s3_content():
    return """<section class="lesson-section">
  <div class="lesson-intro-box">
    <p><strong>Objetivo da semana:</strong> Criar scripts robustos que automatizam tarefas repetitivas. Você vai aprender a controlar o mouse, teclado e janelas do Windows, além de tratar erros para que a automação não quebre na primeira falha.</p>
  </div>

  <h2>🤖 O que é Automação de Processos (RPA)?</h2>
  <p>RPA significa <em>Robotic Process Automation</em> — automação de processos com robôs de software. A ideia é simples: qualquer tarefa repetitiva que um humano faz no computador pode ser ensinada a um script. Clicar em botões, abrir sistemas, copiar e colar dados entre planilhas, preencher formulários — tudo isso vira código.</p>
  <p>O impacto é imediato. Uma tarefa que consome 30 minutos por dia vira um script de 2 minutos que roda sozinho toda manhã, sem erros humanos, sem esquecimentos, sem cansaço. Multiplicado por dias úteis do ano, são mais de 100 horas liberadas para trabalho de maior valor. No mercado brasileiro, profissionais com habilidades de automação RPA estão entre os mais bem remunerados da área de tecnologia.</p>
  <div class="highlight-grid">
    <div class="highlight-card"><span>⏰</span><strong>Antes:</strong> 30 min/dia copiando relatórios manualmente entre sistemas.</div>
    <div class="highlight-card"><span>⚡</span><strong>Depois:</strong> Script roda em 2 min toda manhã sozinho, sem erro humano.</div>
    <div class="highlight-card"><span>📋</span><strong>Casos de uso:</strong> Formulários, extração de sistemas legados, relatórios, e-mails em massa.</div>
    <div class="highlight-card"><span>💰</span><strong>Mercado:</strong> Automação RPA é uma das habilidades mais valorizadas em TI no Brasil.</div>
  </div>

  <h2>🖱️ PyAutoGUI — Controlando Mouse e Teclado</h2>
  <p>PyAutoGUI é a biblioteca Python que simula ações físicas do usuário: mover o mouse, clicar em posições específicas da tela, digitar texto e pressionar teclas de atalho. Instale com <code>pip install pyautogui</code>. Ela funciona com qualquer programa que rode na sua tela, independente de ter uma API — é como um robô que olha para o monitor e age.</p>
  <p>Antes de qualquer coisa, ative o <strong>FAILSAFE</strong>. Com ele ligado, mover o mouse rapidamente para o canto superior esquerdo da tela interrompe o script imediatamente. Isso é essencial porque, se algo der errado durante o desenvolvimento, você precisa de uma forma de parar o robô sem fechar o terminal manualmente.</p>
  <div class="code-block">
    <div class="code-header">Python — Comandos essenciais do PyAutoGUI</div>
    <pre><code">import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

print(pyautogui.position())

pyautogui.moveTo(500, 300, duration=0.5)
pyautogui.click(x=200, y=400)
pyautogui.doubleClick(x=200, y=400)
pyautogui.rightClick(x=200, y=400)

pyautogui.typewrite("relatório mensal", interval=0.05)
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")
pyautogui.hotkey("ctrl", "v")

time.sleep(1)</code></pre>
  </div>
  <p>A propriedade <code>PAUSE</code> adiciona um intervalo automático entre cada ação do PyAutoGUI. Isso é diferente do <code>time.sleep()</code> manual — funciona como um freio global. Para automações em sistemas rápidos, 0.3 segundos costuma ser suficiente. Para sistemas mais lentos, use 0.5 ou mais.</p>
  <p>A função <code>pyautogui.position()</code> retorna as coordenadas atuais do mouse. Use isso para descobrir exatamente onde está cada elemento na tela antes de codificar os cliques — mova o mouse até o botão desejado e execute essa linha para obter as coordenadas.</p>
  <div class="code-block">
    <div class="code-header">Exemplo real — Preenchendo um formulário para múltiplos registros</div>
    <pre><code">import pyautogui
import time

def preencher_formulario(nome, cpf, email):
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.3

    pyautogui.click(200, 150)
    time.sleep(0.2)
    pyautogui.typewrite(nome, interval=0.05)

    pyautogui.press("tab")
    pyautogui.typewrite(cpf, interval=0.05)

    pyautogui.press("tab")
    pyautogui.typewrite(email, interval=0.05)

    pyautogui.press("enter")
    print(f"Formulário preenchido para {nome}")

cadastros = [
    ("Ana Silva",  "123.456.789-00", "ana@email.com"),
    ("Bob Santos", "987.654.321-00", "bob@email.com"),
]

for nome, cpf, email in cadastros:
    preencher_formulario(nome, cpf, email)
    time.sleep(2)</code></pre>
  </div>
  <p>O padrão de extrair a lógica para uma função (<code>preencher_formulario</code>) e depois chamar em loop é fundamental em automação. Você testa a função com um único registro, valida que funciona, e só então processa a lista completa. Isso economiza muito tempo de debug.</p>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Por que é importante usar <code>time.sleep()</code> entre ações de automação?</div>
    <div class="check-options">
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">Para dar tempo ao sistema/programa carregar antes da próxima ação</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Para tornar o script mais lento de propósito</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">O PyAutoGUI exige sleep após cada clique</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Desafio rápido</div>
    <div class="check-question">Qual variável do PyAutoGUI deve ser <code>True</code> para que mover o mouse ao canto esquerdo <strong>interrompa o script</strong>?</div>
    <input type="text" class="check-input" data-answer="FAILSAFE" placeholder="pyautogui.___ = True">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <h2>🪟 pywin32 — Controlando Janelas do Windows</h2>
  <p>PyAutoGUI controla o mouse e teclado, mas não sabe nada sobre as janelas abertas. O pywin32 preenche essa lacuna: ele acessa a API do Windows para encontrar janelas pelo título, trazê-las para o primeiro plano, maximizá-las, minimizá-las e até verificar se estão visíveis. Instale com <code>pip install pywin32</code>.</p>
  <p>Cada janela aberta no Windows tem um identificador único chamado <strong>hwnd</strong> (handle to a window). O pywin32 usa esse handle para todas as operações. A função <code>FindWindow</code> busca uma janela pelo título exato, enquanto <code>EnumWindows</code> lista todas as janelas abertas — útil quando você não sabe o título exato.</p>
  <div class="code-block">
    <div class="code-header">Python — Encontrando e controlando janelas</div>
    <pre><code">import win32gui
import win32con
import subprocess
import time

subprocess.Popen(r"C:\Windows\System32\notepad.exe")
time.sleep(1.5)

hwnd = win32gui.FindWindow(None, "Sem título - Bloco de Notas")

if hwnd:
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    print(f"Janela encontrada: {hwnd}")
else:
    print("Janela não encontrada")

def listar_janelas():
    janelas = []
    def callback(hwnd, _):
        titulo = win32gui.GetWindowText(hwnd)
        if titulo and win32gui.IsWindowVisible(hwnd):
            janelas.append((hwnd, titulo))
    win32gui.EnumWindows(callback, None)
    return janelas

for hwnd, titulo in listar_janelas()[:5]:
    print(f"{hwnd}: {titulo}")</code></pre>
  </div>
  <p>A combinação pywin32 + PyAutoGUI é poderosa: use pywin32 para abrir e focar a janela do sistema alvo, e então use PyAutoGUI para interagir com ela. Sem trazer a janela para o primeiro plano primeiro, o PyAutoGUI pode clicar na janela errada.</p>

  <h2>🛡️ Tratamento de Erros com try/except</h2>
  <p>Em automações de produção, erros são inevitáveis: o sistema fica lento e uma janela não carrega a tempo, um arquivo está aberto por outra pessoa, uma célula tem um valor inesperado. Sem tratamento de erros, um único problema quebra toda a automação e você precisa reiniciá-la manualmente. Com <code>try/except</code>, o script captura o problema, reage adequadamente e continua.</p>
  <p>A estrutura completa tem quatro blocos. O <code>try</code> contém o código que pode falhar. O <code>except</code> especifica o tipo de erro a tratar — você pode ter vários <code>except</code> para tipos diferentes. O <code>else</code> roda apenas quando não houve nenhum erro. O <code>finally</code> roda sempre, com ou sem erro — ideal para liberar recursos como arquivos abertos ou conexões.</p>
  <div class="code-block">
    <div class="code-header">Python — try / except / else / finally</div>
    <pre><code">try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero")
except ValueError as e:
    print(f"Valor inválido: {e}")
except Exception as e:
    print(f"Erro inesperado: {type(e).__name__}: {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Finalizando...")

try:
    valor = int("abc")
except (ValueError, TypeError) as e:
    print(f"Erro de conversão: {e}")

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisor não pode ser zero")
    return a / b</code></pre>
  </div>
  <p>A palavra-chave <code>raise</code> permite lançar seus próprios erros. Isso é útil quando você quer que uma função sinalize explicitamente condições inválidas — ao invés de retornar <code>None</code> silenciosamente e causar bugs difíceis de rastrear mais adiante, você sinaliza o problema na origem.</p>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Qual bloco do <code>try/except</code> é <strong>sempre executado</strong>, com ou sem erro?</div>
    <input type="text" class="check-input" data-answer="finally" placeholder="try / except / else / ___">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Qual exceção Python levanta ao tentar dividir um número por zero?</div>
    <div class="check-options">
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">ZeroDivisionError</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">ValueError</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">TypeError</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <h2>📝 Logging e Automação Robusta</h2>
  <p>Imprimir mensagens com <code>print()</code> é suficiente durante o desenvolvimento, mas em produção você precisa de registros persistentes. O módulo <code>logging</code> da biblioteca padrão grava mensagens em arquivo com timestamp, nível de gravidade e contexto — exatamente o que você precisa para entender o que aconteceu quando um script falhou às 3h da manhã.</p>
  <p>Combinar logging com try/except e um mecanismo de retry cria automações verdadeiramente robustas. O padrão retry é especialmente útil com sistemas de rede ou que podem estar temporariamente ocupados: tente de novo algumas vezes antes de desistir.</p>
  <div class="code-block">
    <div class="code-header">Python — Logging e padrão de retry</div>
    <pre><code">import logging
import time

logging.basicConfig(
    filename="automacao.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def clicar_com_retry(x, y, nome="botão", tentativas=3):
    for i in range(1, tentativas + 1):
        try:
            import pyautogui
            pyautogui.click(x, y)
            logging.info(f"Clique em '{nome}' OK (tentativa {i})")
            return True
        except Exception as e:
            logging.warning(f"Falha em '{nome}' (tentativa {i}): {e}")
            time.sleep(1)
    logging.error(f"Falha definitiva em '{nome}'")
    return False

if clicar_com_retry(200, 150, "Botão Exportar"):
    print("Exportação iniciada")
else:
    print("Não foi possível clicar no botão")</code></pre>
  </div>

  <h2>💾 Salvando Resultados em Arquivo</h2>
  <p>Toda automação que processa dados precisa salvar os resultados. O Python tem suporte nativo a arquivos CSV e texto puro, sem necessidade de bibliotecas externas. O gerenciador de contexto <code>with open(...) as f</code> garante que o arquivo seja fechado corretamente mesmo que ocorra um erro durante a escrita — nunca use <code>f = open()</code> sem <code>with</code> em código de produção.</p>
  <p>Uma boa prática ao salvar relatórios é incluir a data e hora no nome do arquivo. Isso cria um histórico automático e evita que uma execução sobrescreva os resultados da anterior.</p>
  <div class="code-block">
    <div class="code-header">Python — Escrevendo CSV e log em TXT</div>
    <pre><code">import csv
from datetime import datetime

dados = [
    {"nome": "Produto A", "valor": 150.0, "qtd": 10},
    {"nome": "Produto B", "valor": 89.90, "qtd": 25},
]

data_hoje = datetime.now().strftime("%Y-%m-%d_%H%M")
nome_arquivo = f"relatorio_{data_hoje}.csv"

with open(nome_arquivo, "w", newline="", encoding="utf-8") as f:
    campos = ["nome", "valor", "qtd", "total"]
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    for d in dados:
        d["total"] = d["valor"] * d["qtd"]
        writer.writerow(d)

print(f"Arquivo salvo: {nome_arquivo}")

with open("log.txt", "a", encoding="utf-8") as f:
    f.write(f"{datetime.now()} - {len(dados)} registros processados\n")</code></pre>
  </div>
  <p>O modo <code>"w"</code> sobrescreve o arquivo se já existir. O modo <code>"a"</code> (append) adiciona ao final sem apagar o conteúdo anterior — ideal para logs acumulativos. O parâmetro <code>encoding="utf-8"</code> é essencial para preservar acentuação e caracteres especiais.</p>

  <div class="tip-box">
    <span class="tip-icon">⚠️</span>
    <div><strong>Regra de ouro:</strong> Comece com <code>time.sleep()</code> mais generoso e vá reduzindo. É muito mais fácil acelerar uma automação que funciona do que debugar uma que falha intermitentemente por falta de tempo de espera.</div>
  </div>
</section>"""

def s3_exercises():
    return [
        ("Divisao Segura",
         "Crie a funcao dividir(a, b) com try/except. Se b=0, retorne a string 'Erro: divisao por zero'. Imprima dividir(10, 2) e dividir(5, 0) em linhas separadas.",
         "def dividir(a, b):\n    try:\n        # complete aqui\n        pass\n    except ZeroDivisionError:\n        # complete aqui\n        pass\n\nprint(dividir(10, 2))\nprint(dividir(5, 0))\n",
         "5.0\nErro: divisao por zero",
         "try: return a/b  except ZeroDivisionError: return 'Erro: divisao por zero'", 10),

        ("Validador de Idades",
         "Filtre idades validas (entre 0 e 120, sem None). Imprima 'Validas: 4' e 'Invalidas: 3'.",
         "idades = [25, -3, 18, None, 45, 200, 30]\n\n# Filtre as validas: nao-None e entre 0 e 120\nvalidas = []\n# complete\nprint(f'Validas: {len(validas)}')\nprint(f'Invalidas: {len(idades) - len(validas)}')\n",
         "Validas: 4\nInvalidas: 3",
         "validas = [i for i in idades if i is not None and 0 <= i <= 120]", 10),

        ("Contador de Logs",
         "Conte quantas linhas sao INFO e quantas sao ERROR. Imprima 'INFO: 3' e 'ERROR: 2'.",
         'logs = ["INFO: inicio", "ERROR: falha", "INFO: processando", "ERROR: timeout", "INFO: fim"]\n\n# Use sum() com generator expression\ninfos = 0\nerros = 0\n# complete\nprint(f"INFO: {infos}")\nprint(f"ERROR: {erros}")\n',
         "INFO: 3\nERROR: 2",
         "infos = sum(1 for l in logs if l.startswith('INFO')); erros = sum(1 for l in logs if l.startswith('ERROR'))", 10),

        ("Processador de Vendas",
         "Filtre as vendas com status='ok', some os valores e imprima 'Vendas ok: 2' e 'Total: 450'.",
         'vendas = [\n    {"id": 1, "valor": 150, "status": "ok"},\n    {"id": 2, "valor": -50, "status": "erro"},\n    {"id": 3, "valor": 300, "status": "ok"},\n    {"id": 4, "valor": 0, "status": "erro"},\n]\n\n# Filtre e some\nok = []\n# complete\nprint(f"Vendas ok: {len(ok)}")\nprint(f"Total: {sum(v[\'valor\'] for v in ok)}")\n',
         "Vendas ok: 2\nTotal: 450",
         "ok = [v for v in vendas if v['status'] == 'ok']", 15),

        ("Simulacao de Retry",
         "A funcao executar() deve tentar ate 3 vezes. Nas tentativas 1 e 2, imprime 'Tentativa X falhou'. Na 3, imprime 'Sucesso na tentativa 3'.",
         "def executar(tentativas_max):\n    for tentativa in range(1, tentativas_max + 1):\n        try:\n            if tentativa < 3:\n                raise Exception('Falhou')\n            return f'Sucesso na tentativa {tentativa}'\n        except Exception:\n            print(f'Tentativa {tentativa} falhou')\n    return 'Esgotou tentativas'\n\nresultado = executar(3)\nprint(resultado)\n",
         "Tentativa 1 falhou\nTentativa 2 falhou\nSucesso na tentativa 3",
         "O codigo ja esta quase pronto — revise a logica do try/except e o return dentro do loop", 15),

        ("Gerador de CSV",
         "Gere um relatorio CSV no terminal: cabecalho 'nome,setor,salario' e uma linha por funcionario.",
         'dados = [\n    {"nome": "Ana", "setor": "TI", "salario": 5000},\n    {"nome": "Bob", "setor": "RH", "salario": 4000},\n    {"nome": "Carla", "setor": "TI", "salario": 6000},\n]\n\n# Imprima o cabecalho e depois cada linha no formato CSV\nprint("nome,setor,salario")\nfor d in dados:\n    # complete\n    pass\n',
         "nome,setor,salario\nAna,TI,5000\nBob,RH,4000\nCarla,TI,6000",
         "print(f\"{d['nome']},{d['setor']},{d['salario']}\")", 15),

        ("Verificador de Campos",
         "Verifique quais campos do registro estao vazios (None ou string vazia). Imprima 'Campos invalidos: email, telefone'.",
         'registro = {"nome": "Carlos", "email": "", "telefone": None, "cidade": "SP"}\ncampos_obrigatorios = ["nome", "email", "telefone", "cidade"]\n\nerros = []\nfor campo in campos_obrigatorios:\n    # verifique se o valor esta vazio ou None\n    pass\n\nif erros:\n    print(f"Campos invalidos: {\', \'.join(erros)}")\nelse:\n    print("Registro valido")\n',
         "Campos invalidos: email, telefone",
         "if not registro.get(campo): erros.append(campo)", 15),

        ("Extrator de Dados Estruturados",
         "Extraia os dados de cada registro (separado por ';'), some os salarios e calcule a media. Imprima 'Total folha: 15500' e 'Media: 5167'.",
         'registros = ["Joao;30;5000", "Maria;25;4500", "Pedro;35;6000"]\n\ntotal = 0\nfor r in registros:\n    partes = r.split(";")\n    salario = int(partes[2])\n    total += salario\n\nprint(f"Total folha: {total}")\nprint(f"Media: {total // len(registros)}")\n',
         "Total folha: 15500\nMedia: 5166",
         "Use r.split(';') e int(partes[2]) para extrair o salario", 20),
    ]

# ─────────────────────────── SEMANA 4 CONTENT ───────────────────────────

def s4_content():
    return """<section class="lesson-section">
  <div class="lesson-intro-box">
    <p><strong>Objetivo da semana:</strong> Dominar o Pandas — a biblioteca mais poderosa do Python para dados — e automatizar a execução do script para rodar sozinho todos os dias.</p>
  </div>

  <h2>🐼 O que é o Pandas?</h2>
  <p>Pandas é a biblioteca que transformou Python na linguagem dominante para análise de dados. O nome vem de <em>Panel Data</em> — dados em painel, um conceito da econometria. Criada em 2008 por Wes McKinney enquanto trabalhava numa gestora de investimentos, ela surgiu da necessidade de manipular grandes volumes de dados financeiros de forma eficiente. Hoje é usada por empresas como Google, Facebook, JPMorgan e praticamente qualquer empresa que analise dados com Python.</p>
  <p>A analogia com o Excel é inevitável: o Pandas trabalha com tabelas. Mas a diferença é radical. O Excel trava com planilhas de 100 mil linhas; o Pandas processa milhões de linhas em segundos. O Excel exige cliques manuais; o Pandas é código que você executa, automatiza e versiona. O Excel não tem tratamento de erros; o Pandas tem. Instale com <code>pip install pandas openpyxl</code>.</p>
  <div class="highlight-grid">
    <div class="highlight-card"><span>📊</span><strong>DataFrame</strong><br>Tabela 2D com linhas e colunas — como uma planilha Excel programável.</div>
    <div class="highlight-card"><span>📈</span><strong>Series</strong><br>Uma coluna isolada — como uma lista com índice nomeado e operações vetorizadas.</div>
    <div class="highlight-card"><span>⚡</span><strong>Velocidade</strong><br>Processa milhões de linhas em segundos. O que leva horas no Excel, leva segundos.</div>
    <div class="highlight-card"><span>🔗</span><strong>Integração</strong><br>Lê CSV, Excel, JSON, SQL. Exporta para qualquer formato.</div>
  </div>

  <h2>📂 Lendo e Explorando Arquivos</h2>
  <p>O primeiro passo em qualquer análise é carregar os dados. O Pandas suporta nativamente os formatos mais comuns do mundo corporativo. A função <code>pd.read_csv()</code> lê arquivos separados por vírgula (ou qualquer outro separador). A função <code>pd.read_excel()</code> lê planilhas Excel, podendo especificar qual aba e quantas linhas pular no topo.</p>
  <p>Depois de carregar, o segundo passo sempre é <strong>explorar</strong>: verificar quantas linhas e colunas existem, quais são os nomes das colunas, que tipos de dados cada coluna contém e se há valores ausentes. Esses cinco minutos de exploração evitam horas de bugs durante o processamento.</p>
  <div class="code-block">
    <div class="code-header">Python — Lendo CSV e Excel, explorando o DataFrame</div>
    <pre><code">import pandas as pd

df = pd.read_csv("vendas.csv")
df = pd.read_csv("vendas.csv", sep=";")
df = pd.read_csv("vendas.csv", encoding="latin-1")

df = pd.read_excel("relatorio.xlsx")
df = pd.read_excel("relatorio.xlsx", sheet_name="Jan")
df = pd.read_excel("relatorio.xlsx", skiprows=2)

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())</code></pre>
  </div>
  <p>O retorno de <code>df.shape</code> é uma tupla <code>(linhas, colunas)</code>. O método <code>df.info()</code> mostra o tipo de cada coluna, a contagem de valores não-nulos e a memória usada — é o diagnóstico mais completo em uma linha. O <code>df.describe()</code> gera estatísticas descritivas (média, desvio padrão, mínimo, máximo) para todas as colunas numéricas.</p>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Qual método exibe as primeiras 5 linhas de um DataFrame?</div>
    <input type="text" class="check-input" data-answer="head" placeholder="df.___()" >
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Desafio rápido</div>
    <div class="check-question">Se um DataFrame tem 500 linhas e 6 colunas, qual o resultado de <code>df.shape</code>?</div>
    <input type="text" class="check-input" data-answer="(500, 6)" placeholder="(linhas, colunas)">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <h2>🔍 Selecionando e Filtrando Dados</h2>
  <p>Selecionar colunas e filtrar linhas são as operações mais frequentes no Pandas. Para selecionar uma única coluna, use colchetes com o nome: <code>df["coluna"]</code> — isso retorna uma <strong>Series</strong>. Para selecionar múltiplas colunas, passe uma lista: <code>df[["col1", "col2"]]</code> — isso retorna um <strong>DataFrame</strong>. A diferença importa porque Series e DataFrame têm métodos distintos.</p>
  <p>Filtrar linhas usa o que chamamos de <strong>indexação booleana</strong>: você cria uma condição que gera uma coluna de True/False e passa ela para o DataFrame. O resultado são apenas as linhas onde a condição é verdadeira. Para combinar múltiplas condições, use <code>&</code> para E lógico e <code>|</code> para OU lógico — nunca use <code>and</code> ou <code>or</code> do Python aqui, pois eles não funcionam com arrays.</p>
  <div class="code-block">
    <div class="code-header">Python — Seleção de colunas e filtros de linhas</div>
    <pre><code">import pandas as pd

df = pd.DataFrame({
    "produto":   ["Notebook", "Mouse", "Teclado", "Monitor", "Headset"],
    "categoria": ["Tech", "Periferico", "Periferico", "Tech", "Audio"],
    "valor":     [2500, 90, 150, 1200, 350],
    "estoque":   [10, 50, 30, 8, 20]
})

nomes = df["produto"]
tabela = df[["produto", "valor"]]

caros = df[df["valor"] > 500]
tech  = df[df["categoria"] == "Tech"]

caro_tech     = df[(df["valor"] > 500) & (df["categoria"] == "Tech")]
barato_audio  = df[(df["valor"] < 200) | (df["categoria"] == "Audio")]

selecionados = df[df["categoria"].isin(["Tech", "Audio"])]
tem_tec      = df[df["produto"].str.contains("Tec", case=False)]</code></pre>
  </div>
  <p>O método <code>.isin()</code> é equivalente a múltiplos <code>==</code> unidos por <code>|</code> — muito mais limpo quando você quer filtrar por uma lista de valores. O método <code>.str.contains()</code> aplica uma busca de texto dentro de cada valor da coluna, com <code>case=False</code> para ignorar maiúsculas/minúsculas.</p>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Para combinar dois filtros com E lógico no Pandas, qual operador usar?</div>
    <div class="check-options">
      <button class="check-option" data-correct="true" onclick="checkChoice(this)"><code>&</code> — E lógico entre condições booleanas do Pandas</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)"><code>and</code> — operador lógico do Python</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)"><code>+</code> — concatenação de filtros</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <h2>🔧 Transformando Dados</h2>
  <p>Raramente os dados chegam exatamente como você precisa. É muito comum precisar criar colunas calculadas, transformar valores, renomear colunas com nomes ruins ou reordenar o DataFrame. O Pandas facilita todas essas operações com sintaxe vetorizada — ao invés de escrever um loop para calcular o total de cada linha, você simplesmente multiplica duas colunas.</p>
  <p>O método <code>.apply()</code> é o mais versátil: ele aplica uma função a cada valor de uma coluna, permitindo lógica condicional complexa que seria impossível com operações vetorizadas simples. Para casos simples, porém, sempre prefira a vetorização direta — ela é muito mais rápida.</p>
  <div class="code-block">
    <div class="code-header">Python — Criando colunas e transformando valores</div>
    <pre><code">import pandas as pd

df = pd.DataFrame({
    "produto":     ["Notebook", "Mouse", "Teclado"],
    "valor":       [2500, 90, 150],
    "qtd_vendida": [5, 100, 45]
})

df["total_vendas"]   = df["valor"] * df["qtd_vendida"]
df["valor_com_iva"]  = df["valor"] * 1.12

def classificar(valor):
    if valor >= 1000:   return "Premium"
    elif valor >= 200:  return "Intermediario"
    else:               return "Basico"

df["faixa"] = df["valor"].apply(classificar)

df.rename(columns={"valor": "preco_unit"}, inplace=True)
df = df[["produto", "preco_unit", "qtd_vendida", "total_vendas"]]

print(df["preco_unit"].sum())
print(df["preco_unit"].mean())
print(df["preco_unit"].max())</code></pre>
  </div>
  <p>O parâmetro <code>inplace=True</code> modifica o DataFrame original sem precisar atribuir o resultado de volta. Sem ele, a operação retorna um novo DataFrame e o original não é alterado. Para iniciantes, é mais claro fazer a atribuição explicitamente (<code>df = df.rename(...)</code>) até entender bem o fluxo.</p>

  <h2>🧹 Limpeza de Dados</h2>
  <p>Dados reais são sujos. Valores faltando, duplicatas, formatos inconsistentes, espaços extras no início e fim das strings — esses problemas são a norma, não a exceção. A limpeza é geralmente a etapa que consome mais tempo em qualquer projeto de dados, podendo chegar a 80% do trabalho total. Por isso, dominar as ferramentas de limpeza do Pandas é mais importante do que qualquer análise sofisticada.</p>
  <p>Valores ausentes são representados por <code>NaN</code> (Not a Number) no Pandas. Você pode removê-los com <code>dropna()</code> ou preenchê-los com <code>fillna()</code>. A escolha depende do contexto: remover faz sentido quando a linha inteira é inútil sem aquele campo; preencher com zero, média ou um valor padrão faz sentido quando você quer preservar o registro.</p>
  <div class="code-block">
    <div class="code-header">Python — Nulos, duplicatas e limpeza de strings</div>
    <pre><code">import pandas as pd

print(df.isnull().sum())

df.dropna(subset=["nome", "cpf"], inplace=True)
df["valor"].fillna(0, inplace=True)
df["setor"].fillna("Sem Setor", inplace=True)

print(df.duplicated().sum())
df.drop_duplicates(subset=["cpf"], inplace=True)

df["data"]  = pd.to_datetime(df["data"], format="%d/%m/%Y")
df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

df["nome"] = df["nome"].str.strip().str.upper()
df["cpf"]  = df["cpf"].str.replace(".", "").str.replace("-", "")</code></pre>
  </div>
  <p>O parâmetro <code>errors="coerce"</code> no <code>pd.to_numeric()</code> converte valores inválidos para <code>NaN</code> ao invés de gerar um erro — muito mais seguro quando você não controla a qualidade dos dados de entrada. O encadeamento de métodos string (<code>.str.strip().str.upper()</code>) aplica múltiplas transformações em sequência sem variáveis intermediárias.</p>

  <h2>📊 Agrupando Dados com GroupBy</h2>
  <p>O GroupBy é o equivalente ao SOMASE, MÉDIASE e tabelas dinâmicas do Excel — só que muito mais poderoso e sem limitações de linhas. A ideia é: agrupe as linhas pelo valor de uma coluna e aplique uma função de agregação (soma, média, contagem, máximo) em cada grupo. Em uma linha de código você obtém o que levaria vários passos no Excel.</p>
  <p>O resultado de um GroupBy tem o índice com os valores agrupados. Para usar o resultado como um DataFrame normal e passá-lo para outras operações, use <code>.reset_index()</code> — isso transforma o índice em uma coluna regular.</p>
  <div class="code-block">
    <div class="code-header">Python — GroupBy com soma, média e múltiplas agregações</div>
    <pre><code">import pandas as pd

df = pd.DataFrame({
    "vendedor": ["Ana", "Bob", "Ana", "Bob", "Ana"],
    "produto":  ["A",   "A",   "B",   "B",   "A"],
    "valor":    [1000,  1500,  800,   900,   1200]
})

por_vendedor = df.groupby("vendedor")["valor"].sum()

resumo = df.groupby("vendedor")["valor"].agg(["sum", "mean", "count"])

por_dupla = df.groupby(["vendedor", "produto"])["valor"].sum()

resultado = df.groupby("vendedor")["valor"].sum().reset_index()
resultado.columns = ["vendedor", "total_vendas"]
print(resultado)</code></pre>
  </div>
  <p>Com <code>.agg()</code> você aplica múltiplas funções de uma vez, recebendo uma tabela com todas as estatísticas por grupo. O agrupamento por múltiplas colunas cria uma hierarquia de grupos — útil para relatórios que precisam de desdobramentos como "vendas por vendedor dentro de cada região".</p>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Qual método Pandas agrupa dados por categoria, equivalente ao GROUP BY do SQL?</div>
    <input type="text" class="check-input" data-answer="groupby" placeholder="df.___(coluna)">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <h2>💾 Exportando e Agendando</h2>
  <p>Depois de processar os dados, você precisa salvar os resultados. O Pandas exporta para CSV e Excel com uma única linha. Para CSV, <code>index=False</code> evita que o índice numérico do DataFrame apareça como uma coluna extra no arquivo — quase sempre é o comportamento desejado. Para Excel, o <code>ExcelWriter</code> permite criar múltiplas abas em um mesmo arquivo.</p>
  <p>Para tornar o script verdadeiramente autônomo, configure-o no <strong>Agendador de Tarefas do Windows</strong> (Task Scheduler). Você define o horário de execução, o caminho do Python e o caminho do script — e ele roda sozinho todos os dias, sem intervenção humana.</p>
  <div class="code-block">
    <div class="code-header">Python — Exportando para CSV e Excel</div>
    <pre><code">import pandas as pd
from datetime import datetime

data = datetime.now().strftime("%Y-%m-%d")

df.to_csv(f"relatorio_{data}.csv", index=False, sep=";", encoding="utf-8")

with pd.ExcelWriter(f"relatorio_{data}.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Dados", index=False)

print(f"Salvo: relatorio_{data}.xlsx")</code></pre>
  </div>
  <div class="code-block">
    <div class="code-header">Agendador de Tarefas — Executar todo dia às 8h</div>
    <pre><code"># Win+R → taskschd.msc → Criar Tarefa Básica
# Disparador: Diariamente → 08:00
# Ação: Iniciar um programa
#   Programa:   C:\Python311\python.exe
#   Argumentos: C:\Scripts\relatorio.py
#   Iniciar em: C:\Scripts\

import logging
from datetime import datetime

logging.basicConfig(
    filename=r"C:\Scripts\log_execucao.txt",
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

def main():
    try:
        logging.info("Script iniciado")
        # ... processamento aqui ...
        logging.info("Script concluido com sucesso")
    except Exception as e:
        logging.error(f"Falha: {e}")

if __name__ == "__main__":
    main()</code></pre>
  </div>
  <p>O bloco <code>if __name__ == "__main__":</code> garante que o código só execute quando o arquivo é rodado diretamente, não quando é importado por outro módulo. Isso é uma boa prática em qualquer script que será executado automaticamente.</p>
</section>"""

def s4_exercises():
    return [
        ("Total por Categoria",
         "Some o valor total de vendas por categoria. Imprima 'Tech: 3790' e 'Mobilia: 1400' em linhas separadas (nessa ordem).",
         'vendas = [\n    {"produto": "Notebook", "categoria": "Tech", "valor": 2500},\n    {"produto": "Mouse", "categoria": "Tech", "valor": 90},\n    {"produto": "Cadeira", "categoria": "Mobilia", "valor": 800},\n    {"produto": "Monitor", "categoria": "Tech", "valor": 1200},\n    {"produto": "Mesa", "categoria": "Mobilia", "valor": 600},\n]\n\ntotais = {}\nfor v in vendas:\n    cat = v["categoria"]\n    totais[cat] = totais.get(cat, 0) + v["valor"]\n\nfor cat, total in totais.items():\n    print(f"{cat}: {total}")\n',
         "Tech: 3790\nMobilia: 1400",
         "Use dict com .get(cat, 0) para acumular totais", 15),

        ("Limpeza de Dados",
         "Remova None e duplicatas, ordene e imprima cada numero em uma linha.",
         "dados = [3, 1, None, 4, 1, 5, None, 9, 2, 6, 5, 3]\n\n# 1. Remova os None\n# 2. Remova duplicatas com set()\n# 3. Ordene com sorted()\nlimpos = []\n# complete\nfor n in limpos:\n    print(n)\n",
         "1\n2\n3\n4\n5\n6\n9",
         "limpos = sorted(set(x for x in dados if x is not None))", 10),

        ("Filtro e Ordenacao",
         "Filtre produtos com valor >= 500 e imprima do mais caro ao mais barato no formato 'Nome: R$ valor'.",
         'produtos = [\n    {"nome": "Notebook", "valor": 2500},\n    {"nome": "Mouse", "valor": 90},\n    {"nome": "Cadeira", "valor": 800},\n    {"nome": "Monitor", "valor": 1200},\n]\n\n# Filtre os caros e ordene do maior para o menor\ncaros = [p for p in produtos if p["valor"] >= 500]\ncaros_ord = sorted(caros, key=lambda x: x["valor"], reverse=True)\nfor p in caros_ord:\n    print(f"{p[\'nome\']}: R$ {p[\'valor\']}")\n',
         "Notebook: R$ 2500\nMonitor: R$ 1200\nCadeira: R$ 800",
         "sorted(caros, key=lambda x: x['valor'], reverse=True)", 15),

        ("Media por Grupo",
         "Calcule a media de notas por aluno. Imprima em ordem alfabetica: 'Ana: 8.0' e 'Bob: 7.0'.",
         'notas = [\n    {"aluno": "Ana", "nota": 8},\n    {"aluno": "Bob", "nota": 6},\n    {"aluno": "Ana", "nota": 9},\n    {"aluno": "Bob", "nota": 7},\n    {"aluno": "Ana", "nota": 7},\n    {"aluno": "Bob", "nota": 8},\n]\n\ntotais = {}\ncontagens = {}\nfor n in notas:\n    aluno = n["aluno"]\n    totais[aluno] = totais.get(aluno, 0) + n["nota"]\n    contagens[aluno] = contagens.get(aluno, 0) + 1\n\nfor aluno in sorted(totais.keys()):\n    media = totais[aluno] / contagens[aluno]\n    print(f"{aluno}: {media:.1f}")\n',
         "Ana: 8.0\nBob: 7.0",
         "Divida totais[aluno] por contagens[aluno] e formate com :.1f", 15),

        ("Detector de Duplicatas",
         "Encontre e-mails duplicados. Imprima 'Duplicatas: 2' e depois cada e-mail duplicado em ordem alfabetica.",
         'emails = ["ana@mail.com", "bob@mail.com", "ana@mail.com", "carlos@mail.com", "bob@mail.com"]\n\nvistos = set()\nduplicatas = []\nfor e in emails:\n    if e in vistos and e not in duplicatas:\n        duplicatas.append(e)\n    vistos.add(e)\n\nprint(f"Duplicatas: {len(duplicatas)}")\nfor d in sorted(duplicatas):\n    print(d)\n',
         "Duplicatas: 2\nana@mail.com\nbob@mail.com",
         "Use um set() para rastrear os ja vistos e uma lista para os duplicados", 15),

        ("Transformacao com Bonus",
         "Calcule salario + 10% de bonus para cada funcionario e imprima 'Nome: R$ total' (sem casas decimais).",
         'funcionarios = [\n    {"nome": "Ana Silva", "salario": 5000},\n    {"nome": "Bob Costa", "salario": 3500},\n    {"nome": "Carol Lima", "salario": 7000},\n]\n\nfor f in funcionarios:\n    bonus = f["salario"] * 0.10\n    total = f["salario"] + bonus\n    print(f"{f[\'nome\']}: R$ {total:.0f}")\n',
         "Ana Silva: R$ 5500\nBob Costa: R$ 3850\nCarol Lima: R$ 7700",
         "bonus = salario * 0.10  depois  total = salario + bonus  depois  {total:.0f}", 15),

        ("Agregacao por Mes",
         "Some as quantidades vendidas por mes. Imprima 'Jan: 15 unidades' e 'Fev: 20 unidades'.",
         'vendas = [\n    {"mes": "Jan", "produto": "A", "qtd": 10},\n    {"mes": "Jan", "produto": "B", "qtd": 5},\n    {"mes": "Fev", "produto": "A", "qtd": 8},\n    {"mes": "Fev", "produto": "B", "qtd": 12},\n]\n\npor_mes = {}\nfor v in vendas:\n    mes = v["mes"]\n    por_mes[mes] = por_mes.get(mes, 0) + v["qtd"]\n\nfor mes, total in por_mes.items():\n    print(f"{mes}: {total} unidades")\n',
         "Jan: 15 unidades\nFev: 20 unidades",
         "Use dict com .get(mes, 0) para acumular quantidades", 15),

        ("Relatorio de Estoque",
         "Calcule o valor total em estoque (apenas produtos com estoque > 0). Imprima 'Produtos disponiveis: 3' e 'Valor em estoque: R$ 34000'.",
         'produtos = [\n    {"nome": "Notebook", "valor": 2500, "estoque": 10},\n    {"nome": "Mouse",    "valor": 90,   "estoque": 50},\n    {"nome": "Monitor",  "valor": 1200, "estoque": 0},\n    {"nome": "Teclado",  "valor": 150,  "estoque": 30},\n]\n\ndisponivel = [p for p in produtos if p["estoque"] > 0]\ntotal = sum(p["valor"] * p["estoque"] for p in disponivel)\n\nprint(f"Produtos disponiveis: {len(disponivel)}")\nprint(f"Valor em estoque: R$ {total}")\n',
         "Produtos disponiveis: 3\nValor em estoque: R$ 34000",
         "2500*10 + 90*50 + 150*30 = 25000 + 4500 + 4500 = 34000", 20),
    ]

# ─────────────────────────── PROJETO PRÁTICO ───────────────────────────

def s5_content():
    return """<section class="lesson-section">
  <div class="lesson-intro-box">
    <p><strong>Você chegou até aqui.</strong> Nas quatro semanas anteriores construiu uma base sólida em Python. Agora chegou o momento mais importante: aplicar tudo isso em um projeto real, do zero, com suporte direto do instrutor.</p>
  </div>

  <h2>🎯 O que é o Projeto Prático?</h2>
  <p>O projeto prático é uma sessão individual de 2 horas onde você e o instrutor vão construir juntos um script Python que resolve um problema real da sua rotina. Não é uma aula expositiva — é trabalho de verdade. Você chega com um problema e sai com um código funcional.</p>
  <p>A ideia veio de uma observação simples: a maior parte das pessoas aprende a teoria mas trava quando precisa aplicar. O gap entre "entender um conceito" e "construir algo do zero" é imenso, e essa sessão existe exatamente para cruzar esse gap. Em 2 horas de trabalho conjunto, você vai ver como um programador experiente pensa, toma decisões, pesquisa e resolve obstáculos em tempo real.</p>
  <div class="highlight-grid">
    <div class="highlight-card"><span>⏱️</span><strong>2 horas ao vivo</strong><br>Discord ou Google Meet, com compartilhamento de tela dos dois lados.</div>
    <div class="highlight-card"><span>💻</span><strong>Código real</strong><br>Você sai com um script funcional, comentado e adaptável para outros casos.</div>
    <div class="highlight-card"><span>🧠</span><strong>Raciocínio exposto</strong><br>Cada decisão é explicada: por que essa estrutura, por que essa biblioteca, por que essa abordagem.</div>
    <div class="highlight-card"><span>📩</span><strong>Suporte pós-sessão</strong><br>Código no Discord + até 3 dúvidas por mensagem na semana seguinte.</div>
  </div>

  <h2>🔍 Como escolher seu projeto?</h2>
  <p>O melhor projeto para essa sessão é aquele que resolve um problema que você enfrenta hoje — não um exercício fictício, mas algo que vai economizar horas de trabalho repetitivo ou gerar valor imediato. Pense nas tarefas manuais que você faz toda semana: copiar dados de um sistema para outro, gerar relatórios, preencher planilhas, enviar e-mails padronizados.</p>
  <p>Alguns critérios para avaliar se um projeto é bom para essa sessão: ele deve ser executável em 2 horas (escopo pequeno e bem definido), deve usar os conceitos do módulo (Python, Pandas, automação ou API), e deve ter um resultado claro e verificável ao final. Projetos vagos como "quero aprender mais sobre Python" não funcionam — precisa ser algo concreto.</p>

  <h2>💡 Exemplos de Projetos por Nível</h2>
  <div class="concept-cards">
    <div class="concept-card">
      <div class="concept-card-title">Nível 1 — Script de Dados</div>
      <ul>
        <li>Ler uma planilha Excel com registros de vendas, calcular totais por vendedor/mês e gerar um relatório CSV formatado</li>
        <li>Cruzar duas planilhas (cadastro de clientes + pedidos) e identificar clientes que não compraram nos últimos 90 dias</li>
        <li>Ler logs de um sistema em TXT, contar erros por tipo e gerar um sumário diário</li>
      </ul>
    </div>
    <div class="concept-card">
      <div class="concept-card-title">Nível 2 — Automação de Interface</div>
      <ul>
        <li>Script que abre o sistema interno, busca registros por data, copia dados e cola numa planilha</li>
        <li>Automação de preenchimento de formulário web com lista de dados do Excel</li>
        <li>Script que verifica um portal toda manhã e envia alerta no WhatsApp se houver novidade</li>
      </ul>
    </div>
    <div class="concept-card">
      <div class="concept-card-title">Nível 3 — Automação com IA</div>
      <ul>
        <li>Script que lê e-mails de suporte e usa a API do Claude para classificar e rascunhar respostas</li>
        <li>Pipeline que processa documentos PDF, extrai texto e gera resumos com GPT-4</li>
        <li>Chatbot simples para responder perguntas sobre um documento específico da empresa</li>
      </ul>
    </div>
  </div>

  <h2>📝 Como descrever seu projeto para a sessão</h2>
  <p>Quanto melhor você descrever o projeto antes da sessão, mais aproveitamos o tempo juntos. Uma boa descrição tem quatro elementos: o problema que resolve, os dados ou sistemas envolvidos, o resultado esperado e o que você já tentou fazer.</p>
  <p>Não precisa ser técnico nem formal. Escreva como você explicaria para um colega. "Preciso de um script que leia o relatório que o sistema X gera todo dia em CSV, filtre as linhas com status 'pendente' e mande uma lista formatada por WhatsApp" é uma descrição excelente.</p>

  <div class="tip-box">
    <span class="tip-icon">💡</span>
    <div><strong>Dica antes da sessão:</strong> Prepare um arquivo de exemplo com dados reais (ou dados fictícios com o mesmo formato). Isso economiza 20 minutos que gastaríamos criando dados de teste e permite ir direto ao problema.</div>
  </div>

  <h2>📅 Agendando sua Sessão</h2>
  <p>Use o formulário abaixo para escolher o horário e descrever seu projeto. Após o agendamento, você receberá uma confirmação no Discord com o link da reunião.</p>

  <div style="text-align:center;margin:2rem 0;">
    <a href="/projeto-pratico" class="btn-primary" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.75rem 1.75rem;font-size:0.95rem;">
      <i data-lucide="calendar-plus" style="width:18px;height:18px;display:inline;vertical-align:middle;"></i>
      Agendar Sessão de Projeto
    </a>
  </div>
</section>"""

# ─────────────────────────── IA LESSON 1 ───────────────────────────

def ia1_content():
    return """<section class="lesson-section">
  <div class="lesson-intro-box">
    <p><strong>Objetivo:</strong> Entender como os LLMs funcionam por dentro, qual modelo usar em cada situação, e dominar Prompt Engineering para extrair respostas profissionais. Você vai parar de usar IA como curiosidade e começar a usá-la como ferramenta de trabalho real.</p>
  </div>

  <h2>🧠 Como os LLMs Funcionam por Dentro</h2>
  <p>LLM significa <em>Large Language Model</em> — modelo de linguagem de grande escala. A palavra "grande" refere-se ao número de parâmetros (pesos internos): os modelos atuais têm centenas de bilhões. Esses parâmetros são ajustados durante o treinamento para capturar padrões estatísticos em trilhões de tokens de texto.</p>
  <p>O processo começa na <strong>tokenização</strong>: o texto que você envia é fragmentado em tokens, que são pedaços de palavras. "programação" vira algo como ["progra", "mação"]. Um token em português equivale a aproximadamente 3-4 caracteres. Isso importa porque você paga por token e cada modelo tem um limite máximo de tokens no contexto (janela de contexto). O GPT-4o aceita 128k tokens; o Claude 3.5 Sonnet aceita até 200k tokens — suficiente para analisar um livro inteiro em uma chamada.</p>
  <p>A parte central do modelo é o mecanismo de <strong>atenção</strong> (Transformer). Diferente de modelos antigos que processavam texto palavra por palavra, o Transformer "olha" para todos os tokens ao mesmo tempo e calcula quais relações são relevantes para o contexto atual. É isso que permite ao modelo entender que "ele" em "o cliente ligou e ele reclamou" refere-se ao cliente, não a outra pessoa.</p>
  <div class="code-block">
    <div class="code-header">Conceito — Pipeline interno de uma chamada</div>
    <pre><code"># Entrada: "Qual a capital do Brasil?"
#
# Passo 1: Tokenização
# ["Qual", " a", " capital", " do", " Brasil", "?"]
#
# Passo 2: Embeddings — cada token vira um vetor de ~4096 números
# Esses vetores capturam significado: "rei" e "rainha" ficam próximos
#
# Passo 3: Atenção multi-cabeça — o modelo pondera relações entre tokens
# "capital" ativa relações com "Brasil", "cidade", "governo"
#
# Passo 4: Geração token a token
# P("Bra") = 0.92, P("São") = 0.05, P("Rio") = 0.02 ...
# → "Bra" selecionado
# P("sília") | "Bra" = 0.99 ...
# → "sília"
#
# Resultado: "Brasília"
#
# Implicações práticas:
# ✅ Excelente em padrões de linguagem, código, raciocínio, resumo
# ✅ Janela de contexto grande = analisa documentos longos
# ❌ Não executa código internamente — "simula" o resultado
# ❌ Sem memória entre sessões (cada conversa começa do zero)
# ❌ Alucinações: quando a probabilidade leva a um token errado</code></pre>
  </div>
  <p>O conceito de <strong>temperatura</strong> controla o quanto o modelo "arrisca" nas suas escolhas de token. Com temperatura 0, ele sempre escolhe o token de maior probabilidade — respostas determinísticas e conservadoras. Com temperatura 1.0, ele amostra da distribuição de probabilidade — mais criativo e variado, mas também mais suscetível a erros. Para tarefas analíticas e de dados, use 0.1–0.3. Para criação de texto e brainstorming, use 0.7–0.9.</p>

  <h2>⚖️ Qual Modelo Usar? GPT-4o vs Claude vs Gemini</h2>
  <p>Em 2024-2025 os três grandes modelos atingiram qualidade comparável na maioria das tarefas. A diferença prática está em características específicas, preço e integração. Escolher o modelo certo para cada tarefa pode significar 5x menos custo ou 3x mais qualidade — não é decisão trivial.</p>
  <p>O <strong>GPT-4o</strong> da OpenAI se destaca em tarefas multimodais (imagem + texto), geração de código e uso com ferramentas externas. O <strong>Claude 3.5 Sonnet</strong> da Anthropic tem a maior janela de contexto (200k tokens), segue instruções complexas com mais fidelidade e é menos propenso a recusar tarefas legítimas. O <strong>Gemini</strong> do Google tem integração nativa com Google Workspace e busca em tempo real.</p>
  <div class="code-block">
    <div class="code-header">Guia prático — modelo por tipo de tarefa</div>
    <pre><code"># ── GPT-4o (OpenAI) ──
# Análise de imagens, planilhas com OCR, visão computacional
# Geração de código com execução inline (Code Interpreter)
# Uso com plugins e ferramentas do ecossistema OpenAI
# API: ~R$ 15/M tokens input, R$ 60/M tokens output

# ── Claude 3.5 Sonnet (Anthropic) ──
# Documentos longos: contratos, relatórios, livros inteiros
# Instruções longas e complexas com muitas restrições
# Raciocínio detalhado, análise crítica, revisão de código
# API: ~R$ 15/M tokens input, R$ 75/M tokens output

# ── Claude 3.5 Haiku (Anthropic) ──  ← para automação em escala
# Tarefas simples e repetitivas onde você faz 1000+ chamadas/dia
# Classificação, extração de entidades, formatação de texto
# API: ~R$ 0.50/M tokens input, R$ 1.25/M tokens output  ← 30x mais barato

# ── Gemini 1.5 Pro (Google) ──
# Integração direta com Google Sheets, Docs, Gmail
# Análise de áudio e vídeo
# Busca em tempo real via Google grounding

# ── Regra prática ──
# Prototipagem e desenvolvimento   → Claude Sonnet ou GPT-4o
# Automação em produção (volume)  → Claude Haiku ou GPT-4o-mini
# Análise de documento > 50 páginas → Claude (janela maior)
# Google Workspace                → Gemini</code></pre>
  </div>

  <h2>✍️ Prompt Engineering — A Arte de Pedir</h2>
  <p>Prompt engineering é a disciplina de construir inputs que maximizam a qualidade do output do modelo. Não é um conjunto de truques aleatórios — é uma prática sistemática baseada em como os modelos processam o contexto. A diferença entre um prompt ruim e um prompt profissional pode ser a diferença entre uma resposta inútil e uma que resolve o problema completamente.</p>
  <p>A estrutura mais robusta tem quatro componentes: <strong>contexto</strong> (quem é o modelo, qual o cenário), <strong>tarefa</strong> (exatamente o que fazer), <strong>formato</strong> (como deve ser a saída) e <strong>restrições</strong> (o que não fazer). Quanto mais específico cada componente, menor a ambiguidade e melhor a resposta.</p>
  <div class="code-block">
    <div class="code-header">Prompt amador vs prompt profissional</div>
    <pre><code"># ❌ Amador — vago, sem contexto, sem formato definido:
"me ajuda com relatório de vendas"

# ✅ Profissional — contexto + tarefa + formato + restrições:
'''
[CONTEXTO]
Você é um analista de dados sênior com experiência em varejo.
Tenho dados de vendas mensais de 2024 com colunas: data, produto,
categoria, vendedor, valor, quantidade, região.

[TAREFA]
Analise os dados abaixo e identifique os 3 principais insights
sobre performance de vendas que um gerente comercial precisaria saber.

[FORMATO]
- 3 insights numerados
- Cada insight: título em negrito + 2-3 linhas de explicação
- Inclua qual métrica suporta cada insight
- Termine com 1 recomendação de ação imediata

[RESTRIÇÕES]
- Não repita dados óbvios que já constam na tabela
- Não sugira investimentos sem dados que os justifiquem
- Máximo 300 palavras no total

Dados: [cole os dados aqui]
'''</code></pre>
  </div>
  <p>A especificidade do <strong>formato</strong> é frequentemente o elemento mais negligenciado. Dizer "responda em tópicos" é diferente de dizer "responda em exatamente 5 tópicos, cada um com um título de no máximo 5 palavras seguido de uma explicação de 2-3 linhas". Quanto mais você define o formato, menos o modelo improvisa.</p>

  <h2>🧩 Técnicas Avançadas de Prompting</h2>
  <p><strong>Chain of Thought (CoT)</strong> é a técnica de pedir explicitamente que o modelo raciocine passo a passo antes de dar a resposta final. Funciona porque força o modelo a construir contexto intermediário antes de concluir — o mesmo motivo pelo qual humanos cometem menos erros quando escrevem o raciocínio antes de responder. O simples acréscimo de "pense passo a passo" aumenta significativamente a acurácia em problemas de lógica e matemática.</p>
  <div class="code-block">
    <div class="code-header">Chain of Thought — com e sem</div>
    <pre><code"># ❌ Sem CoT — resposta direta, propensa a erro em raciocínios complexos:
"Qual estratégia de preço devo usar para lançar meu SaaS B2B?"

# ✅ Com CoT — força análise estruturada:
'''
Preciso definir estratégia de preço para meu SaaS B2B.
Pense passo a passo antes de recomendar:

1. Analise o contexto: produto técnico de automação, B2B, PMEs,
   mercado brasileiro, concorrentes cobram R$ 200-800/mês
2. Avalie modelos possíveis: freemium, trial gratuito, por uso,
   assinatura fixa, por seat
3. Considere: custo de aquisição, churn esperado, ticket médio alvo
4. Recomende 1 modelo com justificativa e sugira faixa de preço

Contexto adicional: meu custo de infraestrutura é ~R$ 50/cliente/mes.
'''

# Por que funciona: o modelo "pensa em voz alta" antes de concluir
# Os passos intermediários se tornam contexto para a conclusão final</code></pre>
  </div>
  <p><strong>Few-Shot prompting</strong> funciona fornecendo exemplos do padrão desejado antes da tarefa real. O modelo aprende o formato, o nível de detalhe e o estilo a partir dos exemplos — sem precisar explicar tudo em palavras. É especialmente poderoso para classificação de texto, extração de dados estruturados e transformações de formato.</p>
  <div class="code-block">
    <div class="code-header">Few-Shot — exemplos ensinam melhor que instruções</div>
    <pre><code"># Tarefa: extrair dados de e-mails de pedido em formato estruturado

'''
Extraia os dados do pedido no formato JSON mostrado nos exemplos.

Exemplo 1:
E-mail: 'Ola, quero comprar 3 caixas do produto X-200 para entrega em SP.'
JSON: {produto: X-200, quantidade: 3, entrega: SP}

Exemplo 2:
E-mail: 'Preciso de 1 unidade do notebook Dell para RJ urgente.'
JSON: {produto: notebook Dell, quantidade: 1, entrega: RJ}

Agora extraia:
E-mail: 'Boa tarde, gostaria de solicitar 10 cadeiras ergonomicas
para nosso escritorio em Campinas, SP.'
'''

# O modelo entende: JSON, campos específicos, sem campos extras
# Sem os exemplos, poderia inventar campos ou usar formato diferente</code></pre>
  </div>
  <p><strong>Self-consistency</strong> é uma técnica mais avançada: você faz a mesma pergunta múltiplas vezes com temperatura alta e depois agrega as respostas (votação majoritária ou síntese). Funciona bem para problemas onde há incerteza e a resposta mais frequente tende a ser a mais correta. Custa mais em tokens mas aumenta muito a confiabilidade.</p>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Para uma tarefa de classificar 5.000 e-mails por dia com IA, qual modelo faz mais sentido economicamente?</div>
    <div class="check-options">
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">GPT-4o — o mais capaz</button>
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">Claude Haiku — muito mais barato para volume alto</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Gemini — integração com Google</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <h2>🖥️ IA no Fluxo de Trabalho do Programador</h2>
  <p>GitHub Copilot e Cursor são as duas ferramentas de IA mais produtivas para programadores. O Copilot funciona como um completador de código muito inteligente — ele lê o contexto do arquivo e sugere a próxima linha ou bloco inteiro. O Cursor vai além: é um editor completo onde você pode conversar sobre o código, pedir refatorações, debugar e até escrever código do zero descrevendo o que quer em português.</p>
  <p>A técnica mais produtiva em ambas é <strong>comment-driven development</strong>: ao invés de escrever código e depois pedir para a IA explicar, você escreve comentários descrevendo o que quer e deixa a IA implementar. Os comentários servem simultaneamente como documentação e como prompt.</p>
  <div class="code-block">
    <div class="code-header">Copilot e Cursor — uso profissional</div>
    <pre><code"># ── GitHub Copilot (VS Code) ──
# Tab           → aceita sugestão completa
# Alt+]         → próxima sugestão alternativa
# Ctrl+Enter    → abre painel com 10 opções

# Comment-driven development:
# Lê planilha Excel, agrupa por categoria,
# calcula soma e percentual de cada grupo,
# ordena do maior para o menor e salva em CSV
def gerar_relatorio_categorias(arquivo_entrada, arquivo_saida):
    pass  # ← Copilot implementa a partir do comentário acima

# ── Cursor ──
# Ctrl+K  → editar código selecionado em linguagem natural
# Ctrl+L  → chat com contexto completo do projeto
# @file   → referenciar arquivo específico no chat

# Prompts eficazes no Cursor:
# "Adicione tratamento de erro para FileNotFoundError e PermissionError"
# "Refatore para usar list comprehension onde possível"
# "Escreva docstring no formato Google Style para essa função"
# "Essa função tem um bug quando df está vazio — corrija"

# Limitações críticas (nunca ignore):
# ❌ Código gerado pode ter bugs sutis — sempre teste
# ❌ Pode usar APIs depreciadas ou desatualizadas
# ❌ Não conhece seu domínio de negócio — contexto é responsabilidade sua
# ✅ Excelente para boilerplate, conversão de formato, explicações</code></pre>
  </div>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">A técnica de prompt que pede ao modelo para "pensar passo a passo" antes de responder chama-se Chain of ___.</div>
    <input type="text" class="check-input" data-answer="Thought" placeholder="Chain of ___">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <div class="tip-box">
    <span class="tip-icon">💡</span>
    <div><strong>Regra de ouro:</strong> Se você recebeu uma resposta ruim, o problema quase sempre está no prompt, não no modelo. Antes de trocar de modelo, reescreva o prompt com mais contexto, formato mais específico e exemplos. 90% dos problemas de qualidade resolvem com um prompt melhor.</div>
  </div>
</section>"""

def ia1_exercises():
    return [
        ("Prompt de 4 Partes",
         "Preencha as 4 variaveis com conteudo real e relevante (nao deixe nenhuma vazia). Imprima cada uma.",
         'contexto = "Voce e um assistente de RH especializado em triagem de curriculos."\ntarefa = "Analise o curriculo e liste 3 pontos fortes e 2 areas de melhoria."\nformato = "Responda em topicos. Use ✅ para pontos fortes e ⚠️ para melhorias."\nrestricoes = "Seja objetivo. Maximo 2 linhas por ponto. Nao julgue dados pessoais."\n\nprint(contexto)\nprint(tarefa)\nprint(formato)\nprint(restricoes)\n',
         None,
         "Preencha cada variavel com texto nao-vazio e relevante para a tarefa", 20),

        ("Chain of Thought",
         "Monte um prompt Chain-of-Thought para a tarefa abaixo. O prompt deve pedir que o modelo pense em pelo menos 3 passos antes de concluir. Imprima o prompt final.",
         'tarefa = "Decidir se devo usar banco SQL ou NoSQL para meu projeto"\n\n# Monte um prompt CoT com:\n# 1. Instrucao para pensar passo a passo (pelo menos 3 passos)\n# 2. Contexto sobre o projeto (invente um contexto realista)\n# 3. Pedido de recomendacao final\nprompt = ""\n\n# complete o prompt\nprint(prompt)\n',
         None,
         "O prompt deve conter: instrucao de raciocinar passo a passo, contexto do projeto e pedido de conclusao", 20),

        ("Few-Shot Classificador",
         "Crie uma lista com 3 exemplos de few-shot para classificar e-mails como Urgente, Normal ou Spam. Imprima cada exemplo no formato 'texto → classificacao'.",
         'exemplos = [\n    # (texto, classificacao)\n    ("", ""),   # adicione exemplos reais\n    ("", ""),\n    ("", ""),\n]\n\nfor texto, cls in exemplos:\n    if texto and cls:  # so imprime se preenchido\n        print(f"{texto} → {cls}")\n',
         None,
         "Exemplos devem ter textos de e-mail reais e classificacoes Urgente/Normal/Spam", 15),

        ("Analise de Prompt Ruim",
         "Melhore o prompt ruim abaixo. Imprima as 4 variaveis preenchidas: problema, contexto, tarefa_melhorada e formato_saida.",
         'prompt_ruim = "me ajuda com minha apresentacao"\n\n# Identifique o que falta e preencha as melhorias\nproblema = "O prompt nao tem contexto, tarefa clara, formato nem restricoes"\ncontexto = ""\ntarefa_melhorada = ""\nformato_saida = ""\n\nprint(problema)\nprint(contexto)\nprint(tarefa_melhorada)\nprint(formato_saida)\n',
         None,
         "Preencha contexto, tarefa_melhorada e formato_saida com conteudo real (nao vazio)", 15),
    ]

def ia2_content():
    return """<section class="lesson-section">
  <div class="lesson-intro-box">
    <p><strong>Objetivo:</strong> Integrar modelos de IA diretamente no seu código Python. Você vai construir automações que entendem linguagem natural, analisam dados, tomam decisões e executam ações — criando assistentes personalizados que vão além do que qualquer interface web oferece.</p>
  </div>

  <h2>🔌 APIs de IA: Acessando o Modelo Diretamente</h2>
  <p>Quando você usa o ChatGPT ou o Claude no navegador, existe uma chamada de API acontecendo por baixo. A interface é apenas um cliente que monta a requisição, envia para o servidor, recebe o JSON de resposta e exibe para você. Com Python, você faz exatamente isso — sem a interface no meio, com controle total sobre cada parâmetro.</p>
  <p>Esse controle tem implicações práticas enormes. Você pode integrar a IA em qualquer fluxo de trabalho existente, processar centenas de itens em lote, combinar a resposta do modelo com dados do seu banco de dados, e criar pipelines que tomam decisões automaticamente. O ChatGPT só processa um prompt por vez, você olhando para a tela. A API processa 1000 prompts enquanto você dorme.</p>
  <div class="code-block">
    <div class="code-header">Conceito — Estrutura de uma requisição e resposta</div>
    <pre><code"># REQUISIÇÃO que você envia (JSON):
{
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 1024,
    "temperature": 0.3,
    "system": "Voce e um analista de dados senior.",
    "messages": [
        {"role": "user", "content": "Analise essas vendas: ..."}
    ]
}

# RESPOSTA que você recebe (JSON):
{
    "id": "msg_01XYZ...",
    "content": [{"type": "text", "text": "Com base nos dados..."}],
    "model": "claude-3-5-sonnet-20241022",
    "stop_reason": "end_turn",
    "usage": {
        "input_tokens": 312,
        "output_tokens": 189
    }
}

# Tokens: 1 token em portugues ~ 3-4 caracteres
# "Qual o total de vendas?" = ~10 tokens
# Voce paga por input_tokens + output_tokens</code></pre>
  </div>
  <p>O campo <code>stop_reason</code> indica por que o modelo parou de gerar. <code>end_turn</code> significa que terminou naturalmente. <code>max_tokens</code> significa que atingiu o limite que você definiu — nesse caso pode ser necessário aumentar o <code>max_tokens</code> ou dividir a tarefa em partes menores.</p>

  <h2>🔑 Configurando o Ambiente com Segurança</h2>
  <p>A API key é uma credencial de segurança — quem a tiver pode fazer chamadas na sua conta e gastar seu crédito. Nunca coloque a chave diretamente no código (hardcoded), especialmente se você vai subir o código para o GitHub. O padrão correto é usar <strong>variáveis de ambiente</strong>: a chave fica num arquivo <code>.env</code> local que não é versionado, e o código lê esse arquivo em tempo de execução.</p>
  <div class="code-block">
    <div class="code-header">Python — Configuração segura com .env (pip install anthropic openai python-dotenv)</div>
    <pre><code">import os
from dotenv import load_dotenv
import anthropic
from openai import OpenAI

load_dotenv()

client_claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
client_oai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resp_claude = client_claude.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": "O que e Pandas em Python?"}]
)
print(resp_claude.content[0].text)

resp_oai = client_oai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "O que e Pandas em Python?"}]
)
print(resp_oai.choices[0].message.content)</code></pre>
  </div>
  <p>O arquivo <code>.env</code> fica na raiz do projeto com o conteúdo <code>ANTHROPIC_API_KEY=sk-ant-...</code>. Adicione <code>.env</code> ao seu <code>.gitignore</code> imediatamente. Nunca commite esse arquivo. Para deploy em servidor, use variáveis de ambiente do próprio sistema operacional ou da plataforma de deploy.</p>

  <h2>⚙️ Parâmetros Críticos e o System Prompt</h2>
  <p>Três parâmetros controlam o comportamento do modelo de forma decisiva. O <strong>system prompt</strong> é o mais impactante: ele define a "personalidade" e as regras do assistente para toda a conversa. Diferente das mensagens normais, o system é processado antes de qualquer coisa e permanece ativo em todos os turnos. Um system prompt bem construído reduz drasticamente o número de respostas ruins.</p>
  <p>O <strong>temperature</strong> controla a aleatoriedade: 0 para respostas sempre iguais (extração de dados, código, classificação), valores mais altos para criatividade (brainstorming, marketing). O <strong>max_tokens</strong> limita o tamanho da resposta — se a resposta for cortada, aumente esse valor.</p>
  <div class="code-block">
    <div class="code-header">Python — System prompt e parâmetros de controle</div>
    <pre><code">import anthropic, os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

resposta = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=2048,
    temperature=0.1,
    system=(
        "Voce e um analista de dados senior especializado em varejo brasileiro.\n"
        "Responda sempre em portugues, de forma tecnica e objetiva.\n"
        "Quando apresentar numeros, use formatacao brasileira (R$ 1.234,56).\n"
        "Se nao tiver dados suficientes para responder, diga explicitamente."
    ),
    messages=[
        {"role": "user",      "content": "Qual a melhor metrica para medir churn?"},
        {"role": "assistant", "content": "A metrica mais usada e a taxa de cancelamento..."},
        {"role": "user",      "content": "Como calculo isso no Pandas?"},
    ]
)

print(resposta.content[0].text)
print(f"Tokens: {resposta.usage.input_tokens} in + {resposta.usage.output_tokens} out")</code></pre>
  </div>
  <p>O array <code>messages</code> é o <strong>histórico da conversa</strong>. Cada entrada tem um <code>role</code> (<code>user</code> ou <code>assistant</code>) e um <code>content</code>. Para criar um chatbot com memória, você simplesmente acumula as mensagens a cada turno — o modelo vê todo o histórico e responde em contexto. Sem você incluir o histórico manualmente, cada chamada é independente e o modelo "esquece" tudo.</p>

  <div class="interactive-check" data-type="choice">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Para um assistente de análise de dados onde a resposta precisa ser sempre precisa e consistente, qual valor de temperature usar?</div>
    <div class="check-options">
      <button class="check-option" data-correct="true" onclick="checkChoice(this)">0.0 ou 0.1 — determinístico, minimiza variação</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">0.9 — mais criativo e variado</button>
      <button class="check-option" data-correct="false" onclick="checkChoice(this)">Temperature não afeta a precisão do modelo</button>
    </div>
    <div class="check-feedback"></div>
  </div>

  <h2>🤖 Construindo um Assistente de Análise de Dados</h2>
  <p>A combinação Pandas + API de IA é uma das mais poderosas para automação. O Pandas carrega e processa os dados; a IA interpreta os resultados em linguagem natural. Você pode criar um assistente que responde perguntas sobre qualquer planilha sem escrever nenhum código de análise específico — a IA faz a interpretação.</p>
  <p>Uma técnica essencial para controlar custos é <strong>não enviar o DataFrame inteiro</strong> para a API. Ao invés disso, envie um resumo estruturado: colunas, tipos, primeiras linhas, estatísticas descritivas. Esse resumo geralmente tem menos de 1000 tokens e contém toda a informação que a IA precisa para responder perguntas de negócio.</p>
  <div class="code-block">
    <div class="code-header">Python — Assistente que responde perguntas sobre Excel</div>
    <pre><code">import pandas as pd
import anthropic, os
from dotenv import load_dotenv

load_dotenv()

def montar_resumo(df, arquivo):
    return (
        f"Arquivo: {arquivo} | Linhas: {len(df)} | Colunas: {list(df.columns)}\n"
        f"Tipos: {df.dtypes.to_dict()}\n"
        f"Nulos por coluna: {df.isnull().sum().to_dict()}\n\n"
        f"Amostra (3 linhas):\n{df.head(3).to_string()}\n\n"
        f"Estatisticas numericas:\n{df.describe().to_string()}"
    )

def perguntar_sobre_dados(arquivo, pergunta, historico=None):
    df = pd.read_excel(arquivo) if arquivo.endswith('.xlsx') else pd.read_csv(arquivo)
    resumo = montar_resumo(df, arquivo)

    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    msgs = historico or []
    msgs.append({"role": "user", "content": f"Dados:\n{resumo}\n\nPergunta: {pergunta}"})

    resp = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        temperature=0.1,
        system="Voce e um analista de dados. Responda perguntas sobre os dados fornecidos. Seja objetivo e cite os numeros exatos.",
        messages=msgs
    )
    return resp.content[0].text, msgs</code></pre>
  </div>

  <h2>🔄 Processamento em Lote com Retry</h2>
  <p>Uma das aplicações mais valiosas das APIs de IA é o processamento em lote: classificar centenas de e-mails, extrair entidades de milhares de documentos, traduzir um banco de dados inteiro. Para isso, você precisa de um loop com tratamento de erros robusto — as APIs de IA às vezes retornam erros de rate limit (429) quando você faz muitas chamadas muito rápido.</p>
  <p>O padrão <strong>exponential backoff</strong> é o padrão correto para isso: quando recebe um erro, espera 1 segundo, tenta de novo, se falhar espera 2 segundos, depois 4, etc. A maioria das APIs recomenda esse padrão explicitamente na documentação.</p>
  <div class="code-block">
    <div class="code-header">Python — Processamento em lote com retry automático</div>
    <pre><code">import anthropic, os, time, logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(message)s")

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def classificar_com_retry(texto, tentativas=3):
    for i in range(tentativas):
        try:
            resp = client.messages.create(
                model="claude-3-5-haiku-20241022",
                max_tokens=50,
                temperature=0,
                system="Classifique o sentimento como: Positivo, Negativo ou Neutro. Responda APENAS uma palavra.",
                messages=[{"role": "user", "content": texto}]
            )
            return resp.content[0].text.strip()
        except anthropic.RateLimitError:
            espera = 2 ** i
            logging.warning(f"Rate limit. Aguardando {espera}s...")
            time.sleep(espera)
        except Exception as e:
            logging.error(f"Erro: {e}")
            return "Erro"
    return "Erro"

feedbacks = [
    "Produto excelente, chegou antes do prazo!",
    "Pessimo, veio com defeito e o suporte nao respondeu.",
    "Ok, atendeu as expectativas basicas.",
]

resultados = []
for i, texto in enumerate(feedbacks):
    classificacao = classificar_com_retry(texto)
    resultados.append({"texto": texto[:40], "classificacao": classificacao})
    logging.info(f"[{i+1}/{len(feedbacks)}] {classificacao}")
    time.sleep(0.3)

for r in resultados:
    print(f"{r['classificacao']:10} | {r['texto']}")</code></pre>
  </div>
  <p>O uso do Claude Haiku para essa tarefa (classificação simples) é intencional — ele custa 30x menos que o Sonnet e para classificação de sentimento a diferença de qualidade é mínima. Escolha o modelo pelo requisito da tarefa, não pelo hábito.</p>

  <h2>🛠️ Tool Use: A IA Executando Ações Reais</h2>
  <p>Tool Use (também chamado de Function Calling no OpenAI) é o mecanismo que transforma a IA de um gerador de texto em um agente que executa ações. Você define um conjunto de "ferramentas" (funções Python), descreve o que cada uma faz, e o modelo decide quando e como chamá-las para responder à pergunta do usuário.</p>
  <p>O fluxo é: você envia a pergunta + lista de ferramentas disponíveis. Se o modelo precisar de uma ferramenta, ele responde com <code>stop_reason="tool_use"</code> e os parâmetros. Você executa a ferramenta localmente, pega o resultado, e envia de volta. O modelo então usa o resultado para formular a resposta final. Isso cria um loop onde a IA pode buscar dados, calcular, consultar APIs externas — tudo em linguagem natural.</p>
  <div class="code-block">
    <div class="code-header">Python — Tool Use: IA que consulta dados reais</div>
    <pre><code">import anthropic, os, json
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

ferramentas = [
    {
        "name": "buscar_vendas_por_mes",
        "description": "Retorna o total de vendas de um mes especifico",
        "input_schema": {
            "type": "object",
            "properties": {
                "mes": {"type": "string", "description": "Mes no formato YYYY-MM, ex: 2024-03"}
            },
            "required": ["mes"]
        }
    }
]

def buscar_vendas_por_mes(mes):
    dados = {"2024-01": 45200, "2024-02": 38900, "2024-03": 52100}
    return dados.get(mes, 0)

def executar_ferramenta(nome, params):
    if nome == "buscar_vendas_por_mes":
        return buscar_vendas_por_mes(params["mes"])

pergunta = "Qual foi o mes com mais vendas no primeiro trimestre de 2024?"
msgs = [{"role": "user", "content": pergunta}]

resp = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=512,
    tools=ferramentas,
    messages=msgs
)

if resp.stop_reason == "tool_use":
    for bloco in resp.content:
        if bloco.type == "tool_use":
            resultado = executar_ferramenta(bloco.name, bloco.input)
            print(f"Ferramenta chamada: {bloco.name}({bloco.input})")
            print(f"Resultado: R$ {resultado:,}")</code></pre>
  </div>

  <h2>💰 Controlando Custos em Produção</h2>
  <p>O custo de uma API de IA em produção é proporcional ao número de tokens processados. Em automações simples com o Haiku, o custo é tão baixo que raramente vale preocupar. Mas em sistemas com muito contexto, documentos grandes ou modelos premium, o custo pode escalar rapidamente se você não monitorar.</p>
  <p>As três alavancas principais para controle de custo são: escolher o <strong>modelo certo</strong> para cada tarefa (Haiku para tarefas simples, Sonnet para complexas), <strong>reduzir o contexto</strong> enviado (resumos ao invés de dados brutos), e <strong>cachear respostas</strong> quando a mesma pergunta é feita repetidamente.</p>
  <div class="code-block">
    <div class="code-header">Python — Estimador de custo e monitor de uso</div>
    <pre><code">def estimar_custo(tokens_in, tokens_out, modelo="haiku"):
    precos = {
        "haiku":   (0.50,  1.25),
        "sonnet":  (15.0,  75.0),
        "gpt4mini": (0.75,  3.0),
        "gpt4o":   (12.50, 37.50),
    }
    p_in, p_out = precos[modelo]
    custo = (tokens_in / 1_000_000 * p_in) + (tokens_out / 1_000_000 * p_out)
    return custo

custo_por_chamada = estimar_custo(500, 200, "haiku")
print(f"Custo por chamada: R$ {custo_por_chamada:.6f}")

custo_1000_chamadas = custo_por_chamada * 1000
print(f"1.000 chamadas/dia: R$ {custo_1000_chamadas:.4f}")
print(f"30 dias:            R$ {custo_1000_chamadas * 30:.2f}")

custo_sonnet = estimar_custo(500, 200, "sonnet") * 1000 * 30
print(f"Mesmo volume no Sonnet: R$ {custo_sonnet:.2f}")</code></pre>
  </div>
  <p>Com 1000 chamadas diárias usando o Haiku com ~700 tokens cada, o custo mensal fica em torno de R$ 1-2. Com o Sonnet, o mesmo volume custa R$ 60-80. Para automações de classificação e extração em escala, o Haiku é quase sempre a escolha certa.</p>

  <div class="interactive-check" data-type="fill">
    <div class="check-header"><i data-lucide="edit-3" style="width:16px;height:16px;display:inline;vertical-align:middle;"></i> Verifique seu conhecimento</div>
    <div class="check-question">Qual campo da resposta da API indica quantos tokens foram consumidos na entrada (prompt)?</div>
    <input type="text" class="check-input" data-answer="input_tokens" placeholder="resposta.usage.___">
    <button class="check-btn" onclick="checkAnswer(this)">Verificar</button>
    <div class="check-feedback"></div>
  </div>

  <div class="tip-box">
    <span class="tip-icon">🚀</span>
    <div><strong>Próximo nível:</strong> Combine tudo o que aprendeu — Python + Pandas + API de IA. Carregue dados com Pandas, monte um resumo inteligente, envie para o Claude com Tool Use para buscar dados complementares, e salve o relatório gerado automaticamente. Esse pipeline resolve em minutos o que levaria horas manualmente.</div>
  </div>
</section>"""

def ia2_exercises():
    return [
        ("Estrutura de Request",
         "Monte um dicionario request_body com as 4 chaves obrigatorias. Todos os valores devem ser preenchidos. Imprima cada chave e valor.",
         'request_body = {\n    "model": "",        # nome de um modelo real\n    "max_tokens": 0,    # numero entre 256 e 4096\n    "temperature": 0.0, # numero entre 0.0 e 1.0\n    "system": ""        # system prompt nao-vazio\n}\n\nfor chave, valor in request_body.items():\n    print(f"{chave}: {valor}")\n',
         None,
         "model='claude-3-5-sonnet-20241022', max_tokens=1024, temperature=0.7, system='Voce e um assistente...'", 20),

        ("Historico de Conversa",
         "Monte uma lista 'messages' com um historico de conversa com pelo menos 3 turnos (user, assistant, user). Imprima o role e os primeiros 30 chars de cada mensagem.",
         'messages = [\n    # {"role": "user", "content": "..."},\n    # {"role": "assistant", "content": "..."},\n    # {"role": "user", "content": "..."},\n]\n\nfor msg in messages:\n    preview = msg["content"][:30]\n    print(f"{msg[\'role\']}: {preview}")\n',
         None,
         "Alterne entre role='user' e role='assistant', com conteudo real em cada mensagem", 15),

        ("Estimador de Tokens e Custo",
         "Crie a funcao estimar(texto, preco_por_milhao) que conta tokens (palavras * 1.3) e calcula custo. Imprima tokens e custo para o texto fornecido.",
         'def estimar(texto, preco_por_milhao=0.50):\n    tokens = round(len(texto.split()) * 1.3)\n    custo = (tokens / 1_000_000) * preco_por_milhao\n    print(f"Tokens: {tokens}")\n    print(f"Custo: R$ {custo:.6f}")\n\ntexto = "Python e uma linguagem de programacao muito utilizada para automacao de dados e inteligencia artificial"\nestimar(texto)\n',
         None,
         "tokens = round(len(texto.split()) * 1.3)  custo = tokens/1_000_000 * preco", 15),

        ("System Prompt Profissional",
         "Escreva um system_prompt para um assistente especializado em Python. Deve ter: papel, tom, instrucoes de formato e pelo menos uma restricao. Imprima o prompt.",
         'system_prompt = ""\n\n# Seu system prompt deve incluir:\n# 1. Papel (quem e a IA)\n# 2. Tom (formal, didatico, tecnico...)\n# 3. Instrucoes de formato (use exemplos de codigo, seja conciso...)\n# 4. Pelo menos uma restricao (nao faca X)\n\nprint(system_prompt)\n',
         None,
         "Um bom system prompt tem: papel claro, nivel de tecnicidade, formato de resposta e restricoes", 20),
    ]

# ─────────────────────────── MAIN RESEED ───────────────────────────

def reseed():
    with app.app_context():
        print("Limpando conteudo existente...")
        ExerciseSubmission.query.delete()
        LessonProgress.query.delete()
        Exercise.query.delete()
        Lesson.query.delete()
        db.session.commit()

        py_mod = Module.query.filter_by(color='green').first()
        ia_mod = Module.query.filter_by(color='purple').first()

        if not py_mod or not ia_mod:
            print("ERRO: Modulos nao encontrados. Execute primeiro: python app.py")
            return

        # Garante que o ícone do módulo Python está correto
        py_mod.icon = '🐍'
        db.session.flush()

        # ── Python lessons ──
        lessons_py = [
            ("Semana 1 — Fundamentos do Python",
             "Variaveis, tipos, operadores, condicionais e f-strings", s1_content(), 1, 1, s1_exercises()),
            ("Semana 2 — Estruturas de Dados e Funcoes",
             "Listas, tuplas, dicionarios, loops e funcoes", s2_content(), 2, 2, s2_exercises()),
            ("Semana 3 — Automacao com Python",
             "RPA, PyAutoGUI, pywin32, try/except e arquivos", s3_content(), 3, 3, s3_exercises()),
            ("Semana 4 — Pandas e Analise de Dados",
             "DataFrames, filtros, limpeza, GroupBy e agendamento", s4_content(), 4, 4, s4_exercises()),
            ("Projeto Pratico — Construindo seu Projeto",
             "Sessao individual de 2h para construir um projeto real do zero", s5_content(), 5, 5, []),
        ]

        for title, subtitle, content, week, order, exercises in lessons_py:
            l = add_lesson(py_mod.id, title, subtitle, content, week, order, 60)
            for i, (t, d, s, e, h, p) in enumerate(exercises):
                add_ex(l.id, i+1, t, d, s, e, h, p)
            print(f"  Criada: {title} ({len(exercises)} exercicios)")

        # ── IA lessons ──
        lessons_ia = [
            ("Aula 1 — Usando IA como Ferramenta de Trabalho",
             "LLMs, Prompt Engineering e ferramentas praticas", ia1_content(), 1, 1, ia1_exercises()),
            ("Aula 2 — Consumindo APIs de IA com Python",
             "API OpenAI/Anthropic, parametros, agentes e custos", ia2_content(), 2, 2, ia2_exercises()),
        ]

        for title, subtitle, content, week, order, exercises in lessons_ia:
            l = add_lesson(ia_mod.id, title, subtitle, content, week, order, 60)
            for i, (t, d, s, e, h, p) in enumerate(exercises):
                add_ex(l.id, i+1, t, d, s, e, h, p)
            print(f"  Criada: {title} ({len(exercises)} exercicios)")

        db.session.commit()
        print(f"\nPronto! {Lesson.query.count()} aulas, {Exercise.query.count()} exercicios.")

if __name__ == '__main__':
    reseed()
