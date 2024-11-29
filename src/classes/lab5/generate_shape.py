from src.classes.lab5.cube import Cube
from src.ui.lab3.art_ui import ArtUI
from src.classes.lab3.generate_art import AsciiArtGenerator
from lib.user_input import UserInput

class AsciiArtGeneratorLab5:
    def __init__(self, config):
        self.config = config
        self.art_ui = ArtUI(self.config)
        self.ascii_art_generator = AsciiArtGenerator(self.config)
        self.user_input = UserInput()

    def start_ui(self):
        self.generate_ascii_art()

    def generate_ascii_art(self):

        size = self.user_input.get_integer_input("Choose a size: ", 5, 20)
        color = self.art_ui.get_color_choice()
        justify = self.art_ui.get_justification_choice()

        cube = Cube(size)
        cube_points = cube.draw()

        ascii_art = self.generate_ascii_art_from_points(cube_points)

        justified_ascii_art = self.ascii_art_generator.apply_justification(ascii_art, justify)

        print(f"{self.config.colors.get(color)}{justified_ascii_art}{self.config.colors.get('reset')}")

        self.art_ui.prompt_to_save_ascii_art(ascii_art)


    def generate_ascii_art_from_points(self, points):
        grid_size = 35
        grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

        for x, y in points:
            if 0 <= x < grid_size and 0 <= y < grid_size:
                grid[y][x] = '#'

        ascii_art = '\n'.join(''.join(row) for row in grid)
        return ascii_art