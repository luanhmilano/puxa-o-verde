# Filtro Verde com Porta AND

O objetivo principal deste script é aplicar um filtro de cor em uma imagem. Especificamente, ele isola o canal de cor verde da imagem original. Para fazer isso, ele utiliza uma operação lógica "E" (AND) bit a bit entre a imagem de entrada e uma máscara totalmente verde. O resultado é uma nova imagem que contém apenas as informações do canal verde da imagem original. Utiliza Python, OpenCV e NumPy.

## Instalação

1. **Clone o repositório** (se necessário) e navegue até a pasta do projeto.
2. **Instale as dependências**:
   ```sh
   pip install opencv-python numpy
   ```

## Como usar
1. Coloque a imagem que deseja processar na mesma pasta do script `main.py`.
2. Edite as variáveis `arquivo_de_entrada` e `arquivo_de_saida` no final do script `main.py` para definir o arquivo de entrada e o nome do arquivo de saída.

3. Execute o script
```sh
   python main.py
```

4. A imagem filtrada será salva com o nome definido em `arquivo_de_saida`.

## Análise das Bibliotecas
- **OpenCV (cv2)**: Esta é a biblioteca OpenCV (Open Source Computer Vision Library), uma das mais poderosas e populares para tarefas de visão computacional e processamento de imagem em Python. Neste código, ela é usada para carregar a imagem de um arquivo `(cv2.imread)`, aplicar a operação lógica `(cv2.bitwise_and)` e salvar a imagem resultante `(cv2.imwrite)`.
- **NumPy**: NumPy (Numerical Python) é uma biblioteca fundamental para computação científica em Python. Imagens, para o OpenCV, são representadas como matrizes (arrays) de números (os valores dos pixels). O NumPy é extremamente eficiente para criar e manipular essas matrizes. Aqui, ele é usado para criar a "máscara" de cor verde `(np.full)` que terá as mesmas dimensões da imagem original.
- **Sys**: Esta biblioteca fornece acesso a variáveis e funções que interagem com o interpretador Python. Neste script, sys.stderr é usado para direcionar mensagens de erro para a saída de erro padrão, que é uma prática recomendada para separar mensagens de erro das saídas normais do programa.

## Explicação da função `filtrar_com_porta_and`

Esta é a função principal que realiza todo o processamento. Vamos analisar cada passo dentro dela.

```python
    def filtrar_com_porta_and(caminho_imagem_entrada: str, caminho_imagem_saida: str):
```
A função é definida para aceitar dois argumentos: o caminho do arquivo da imagem que será processada `(caminho_imagem_entrada)` e o caminho onde a imagem final será salva `(caminho_imagem_saida)`.

### 1. Carregamento da Imagem
```python
    imagem_bgr = cv2.imread(caminho_imagem_entrada)
    if imagem_bgr is None:
        print(f"Erro: Não foi possível carregar a imagem em '{caminho_imagem_entrada}'.", file=sys.stderr)
        return
```
* `cv2.imread()`: Esta função do OpenCV carrega a imagem especificada. Um detalhe crucial é que o OpenCV carrega imagens no formato de cores BGR (Azul, Verde, Vermelho) por padrão, e não no formato mais comum RGB. É por isso que a variável foi nomeada `imagem_bgr`.

* `if imagem_bgr is None:`: Esta é uma verificação de segurança. Se o caminho da imagem estiver errado ou o arquivo estiver corrompido, `cv2.imread()` retornará `None`. O código verifica isso e, se for o caso, imprime uma mensagem de erro e encerra a função.

### 2. Criação da Máscara de Cor
```python
    mascara_cor_verde = np.full(imagem_bgr.shape, (0, 255, 0), dtype=np.uint8)
```
* `imagem_bgr.shape`: Retorna as dimensões da imagem (altura, largura, número de canais de cor).

* `np.full(...)`: Esta função do NumPy cria uma nova matriz com as mesmas dimensões (`imagem_bgr.shape`) da imagem original.

* `(0, 255, 0)`: Este é o valor com o qual cada pixel da nova matriz será preenchido. Como o OpenCV usa o formato BGR, `(0, 255, 0)` representa a cor verde pura (Azul=0, Verde=255, Vermelho=0).

* `dtype=np.uint8`: Define o tipo de dados dos elementos da matriz como inteiros de 8 bits sem sinal (valores de 0 a 255), que é o tipo padrão para representar cores em imagens.

O resultado é a criação de uma imagem "virtual" (a máscara) que tem o mesmo tamanho da original, mas é inteiramente pintada de verde.

### 3. Aplicação da Operação Lógica AND
```python
    resultado = cv2.bitwise_and(imagem_bgr, mascara_cor_verde)
```

Esta é a etapa central do código.

* `cv2.bitwise_and()`: Esta função aplica uma operação "E" (AND) bit a bit entre duas imagens, pixel por pixel.

Como funciona o `bitwise_and` com cores?
A operação é feita para cada canal de cor (B, G, R) de cada pixel. Vamos pegar um pixel da imagem original com a cor, por exemplo, `(B=150, G=200, R=100)`. A máscara verde tem o valor `(B=0, G=255, R=0)` em todos os pixels. A operação AND será:

Canal Azul: `150 AND 0`  -> `0`

Canal Verde: `200 AND 255` -> `200`

Canal Vermelho: `100 AND 0` -> `0`

O pixel resultante terá a cor `(0, 200, 0)`.

A operação AND com `0` sempre resulta em `0`. A operação AND de um número com `255` (que em binário é `11111111`) sempre resulta no próprio número. Portanto, ao aplicar essa máscara:

* Os canais Azul e Vermelho da imagem original são zerados.

* O canal Verde da imagem original é preservado.

O efeito prático é "filtrar" a imagem, mantendo apenas as informações do canal verde.

### 4. Salvando a Imagem Resultante
```python
    cv2.imwrite(caminho_imagem_saida, resultado)
```

## Bloco de Execução Principal

```python
    if __name__ == "__main__":
        arquivo_de_entrada = "deepSpace_1_new.png"
        arquivo_de_saida = "resultado1.png"
    
        filtrar_com_porta_and(arquivo_de_entrada, arquivo_de_saida)
```

* `if __name__ == "__main__"`:: Esta é uma construção padrão em Python que garante que o código dentro deste bloco só será executado quando o script for rodado diretamente (e não quando for importado como um módulo em outro script).

* Aqui, definimos os nomes dos arquivos de entrada e saída e, em seguida, chamamos a função filtrar_com_porta_and para executar todo o processo.