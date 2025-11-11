from PIL import Image, ImageFilter

def resize_image(input_path, output_path, size):
    """Redimensiona uma imagem para o tamanho especificado."""
    image = Image.open(input_path)
    image = image.resize(size)
    image.save(output_path)

def convert_image(input_path, output_path, format):
    """Converte uma imagem para o formato especificado (ex: 'PNG', 'JPEG')."""
    image = Image.open(input_path)
    image.save(output_path, format=format)

def apply_blur(input_path, output_path):
    """Aplica um filtro de desfoque à imagem."""
    image = Image.open(input_path)
    blurred = image.filter(ImageFilter.BLUR)
    blurred.save(output_path)
