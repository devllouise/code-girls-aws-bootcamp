## ☁️ Desafio 06 - Automatizando Tarefas com Lambda e S3

### Objetivo
Neste laboratório, o objetivo foi **consolidar conhecimentos em tarefas automatizadas** utilizando **AWS Lambda** e **S3**.  
O projeto cria, de forma prática, uma **função Lambda** que grava automaticamente arquivos de log em um **bucket S3**, permitindo entender a integração entre os serviços e reforçando conceitos de **automação na nuvem**.

A ideia foi aprender como **automatizar processos simples** sem depender de CloudFormation, usando apenas código Python e permissões corretas no IAM.

---

### O que foi construído
O projeto desenvolvido faz o seguinte:

1. Cria um **bucket S3** (`maira-lambda-s3-lab`) para armazenar logs.  
2. Cria uma **IAM Role** (`LambdaS3LabRole`) com permissões de execução da Lambda e acesso ao S3.  
3. Cria uma **função Lambda Python** (`LambdaS3Lab`) que grava automaticamente um arquivo de log no S3 ao ser executada.  
4. Permite visualizar logs no **CloudWatch**, confirmando a execução correta da Lambda.

---

### Fluxo de execução
1. O bucket S3 e a IAM Role foram criados manualmente no console da AWS.  
2. A função Lambda foi criada e configurada com a role correta.  
3. Um evento de teste simples (`{}`) foi disparado na Lambda.  
4. A Lambda gravou um arquivo de log no bucket S3 e registrou informações no CloudWatch.  
5. Verificamos a criação do arquivo e os logs para confirmar o funcionamento completo.

---

### Evidências do Lab

| Etapa | Evidência |
|-------|------------|
| 1️⃣ | Console do **S3 Bucket** criado manualmente (`maira-lambda-s3-lab`) |
| 2️⃣ | Console da **Lambda Function** (`LambdaS3Lab`) criada e configurada |
| 3️⃣ | **Execução da Lambda** confirmando sucesso no teste |
| 4️⃣ | **Objeto criado no S3** (`log-YYYY-MM-DDTHH:MM:SS.txt`) |
| 5️⃣ | **Logs no CloudWatch** mostrando a execução detalhada |

> Todas as evidências estão na pasta `/images`, nomeadas conforme a sequência acima.

---

### Aprendizados do desafio
- Criei e configurei buckets S3 e funções Lambda para automação.  
- Entendi como **roles IAM e permissões** funcionam na prática para Lambda + S3.  
- Consolidei conceitos de **automação na nuvem**, sem depender de CloudFormation.  
- Testei execuções e validei logs no CloudWatch, reforçando boas práticas de monitoramento.  
- Documentei todo o fluxo, criando material de referência para futuros estudos e implementações.
