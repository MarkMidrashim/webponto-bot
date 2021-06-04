# WebPonto BOT

## Índice
* [Intuíto](#intuito)
* [Notas Importante](#notas-importantes)
* [Execução](#execucao)
* [Estrutura](#estrutura)

### Intuíto:
Realizar apontamento automático de horário no portal **NORBER**.

### Notas Importantes

> Sistemas Operacionais

O BOT desenvolvido foi executado, somente, sobre o **Windows**.

<br/>

> Drivers do Browser

É necessário ter o webdriver com versão compatível a do seu navegador Google Chrome e, colocar no diretório `./drivers`.
Para realizar o download, basta acessar o [Chrome Driver](https://chromedriver.chromium.org/downloads).

<br/>

> Ambiente

É necessário configurar o arquivo `.env` e configurar informações importantes para que o BOT execute os apontamentos com sucesso.


### Execução
Para executar o projeto é necessário renomear o arquivo `.env.example` para `.env` e preencher o arquivo com as informações necessárias.
Depois, basta executar o seguinte comando:

```Bash
$ python starter.py
```

Quando o horário for o de realizar a marcação, o BOT, após apontar a marcação, fará um banco de dados em JSON para manter o histórico de marcações.

### Estrutura
No download, você encontrará os seguintes diretórios e arquivos:

```
webponto-bot
    ├── src
    │ ├── bot.py
    │ ├── commons.py
    │ ├── database.py
    │ ├── main.py
    │ ├── webdriver.py
    ├── database
    ├── log
    ├── drivers
    ├── starter.py
    ├── .env.example
    ├── requirements.txt
    ├── README.md
```
