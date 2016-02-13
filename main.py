#!/usr/bin/python
# -*- coding: utf-8 -*-

# import geometry
# import sys
# from PyQt4 import QtGui


# def main():
#
#     app = QtGui.QApplication(sys.argv)
#
#     w = QtGui.QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('Simple')
#     w.show()
#
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
#
# def main():
#     r = float(input("Enter the radius please:"))
#     x = geometry.circle_area(r)
#     print(x)
#     side = float(input("Enter the square side please:"))
#     x = geometry.square_perimeter(side)
#     print(x)
#
# main()


import pygame

pygame.init()

size = (700, 500)
surface = pygame.display.set_mode(size)
pygame.display.set_caption("My game")

end = False
orange = (255, 167, 43)
gold = (250, 237, 50)
blue = (31, 176, 224)

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    surface.fill(orange)
    pygame.draw.circle(surface, gold, [350, 150], 120, 0)
    pygame.draw.rect(surface, blue, [0, 320, 700, 180], 0)
    #   ha le va nyomva akkor menjen is elorre

    #   rajzoljuk ki

    #   takaritsunk
    pygame.display.flip()

pygame.quit()
