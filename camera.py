
import cv2



vid = cv2.VideoCapture(1)

while(True):
    
    
    ret, frame = vid.read()

    
    cv2.imshow('20230001', frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()
