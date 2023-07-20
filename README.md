# Monitoramento-B3

Sistema de monitoramento de ativos da B3 desenvolvido em Django. Conta com configurações de limite superior e inferior de túnel com o envio de e-mail para o usuário caso o ativo atinja o valor configurado.

## Instalação

As versões abaixo são **recomendadas**, mas não obrigatórias, provavelmente o projeto funcionará também com versões mais recentes das tecnologias usadas.

### Python 3.7.x

- Instale o Python  disponível [aqui](https://www.python.org/downloads/release/python-379/)
- Instale o PIP
  - Adicione o pip às variáveis de ambiente
- Instale os requisitos do projeto
  ```bash
  # /Monitoramento-B3/
  pip install -r "requirements.txt"
  ```

### PostgreSQL 11.x

-  **Windows**/**Mac**: Instalação disponível  [aqui](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)  
 
-  **Linux**: Siga as instruções disponíveis [aqui](https://computingforgeeks.com/install-postgresql-11-on-ubuntu-linux/)

### MetaTrader 5

-  Essa versão é **obrigatória**
 
-  O MetaTrader 5 é uma ferramenta gratuita que permite realizar análise de ativos em tempo real
- Disponível para Windows e Linux [aqui](https://www.metatrader5.com/pt/download)
- Após a instalação será necessário um login e senha, disponibilizados gratuitamente por diversas corretoras, como Xp e Rico
	- [Xp](https://atendimento.xpi.com.br/artigo/1476-como-realizar-contratacao-e-instalacao-do-metatrader-5)
	- [Rico](https://www.rico.com.vc/plataformas/metatrader/)

## Preparação do ambiente

### Variáveis de ambiente
- Renomeie o arquivo `template_env.txt` para `.env`
- Altere os exemplos de strings atribuídos a cada variável, adicionando suas credenciais do Banco de dados e E-mail
	- Se você não possuir uma senha de app definida para o seu e-mail pode consultar o passo a passo [aqui](https://support.google.com/mail/answer/185833?hl=en)

### Migrações
- Rode as migrações do python
  ```
  # /Monitoramento-B3/core/
  python manage.py migrate
  ```

### Criação de conta de administrador
- Execute o seguinte comando, em seguida escolha um usuário, e-mail, e senha
  ```
  # /Monitoramento-B3/core/
  python manage.py createsuperuser
  ```
  
### Criação de conta para usuários
- Contas para usuários podem ser criadas à partir do painel de admin, para isso acesse a rota `/admin`
- Em seguida faça login com o usuário e senha definidos por você na etapa na contra de administrador

### Inicialização do sistema
- Execute o comando abaixo para iniciar a aplicação
  ```
  # /Monitoramento-B3/core/
  python manage.py runserver
  ```
  - para acessar a aplicação basta usar o link que aparecerá no seu terminal

- Inicialização dos monitoramentos criados
  ```
  # /Monitoramento-B3/core/
  python manage.py continuously_monitor
  ```