from _nodes.node import Node

class TestNodeClass(Node):
    def __init__(self) -> None:
        super.__init__(self)

    def info(self):

        # TODO
        # Log this
        print("I am a test node")