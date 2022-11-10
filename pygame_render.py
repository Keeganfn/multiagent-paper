import pygame
import numpy as np
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class PygameRender():
    def __init__(self, orchard_map) -> None:
        self.map = orchard_map
        self.x_dim = np.shape(self.map.orchard_map)[0]
        self.y_dim = np.shape(self.map.orchard_map)[1]
        self.margin = 2
        self.width = 20
        self.height = 20
        self.window_size = [(self.width * self.y_dim) + (self.y_dim * self.margin),
                            (self.height * self.x_dim) + (self.x_dim * self.margin)]
        pygame.init()
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("ORCHARD")

    def start(self, agents):
        done = False
        clock = pygame.time.Clock()
        while not done:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (self.width + self.margin)
                    row = pos[1] // (self.height + self.margin)
                    # Set that location to one
                    self.map.orchard_map[row][column] = 5
                    print("Click ", pos, "Grid coordinates: ", row, column)

            for i in agents:
                valid_moves = self.map.get_valid_moves(i.cur_pose)
                move = i.random_move(valid_moves)
                self.map.update_map(i.cur_pose, move, i)
                i.cur_pose = move
            # valid_moves = self.map.get_valid_moves(agents[0].cur_pose)
            # move = agents[0].random_move(valid_moves)
            # self.map.update_map(agents[0].cur_pose, move, agents[0])
            # agents[0].cur_pose = move

            self.draw_grid()
            time.sleep(.1)

            pygame.display.update()
        pygame.quit()

    def draw_grid(self):
        self.screen.fill(BLACK)
        # Draw the grid
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                if self.map.orchard_map[i][j] == -1:
                    color = GREEN
                if self.map.orchard_map[i][j] == -2:
                    color = RED
                if self.map.orchard_map[i][j] == 3:
                    color = BLUE
                if self.map.orchard_map[i][j] == 0:
                    color = WHITE
                if self.map.orchard_map[i][j] == 5:
                    color = BLACK
                pygame.draw.rect(self.screen,
                                 color,
                                 [(self.margin + self.width) * j + self.margin,
                                     (self.margin + self.height) *
                                     i + self.margin,
                                     self.width,
                                     self.height])


# # This sets the WIDTH and HEIGHT of each grid location

# # This sets the margin between each cell
# # Create a 2 dimensional array. A two dimensional
# # array is simply a list of lists.
# grid = []
# for row in range(10):
#     # Add an empty array that will hold each cell
#     # in this row
#     grid.append([])
#     for column in range(10):
#         grid[row].append(0)  # Append a cell

# # Set row 1, cell 5 to one. (Remember rows and
# # column numbers start at zero.)
# grid[1][5] = 1

# # Initialize pygame
# pygame.init()

# # Set the HEIGHT and WIDTH of the screen
# WINDOW_SIZE = [510, 510]
# screen = pygame.display.set_mode(WINDOW_SIZE)

# # Set title of screen
# pygame.display.set_caption("Array Backed Grid")

# # Loop until the user clicks the close button.
# done = False

# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()

# # -------- Main Program Loop -----------
# while not done:
#     for event in pygame.event.get():  # User did something
#         if event.type == pygame.QUIT:  # If user clicked close
#             done = True  # Flag that we are done so we exit this loop
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # User clicks the mouse. Get the position
#             pos = pygame.mouse.get_pos()
#             # Change the x/y screen coordinates to grid coordinates
#             column = pos[0] // (WIDTH + MARGIN)
#             row = pos[1] // (HEIGHT + MARGIN)
#             # Set that location to one
#             grid[row][column] = 1
#             print("Click ", pos, "Grid coordinates: ", row, column)

#     # Set the screen background
#     screen.fill(BLACK)

#     # Draw the grid
#     for row in range(10):
#         for column in range(10):
#             color = WHITE
#             if grid[row][column] == 1:
#                 color = GREEN
#             pygame.draw.rect(screen,
#                              color,
#                              [(MARGIN + WIDTH) * column + MARGIN,
#                               (MARGIN + HEIGHT) * row + MARGIN,
#                               WIDTH,
#                               HEIGHT])

#     # Limit to 60 frames per second
#     clock.tick(60)

#     # Go ahead and update the screen with what we've drawn.
#     pygame.display.update()

# # Be IDLE friendly. If you forget this line, the program will 'hang'
# # on exit.
# pygame.quit()
