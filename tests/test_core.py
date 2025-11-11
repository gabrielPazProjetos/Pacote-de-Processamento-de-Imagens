import pytest
from PIL import Image
from io import BytesIO
from image_processing import resize_image, convert_image, apply_blur

# Função auxiliar para criar uma imagem em memória
def create_test_image(color=(255, 0, 0), size=(100, 100)):
    image = Image.new("RGB", size, color)
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)
    return Image.open(buffer)

def test_resize_image(tmp_path):
    input_image = create_test_image()
    input_path = tmp_path / "input.jpg"
    output_path = tmp_path / "output.jpg"
    input_image.save(input_path)

    resize_image(str(input_path), str(output_path), (50, 50))
    result = Image.open(output_path)
    assert result.size == (50, 50)

def test_convert_image(tmp_path):
    input_image = create_test_image()
    input_path = tmp_path / "input.jpg"
    output_path = tmp_path / "output.png"
    input_image.save(input_path)

    convert_image(str(input_path), str(output_path), "PNG")
    result = Image.open(output_path)
    assert result.format == "PNG"

def test_apply_blur(tmp_path):
    input_image = create_test_image()
    input_path = tmp_path / "input.jpg"
    output_path = tmp_path / "blurred.jpg"
    input_image.save(input_path)

    apply_blur(str(input_path), str(output_path))
    result = Image.open(output_path)
    assert result.size == input_image.size
