# 🧮 Calculadora em Python  

Este projeto é uma calculadora simples desenvolvida em **Python**, permitindo realizar operações matemáticas básicas como **adição, subtração, multiplicação e divisão**. O código foi projetado para ser executado no terminal e inclui tratamento de erros para entradas inválidas.  

---

## 📌 Como executar o código  

### 1️⃣ Executando diretamente via Python  
Para rodar o código no terminal, certifique-se de que tem o **Python 3** instalado.  
Depois, siga os passos:  

1. Abra o terminal (ou prompt de comando).  
2. Navegue até a pasta onde o arquivo `calculadora.py` está salvo:  
   ```bash
   cd /caminho/para/o/arquivo
   ```  
3. Execute o script com o comando:  
   ```bash
   python3 calculadora.py
   ```  

---

### 2️⃣ Executando via script `.sh` (Linux/macOS)  
Se estiver utilizando **Linux/macOS**, você pode criar um arquivo **`executar.sh`** para facilitar a execução.  

1. **Criar o arquivo `executar.sh`**  
   No terminal, crie um novo arquivo com o comando:  
   ```bash
   touch executar.sh
   ```  

2. **Editar o arquivo e adicionar o seguinte conteúdo:**  
   ```sh
   #!/bin/bash
   python3 calculadora.py
   ```  

3. **Dar permissão de execução ao script:**  
   ```bash
   chmod +x executar.sh
   ```  

4. **Executar o código usando:**  
   ```bash
   ./executar.sh
   ```  

---

## 📜 Explicação do código  

O código segue uma lógica simples de **entrada de dados, processamento e saída**. Aqui está um resumo de cada parte:  

### 1️⃣ **Loop principal**  
O código roda dentro de um **loop `while` infinito**, permitindo que o usuário realize múltiplas operações sem precisar reiniciar o programa. O loop só é interrompido quando o usuário escolhe sair.  

### 2️⃣ **Entrada de dados**  
O programa solicita que o usuário **digite dois números**. Caso seja inserido um valor inválido (como letras), o programa exibe uma mensagem de erro e solicita uma nova entrada.  

### 3️⃣ **Escolha da operação**  
O usuário pode escolher entre cinco opções:  

- **1**: Adição (`+`)  
- **2**: Subtração (`-`)  
- **3**: Multiplicação (`*`)  
- **4**: Divisão (`/`)  
- **5**: Sair do programa  

### 4️⃣ **Tratamento de divisão por zero**  
Se o usuário tentar dividir por zero, o programa exibe um **erro específico** e retorna ao menu principal.  

### 5️⃣ **Saída do programa**  
O usuário pode optar por sair do programa digitando **5** no menu ou escolhendo a opção de saída quando perguntado.  

---

## 📝 Exemplo de execução  

**Entrada:**  
```bash
Digite o primeiro número: 10
Digite o segundo número: 5

Escolha a operação:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair
Digite o número da operação desejada: 1
```

**Saída esperada:**  
```bash
Resultado: 10 + 5 = 15
```

---

🔗 **Criado por:** Luiz Ricardo Garcia
📅 **Última atualização:** 2025  