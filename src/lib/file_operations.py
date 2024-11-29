import os

class FileOperations:
    @staticmethod
    def save_art(ascii_art, base_path, filename):
        ascii_artworks_path = os.path.join(base_path, "ascii_artworks")

        # Ensure the ascii_artworks directory exists
        os.makedirs(ascii_artworks_path, exist_ok=True)

        # Define the full file path for saving
        file_path = os.path.join(ascii_artworks_path, filename)

        try:
            with open(file_path, 'w') as file:
                file.write(ascii_art)
            print(f"~ saved in  {file_path}\n")
        except Exception as e:
            print(f"! an error occurred while saving: {e}")
