from PIL import Image, ImageDraw, ImageFont
import os
import glob

# Global Variables
BASE_IMAGE_PATH = "Certificate.png"
NAMES_FILE_PATH = "names.txt"
FONTS_FOLDER = "./fonts/bogart-cufonfonts/"
DEFAULT_FONT_PATH = "./fonts/bogart-cufonfonts/BOGARTREGULARTRIAL.ttf"
OUTPUT_FOLDER = "output/"
FONT_SIZE = 100
Y_COORDINATE = 520
TEXT_COLOR = "black"

def generateCertificates(font_path):
    """
    Generate certificates for all names using a specific font.

    Parameters:
    - font_path: Path to the specific font (.ttf) file.
    """
    # Load the base image
    image = Image.open(BASE_IMAGE_PATH)

    # Read the list of names
    with open(NAMES_FILE_PATH, "r") as file:
        names = file.read().splitlines()

    # Get the font name without the extension
    font_name = os.path.splitext(os.path.basename(font_path))[0]

    # Load the font
    font = ImageFont.truetype(font_path, FONT_SIZE)

    # Ensure the output folder for this font exists
    font_output_folder = os.path.join(OUTPUT_FOLDER, font_name)
    os.makedirs(font_output_folder, exist_ok=True)

    # Generate certificates for each name
    for name in names:
        # Convert name to title case
        title_case_name = ' '.join(word.capitalize() for word in name.split())

        # Create a copy of the input image
        certificate = image.copy()

        # Create a drawing context for adding text to the copy
        draw = ImageDraw.Draw(certificate)

        # Calculate the text width and height for center alignment
        text_bbox = font.getbbox(title_case_name)
        text_width = text_bbox[2] - text_bbox[0]
        image_width, image_height = certificate.size
        x = (image_width - text_width) // 2

        # Add the name in title case to the certificate with center alignment
        draw.text((x, Y_COORDINATE), title_case_name, fill=TEXT_COLOR, font=font)

        # Save the individual certificate
        output_path = os.path.join(font_output_folder, f"{title_case_name}.png")
        certificate.save(output_path)
        # break

    print(f"Certificates generated successfully for font '{font_name}' in '{font_output_folder}'.")
    
# def traverse_all_fonts():
#     """
#     Function to iterate over all fonts and generate certificates.
#     """
#     # Iterate over all fonts in the fonts folder
#     for font_path in glob.glob(os.path.join(FONTS_FOLDER, "*.ttf")):
#         # Generate certificates using the current font
#         generateCertificates(font_path)
        
def main():
    generateCertificates(DEFAULT_FONT_PATH)

if __name__ == "__main__":
    main()
