# flake8: noqa
import os.path as osp

import hmoe.archs
import hmoe.data
import hmoe.models
from basicsr.train import train_pipeline

if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    train_pipeline(root_path)
