import os
from PIL import Image

def images_to_pdf(folder_path, output_folder, output_pdf_name):
    # List all files in the folder and filter for image files
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff'))]
    
    # Sort files alphabetically to maintain order
    image_files.sort()
    
    # Ensure there are images to process
    if not image_files:
        print("No image files found in the folder.")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Open images and convert them to RGB mode (required for PDF)
    images = []
    for file in image_files:
        img_path = os.path.join(folder_path, file)
        img = Image.open(img_path)
        # Convert image to RGB if it's not already in RGB mode
        if img.mode in ("RGBA", "P"):  
            img = img.convert("RGB")
        images.append(img)
    
    # Construct the output PDF path
    pdf_path = os.path.join(output_folder, output_pdf_name)
    
    # Save all images into a single PDF
    images[0].save(pdf_path, save_all=True, append_images=images[1:])
    print(f"PDF created successfully at {pdf_path}")

# Example usage
folder = "./output/BOGARTREGULARTRIAL/"  # Replace with your folder path
output_folder = "./output/pdf/"         # Desired output folder for the PDF
output_pdf_name = "INJPC24 - Participant Certificate (All).pdf"  # Desired PDF file name
images_to_pdf(folder, output_folder, output_pdf_name)
