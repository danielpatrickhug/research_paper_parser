import layoutparser as lp
import torch

class PubLayNet_MaskRCNN(object):
    def __init__(self):
        self.model_path = 'lp://PubLayNet/mask_rcnn_X_101_32x8d_FPN_3x/config' # In model catalog
        self.label_map = {0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"} # In model`label_map`
        self.extra_config = ["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8] # Optional
        self.model = lp.Detectron2LayoutModel(
                    config_path = self.model_path,
                    label_map = self.label_map,
                    extra_config = self.extra_config
                )
    def predict(self, image):
        return self.model.detect(image)





