import vvclasses
from vvclasses import ColorPrinter

import os

print_dir = (dir(vvclasses))
utils = vvclasses.utils.__file__
name = vvclasses.utils.__name__
package = vvclasses.utils.__package__
path = vvclasses.utils.__path__
utils_dir = dir(vvclasses.utils)
color_printer = vvclasses.utils.ColorPrinter 

list_of_text = [print_dir, utils, name, package, path, utils_dir, color_printer]


blue = ColorPrinter.COLORS['blue']
green = ColorPrinter.COLORS['green']
red = ColorPrinter.COLORS['red']
bold = ColorPrinter.COLORS['bold']
bright_magenta = ColorPrinter.COLORS['bright_magenta']
bright_red = ColorPrinter.COLORS['bright_red']
cyan = ColorPrinter.COLORS['cyan']
bright_blue = ColorPrinter.COLORS['bright_blue']
bright_yellow = ColorPrinter.COLORS['bright_yellow']
bright_cyan = ColorPrinter.COLORS['bright_cyan']

with open("EXAMPLEREADME.md", "r") as f:
    markdown_text_list = f.readlines()

printer_markdown = ColorPrinter(
    print_pattern="markdown",
    color_list=[
        bright_magenta,  # headers
        bright_red,      # bold
        green,           # italics
        cyan,            # inline code
        bright_blue,     # links
        bright_yellow,   # lists
        bright_cyan      # blockquotes
    ],
    text_list=markdown_text_list
)

# printer_markdown.execute_print(text=markdown_text_list)

printer_alternating = ColorPrinter(
    print_pattern="new-line-alternating",
    color_list=[blue, green, red],
    text_list=list_of_text
)

printer_alternating.execute_print()

