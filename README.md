Poc - Redis vs Relacional. 
===================

#### Múltiplas Inserções.
Prova de conceito entre o uso do banco chave-valor Redis se saíra melhor em questão de performance comparado com um relacional quando muitas requisições de insertes a base de dados.

#### Instalação
Se preferir você pode acessar o repositório com diversos Poc entre redis e mysql sem precisar criar um projeto django para instalar essa app. [LINK](https://github.com/douglasbastos/redis_practice_with_django)

#### Configurando em sua máquina.

Necessários:
Django >= 1.8

    Adiciona no settings ou altere para onde seu redis está instalado
    
    REDIS_DB = {
        'host': '127.0.0.1',
        'port': 6379,
        'pass': '',
        'db': 0
    }

Execute o comando para criar votação na base de dados
./manager.py gera_votacao

Após você pode executar teste de carga entre as duas urls.

    Mysql
    http://www.mysite.com/votacao/mysql/vote/
.

    Redis
    http://www.mysite.com/votacao/redis/vote/

Você pode usar o [siege](https://www.joedog.org/siege-manual/) para realizar esses testes