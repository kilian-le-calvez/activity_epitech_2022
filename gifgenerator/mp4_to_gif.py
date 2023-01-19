from email.mime import base
import cv2
import os
import random
import shutil
import glob
from PIL import Image

time_duration_gif = 3

class Decoupeur:
    def __init__(self, path):
        self.dirName = "tmp"
        self.path = path
        self.fps = 30
        self.duration = 1.5
        self.status = "Success"
        self.videoImages = []
        try:
            print(self.path)
            self.video = cv2.VideoCapture(self.path)
            self.maxFrames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
            self.biggestStartFrame = self.maxFrames - self.fps * self.duration
        except:
            self.status = "Error"
    
    def setFPS(self):
        self.fps = self.video.get(cv2.CAP_PROP_FPS)

    def setDuration(self, duration):
        self.duration = duration
    
    def loadVideo(self):
        frame = 0
        while frame < self.maxFrames:
            reading, image = self.video.read()
            self.videoImages.append(image)
            frame += 1
            # print("Reading video ", frame / self.maxFrames * 100, " %")
    
    def createImages(self):
        if os.path.exists(self.dirName):
            shutil.rmtree(self.dirName)
        os.mkdir(self.dirName)
        startFrame = random.randint(0, self.biggestStartFrame)
        frame = startFrame
        while frame < startFrame + self.duration * self.fps and frame < self.maxFrames:
            image = self.videoImages[frame]
            cv2.imwrite(f"{self.dirName}/frame_{frame:03d}.jpg", image)
            frame += 1
            print("Saving usefull images ", frame / (startFrame + self.duration * self.fps) * 100, " %")

    def make_gif(self, name):
        images = glob.glob(f"{self.dirName}/*.jpg")
        images.sort()
        frames = [Image.open(image) for image in images]
        frame_one = frames[0]
        baseName = name
        nb = 1
        while os.path.exists("gifs/" + name + ".gif"):
            name = baseName + "" + str(nb)
            nb += 1
        frame_one.save("gifs/" + name + ".gif", format="GIF", append_images=frames, save_all=True, duration=50, loop=0)
        return "gifs/" + name + ".gif"

if __name__ == "__main__":
    decoupeur = Decoupeur("/Users/kilianlecalvez/code/gifgenerator/vegeta.mp4")
    decoupeur.__init__("vegeta.mp4")
    if decoupeur.status != "Success":
        print("Can't load this video !")
        exit(84)
    decoupeur.loadVideo()
    for i in range(0, 70):
        decoupeur.createImages()
        decoupeur.make_gif("mygif")
# Regarder pour ne devoir que read une portion de la video