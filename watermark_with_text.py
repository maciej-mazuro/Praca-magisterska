import cv2
from utils import CFEVideoConf

cap = cv2.VideoCapture(0)

save_path = 'saved-media/watermark_text.mp4'
frames_per_seconds = 24 # taka wartosc moze nie dzialac
config = CFEVideoConf(cap, filepath=save_path, res='720p')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)

while(True):

	ret, frame = cap.read()
	out.write(frame)
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame, 'Hello world', (50,50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
	cv2.imshow('video', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()