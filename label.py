import os
import sys

from annotator import Annotator

# define the labels
labels = [{'name': 'header down', 'color': (255, 0, 0)}, # R
          {'name': 'header up', 'color': (0, 255, 0)}, # G
          {'name': 'transition', 'color': (0, 0, 255)}] # B

# cam type
cam_type = 'left'

# video datetime
vid_dt = '2019-07-15_18-23-47'

# folder for storing clips
clips_folder = '/home/yang/research/dock/explicator/videos-onehr-ds-labeled/' \
               + cam_type \
               + '/' + vid_dt

# define video path
vid_path = '/home/yang/research/dock/explicator/videos-onehr-ds/' + cam_type

# define video for labeling
vid_name = 'out_' + vid_dt + '_fin.mp4'
vid_name_cut = vid_name.strip('_fin.mp4')
vid_anno = vid_path + '/' + vid_name

label_path = clips_folder # put label json file into clips folder
label_file = os.path.join(label_path, vid_name.replace('.mp4', '-labels.json'))

# set up annotator
annotator = Annotator(labels, clips_folder, annotation_file=label_file)

# check if we already generated clips
if [f for f in os.listdir(clips_folder) if not f.startswith('.')] == []:
    # no prior generated clips
    print('Clips folder is empty.')
    # split the main video into 3-second clips
    # note: our video is 30 fps, 30 * 3 = 90 = clip_length
    annotator.video_to_clips(vid_anno, clips_folder, clip_length=90)
else:
    print('Clips folder not empty.')
    for f in os.listdir(clips_folder):
        if not f.startswith(vid_name_cut):
            print('Detected different clip name,', \
                  'please verify your clips folder:\n\n\t{}\n'.format( \
                        clips_folder))
            sys.exit(1)

# run the GUI
annotator.main()
