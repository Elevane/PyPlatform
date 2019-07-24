
# GAME OPTIONS
TITLE = "Jumpy!"
WIDTH = 480
HEIGHT = 600
FPS = 60

# PLAYER PROPERTIES
PLAYER_ACC = 0.8 # more u put more acc u get
PLAYER_FRICTION = -0.12 # less is more friction
PLAYER_GRAVITY = 0.8 # less is  more Gravity
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 40

# PLATFORMS SETTINGS
# platform list : x , y , width, height
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

# COLORS
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)