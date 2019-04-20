import cv2
import numpy as np
from keyboard.keyboard import KeyboardBasis as kb

#1 rectangle size
x = 150
y = 150
height_ratio = 6
width_ratio = 8
#screen size = (a*b) * height_ratio * width_ratio

kb_settings = {'width': width_ratio * x, 'height': height_ratio * y, 'un': 3}
rec_settings = {'height': y, 'width': x, 'thickness': 3, 'color': (255, 0, 0)}
letter_settings = {'font_scale': 10, 'font_thickness': 4}

kb_settings['rectangle'] = rec_settings
kb_settings['letter'] = letter_settings

kb_obj = kb(kb_settings)
keyboard = kb_obj.get_background()

letters_rus = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'К', 'Л']
letters_eng = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']

def letter(x, y, text):
    # Keys
    width = 200
    height = 200
    th = 3 # thickness
    cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (255, 0, 0), th)

    # Text settings
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 10
    font_th = 4
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((height + height_text) / 2) + y
    cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (255, 0, 0), font_th)


# letter(0, 0, "A")
# letter(200, 0, "B")
# letter(400, 0, "C")
#kb_obj.set_letter_placeholder(rec_settings)

kb_obj.set_letters(rec_settings, letter_settings, letters_eng)
kb_obj.set_adjustable_rectangle(0, 0, 2, 1)
kb_obj.show_keyboard()
