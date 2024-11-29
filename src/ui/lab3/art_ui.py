"""
This module defines the ArtUI class, which provides an interface for
generating and saving ASCII art based on user preferences.
Users can select text, font, color, justification, and width for the ASCII art.
"""

from src.classes.lab3.generate_art import AsciiArtGenerator
from src.const.const import (
    FONT_CHOICE_PROMPT, COLOR_CHOICE_PROMPT, JUSTIFY_CHOICE_PROMPT,
    WIDTH_CHOICE_PROMPT, SAVE_CHOICE_PROMPT, FILE_NAME_PROMPT,
    USER_ASCII_TEXT_PROMPT
)

from lib import FileOperations, UserInput


class ArtUI:
    """
    Interface class for managing user input, generating ASCII art,
    and providing options to save the artwork.
    """

    def __init__(self, config):
        """Initialize ArtUI with a configuration and ASCII art generator."""
        self.config = config
        self.art_generator = AsciiArtGenerator(self.config)

    def get_text_input(self):
        """Prompt the user to input text for ASCII art generation."""
        return input(USER_ASCII_TEXT_PROMPT)

    def get_font_choice(self):
        """Prompt the user to choose a font from available options."""
        return UserInput.get_input(FONT_CHOICE_PROMPT, self.config.fonts)

    def get_color_choice(self):
        """Prompt the user to choose a color from available options."""
        return UserInput.get_input(COLOR_CHOICE_PROMPT, list(self.config.colors.keys()))

    def get_justification_choice(self):
        """Prompt the user to select text justification."""
        return UserInput.get_input(JUSTIFY_CHOICE_PROMPT, self.config.justify)

    def get_width_input(self):
        """Prompt the user to input a width for the ASCII art."""
        return UserInput.get_integer_input(WIDTH_CHOICE_PROMPT, 10, 175)

    def generate_ascii_art(self):
        """Generate ASCII art based on user preferences for text, font, color, and alignment."""
        text = self.get_text_input()
        font = self.get_font_choice()
        color = self.get_color_choice()
        justify = self.get_justification_choice()
        width = self.get_width_input()

        ascii_art = self.art_generator.generate_art(text, color, font, width, justify)
        print(f"{self.config.colors.get(color)}{ascii_art}{self.config.colors.get('reset')}")

        self.prompt_to_save_ascii_art(ascii_art)

    def prompt_to_save_ascii_art(self, ascii_art):
        """Prompt the user to decide if the ASCII art should be saved."""
        save_choice = input(SAVE_CHOICE_PROMPT).strip().lower()
        if save_choice in ('yes', 'y'):
            self.save_ascii_art(ascii_art)

    def save_ascii_art(self, ascii_art):
        """Save ASCII art to a specified file."""
        filename = input(FILE_NAME_PROMPT).strip()
        if not filename.endswith('.txt'):
            filename += '.txt'

        FileOperations.save_art(ascii_art, self.config.file_path, filename)

    def start_ui(self):
        """Initiate the ASCII art generation process."""
        self.generate_ascii_art()
