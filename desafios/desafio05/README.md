## ☁️ Desafio 05 - Implementando Infraestrutura Automatizada com AWS CloudFormation

### Objetivo
Neste laboratório, o desafio foi **automatizar a criação de uma pequena infraestrutura em nuvem** usando o **AWS CloudFormation**.  
O projeto cria, de forma totalmente automatizada, um **bucket S3**, uma **função Lambda** e a **IAM Role** necessária para sua execução — tudo controlado via código YAML.

A ideia foi entender como o CloudFormation **orquestra múltiplos serviços** da AWS sem precisar configurar nada manualmente, reforçando o conceito de **Infraestrutura como Código (IaC)**.

---

### 🧩 O que foi construído
O template YAML que desenvolvi faz o seguinte:

1. Cria um **bucket S3 versionado**, usado para armazenar logs.  
2. Cria uma **IAM Role** com permissões de execução para a função Lambda.  
3. Cria uma **função Lambda Python**, que grava automaticamente um log no S3 ao ser executada.  
4. Tudo é conectado dinamicamente, com variáveis de ambiente e dependências automáticas.

---

### ⚙️ Arquitetura Final
CloudFormation Stack
│
├── S3 Bucket (armazenamento de logs)
├── IAM Role (permissões da Lambda)
└── Lambda Function (gera log e envia para o bucket)

---

### 🚀 Fluxo de criação
1. O template foi carregado no **AWS CloudFormation Console**.  
2. A Stack foi criada e todos os recursos foram provisionados automaticamente.  
3. Após a execução da Lambda, um novo log foi gerado e armazenado no bucket S3.  
4. Os **outputs** confirmaram a criação dos recursos com sucesso.

---

### 📸 Evidências do Lab

| Etapa | Evidência |
|-------|------------|
| 1️⃣ | Console do **CloudFormation** mostrando a Stack criada |
| 2️⃣ | Console do **S3 Bucket** criado automaticamente |
| 3️⃣ | **Propriedades do bucket** com versionamento habilitado |
| 4️⃣ | Console da **Lambda Function** criada via CloudFormation |
| 5️⃣ | **Execução da Lambda** e log de sucesso |
| 6️⃣ | **Objeto criado no S3** confirmando a automação |
| 7️⃣ | **Outputs do CloudFormation** com os nomes dos recursos |

> Todas as evidências estão na pasta `/images`, nomeadas conforme a sequência acima.

---

### 💡 Aprendizados do desafio
- Conectei múltiplos serviços AWS de forma 100% automatizada.  
- Entendi o uso de **dependências (`DependsOn`)** e **variáveis de ambiente** no YAML.  
- Reforcei a importância de versionar e documentar templates IaC.  
- Vi na prática como **o CloudFormation elimina o trabalho manual** e reduz erros de configuração.