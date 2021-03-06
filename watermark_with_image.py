import numpy as np
import cv2
import os
from utils import CFEVideoConf, image_resize

cap = cv2.VideoCapture(0)

save_path = 'saved-media/watermark.mp4'
frames_per_seconds = 24
config = CFEVideoConf(cap, filepath=save_path, res='720p') 
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)

user_name = os.getenv("USERNAME")
if user_name == 'Maciek':
	img_path = "C:\\Users\\Maciek\\projects\\Praca-magisterska\\images\\watka.png"
else:
	img_path = "C:\\Users\\ADMIN\\projects\\Praca-magisterska\\images\\watka.png"

logo = cv2.imread(img_path, -1)
watermark = image_resize(logo, height=100)
watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)

while(True):
	ret, frame = cap.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
	frame_h, frame_w, frame_s = frame.shape
	overlay = np.zeros((frame_h, frame_w, 4), dtype='uint8')
	watermark_h, watermark_w, watermark_c = watermark.shape
	for i in range(0, watermark_h):
		for j in range(0, watermark_w):
			if watermark[i,j][3] != 0:
				offset = 10
				h_offset = frame_h - watermark_h - offset
				w_offset = frame_w - watermark_w - offset
				overlay[h_offset + i, w_offset + j] = watermark[i,j]

	cv2.addWeighted(overlay, 0.5, frame, 1.0, 0, frame)

	frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
	out.write(frame)
	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()