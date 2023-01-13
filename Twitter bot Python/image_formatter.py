from PIL import Image, ImageDraw, ImageFont
from typing import List
from textwrap import wrap


class ImageFormatter:
    def __init__(self, tweets: List[str], image_path: str):
        self.tweets = tweets  # lista de tweets que serão escritos na imagem
        self.image_path = image_path  # caminho da imagem
        # cria uma nova imagem com tamanho 800x800 e cor de fundo
        self.img = Image.new('RGB', (800, 800), color=(73, 109, 137))
        # cria um objeto para desenhar na imagem
        self.d = ImageDraw.Draw(self.img)
        # define a fonte e tamanho do texto
        self.font = ImageFont.truetype('arial.ttf', 24)

    def create_image(self):
        text_y = 50  # posição inicial do texto na imagem
        for tweet in self.tweets:
            text = tweet
            # divide o texto em linhas com no máximo 40 caracteres
            wrapped_text = wrap(text, width=40)
            for line in wrapped_text:
                self.d.text((50, text_y), line, font=self.font,
                            fill=(255, 255, 255))  # escreve o texto na imagem
                text_y += 30  # incrementa a posição do texto na imagem

            # desenha uma linha abaixo do texto
            self.d.line((50, text_y, 750, text_y), fill=(255, 255, 255))
            text_y += 10
        self.img.save(self.image_path)  # salva a imagem

    def format_image(self, css_path: str):
        with open(css_path, 'r') as css:
            styles = css.read()  # pega o nome da fonte no arquivo CSS
            # Get the font-family from the CSS file
            font_family = styles.split("font-family:")[1].split(";")[0].strip()
            # Get the font-size from the CSS file
            font_size = int(styles.split("font-size:")
                            [1].split(";")[0].strip().replace("px", ""))
            # Get the font-color from the CSS file
            font_color = styles.split("color:")[1].split(";")[0].strip()
            # Update the font object with the new font-family and font-size
            # self.font = ImageFont.truetype(font_size)
            # self.font = ImageFont.truetype(font_family, font_size)

            # salva a imagem com as novas formatações
            self.img.save(self.image_path)


