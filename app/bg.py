import torch
from model import MattingNetwork
from inference import convert_video
from app.utilities import generate_final_video, generate_video_path


def removal(uid):
    model = MattingNetwork('mobilenetv3').eval().cuda()  # or "resnet50"
    model.load_state_dict(torch.load('rvm_mobilenetv3.pth'))

    video_local = generate_video_path(uid)
    final_video = generate_final_video(uid)

    convert_video(
        model,  # The model, can be on any device (cpu or cuda).
        input_source=video_local,  # A video file or an image sequence directory.
        output_type='video',  # Choose "video" or "png_sequence"
        output_composition=final_video,  # File path if video; directory path if png sequence.
        # output_alpha="pha.mp4",  # [Optional] Output the raw alpha prediction.
        # output_foreground="fgr.mp4",  # [Optional] Output the raw foreground prediction.
        output_video_mbps=4,  # Output video mbps. Not needed for png sequence.
        downsample_ratio=None,  # A hyperparameter to adjust or use None for auto.
        seq_chunk=12,  # Process n frames at once for better parallelism.
    )