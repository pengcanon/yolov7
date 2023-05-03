import matplotlib.pyplot as plt
import numpy as np
import cv2
import json
import math

def Video_from_webcam(filename, fr=30): #save a video from webcam at frame rate fr
    cap = cv2.VideoCapture(0)
    success, image = cap.read()

    if success:
        height, width, _ = image.shape
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        video = cv2.VideoWriter(filename, 0, fr, (width, height))   
    else:
        print("Unable to access webcam")
        return None
    
    savevideo = False
    run_func = False
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if savevideo:
            video.write(image)
        cv2.imshow('Demo', image)
        key=cv2.waitKey(5)
        if key & 0xFF == 27:
            break
        if key & 0xFF == ord('s'):
            savevideo = not savevideo
            print(f'saving video...')
    cap.release()
    video.release()
    cv2.destroyAllWindows()
    print(f"video saved successfully")

def Loadframes_video(filename, fr = 0.033): #save a video from webcam at frame rate fr
    cap = cv2.VideoCapture(filename)
    
    success = True
    sec = 0.0
    frames =[]
    while success:
        sec += fr
        sec = round(sec, 2)
        cap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        success, image = cap.read()
        if success:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            frames.append(image)
    return frames

def save_video_from_frames(filename, frames, fr = 30):
    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    video = cv2.VideoWriter(filename, 0, fr, (width, height))   
    
    for frame in frames:
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) 
        video.write(frame)
    video.release()
    print(f'video saved successfully')