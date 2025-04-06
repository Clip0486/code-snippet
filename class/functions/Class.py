import os
import cv2
import numpy as np

class templete:
    def __init__(self, input_path):
        print('Instance 초기화')
        self.input_path = input_path

        self.images = []
        if os.path.isfile(input_path):  # 입력이 파일인 경우, 한 장만 처리함
            self.images.append(input_path)
        elif os.path.isdir(input_path):  # 입력이 디렉토리인 경우, 폴더에 있는 파일들 반복하여 한 장씩 처리함
            self.images = self.load_images_from_directory(input_path)
        else:
            raise ValueError("입력 경로가 유효하지 않습니다.")

    def load_images_from_directory(self, directory):  # 입력이 디렉토리라면, 이미지들을 불러옴
        image_files = []
        for filename in os.listdir(directory):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_files.append(directory + '/' + filename)
        return image_files

    def View(self):
        print('\nView')
        for image in self.images:
            image = cv2.imread(image)
            size = image.shape
            resize = cv2.resize(image, (int(0.5 * size[1]), int(0.5 * size[0])))
            cv2.imshow('image', resize)
            key = cv2.waitKey()
            if key == ord('q'):    # q를 누르면 꺼짐
                cv2.destroyAllWindows()
                break

