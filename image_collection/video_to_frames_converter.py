import os
import cv2


class VideoToFramesConverter:
    def __init__(self, video_path):
        self.video_path = video_path

    def extract_frames(self, output_path, filename_prefix='frame'):
        """
        Convert the video into individual frames and save them as images.
        
        Args:
        output_path (str): The path where the frames will be saved.
        filename_prefix (str): The prefix of the filename for each frame. Default is 'frame'.
        """
        # Load the video
        video = cv2.VideoCapture(self.video_path)

        # Extract the frames
        counter = 0
        while True:
            # Capture the frame
            ret, frame = video.read()

            # Break the loop if the video has ended
            if not ret:
                break

            # Save the frame as an image
            filename = f"{output_path}/{filename_prefix}{counter}.jpg"
            cv2.imwrite(filename, frame)
            counter += 1

        # Release the video capture
        video.release()




# video = 'tasmanian_tiger/tasmanian_tiger_video.mp4'
# output = 'frames/'

# captures = VideoToFramesConverter(video) 
# captures.extract_frames(output)