import cv2
import threading

cam = cv2.VideoCapture(0)

def getFrame(name):
	while True:
		ok, frame = cam.read()
		if ok:
			cv2.imshow(name, frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

# getFrame("1")
# thread1 = threading.Thread(target=getFrame, args=("1", ), daemon=True)
thread2 = threading.Thread(target=getFrame, args=("2", ), daemon=True)
thread3 = threading.Thread(target=getFrame, args=("3", ), daemon=True)
thread4 = threading.Thread(target=getFrame, args=("4", ), daemon=True)

# thread1.start()
thread2.start()
thread3.start()
thread4.start()
# getFrame("1")
# thread1.join()
thread2.join()
thread3.join()
thread4.join()
getFrame("1")
