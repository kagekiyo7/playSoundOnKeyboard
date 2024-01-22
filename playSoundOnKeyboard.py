# -*- coding: utf-8 -*-
import os
import json
import keyboard
import pygame

def init():
    pygame.mixer.init()
    global seList
    seList = {}
    with open(os.path.join(os.path.dirname(__file__), "seList.json")) as file:
        seListJson = json.load(file)
    for key, seName in seListJson.items():
        if seName:
            seList[key] = {
                "name": seName,
                "file": pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "SE", seName))
            }
    print("Preparation is complete. The following files are defined.:")
    for key, se in seList.items():
        print(f"key: {key},\tfileName: {se['name']}")

def main():
    while True:
        if (keyboard.read_event().event_type != keyboard.KEY_DOWN):
            continue
        for key, se in seList.items():
            if (keyboard.is_pressed(key)):
                se["file"].play(0)

if __name__ == "__main__":
    init()
    main()
