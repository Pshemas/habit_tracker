def convert_color(R,G,B): # Convert RGB888 to RGB565
    return (((G&0b00011100)<<3) +((B&0b11111000)>>3)<<8) + (R&0b11111000)+((G&0b11100000)>>5)

WIDTH = 160
HEIGHT = 80

RED = 0x00F8
GREEN = 0xE007
BLUE = 0x1F00
WHITE = 0xFFFF
BLACK = 0x0000

lightgrey = convert_color(238,238,238)

blue1 = convert_color(213, 234, 255)
blue2 = convert_color(128,192,255)
blue3 = convert_color(43, 149, 255)
blue4 = convert_color(0, 96, 191)

green1 = convert_color(214,230,133)
green2 = convert_color(140,198,101)
green3 = convert_color(68,163,64)
green4 = convert_color(30,104,35)

purple1 = convert_color(224,189,231)
purple2 = convert_color(170,69,187)
purple3 = convert_color(116, 48, 128)
purple4 = convert_color(69, 34, 87)

yellow1 = convert_color(255,244,156)
yellow2 = convert_color(255,231,51)
yellow3 = convert_color(227,191,38)
yellow4 = convert_color(184,140,57)

scarlet1 = convert_color(255,199,221)
scarlet2 = convert_color(239,97,145)
scarlet3 = convert_color(233,29,98)
scarlet4 = convert_color(136,13,78)