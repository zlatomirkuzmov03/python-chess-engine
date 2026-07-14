from color import Color


class Theme:

    def __init__(self, light_bg, dark_bg,
                 light_trace, dark_trace,
                 light_moves, dark_moves):

        self.bg = Color(light_bg, dark_bg)
        self.trace = Color(light_trace, dark_trace)
        self.moves = Color(light_moves, dark_moves)

    def update_colors(self, light_bg, dark_bg,
                      light_trace, dark_trace,
                      light_moves, dark_moves):
        
        self.bg.light = light_bg
        self.bg.dark = dark_bg
        self.trace.light = light_trace
        self.trace.dark = dark_trace
        self.moves.light = light_moves
        self.moves.dark = dark_moves
