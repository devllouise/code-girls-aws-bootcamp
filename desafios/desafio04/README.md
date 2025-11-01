## ☁️ Desafio 04 - Criando Infraestrutura como Código com AWS CloudFormation

### Objetivo
Este laboratório teve como foco colocar em prática o conceito de **Infraestrutura como Código (IaC)**, utilizando o **AWS CloudFormation**.  
O desafio foi implementar minha **primeira Stack**, documentar o processo e registrar os principais **insights** sobre a criação e gerenciamento de recursos automatizados na nuvem.

---

### O que é o AWS CloudFormation
O **AWS CloudFormation** é um serviço que permite **criar e gerenciar recursos da AWS automaticamente**, a partir de **modelos declarativos** escritos em **YAML ou JSON**.  
Em vez de configurar manualmente buckets, filas, tópicos ou funções Lambda pelo console, o CloudFormation faz isso **de forma automatizada e versionável**.

Pensa nele como um **“montador de infraestrutura”**: você descreve o que quer — e ele constrói tudo pra você.  

---

### Como funciona
1. Você cria um **template** (modelo) descrevendo os recursos que deseja criar — por exemplo, um bucket S3 e uma fila SQS.  
2. O CloudFormation interpreta esse modelo e **monta tudo automaticamente** na sua conta AWS.  
3. Essa estrutura criada é chamada de **Stack** (pilha).  
4. Se você quiser atualizar ou excluir, basta alterar o template e aplicar novamente — o serviço cuida de todo o processo.  

---

### Conceitos Principais

| Conceito | Descrição |
|-----------|-----------|
| **Template** | O arquivo (YAML/JSON) que descreve toda a infraestrutura. |
| **Stack** | O conjunto de recursos criados a partir de um template. |
| **Resources** | São os componentes da AWS (como EC2, S3, Lambda, etc.). |
| **Parameters** | Variáveis que permitem personalizar o template. |
| **Outputs** | Valores retornados após a criação da Stack (ex: o nome de um bucket). |
| **Change Set** | Mostra as mudanças que serão aplicadas antes de atualizar uma Stack. |

---

### Estrutura Básica de um Template (YAML)

AWSTemplateFormatVersion: "2010-09-09"
Description: "Exemplo de template simples"

Resources:
  MeuBucketS3:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: "meu-primeiro-bucket-cloudformation"

> Esse exemplo cria automaticamente um bucket S3, sem precisar clicar nada no console.

---

### Benefícios do CloudFormation

- **Automação total**: cria, atualiza e remove recursos sem intervenção manual.
- **Consistência**: garante que ambientes (dev, staging, prod) sejam idênticos.
- **Versionamento**: templates podem ser versionados no GitHub.
- **Reprodutibilidade**: facilita recriar a infraestrutura em diferentes regiões/contas.
- **Integração com CI/CD**: pode ser usado junto com pipelines de automação.

---

### O que foi desenvolvido
O template YAML criado neste desafio tem o objetivo de provisionar um **bucket S3** automaticamente, sem precisar usar o console.  
Ele define apenas um recurso, mas já demonstra todo o poder do CloudFormation na automação da infraestrutura.

**Principais características do template:**
- Criação de um **bucket S3** com nome personalizado.  
- Uso de uma **descrição YAML** organizada e declarativa.  
- Aplicação de **tags de identificação**, facilitando rastreabilidade.  

---

### Etapas do Lab
1. Criei o arquivo `template-primeira-stack.yaml` com a definição do bucket.  
2. Carreguei o template no **AWS CloudFormation Console**.  
3. Esperei a Stack ser criada e conferi o status **CREATE_COMPLETE**.  
4. Validei o bucket no **Amazon S3 Console**, confirmando a automação.  

---

### Evidências

| Etapa | Evidência |
|-------|------------|
| 1️⃣ | Console do **CloudFormation** mostrando a Stack criada |
| 2️⃣ | Console do **S3 Bucket** criado automaticamente |
| 3️⃣ | **Propriedades do bucket** com o nome definido no template |
| 4️⃣ | **Outputs da Stack** confirmando a criação com sucesso |

> As imagens estão na pasta `/images/`

---

### Aprendizados do desafio

- Entender a estrutura e sintaxe dos templates CloudFormation.
- Criar e gerenciar uma Stack completa via console e código.
- Utilizar parâmetros e outputs para tornar o template dinâmico.
- Documentar o processo e versionar tudo no GitHub.
- Aplicar práticas de IaC que tornam o ambiente mais escalável e confiável.