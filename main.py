import cv2
import numpy as np
import sys

def filtrar_com_porta_and(caminho_imagem_entrada: str, caminho_imagem_saida: str):
    """
    Aplica um filtro de porta lógica AND com uma máscara verde (0x00FF00)
    a uma imagem, isolando efetivamente o canal verde.

    Args:
        caminho_imagem_entrada (str): O caminho para a imagem de entrada.
        caminho_imagem_saida (str): O caminho para salvar a imagem resultante.
    """
    try:
        # 1. Carregar a imagem com OpenCV (formato BGR)
        imagem_bgr = cv2.imread(caminho_imagem_entrada)
        if imagem_bgr is None:
            print(f"Erro: Não foi possível carregar a imagem em '{caminho_imagem_entrada}'.", file=sys.stderr)
            return

        print(f"Imagem '{caminho_imagem_entrada}' carregada. Dimensões: {imagem_bgr.shape}")

        # 2. Criar a máscara de cor para a operação AND
        # A máscara precisa ter as mesmas dimensões da imagem original.
        # Criamos uma matriz cheia da cor que queremos usar como máscara.
        # Lembre-se, OpenCV usa BGR, então (0, 255, 0) é a ordem correta para verde.
        mascara_cor_verde = np.full(imagem_bgr.shape, (0, 255, 0), dtype=np.uint8)

        # 3. Aplicar a operação bitwise AND
        # Esta operação é feita pixel a pixel entre a imagem original e a nossa máscara de cor.
        resultado = cv2.bitwise_and(imagem_bgr, mascara_cor_verde)

        # 4. Salvar a imagem resultante
        cv2.imwrite(caminho_imagem_saida, resultado)
        print(f"Filtro AND aplicado. Imagem resultante salva em '{caminho_imagem_saida}'")
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}", file=sys.stderr)

# --- Exemplo de Uso ---
if __name__ == "__main__":
    arquivo_de_entrada = "deepSpace_5_new.png"
    arquivo_de_saida = "resultado3.png"
    
    filtrar_com_porta_and(arquivo_de_entrada, arquivo_de_saida)