import pygame as pg
import sys, random, os

import inc.settings

class TextInput:
    
    color_active = inc.settings.COLOR_ACTIVE
    color_inactive = inc.settings.COLOR_INACTIVE
    color = color_inactive
    text_color = inc.settings.TEXT_COLOR
    text = ''
    active = False
    text_surf = None
    max_width = 15

    def __init__(self, x, y, width, height, font):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect(x, y, width, height)
        self.font = font

        self.render_text()

    def draw(self, screen):
        pg.draw.rect(screen, inc.settings.WHITE, self.rect, border_radius=15)
        pg.draw.rect(screen, self.color, self.rect, width=2, border_radius=15)
        screen.blit(self.txt_surface, (self.rect.x + 10, self.rect.y + (self.height/4)))
             
    def event_handler(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = self.color_active
            else:
                self.active = False
                self.color = self.color_inactive
        elif event.type == pg.KEYUP and self.active:
            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            elif len(self.text) < self.max_width:
                self.text += event.unicode

            self.render_text()

    def render_text(self):
        self.txt_surface = self.font.render(self.text, True, self.text_color)

class Gui:
    def __init__(self):
        pg.init()
        self.dir = os.path.dirname(__file__)
        
        self.icon = pg.image.load(os.path.join(self.dir, 'img', 'cripto.ico'))
        self.screen = pg.display.set_mode((inc.settings.WIDTH, inc.settings.HEIGHT))
        pg.display.set_caption(inc.settings.TITLE)
        pg.display.set_icon(self.icon)

        self.clock = pg.time.Clock()

        self.running = True
        pg.key.set_repeat(10)

        self.font_name = pg.font.match_font(inc.settings.FONT_NAME)

        self.inputs = [TextInput((inc.settings.WIDTH/2) - 100, 100, 200, 30, pg.font.Font(None, 25))]

        self.load_data()

    def load_data(self):
        pass

    def run(self):
        while self.running:
            self.clock.tick(inc.settings.FPS)

            self.input()
            self.update()
            self.draw()

    def input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            for i in self.inputs:
                i.event_handler(event)

    def update(self):  
        pg.display.update()
                   
    def draw(self):
        self.screen.fill(inc.settings.BGCOLOR)

        for i in self.inputs:
            i.draw(self.screen)

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

game = Gui()
game.run()

