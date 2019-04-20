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
func_letter_settings = {'font_scale': 7, 'font_thickness': 4}

kb_settings['rectangle'] = rec_settings
kb_settings['letter'] = letter_settings
kb_settings['func_letter'] = func_letter_settings

kb_obj = kb(kb_settings)
keyboard = kb_obj.get_background()

letters_rus = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'К', 'Л']
letters_eng = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']

kb_obj.set_letters(rec_settings, letter_settings, letters_eng)
kb_obj.set_adjustable_rectangle_with_text(0, 0, 2, 1, 'Ent')
kb_obj.set_adjustable_rectangle_with_text(6, 0, 2, 1, 'Del')

kb_obj.set_adjustable_rectangle_with_text(0, 5, 2, 1, 'Ent')
kb_obj.set_adjustable_rectangle_with_text(6, 5, 2, 1, 'Del')

kb_obj.show_keyboard()
