WebPonto BOT
============

### Intuíto:
Realizar apontamento automático de horário no portal NORBER.

### Execução
Para executar o projeto é necessário renomear o arquivo `.env.example` para `.env` e preencher o arquivo com as informações necessárias.
Depois, basta executar o seguinte comando:

```Bash
$ python main.py
```

Quando o horário for o de realizar a marcação, o BOT, após apontar a marcação, fará um banco de dados em JSON para manter o histórico de marcações.

### Necessário

> Sistema Operacional

O BOT desenvolvido foi projetado para executar sobre o Windows.

> Drivers do Browser

É necessário realizar o download das versões 91 e/ou 90 do Chrome e colocar no diretório `./drivers` do projeto.
Basta [clicar aqui](https://chromedriver.chromium.org/downloads) para acessar o webdriver.
Então renomeie o .exe da seguinte forma: chromedriver90.exe
