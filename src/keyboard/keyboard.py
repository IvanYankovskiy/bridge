import cv2
import numpy as np


class KeyboardBasis(object):
    def __init__(self, parameters):
        self.width = parameters['width']
        self.height = parameters['height']
        self.un = parameters['un']
        self.keyboard_background = np.zeros((self.height, self.width, self.un), np.uint8)

        self.letter_rectangle_settings = parameters.get('rectangle')
        self.letter_settings = parameters.get('letter')

    def get_background(self):
        return self.keyboard_background

    def show_keyboard(self):
        self.farme = cv2.imshow("keyboard", self.keyboard_background)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def set_letter_placeholder(self, parameters):
        for order in range(7):
            rectangle = TrueRectangle(parameters)
            rel_y = int(self.height / 2) - rectangle.height
            rel_x = order * rectangle.width
            rectangle.show_rectangle(self.get_background(), rel_x, rel_y)

    def set_letters(self, ph_parameters, letter_parameters, letters):
        max_inline_rectangle_num = self.width // ph_parameters.get('width')
        max_lines_num = 2
        letter_counter = 0
        for line_order in range(max_lines_num):
            for order in range(max_inline_rectangle_num):
                rectangle = TrueRectangle(ph_parameters)

                rel_y = int(self.height / 2) - rectangle.height + rectangle.height * line_order
                rel_x = order * rectangle.width
                rectangle.show_rectangle(self.get_background(), rel_x, rel_y)

                letter = Letter(letters[letter_counter], letter_parameters)
                letter.show_letter(self.get_background(), rectangle, rel_x, rel_y)
                letter_counter += 1

    def set_adjustable_rectangle(self, column, row, column_size, row_size):
        a_rect = AdjustableRectangle(column, row, column_size, row_size, self.letter_rectangle_settings)
        a_rect.show_rectangle(self.get_background())


class Rectangle(object):
    def __init__(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y, letter):
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.bottom_right_x = bottom_right_x
        self.bottom_right_y = bottom_right_y
        self.text = letter


class TrueRectangle(object):
    def __init__(self, parameters):
        self.width = parameters.get('width')
        self.height = parameters.get('height')
        self.th = parameters.get('thickness')
        self.color = parameters.get('color')

    def show_rectangle(self, source, rel_x0, rel_y0):
        cv2.rectangle(source,
                      (rel_x0 + self.th, rel_y0 + self.th),
                      (rel_x0 + self.width - self.th, rel_y0 + self.height - self.th),
                      (255, 0, 0),
                      self.th)


class Letter(object):
    def __init__(self, text, parameters):
        self.text = text
        self.font_letter = cv2.FONT_HERSHEY_PLAIN
        self.font_scale = parameters.get('font_scale')
        self.font_thickness = parameters.get('font_thickness')
        self.text_size = cv2.getTextSize(self.text, self.font_letter, self.font_scale, self.font_thickness)[0]
        self.width_text = self.text_size[0]
        self.height_text = self.text_size[1]

    def show_letter(self, source, placeholder, rel_x, rel_y):
        text_x = int((placeholder.width - self.width_text) / 2) + rel_x
        text_y = int((placeholder.height + self.height_text) / 2) + rel_y
        cv2.putText(source, self.text, (text_x, text_y), self.font_letter, self.font_scale, (255, 0, 0), self.font_thickness)


class AdjustableRectangle(object):
    def __init__(self, column, row, column_size, row_size, parameters):
        self.height = parameters['height']
        self.width = parameters['width']
        self.th = parameters['thickness']
        self.color = parameters['color']

        self.x0 = column * self.width + self.th
        self.y0 = row * self.height + self.th
        self.x = self.x0 + self.width * column_size - self.th
        self.y = self.y0 + self.height * row_size - self.th

    def show_rectangle(self, source):
        cv2.rectangle(source,
                      (self.x0, self.y0),
                      (self.x, self.y),
                      self.color,
                      self.th)
