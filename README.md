# Apoia+ (Plataforma de Doações)

O **Apoia+** é uma plataforma desenvolvida em **Django** que conecta **doadores** e **destinatários** de forma simples, transparente e intuitiva.  
O sistema permite o cadastro de usuários, login, redefinição de senha, gerenciamento de itens doados e solicitados.

---

## 🚀 Funcionalidades Principais

### 👤 Autenticação de Usuário
- Cadastro de novos usuários com seleção de perfil (**Doador** ou **Destinatário**)
- Login e Logout com controle de sessão
- Redefinição de senha completa via e-mail (com fluxo do Django)
- Mensagens de feedback

### 🎁 Área do Doador
- Interface moderna com abas (“Minhas Doações”, “Ranking” e “Perfil”)
- Modal para cadastrar novas doações
- Edição e visualização dos dados do perfil

### 📦 Área do Destinatário
- Cadastro de **itens solicitados** (CRUD completo)
  - Criar novos pedidos de itens
  - Editar informações
  - Excluir solicitações antigas
  - Listagem automática com data e quantidade
- Ranking de instituições mais beneficiadas

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia |
|-|-|
| Back-end | Python  + Django |
| Front-end | HTML5, CSS3, JavaScript |
| Banco de Dados | SQLite (padrão do Django) |
| Estilo | Tema escuro e uso do Font Awesome |
| Autenticação | Nativa do Django |
