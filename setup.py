from setuptools import setup, find_packages

setup(
    name="image_processing",
    version="0.1.0",
    author="Seu Nome",
    description="Pacote local para processamento de imagens com Python",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["Pillow"],
    python_requires=">=3.7",
)
