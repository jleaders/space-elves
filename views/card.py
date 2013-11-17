""" Includes all code for handling and drawing cards
"""

from sprite import *
from animation import *
import global_mod as g
from util.math import *

class CardView (SpriteView):

    def __init__(self, pos):
        super(CardView, self).__init__( pygame.Rect(pos.x, pos.y, 200, 270) )

        self.visible = False
        self.inSlot = False
        self.status = STATIC
        self.effects = {
            "hover" : False,
            "highlight" : False,
            "Disabled" : False,
        }

        self.listening = True
        self.grabbed = False
        self.grabbedPos = Position(0,0)

    def draw(self):

        rect = self.getAbsoluteRect()

        if self.inSlot:
            g.screen.blit(g.image_manager.card_slot, rect)
        elif self.visible:
            g.screen.blit(g.image_manager.card_front, rect)
        elif self.grabbed:
            newPos = Position(*pygame.mouse.get_pos())
            r = rect
            r = r.move(newPos.x - self.grabbedPos.x,
                       newPos.y - self.grabbedPos.y)
            g.screen.blit(g.image_manager.card_front, r)
        else:
            g.screen.blit(g.image_manager.card_back, rect)

        super(CardView, self).draw()