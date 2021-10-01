import cv2
from pdf2image import convert_from_path
import layoutparser as lp
import os
import shutil
import arxiv
import numpy as np
import json

def zip_output_dir(arxiv_id: str):
    shutil.make_archive(f'./{arxiv_id}_zipped', 'zip', './output')
    shutil.rmtree('./output')

def download_arxiv_paper(paper_id: str) -> str:
    paper = next(arxiv.Search(id_list=[paper_id]).results())
    file_name = f"{paper_id}.pdf"
    # Download the PDF to the PWD with a default filename.
    paper.download_pdf(filename=file_name)
    return file_name

def remove_temp_dir():
    if os.path.exists('./temp'):
        shutil.rmtree('./temp')

def remove_arxiv_paper(file_name: str):
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

def segment_page(text_blocks, idx: int, image, arxiv_id: str, extract_text: bool):
    txt_data = {}
    txt_data['segment'] = []
    for j, block in enumerate(text_blocks):
        segment_image = (block
                        .pad(left=30, right=30, top=30, bottom=30)
                        .crop_image(image))
        if extract_text:
            ocr_agent = lp.TesseractAgent(languages='eng')
            text = ocr_agent.detect(segment_image)
            txt_data['segment'].append({
                             'name': f'{arxiv_id}_page_{str(idx)}_segment_{str(j)}_paper',
                             'text': text
                            })
        cv2.imwrite(f'./output/{arxiv_id}_page_{str(idx)}_segment_{str(j)}_paper.jpg', segment_image)
        print(f"Saving segment to ./output/{arxiv_id}_page_{str(idx)}_segment_{str(j)}_paper.jpg")
    if extract_text:
        with open(f'./output/{arxiv_id}_page_{str(idx)}.json', 'w') as f:
            json.dump(txt_data, f)

def parse_pages(images, model, arxiv_id: str, extract_text: bool):
    for i in range(len(images)):
        image = cv2.imread(f"./temp/page{i}.jpg")
        image = image[..., ::-1] 
        layout = model.predict(image)
        print(lp.draw_box(image, layout, box_width=5))
        text_blocks = lp.Layout([b for b in layout if b.type == 'Text'])
        segment_page(text_blocks, i, image, arxiv_id, extract_text)