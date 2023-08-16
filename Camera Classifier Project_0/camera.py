import cv2 as cv

class Camera:

    def __init__(self):

        self.camera = cv.VideoCapture(0)

        if not self.camera.isOpened():
            raise ValueError("Camera could not be Opened! Please Check.")
        
        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)

    
    def __del__(self):

        if self.camera.isOpened():
            self.camera.release()

    
    def get_frame(self):
        if self.camera.isOpened():
            ok, frame = self.camera.read()

            if ok:
                return(ok, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return(ok, None)
        else:
            return None

