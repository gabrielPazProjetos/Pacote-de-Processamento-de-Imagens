--- image_processing
Pacote local de processamento de imagens com Python — funcional e pronto para uso.

Este projeto foi desenvolvido com base em boas práticas de empacotamento Python. Ele ão precisa ser publicado no PyPI para funcionar: basta clonar o repositório e instalar localmente com pip install .

--- Funcionalidades
- Redimensionamento de imagens
- Conversão de formatos (JPEG, PNG, etc.)
- Aplicação de desfoque (blur)

--- Como usar
- Clone o repositório

- bash
git clone 
cd ***
- Instale o pacote localmente
bash
pip install .
- O pacote será instalado e poderá ser importado normalmente em qualquer script Python.

--- Exemplo de uso
python
from image_processing import resize_image, convert_image, apply_blur
resize_image("entrada.jpg", "saida.jpg", (300, 300))
convert_image("entrada.jpg", "saida.png", "PNG")
apply_blur("entrada.jpg", "saida_borrada.jpg")

--- Testes automatizados
Este projeto inclui testes automatizados com pytest. Para executá-los:
- bash
pip install pytest
pytest tests/

--- Requisitos
Python 3.7+
Pillow

--- Instale as dependências com:
- bash
pip install 
