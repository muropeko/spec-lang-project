from src.const.const import REPLACE_CHARACTER_PROMPT, ONE_CHARACTER_MESSAGE
from src.ui.lab3.art_ui import ArtUI

class AsciiArtGeneratorLab4:
    def __init__(self, config):
        self.config = config
        self.art_ui = ArtUI(self.config)

    def generate_ascii_art(self):
        text = self.art_ui.get_text_input()
        font_name = self.art_ui.get_font_choice()
        color = self.art_ui.get_color_choice()
        justify = self.art_ui.get_justification_choice()

        font = self.config.custom_font if font_name == "custom" else self.config.star_font

        replacement_char = self.get_replacement_char()

        ascii_art = self.create_custom_ascii_art(text, font, justify, color, replacement_char)
        print(f"{self.config.colors.get(color)}{ascii_art}{self.config.colors.get('reset')}")
        
        self.art_ui.prompt_to_save_ascii_art(ascii_art)


    def start_ui(self):
        self.generate_ascii_art()

    def get_replacement_char(self):
        while True:
            replacement_char = input(REPLACE_CHARACTER_PROMPT)
            if len(replacement_char) <= 1:
                return replacement_char
            else:
                print(ONE_CHARACTER_MESSAGE)

    def create_custom_ascii_art(self, text, font, justify, color='reset', replacement_char=None):
        ascii_art_lines = []

        for char in text.upper():
            if char in font:
                char_art = font[char]
                for i in range(len(char_art)):
                    if i >= len(ascii_art_lines):
                        ascii_art_lines.append([''])
                    line = char_art[i]
                    ascii_art_lines[i].append(line)
            else:
                for i in range(len(ascii_art_lines)):
                    if i >= len(ascii_art_lines):
                        ascii_art_lines.append([''])
                    ascii_art_lines[i].append(' ' * (len(next(iter(font.values()))[0]) + 1))

        for i in range(len(ascii_art_lines)):
            ascii_art_lines[i] = ''.join(ascii_art_lines[i])

        ascii_art = '\n'.join(ascii_art_lines)

        ascii_art = self.replace_characters_in_art(ascii_art, replacement_char)

        justified_art = self.apply_justification(ascii_art, justify)

        return self.apply_color(justified_art, color)

    def replace_characters_in_art(self, ascii_art, replacement_char):
        if replacement_char:
            ascii_art = ascii_art.replace('x', replacement_char)
            ascii_art = ascii_art.replace('☆', replacement_char)
        return ascii_art

    def apply_justification(self, ascii_art, justify):
        justified_lines = []
        for line in ascii_art.splitlines():
            if justify == 'center':
                justified_lines.append(line.center(self.config.fixed_width))
            elif justify == 'right':
                justified_lines.append(line.rjust(self.config.fixed_width))
            else:
                justified_lines.append(line.ljust(self.config.fixed_width))
        return '\n'.join(justified_lines)

    def apply_color(self, ascii_art, color):
        color_code = self.config.colors.get(color, self.config.colors['reset'])
        return f"{color_code}{ascii_art}{self.config.colors['reset']}"
