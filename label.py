import os

from annotator import Annotator

# define the labels
labels = [{'name': 'header-up', 'color': (0, 255, 0)},
          {'name': 'header-down', 'color': (255, 0, 0)}]

# folder for storing clips
clips_folder = '/home/yang/research/dock/explicator/tmp-clips'

# define video path
videos_path = '/home/yang/research/dock/explicator/videos-paper/left'

# define video for labeling
video_name = 'out_2019-07-15_14-36-14_fin.mp4'
video_anno = videos_path + '/' + video_name

anno_file = video_name.replace('.mp4', '-labels.json')

# set up annotator
annotator = Annotator(labels, clips_folder, annotation_file=anno_file)

# check if we already generated clips
if [f for f in os.listdir(clips_folder) if not f.startswith('.')] == []:
    # no prior generated clips
    print('Clips folder is empty.')
    # split the main video into 3-second clips
    # note: our video is 30 fps, 30 * 3 = 90 = clip_length
    annotator.video_to_clips(video_anno, clips_folder, clip_length=90)
else:
    print('Clips already generated.')

# run the GUI
annotator.main()
