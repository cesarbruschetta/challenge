# Explicação da solução

Na minha solução eu utilizei a linguagem python, tenho mais experiência do desenvolvimento com essa linguagem e para fazer as regras de 
envio dos produtos eu utilizei como solução a criação de `factores`, onde consiste em ter uma classe básica que tem a lógica e os métodos 
padrões, para cada regra de envio implementei uma nova classe que extente a classe base e impletenta os métodos e rotinas que são específicas 
para determinado envio.

Assim quando a venda é processada pelo método `make_sale` ela chama um método que esta implementado dentro da classe `Order` que utiliza o tipo 
do produto como chave do dicionário de Classes de envio de produto, para pegar a classe correspondente e realizar a importação e chamar o método 
base `run`que é comum para as implementações e caso o tipo do produto não esteja implementado o método utiliza a classe base para tratar essa 
exceção.

E para testar as 4 tipos de produto mais a exceção do tipo de produto criei um pequeno script (`tests.py`) que consistem em uma classe de teste unitário 
que cria uma venda com cada tipo de produto e espera o seu retorno apropriado.


## Testes

```
$ coverage run test.py -v

```

## Code analysis

```
$ coverage html
```
