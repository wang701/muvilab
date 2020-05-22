import os
import sys

from annotator import Annotator

# define the labels
labels = [{'name': 'button press', 'color': (255, 0, 0)}, # R
          {'name': 'no action', 'color': (0, 255, 0)}] # G
#          {'name': 'transition', 'color': (0, 0, 255)}] # B

# cam type
cam_type = 'op'

# video datetime
vid_dt = '2019-07-15_19-16-10'

# folder for storing clips
clips_folder = '/home/yang/research/dock/explicator/videos-test/tri-cam-label/' \
               + cam_type + '_' + vid_dt

# define video path
vid_path = '/home/yang/research/dock/explicator/videos-test/tri-cam' \

# define video for labeling
vid_name = cam_type + '_' + vid_dt + '_fin.mp4'
vid_name_cut = vid_name.strip('_fin.mp4')
vid_anno = vid_path + '/' + vid_name

# put label json file into clips folder
label_path = clips_folder
label_file = os.path.join(label_path, vid_name.replace('.mp4', '-labels.json'))

# set up annotator
annotator = Annotator(labels, clips_folder, \
                      annotation_file=label_file, \
                      N_show_approx=20)

# check if we already generated clips
if [f for f in os.listdir(clips_folder) if not f.startswith('.')] == []:
    # no prior generated clips
    print('Clips folder is empty.')
    # split the main video into 3-second clips
    # note: our video is 10 fps, 10 * 3 = 30 = clip_length
    annotator.video_to_clips(vid_anno, clips_folder, clip_length=30)
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
