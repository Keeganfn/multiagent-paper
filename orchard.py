import numpy as np
import pygame_render

default_row = [0, 0, -2, -1, -1, -2, 0, 0, -2, -1, -1, -2, 0,
               0, -2, -1, -1, -2, 0, 0, -2, -1, -1, -2, 0, 0,
               -2, -1, -1, -2, 0, 0]


class OrchardMap():

    def __init__(self, row_height: int = 10, row_description: list = default_row, top_buffer: int = 3,
                 bottom_buffer: int = 2, spawn_length: int = 10) -> None:
        self.row_height = row_height
        self.row_description = row_description
        self.top_buffer = top_buffer
        self.bottom_buffer = bottom_buffer
        self.orchard_map = np.zeros(
            (self.row_height + self.top_buffer + self.bottom_buffer, len(row_description)))
        self.original_map = None

    def create_map(self, agents: list = None) -> None:
        for i in range(self.top_buffer, len(self.orchard_map) - self.bottom_buffer):
            self.orchard_map[i, :] = self.row_description

        self.original_map = np.copy(self.orchard_map)
        start = (len(self.row_description) // 2) - (len(agents) // 2)
        end = start + len(agents)

        for i in range(len(agents)):
            self.orchard_map[0][start + i] = agents[i].type
            agents[i].cur_pose = [0, start + i]

    def get_valid_moves(self, start: list) -> list:
        valid = []
        valid_token = []
        if start[0] < self.row_height + self.top_buffer + self.bottom_buffer - 1:
            valid.append([start[0]+1, start[1]])
            valid_token.append(self.orchard_map[start[0]+1, start[1]])
        if start[0] > 0:
            valid.append([start[0]-1, start[1]])
            valid_token.append(self.orchard_map[start[0]-1, start[1]])
        if start[1] < len(self.row_description)-1:
            valid.append([start[0], start[1]+1])
            valid_token.append(self.orchard_map[start[0], start[1]+1])
        if start[1] > 0:
            valid.append([start[0], start[1]-1])
            valid_token.append(self.orchard_map[start[0], start[1]-1])
        final = []
        for i in range(len(valid)):
            if valid_token[i] == 0 or valid_token[i] == -2:
                final.append(valid[i])
        return final

    def update_map(self, start: list, goal: list, agent) -> None:
        self.orchard_map[start[0]][start[1]
                                   ] = self.original_map[start[0]][start[1]]
        self.orchard_map[goal[0]][goal[1]] = agent.type


class Agenttest():
    def __init__(self) -> None:
        self.type = 3
        self.cur_pos = [0, 0]

    def random_move(self, valid_moves):
        choice = np.random.randint(len(valid_moves))
        return valid_moves[choice]


class OrchardSim():

    def __init__(self, orchard_map: OrchardMap = OrchardMap(), agents: list = None) -> None:
        self.map = orchard_map
        self.agents = agents
        self.map.create_map(self.agents)
        self.render = pygame_render.PygameRender(self.map)

    def run_gui(self):
        self.render.start(self.agents)


l = []
for i in range(10):
    l.append(Agenttest())

test = OrchardSim(agents=l)
test.run_gui()


#j = pygame_render.PygameRender(t.orchard_map)
# j.start()
