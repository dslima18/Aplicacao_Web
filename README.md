# Registro de Aprendizados

Bem-vindo ao Registro de Aprendizados! Este projeto Django permite que você crie um usuário e registre os tópicos que está aprendendo, fornecendo informações detalhadas sobre cada tópico.

## Funcionalidades

- **Autenticação de Usuário:** Crie uma conta para começar a registrar seus aprendizados.
  
- **Registro de Tópicos:** Adicione tópicos específicos que você está estudando ou aprendendo.

- **Descrição Detalhada:** Forneça informações detalhadas sobre cada tópico, incluindo uma descrição abrangente.

- **Gerenciamento de Assuntos:** Associe assuntos específicos a cada tópico para organizar seus aprendizados de maneira eficiente.

## Como Executar Localmente

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/seunomeusuario/registro-de-aprendizados.git
   cd registro-de-aprendizados
Crie um Ambiente Virtual:

python -m venv venv

Ative o Ambiente Virtual:

No Windows:

venv\Scripts\activate

No Linux/Mac:

source venv/bin/activate

Instale as Dependências:

pip install -r requirements.txt

Execute as Migrações:

python manage.py migrate

Crie um Superusuário (Admin):

python manage.py createsuperuser

Inicie o Servidor de Desenvolvimento:

python manage.py runserver

Acesse o Site:

Abra o navegador e acesse http://localhost:8000/

Acesse o Painel de Administração:

Faça login como superusuário em http://localhost:8000/admin/ para gerenciar usuários, tópicos e assuntos.

Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas, sugerir melhorias ou enviar pull requests.