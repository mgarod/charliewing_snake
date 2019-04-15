from math import sqrt
from random import choice, randint
from time import sleep


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "{}({}, {})".format(type(self), self.x, self.y)


class Apple(Point):
    def __init__(self, w, h):
        self.x = randint(0, w-1)
        self.y = randint(0, h-1)

    def display(self, display):
        display.pixel(self.x, self.y, 150)


class Snake:
    def __init__(self):
        self._snake = [Point(4,4), Point(5,4), Point(6,4), Point(7,4)]

    @property
    def head(self):
        self._head = self._snake[-1]
        return self._head
    
    def __contains__(self, point):
        return point in self._snake

    def __iter__(self):
        return iter(self._snake)

    def __len__(self):
        return len(self._snake)

    def display(self, display):
        for i, point in enumerate(self._snake):
            if point == self.head:
                display.pixel(point.x, point.y, 150)
            else:
                display.pixel(point.x, point.y, 10)

    def clear(self, display):
        for i, point in enumerate(self._snake):
            display.pixel(point.x, point.y, 0)

    def flash(self, times, display):
        for x in range(times):
            self.clear(display)
            sleep(0.4)
            self.display(display)
            sleep(0.4)

    def move(self, point, display):
        # Dim the current head
        display.pixel(self._head.x, self._head.y, 10)
        # Add and brighten the new head
        self._snake.append(point)
        display.pixel(point.x, point.y, 150)
        # Remove and dim the tail
        tail_bit = self._snake.pop(0)
        display.pixel(tail_bit.x, tail_bit.y, 0)

    def eat_move(self, apple, display):
        # Dim the current head to 10
        head = self.head
        display.pixel(head.x, head.y, 10)
        # Add the apple to be the new head
        self._snake.append(apple)
        # Apple is already brightened, no need to do more

    def calc_dist(self, move, apple):
        # Turns will be stairstepped, as diagonal as possible
        def euclid_dist(p1, p2):
            return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

        # Turns will be very wide, always moving along perimiter of rectangles
        def manhattan_dist(p1, p2):
            return abs(p1.x - p2.x) + abs(p1.y - p2.y)

        return euclid_dist(move, apple)

    def get_possible_moves(self, display):
        x, y = self.head.x, self.head.y
        # list.index() causes bias: Right > Down > Left > Up
        all_possible = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
        return [
            Point(x, y) for x, y in all_possible
            if 0 <= x < display.width
            and 0 <= y < display.height
            and Point(x, y) not in self._snake
        ]

    def get_best_move(self, possible_moves, apple):
        distances = [self.calc_dist(move, apple) for move in possible_moves]
        min_dist = min(distances)
        index_of_min_dist = distances.index(min_dist)

        return possible_moves[index_of_min_dist]

    def advance_snake(self, apple, display):
        possible_moves = self.get_possible_moves(display)
        if len(possible_moves) == 0:
            raise DeadSnakeException("Snake is blocked in!")
        
        best_move = self.get_best_move(possible_moves, apple)
        if apple == best_move:
            self.eat_move(apple, display)
            return 1
        else:
            self.move(best_move, display)
            return 0


def create_apple(snake, display):
    ''' Creates an apple which is ensured to be placed on an empty space '''
    apple = Apple(display.width, display.height)
    while apple in snake:
        apple = Apple(display.width, display.height)
    return apple


def sleep_duration(snake):
    ''' Sleep time decreases as snake grows longer '''
    return 4.0 / float(len(snake))


class DeadSnakeException(Exception):
    pass


def play_game(display):
    snake = Snake()
    apple = create_apple(snake, display)
    apple.display(display)
    snake.display(display)
    try:  # Play Snake
        while 1:
            if snake.advance_snake(apple, display):
                apple = create_apple(snake, display)
                apple.display(display)
            sleep(sleep_duration(snake))
    except DeadSnakeException as dse:
        print(dse)
        snake.flash(8, display)
        display.fill(0)
        sleep(1)
    return


if __name__ == '__main__':
    while 1:
        play_game(display)
