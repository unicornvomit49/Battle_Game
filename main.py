import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from settings.messages import *

def main(stdscr):
    curses.init_color(1, 200, 75, 200)
    curses.init_color(2, 69, 69, 69)
    curses.init_color(3, 255, 38, 116)
    curses.init_color(4, 16, 210, 117)

    curses.init_pair(1, 1, 2)
    curses.init_pair(2, 3, 4)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)

    g59 = curses.color_pair(1)
    pink_mint = curses.color_pair(2)
    black_white = curses.color_pair(3)
    white_blue = curses.color_pair(4)

    scr_size_y, scr_size_x = stdscr.getmaxyx()

    b1_x1 = 0
    b1_y1 = 0
    b1_x2 = int(scr_size_x * .33)
    b1_y2 = scr_size_y - 1

    b2_x1 = b1_x2 + 1
    b2_y1 = 0
    b2_x2 = int(scr_size_x * .33 + b1_x2)
    b2_y2 = (scr_size_y - 1) // 2

    b3_x1 = b2_x2 + 1
    b3_y1 = 0
    b3_x2 = scr_size_x - 2
    b3_y2 = scr_size_y - 1

    b4_x1 = b1_x2 + 1
    b4_y1 = b2_y2 + 1
    b4_x2 = b2_x2
    b4_y2 = scr_size_y - 1

    b3_display = f'X: {scr_size_x} Y: {scr_size_y}'

    # inv_win = curses.newwin(inv_h, inv_w, inv_y, inv_x)

    # inv_pad = curses.newpad()

    curses.curs_set(False)
    while True:
        stdscr.refresh()
        
        rectangle(stdscr, b1_y1, b1_x1, b1_y2, b1_x2)
        rectangle(stdscr, b2_y1, b2_x1, b2_y2, b2_x2)
        rectangle(stdscr, b3_y1, b3_x1, b3_y2, b3_x2)
        rectangle(stdscr, b4_y1, b4_x1, b4_y2, b4_x2)
        stdscr.addstr(0, (b1_x2//2)-(len(inv_label)//2), inv_label, pink_mint)
        # rectangle(stdscr, 2, 2, 10, 20)
        # rectangle(stdscr, 2, 2, 10, 20)
        stdscr.addstr(scr_size_y//2, (scr_size_x//2)-(len(b3_display)//2), sel_label, black_white)
        
        key = stdscr.getkey()
        if key == 'q':
            break
        if key == 'w':
            pass
        if key == 's':
            pass
        if key == 'a':
            pass
        if key == 'd':
            pass
        stdscr.clear()


if __name__ == '__main__':
    wrapper(main)
