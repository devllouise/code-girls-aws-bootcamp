## 🗂 Desafio 03 - Automação de Workflows com AWS Step Functions

### Objetivo
Este desafio teve como foco entender e aplicar os conceitos de **orquestração de processos** dentro da AWS, utilizando o serviço **Step Functions**.  
> A ideia é aprender como automatizar fluxos de tarefas — como chamadas de Lambda, validações e integrações — de forma visual, estruturada e fácil de monitorar.

---

### O que é o AWS Step Functions
O **AWS Step Functions** é um serviço que permite **criar fluxos automatizados** entre diferentes componentes da AWS.  

Ele é ideal quando se precisa:
- Controlar a **ordem de execução** de tarefas;
- **Tomar decisões condicionais** no meio do processo;
- **Tratar erros automaticamente** (com retry e catch);
- E ainda acompanhar tudo de forma **visual** pelo console da AWS.

---

### Como o Step Functions funciona
O Step Functions usa o conceito de **máquina de estados** (*state machine*).  
Cada etapa do seu fluxo é um **estado**, e o serviço segue o caminho de acordo com as transições definidas — como um fluxograma automatizado.

**Em resumo:**
1. Definimos os estados (as etapas do processo).  
2. O Step Functions executa cada estado na ordem correta.  
3. Cada estado pode rodar uma **função Lambda**, esperar um tempo, validar uma condição ou até encerrar o fluxo.  
4. Tudo é gerenciado automaticamente — inclusive repetições e falhas.

---

### Estrutura de um Workflow

| Tipo de Estado | Descrição                                                                 |
|----------------|---------------------------------------------------------------------------|
| **Task**       | Executa uma ação (como chamar uma função Lambda).                         |
| **Choice**     | Define uma condição (ex: se X for verdadeiro, siga por outro caminho).     |
| **Wait**       | Faz o fluxo pausar por um tempo determinado.                              |
| **Parallel**   | Executa várias etapas ao mesmo tempo.                                     |
| **Pass**       | Passa dados adiante sem executar código (usado para testes e ajustes).     |
| **Succeed**    | Finaliza o fluxo com sucesso.                                             |
| **Fail**       | Finaliza o fluxo com erro.                                                |

---

### Conceito-Chave
O Step Functions usa uma **linguagem de definição em JSON** chamada *Amazon States Language (ASL)*, que descreve como o fluxo deve funcionar — quais estados existem, a ordem deles, as condições, e o que acontece em caso de erro.

---

### Por que usar Step Functions
- **Menos código e mais clareza:** grande parte da lógica é visual e declarativa.  
- **Fluxos confiáveis:** o Step Functions cuida de erros, repetições e exceções sozinho.  
- **Integração nativa com AWS Lambda, SQS, SNS, DynamoDB, S3, ECS, entre outros.**  
- **Escalabilidade automática:** o fluxo acompanha o volume de execuções sem precisar configurar servidores.  
- **Observabilidade:** cada execução pode ser inspecionada passo a passo.  

---

### Exemplo de Caso de Uso
Um caso comum é o processamento de pedidos:
1. O Step Functions recebe a requisição inicial.  
2. Chama uma função **Lambda** que valida os dados do pedido.  
3. Um **Choice State** verifica se o pedido é válido.  
4. Se sim, o fluxo segue para aprovação; se não, encerra com erro.  
5. O status final é retornado e armazenado.

---

### Integrações Possíveis
O Step Functions pode se conectar com vários serviços AWS:
- **AWS Lambda** → para executar lógicas de negócio.  
- **Amazon SQS / SNS** → para filas e notificações.  
- **DynamoDB** → para leitura e escrita de dados.  
- **ECS / Fargate** → para orquestrar containers.  
- **S3** → para armazenar resultados e logs.

---

### Insight pessoal
Depois de estudar o Step Functions, percebi que ele **simplifica muito a automação** dentro da AWS.  
Em vez de escrever scripts enormes pra controlar ordens e condições, dá pra montar tudo **como um diagrama interativo**, o que torna o processo muito mais visual e intuitivo.  
É como se o fluxo “ganhasse vida” e você pudesse assistir cada parte funcionando em tempo real.  

---

### Aprendizados do desafio
- Entender o conceito de **máquina de estados** e como aplicá-lo na prática.  
- Criar fluxos automáticos e inteligentes entre serviços da AWS.  
- Integrar o Step Functions com **Lambda** para executar lógicas personalizadas.  
- Aprender sobre **tratamento de erros**, **condições** e **paralelismo**.  
- Documentar e versionar o fluxo no GitHub como parte do meu aprendizado em automação cloud.  