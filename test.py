from annotator import Annotator

# define the labels
labels = [{'name': 'harvest', 'color': (0, 255, 0)},
          {'name': 'maneuvering', 'color': (0, 0, 255)},
          {'name': 'idling', 'color': (255, 0, 0)}]

# path for the video
video_path = '/home/yang/research/dock/explicator/sample.mp4'

# folder for storing clips
clips_folder = '/home/yang/research/dock/explicator/clips'

# set up annotator
annotator = Annotator(labels, clips_folder, annotation_file='labels.json')

# split the main video into 3-second clips (3s * 30 fps = 90 frames)
annotator.video_to_clips(video_path, clips_folder, \
                         clip_length=90, overlap=0, resize=0.5)
# run the GUI
annotator.main()
