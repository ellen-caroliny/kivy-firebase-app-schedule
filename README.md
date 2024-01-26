![Imagem alt](./clip.gif)


#Visão geral

Este aplicativo é projetado para auxiliar clientes a agendar compromissos em um salão de beleza. Ele oferece as seguintes funcionalidades:

* Registro e login de usuários usando a autenticação Firebase
* Agendamento de compromissos com seleção de data e hora
* Confirmação e armazenamento de compromissos no banco de dados Firebase Realtime

#Recursos principais

* Interface amigável ao usuário construída com KivyMD
* Componentes de Design Material para uma experiência visualmente atraente
* Integração com o Firebase para autenticação e armazenamento de dados
* Funcionalidade de agendamento de compromissos

#Tecnologias usadas

* Python
* Kivy
* KivyMD
* Pyrebase
* Autenticação Firebase
* Banco de dados Firebase Realtime

1. Instale as bibliotecas necessárias:

   ```bash
   pip install kivymd pyrebase firebase-admin
   ```

2. Crie um projeto Firebase e habilite a autenticação e o banco de dados Realtime.
3. Obtenha os detalhes de configuração do seu projeto Firebase e substitua o espaço reservado em `firebaseConfig` no código.
4. Execute o aplicativo:

   ```bash
   python main.py
   ```

#Uso

1. Cadastre-se ou faça login usando seu e-mail e senha.
2. Na tela inicial, clique no ícone do calendário para selecionar uma data.
3. Escolha um horário para o seu compromisso.
4. Clique no botão "Agendar" para confirmar seu compromisso.
