# Deploy no PythonAnywhere (Free Tier)

## Pré-requisitos
- Conta no [PythonAnywhere](https://www.pythonanywhere.com) (plano Beginner é grátis)
- Todos os arquivos do projeto

---

## Passo a Passo

### 1. Criar conta
- Acesse [pythonanywhere.com](https://www.pythonanywhere.com) → **Sign up** → **Beginner** (grátis)
- Escolha um username (ex: `matheusdev`) — sua URL será `matheusdev.pythonanywhere.com`

### 2. Upload dos arquivos

**Opção A — Via Git (recomendado):**
Na aba **Consoles** → **Bash**:
```bash
git clone https://github.com/SEU_REPO/plataforma_de_cursos.git
```

**Opção B — Upload manual:**
- Clique em **Files** (aba superior)
- Crie a pasta `plataforma_de_cursos`
- Faça upload de todos os arquivos mantendo a estrutura:
  ```
  plataforma_de_cursos/
  ├── app.py
  ├── seed_data.py
  ├── reseed.py
  ├── wsgi.py
  ├── requirements.txt
  ├── templates/
  │   ├── base.html
  │   ├── login.html
  │   ├── admin/
  │   └── student/
  └── static/
      ├── css/style.css
      └── js/main.js
  ```

### 3. Instalar dependências
Na aba **Consoles** → **Bash**:
```bash
cd ~/plataforma_de_cursos
pip3 install --user -r requirements.txt
```

### 4. Configurar variável de ambiente (opcional mas recomendado)
Na aba **Web**, na seção **Environment variables**, adicione:
```
SECRET_KEY = sua-chave-secreta-aqui-mude-isso
```
> Se não configurar, o app usará a chave padrão definida em `app.py`.

### 5. Inicializar o banco de dados
No console Bash:
```bash
cd ~/plataforma_de_cursos
python3 -c "
from app import app, init_db
with app.app_context():
    init_db()
    print('Banco de dados criado com sucesso!')
"
```

### 6. Configurar a Web App
- Aba **Web** → **Add a new web app**
- Escolha: **Manual configuration** → **Python 3.10**
- Em **WSGI configuration file**, clique no link e substitua **TODO** o conteúdo por:

```python
import sys
import os

path = '/home/SEU_USUARIO/plataforma_de_cursos'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

from app import app as application
```

> **IMPORTANTE:** Troque `SEU_USUARIO` pelo seu username do PythonAnywhere em todos os campos.

- Em **Static files**, adicione:
  - **URL:** `/static/`
  - **Directory:** `/home/SEU_USUARIO/plataforma_de_cursos/static`

### 7. Acessar
- Clique em **Reload** na aba Web
- Acesse: `https://SEU_USUARIO.pythonanywhere.com`

---

## Credenciais de Admin
| Usuário | Senha | Perfil |
|---------|-------|--------|
| mathmugiwara | Mugiwara1! | Administrador |

## Gerenciar Alunos
1. Faça login como admin (`mathmugiwara`)
2. Vá em **Alunos** → **Novo Aluno**
3. Crie o usuário e senha para o aluno
4. Clique em **Gerenciar** → **Atribuir Módulo** para liberar módulos

## Atualizar o Site
Quando fizer alterações nos arquivos:
1. Faça upload dos arquivos atualizados (ou `git pull` se usar Git)
2. Na aba **Web**, clique em **Reload**

## Re-seed do banco (se necessário)
Para atualizar conteúdo das aulas sem perder dados de alunos:
```bash
cd ~/plataforma_de_cursos
python3 reseed.py
```

## Contato
- **WhatsApp:** (15) 98140-7589
- **Discord:** matheusdeoliveira1936

---

## Troubleshooting

**Erro 500 / Página não carrega:**
- Verifique o **Error log** na aba Web
- Confirme que o path no WSGI está correto
- Verifique se as dependências foram instaladas

**Banco não encontrado:**
- Execute novamente o passo 5 para inicializar o banco

**CSS/JS não carregam:**
- Verifique a configuração de Static files (passo 6)
- Confirme que o path aponta para a pasta `static/` correta
