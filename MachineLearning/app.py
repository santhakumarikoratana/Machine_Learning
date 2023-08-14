from flask import Flask, render_template, request, session
import cv2
import pickle
import cvzone
import numpy as np
import ibm_db
import re
@app.route('/')
def project():
    return render_template('index.html')
    @app.route('/hero')
    def home():
        return render_template('index.html')
        @app.route('/model')
        def model():
            return render_template('model.html')
            @app.route('/predict_live')
            def liv_pred():
                # Video feed
                cap = cv2.VideoCapture('carParking Input.mp4')
                with open('parkingSlotPosition', 'rb') as f:
                    poslist=pickle.load(f)
                    width, height = 107, 48
                    def checkParkingSpace(imgPro):
                        spaceCounter = 0
                        for pos in posList:
                            x, y = pos
                            imgCrop=imgPro[y:y + height, x:x + width]
                            #cv2.imshow(str(x * y), imgCrop)
                            count = cv2.countNonZero (imgCrop)
                            if count < 900:
                                color= (0, 255, 0)
                                thickness= 5
                                spaceCounter += 1
                            else:
                                color= (0, 0, 255)
                                thickness = 2
                                cv2.rectangle(img, pos, (pos[0] + width, pos [1] + height), color, thickness)
                                cvzone.putTextRect(img, f'Free: (spaceCounter)/{Len(posList)}'(100, 50), scale=3,thickness=5, offset=20, colorR=(0, 200, 0))
                            while True:
                                if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT): 
                                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                                    Success, img = cap.read()
                                    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                                    imgBlur = cv2.GaussianBlur (imgGray, (3, 3), 1)
                                    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    Cv2.THRESH_BINARY_INV, 25, 16)
                                    imgMedian = cv2.medianBlur (imgThreshold, 5)
                                    kernel = np.ones((3, 3), np. uint8)
                                    imgDilate =cv2.dilate(imgMedian, kernel, iterations=1) = checkParkingSpace (imgDilate)
                                    cv2.imshow("Image", img)
                                    #cv2.imshow("ImageBlur", imgBlur)
                                    # cv2.imshow("Image Thres", imgMedian)
                                    if cv2.waitKey(1) & 0xFF == ord('q'):
                                        break

