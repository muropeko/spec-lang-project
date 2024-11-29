from src.ui.lab3.art_ui import ArtUI
from src.config.lab3_config import Lab3Config

def main():
    config = Lab3Config()
    art_ui = ArtUI(config)
    art_ui.start_ui()

if __name__ == "__main__":
    main()