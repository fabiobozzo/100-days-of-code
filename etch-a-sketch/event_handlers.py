def move(_turtle, _step, _direction):
    def _move():
        if _direction == "forward":
            _turtle.forward(_step)
        elif _direction == "backward":
            _turtle.backward(_step)

    return _move


def rotate(_turtle, _step, _direction):
    def _rotate():
        if _direction == "right":
            _turtle.right(_step)
        elif _direction == "left":
            _turtle.left(_step)

    return _rotate
