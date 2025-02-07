class GameObject:
    def __init__(self, column : int, line : int):
        self.column = column
        self.line = line

    def move_right(self):
        self.column+=1
    
    def move_left(self):
        self.column-=1

    def move_down(self):
        self.line+=4

    def move_up(self):
        self.line-=4

    def is_on_the_right_edge(self):
        if self.column > 96 :
            return True
        
    def is_on_the_left_edge(self):
        if self.column < 1 :
            return True
        
    def is_on_the_up_edge(self):
        if self.line < 0 :
            return True

    def is_on_the_down_edge(self):
        if self.line > 5/3*100 :
            return True


