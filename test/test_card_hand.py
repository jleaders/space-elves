from app import *

from controllers import *
from views import *
import global_mod as g

class TestSceneGraph (SceneGraph):

    def __init__(self):
        self.root = None

    def initControllers(self):

        g.image_manager.card_back = "data/img/card_back.jpg"
        g.image_manager.card_front = "data/img/card_front.jpg"
        g.image_manager.card_slot = "data/img/card_slot.png"
        g.image_manager.board_back   = "data/img/board_background.png"

        c = GameController()

        # Code for the board controller
        bc = BoardController()
        c.board = bc
        c.view.addChild(bc.view)

        # Code for the player controller
        pc = PlayerController()
        c.players.append(pc)
        c.view.addChild(pc.view)

        # Code for the hand controller
        hand = HandController(visible=True)
        hand.view.position = Position(100,0)
        hand.view.size = Dimensions(800, 270)
        pc.hand = hand
        pc.view.addChild(hand.view)

        # Code for the cards
        for i in range(3):
            card = CardController(playerId=0)
            hand.addCard(card)

        # Code for the lane controller
        lane = LaneController(4)
        lane.view.position = Position(50, 270)
        lane.view.size = Dimensions(200, 400)
        c.view.addChild(lane.view)


        bc.lanes.append(lane)
        bc.view.addChild(lane.view)

        button = ButtonController(Position(300,300),
                                  Dimensions(150,50),
                                  "Test")

        bc.view.addChild(button.view)



        #cardSlotController = CardSlotController()
        #gameController.view.children.append(cardSlotController.view)
        #cardSlotController.view.position = Position(300,100)

        self.root = c.view


app = App(sceneGraphClass=TestSceneGraph)
app.run()