from pdf2image import convert_from_path
from models import PubLayNet_MaskRCNN
from utils import unroll_pdf_to_images, segment_page, parse_pages, configure_dirs, remove_temp_dir

class Parser():
    def __init__(self, input_file, arxiv_id, model_name):
        self.input_file = input_file
        self.arxiv_id = arxiv_id
        if model_name == 'publaynet':
            self.model = PubLayNet_MaskRCNN()

    def parse(self):
        images = convert_from_path(self.input_file)
        model = self.model
        configure_dirs()
        # Unroll PDF to images
        unroll_pdf_to_images(images)
        # Parse pages
        parse_pages(images, model, self.arxiv_id)
        # Remove temp dir
        remove_temp_dir()

