import cv2
from pdf2image import convert_from_path
import layoutparser as lp
import os
import shutil

def remove_temp_dir():
    if os.path.exists('./temp'):
        shutil.rmtree('./temp')

def configure_dirs():
    if os.path.exists('./temp'):
        shutil.rmtree('./temp')
    os.mkdir('./temp')
    if os.path.exists('./output'):
        shutil.rmtree('./output')
    os.mkdir('./output')

def unroll_pdf_to_images(images):
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('./temp/page'+ str(i) +'.jpg', 'JPEG')

def segment_page(text_blocks, idx, image):
    for j, block in enumerate(text_blocks):
        segment_image = (block
                        .pad(left=30, right=30, top=30, bottom=30)
                        .crop_image(image))
        cv2.imwrite(f'./output/page_{str(idx)}_segment_{str(j)}_paper.jpg', segment_image)
        print(f"Saving segment to ./output/page_{str(idx)}_segment_{str(j)}_paper.jpg")

def parse_pages(images, model):
    for i in range(len(images)):
        image = cv2.imread(f"./temp/page{i}.jpg")
        image = image[..., ::-1] 
        layout = model.predict(image)
        print(lp.draw_box(image, layout, box_width=5))
        text_blocks = lp.Layout([b for b in layout if b.type == 'Text'])
        segment_page(text_blocks, i, image)