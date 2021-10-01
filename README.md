# Research Paper Parser
Repository for parsing research paper pdfs and outputting image segments

[Source](https://github.com/Layout-Parser/layout-parser)
[Docs](https://layout-parser.readthedocs.io/en/latest/notes/modelzoo.html)
[Model Zoo](https://layout-parser.readthedocs.io/en/latest/notes/modelzoo.html)

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

