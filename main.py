from image_handler.screen_handler import ScreenHandler
import os
import time

my_assets = {'start': 'start_butt.PNG', 'play': 'play_butt.PNG', 'submit': 'submit_butt.PNG', 'fly': 'fly.png'}
for asset in my_assets:
    my_assets[asset]= os.path.join('assets', my_assets[asset])


def main():
    a = ScreenHandler()
    a.capture()
    a.find_box_by_color((102, 204, 255))
    a.click_image_in_capture(my_assets['start'])
    a.click_image_in_capture(my_assets['play'])
    a.click_image_in_capture(my_assets['submit'])
    while True:
        if a.is_image_in_capture(my_assets['fly'], is_fly=True):
            a.click(530, 340)
            print('hiyush')
        time.sleep(1)


if __name__ == '__main__':
    main()
