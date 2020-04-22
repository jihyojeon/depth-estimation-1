# Copyright Niantic 2019. Patent Pending. All rights reserved.
#
# This software is licensed under the terms of the Monodepth2 licence
# which allows for non-commercial use only, the full terms of which are made
# available in the LICENSE file.

from __future__ import absolute_import, division, print_function

from trainer import Trainer
from options import MonodepthOptions

# options = MonodepthOptions()
# opts = options.parse()

# if __name__ == "__main__":
#     trainer = Trainer(opts)
#     trainer.train()

class Opts:
    png = False
    use_stereo = False
    #1 -------------------------------
    v1_multiscale = True
    #2
    avg_reprojection = False
    #3
    disable_automasking = False
    # --------------------------------
    predictive_mask = False
    no_ssim = False
    no_cuda = False # false->cuda / True ->CPU
    eval_stereo = False
    eval_mono = False
    disable_median_scaling = False
    ext_disp_to_eval = False
    save_pred_disps = False
    no_eval = False
    eval_eigen_to_benchmark = False
    eval_out_dir = './eval_out'
    post_process = False

    data_path = '/home/jihyo/PycharmProjects/monodepth/KITTI_raw_data'
    log_dir = './log'
    model_name = 'a'
    split = 'eigen_zhou'
    num_layers = 50 # resnet layers 18 34 50 101 152
    dataset = 'kitti' #kitti, kitti_odom, kitti_depth, kitti_test
    height = 192
    width = 640
    disparity_smoothness = 1e-3
    scales = [0,1,2,3]
    frame_ids = [0, -1, 1]

    # OPTIMIZATION options
    batch_size = 2
    learning_rate = 1e-4
    num_epochs = 20
    min_depth = 0.1  # minimum depth
    max_depth = 100
    scheduler_step_size = 15

    # ABLATION options
    weights_init = 'pretrianed' #pretrained , scratch
    pose_model_input = 'pairs' #pairs, all
    pose_model_type = 'separate_resnet' #posecnn, seperate_resnet, shared

    # SYSTEM options
    num_workers = 12

    #LOADING options
    load_weights_folder = './log/mono_model_pretrained/models/weights_19'
    models_to_load = ['encoder', 'depth'] #['encoder', 'depth', 'pose_encoder', 'pose']

    #log
    log_frequency = 250
    save_frequency = 1

    #Evaluation options
    pred_depth_scale_factor = 1
    eval_split = 'eigen' #choices=["eigen", "eigen_benchmark", "benchmark", "odom_9", "odom_10"]

opts = Opts()
trainer = Trainer(opts)
trainer.train()
