import os
import cv2
import face_recognition
from tkinter import *


def Register():
    print("*work in progress*")

def Login():
    KNOWN_FACES_DIR = "./known_faces"
    # UNKNOWN_FACES_DIR = "unknown_faces"
    TOLERANCE = 0.6
    FRAME_THIKNESS = 3
    FONT_THIKNESS = 2
    MODEL = "cnn"  # hog
    video = cv2.VideoCapture(0)

    print("loading known faces")

    known_faces = []
    known_names = []

    for name in os.listdir(KNOWN_FACES_DIR):
        for filename in os.listdir(KNOWN_FACES_DIR):
            image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{filename}")
            encoding = face_recognition.face_encodings(image)[0]
            known_faces.append(encoding)
            known_names.append(name)

    print("procesing unknown faces")
    while True:
        # print(filename)
        # image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
        ret, image = video.read()

        rgb_image = image[:, :, ::-1]

        locations = face_recognition.face_locations(rgb_image)
        encodings = face_recognition.face_encodings(rgb_image, locations)
        # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            match = None
            if True in results:
                match = known_names[results.index(True)]
                print(f"match found: {match}")

                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])
                color = [0, 255, 0]
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THIKNESS)

                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2] + 22)
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 0, 0), FONT_THIKNESS)

        cv2.imshow('filename', image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        # cv2.waitKey(20000)
        # cv2.destroyWindow(filename)


def starting_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Inicio de sesion")
    Label(screen, text = "Inicio de sesion", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack
    Button(text="Login", height="2", width = "30", command =Login).pack()
    Label(text="").pack
    Button(text="Register", height="2", width="30", command=Register).pack()

    screen.mainloop()
starting_screen()


