import os
import time
import requests
import json
import math
import textwrap


def make_display(columns, lines):
    display = []
    for i in range(lines - 1):
        line = []
        for j in range(columns):
            line.append("-")
        display.append(line)
    return display


def print_display(display: [list]):
    output = ""
    for i in range(len(display)):
        for j in range(len(display[i])):
            output = output + display[i][j]
        output = output + "\n"
    print(output[:-1])


def boxify_string(string: str, length: int, height: int) -> list:
    output = []
    count = 0
    wrapper = textwrap.TextWrapper(width=length)
    dedented_text = textwrap.dedent(text=string)
    original = wrapper.fill(text=dedented_text)
    split_quote = original.split("\n")[:height]
    for i in range(height):
        line = []
        for j in range(length):
            try:
                line.append(split_quote[i][j])
            except:
                line.append(" ")
            count += 1
        output.append(line)
    return output


def place_box(display: [list], box: [list], coordinates: list) -> [list]:
    x_count = 0
    y_count = 0
    for i in range(coordinates[0], coordinates[0] + len(box)):
        for j in range(coordinates[1], coordinates[1] + len(box[0])):
            try:
                display[i][j] = box[y_count][x_count]
                x_count += 1
            except:
                pass
        x_count = 0
        y_count += 1
    return display


while True:
    (columns, lines) = os.get_terminal_size()
    display = make_display(columns, lines)
    quote = json.loads(requests.get("https://bad-guy-quotes.herokuapp.com/").content)[0]
    box_string1 = boxify_string(f"lines:{lines - 1} columms: {8}", 8, lines - 1)
    box_string2 = boxify_string(f"lines:5 columns: {columns -30}", columns -(columns // 5), 5)
    box_string3 = boxify_string(quote, 20, 10)
    box_string4 = boxify_string(f"lines:{lines} columms: {30}", 30, lines)
    display = place_box(display, box_string1, [0, 0])
    display  = place_box(display, box_string2,[lines - 5, 8])
    display = place_box(display, box_string3, [14, 24])
    display = place_box(display, box_string4, [0, columns -30])
    print_display(display)
    time.sleep(3)
