### test unittest

- A biblioteca _unnitest_ não precisa de instalção e nativa do python.

`python test_assertions.py`

`python -m unittest`

#### Para executar um arquivo de teste, você pode simplesmente executá-lo como um script Python:

```
python testes.py
```

Ou, se estiver usando um ambiente de desenvolvimento integrado (IDE) executar testes diretamente do ambiente.

O código if **name** == '**main**': garante que o arquivo seja executado como um script principal, e unittest.main() descobre todos os métodos de teste na classe TestesBasicos e os executa.

### Convenções de nomenclatura

- nomes de classe e método prefixados com *test* .
- classes de teste usam _camel-casing_, e os métodos de teste são em letras _minúsculas_ e as palavras são separadas por um _sublinhado_

- nome de arquivo do Python para arquivos de teste, é _test_exercise.py_

### Conveções pytest

- padrão deixar o diretorio _tests_ na raiz do projeto, mas também não é incomum vê-lo ao lado dos módulos de código.

- funções de teste devem ser prefixadas com \_test\_\_.

- As classes de teste têm o prefixo _Test_
- Os métodos de teste têm o prefixo \_test\_\_

### Instalação da biblioteca pytest

```
pip install pytest
```

### Executando todos os teste

```
pytest
```

### Executar um teste especifico

```
pytest test_arquivo.py
```

### Observação

- Ao executar _pytest -vv_, o relatório aumenta a quantidade de detalhes e fornece uma comparação granular. Esse relatório não apenas detecta e mostra a falha, mas também permite que você faça alterações rapidamente para corrigir o problema.
