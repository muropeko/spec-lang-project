from src.config.lab5_config import Lab5Config
from src.classes.lab5.generate_shape import AsciiArtGeneratorLab5

def main():
    config = Lab5Config()
    generator = AsciiArtGeneratorLab5(config)
    generator.start_ui()

if __name__ == "__main__":
    main()

