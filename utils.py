import cv2
from pdf2image import convert_from_path
import layoutparser as lp
import os
import shutil
import arxiv

def download_arxiv_paper(paper_id):
    paper = next(arxiv.Search(id_list=[paper_id]).results())
    file_name = f"{paper_id}.pdf"
    # Download the PDF to the PWD with a default filename.
    paper.download_pdf(filename=file_name)
    return file_name

def remove_temp_dir():
    if os.path.exists('./temp'):
        shutil.rmtree('./temp')

def remove_arxiv_paper(file_name):
    os.remove(file_name)

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

def segment_page(text_blocks, idx, image, arxiv_id):
    for j, block in enumerate(text_blocks):
        segment_image = (block
                        .pad(left=30, right=30, top=30, bottom=30)
                        .crop_image(image))
        cv2.imwrite(f'./output/{arxiv_id}_page_{str(idx)}_segment_{str(j)}_paper.jpg', segment_image)
        print(f"Saving segment to ./output/{arxiv_id}_page_{str(idx)}_segment_{str(j)}_paper.jpg")

def parse_pages(images, model,arxiv_id):
    for i in range(len(images)):
        image = cv2.imread(f"./temp/page{i}.jpg")
        image = image[..., ::-1] 
        layout = model.predict(image)
        print(lp.draw_box(image, layout, box_width=5))
        text_blocks = lp.Layout([b for b in layout if b.type == 'Text'])
        segment_page(text_blocks, i, image, arxiv_id)