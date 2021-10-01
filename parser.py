from pdf2image import convert_from_path
from models import PubLayNet_MaskRCNN
from utils import unroll_pdf_to_images, segment_page, parse_pages, configure_dirs, remove_temp_dir

class Parser():
    def __init__(self, input_file):
        self.input_file = input_file

    def parse(self):
        images = convert_from_path(self.input_file)
        model = PubLayNet_MaskRCNN()
        configure_dirs()
        # Unroll PDF to images
        unroll_pdf_to_images(images)
        # Parse pages
        parse_pages(images, model)
        # Remove temp dir
        remove_temp_dir()

