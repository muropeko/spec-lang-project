from src.classes.lab4.generate_art import AsciiArtGeneratorLab4
from src.config.lab4_config import Lab4Config

def main():
    config = Lab4Config()
    generator = AsciiArtGeneratorLab4(config)
    generator.start_ui()

if __name__ == "__main__":
    main()
