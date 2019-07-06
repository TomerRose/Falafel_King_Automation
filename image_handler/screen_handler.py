from PIL import ImageGrab,Image
import cv2
import pyautogui


TEMP_IMAGE_NAME = 'CAP.PNG'

class ScreenHandler:
    def __init__(self):
        self.box = None

    def capture(self):
        image = ImageGrab.grab(self.box)
        image.save(TEMP_IMAGE_NAME)

    def find_box_by_color(self, color):
        img_rgb = Image.open(TEMP_IMAGE_NAME)
        pixels = img_rgb.load()
        xlist = []
        ylist = []
        for y in range(img_rgb.size[1]):
            for x in range(img_rgb.size[0]):
                if pixels[x, y] == color:
                    xlist.append(x)
                    ylist.append(y)

        # 4 corners of the black square
        self.box = (min(xlist), min(ylist), max(xlist), max(ylist))


    def click_image_in_capture(self, img_path):
        self.capture()
        method = cv2.TM_SQDIFF_NORMED
        small_image = cv2.imread(img_path)
        large_image = cv2.imread(TEMP_IMAGE_NAME)
        result = cv2.matchTemplate(small_image, large_image, method)
        mnLoc = cv2.minMaxLoc(result)
        _, _, res, _ = mnLoc
        x, y = res
        pyautogui.click(self.box[0] + x, self.box[1] + y)

    def is_image_in_capture(self, img_path, is_fly=False):
        self.capture()
        method = cv2.TM_SQDIFF_NORMED
        small_image = cv2.imread(img_path)
        large_image = cv2.imread(TEMP_IMAGE_NAME)
        result = cv2.matchTemplate(small_image, large_image, method)
        mnLoc = cv2.minMaxLoc(result)
        _, _, res, _ = mnLoc
        print(res)
        if is_fly:
            if res[0] < 500 and res[0] > 150 and res[1] > 350 and res[1] <500:
                return True
            return False
        if result is not None:
            return True
        return False

    def click(self, x, y):
        pyautogui.click(self.box[0] + x, self.box[1] + y)


