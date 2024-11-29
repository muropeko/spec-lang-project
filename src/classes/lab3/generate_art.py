import pyfiglet

class AsciiArtGenerator:
    def __init__(self, config):
        self.config = config
        self.fixed_width = 175

    def generate_art(self, text, color, font_choice, user_width, justify):
        if font_choice in self.config.fonts:
            return self.create_standard_ascii_art(text, font_choice, user_width, justify)
        else:
            print(f"Font '{font_choice}' not found. Using default font.")
            return self.create_standard_ascii_art(text, 'standard', user_width, justify)

    def create_standard_ascii_art(self, text, font_choice, user_width, justify):
        figlet = pyfiglet.Figlet(font=font_choice, width=user_width)
        ascii_art = figlet.renderText(text)

        wrapped_ascii_art = self.wrap_text(ascii_art, user_width)

        return self.apply_justification(wrapped_ascii_art, justify)

    def wrap_text(self, ascii_art, user_width):
        wrapped_lines = []
        for line in ascii_art.splitlines():
            while len(line) > user_width:
                wrapped_lines.append(line[:user_width])
                line = line[user_width:]
            wrapped_lines.append(line)
        return '\n'.join(wrapped_lines)

    def apply_justification(self, ascii_art, justify):
        justified_lines = []
        for line in ascii_art.splitlines():
            if justify == 'center':
                justified_lines.append(line.center(self.fixed_width))
            elif justify == 'right':
                justified_lines.append(line.rjust(self.fixed_width))
            else:
                justified_lines.append(line.ljust(self.fixed_width))
        return '\n'.join(justified_lines)
