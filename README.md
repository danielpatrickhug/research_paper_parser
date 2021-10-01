# Research Paper Parser
Repository for parsing research paper pdfs and outputting image segments

| [Source](https://github.com/Layout-Parser/layout-parser) |
[Paper](https://arxiv.org/abs/2103.15348) |
[Docs](https://layout-parser.readthedocs.io/en/latest/notes/modelzoo.html) |
[Model Zoo](https://layout-parser.readthedocs.io/en/latest/notes/modelzoo.html) |

### TODO
- Parse references and output a text file of arxiv links
- Add a Fast API and frontend for interacting with code
- Add GPT3 study note generation for research paper

### Run
``` bash
conda create --name env-name
conda activate env-name
pip install -r requirements.txt
python main.py -i arxiv_id -m model_name
```

### Example: EfficientNet
[EfficientNet Arxiv Link: https://arxiv.org/abs/1905.11946](https://arxiv.org/abs/1905.11946)
``` bash
python main.py -i 1905.11946 -m publaynet
```

model_name list = {publaynet}

### Citation

```
@article{shen2021layoutparser,
  title={LayoutParser: A Unified Toolkit for Deep Learning Based Document Image Analysis},
  author={Shen, Zejiang and Zhang, Ruochen and Dell, Melissa and Lee, Benjamin Charles Germain and Carlson, Jacob and Li, Weining},
  journal={arXiv preprint arXiv:2103.15348},
  year={2021}
}

```

