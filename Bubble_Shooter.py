from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

width, height = 400, 600

score = 0
total_chances = 3
button_width = 30
button_height = 25
circles_missed = 0
game_over = False
paused = False

circle_x = width // 2
circle_speed = 10
circle_radius = 20

new_circle_x, new_circle_y = None, None
new_circle_radius = random.randint(15, 40)
new_circle_speed_y = 10

falling_circles = []
upward_circles = []


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # background
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, width, 0, height)


def reshape(w, h):
    global width, height
    width = w
    height = h
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)


def midpoint_line(x1, y1, x2, y2):
    zone = find_zone(x1, y1, x2, y2)
    x1, y1, x2, y2 = zone0_conv(x1, y1, x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    moveE = 2 * dy
    moveNE = 2 * (dy - dx)
    x, y = x1, y1
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(*actual_zone_conv(x, y, zone))
    while x < x2:
        if d <= 0:
            d += moveE
        else:
            d += moveNE
            y += 1
        x += 1
        glVertex2f(*actual_zone_conv(x, y, zone))
    glEnd()
    glFlush()


def find_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 0  # Zone 0
        elif dx >= 0 > dy:
            return 7  # Zone 7
        elif dx < 0 <= dy:
            return 3  # Zone 3
        else:
            return 4  # Zone 4
    else:
        if dx >= 0 and dy >= 0:
            return 1  # Zone 1
        elif dx >= 0 > dy:
            return 6  # Zone 6
        elif dx < 0 <= dy:
            return 2  # Zone 2
        else:
            return 5  # Zone 5


def zone0_conv(x1, y1, x2, y2, zone):
    if zone == 1:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    elif zone == 2:
        x1, y1 = y1, -x1
        x2, y2 = y2, -x2
    elif zone == 3:
        x1, y1 = -x1, y1
        x2, y2 = -x2, y2
    elif zone == 4:
        x1, y1 = -x1, -y1
        x2, y2 = -x2, -y2
    elif zone == 5:
        x1, y1 = -y1, -x1
        x2, y2 = -y2, -x2
    elif zone == 6:
        x1, y1 = -y1, x1
        x2, y2 = -y2, x2
    elif zone == 7:
        x1, y1 = x1, -y1
        x2, y2 = x2, -y2
    return x1, y1, x2, y2


def actual_zone_conv(x, y, zone):
    if zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y
    return x, y


def draw_buttons_and_boxes():
    global height, width, paused, button_height, button_width
    glColor3f(0.0, 0.0, 0.0)  # Border Colour
    margin = 20

    # Restart button box
    restart_x1 = margin
    restart_y1 = height - margin - button_height
    restart_x2 = restart_x1 + button_width
    restart_y2 = height - margin
    midpoint_line(restart_x1, restart_y1, restart_x2, restart_y1)
    midpoint_line(restart_x2, restart_y1, restart_x2, restart_y2)
    midpoint_line(restart_x2, restart_y2, restart_x1, restart_y2)
    midpoint_line(restart_x1, restart_y2, restart_x1, restart_y1)

    # Restart Button
    glColor3f(0.0, 0.0, 1.0)
    restart_center_x = (restart_x1 + restart_x2) // 2
    restart_center_y = (restart_y1 + restart_y2) // 2
    midpoint_line(restart_center_x - 10, restart_center_y, restart_center_x + 5, restart_center_y + 10)
    midpoint_line(restart_center_x - 10, restart_center_y, restart_center_x + 5, restart_center_y - 10)
    midpoint_line(restart_center_x - 10, restart_center_y, restart_center_x + 15, restart_center_y)

    # Play/Pause button box
    glColor3f(0.0, 0.0, 0.0)
    play_pause_x1 = (width // 2) - (button_width // 2)
    play_pause_y1 = height - margin - button_height
    play_pause_x2 = play_pause_x1 + button_width
    play_pause_y2 = height - margin
    midpoint_line(play_pause_x1, play_pause_y1, play_pause_x2, play_pause_y1)
    midpoint_line(play_pause_x2, play_pause_y1, play_pause_x2, play_pause_y2)
    midpoint_line(play_pause_x2, play_pause_y2, play_pause_x1, play_pause_y2)
    midpoint_line(play_pause_x1, play_pause_y2, play_pause_x1, play_pause_y1)

    # Play/Pause Button
    glColor3f(1.0, 0.65, 0.0)
    play_pause_center_x = (play_pause_x1 + play_pause_x2) // 2
    play_pause_center_y = (play_pause_y1 + play_pause_y2) // 2
    if not paused:
        midpoint_line(play_pause_center_x - 5, play_pause_y1 + 3, play_pause_center_x - 5, play_pause_y2 - 3)
        midpoint_line(play_pause_center_x + 5, play_pause_y1 + 3, play_pause_center_x + 5, play_pause_y2 - 3)
    else:
        midpoint_line(play_pause_center_x - 7, play_pause_y1 + 3, play_pause_center_x + 7, play_pause_center_y)
        midpoint_line(play_pause_center_x + 7, play_pause_center_y, play_pause_center_x - 7, play_pause_y2 - 3)
        midpoint_line(play_pause_center_x - 7, play_pause_y1 + 3, play_pause_center_x - 7, play_pause_y2 - 3)

    # Exit button box
    glColor3f(0.0, 0.0, 0.0)
    exit_x1 = width - margin - button_width
    exit_y1 = height - margin - button_height
    exit_x2 = exit_x1 + button_width
    exit_y2 = height - margin
    midpoint_line(exit_x1, exit_y1, exit_x2, exit_y1)
    midpoint_line(exit_x2, exit_y1, exit_x2, exit_y2)
    midpoint_line(exit_x2, exit_y2, exit_x1, exit_y2)
    midpoint_line(exit_x1, exit_y2, exit_x1, exit_y1)

    # Exit button
    glColor3f(1.0, 0.0, 0.0)
    exit_center_x = (exit_x1 + exit_x2) // 2
    exit_center_y = (exit_y1 + exit_y2) // 2
    midpoint_line(exit_center_x - 10, exit_center_y - 10, exit_center_x + 10, exit_center_y + 10)
    midpoint_line(exit_center_x + 10, exit_center_y - 10, exit_center_x - 10, exit_center_y + 10)


def midpoint_circle_drawing(x_center, y_center, radius, color):
    x = 0
    y = radius
    d = 1 - radius
    draw_circle_points(x_center, y_center, x, y, color)
    while x < y:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
        draw_circle_points(x_center, y_center, x, y, color)


def draw_circle_points(x_center, y_center, x, y, color):
    glColor(color)
    glBegin(GL_POINTS)
    glVertex2f(x_center + x, y_center + y)
    glVertex2f(x_center - x, y_center + y)
    glVertex2f(x_center + x, y_center - y)
    glVertex2f(x_center - x, y_center - y)
    glVertex2f(x_center + y, y_center + x)
    glVertex2f(x_center - y, y_center + x)
    glVertex2f(x_center + y, y_center - x)
    glVertex2f(x_center - y, y_center - x)
    glEnd()


def keyboard(key, x, y):
    global circle_x
    if key == b'A' or key == b'a':
        if circle_x - circle_speed >= 0 + 40:
            circle_x -= circle_speed
    elif key == b'D' or key == b'd':
        if circle_x + circle_speed <= width - 40:
            circle_x += circle_speed
    elif key == b' ':
        upward_circle_maker()

    glutPostRedisplay()  # Redraw the screen


def special_keys(key, x, y):
    global circle_x, circle_speed, width, circle_radius, game_over

    if game_over:
        return

    if key == GLUT_KEY_LEFT:
        if circle_x - circle_speed - circle_radius >= 0:
            circle_x -= circle_speed
    elif key == GLUT_KEY_RIGHT:
        if circle_x + circle_speed + circle_radius <= width:
            circle_x += circle_speed

    glutPostRedisplay()


def upward_circle_movement():
    global upward_circles
    for circle in upward_circles:
        circle['y'] += circle['speed']


def upward_circle_boundary():
    global upward_circles, height, game_over, circles_missed
    for circle in upward_circles:
        if circle['y'] > height - 10:
            upward_circles.remove(circle)
            circles_missed += 1
    if circles_missed >= 3:
        game_over = True


def draw_upward_circles():
    for circle in upward_circles:
        glColor(circle['color'])
        midpoint_circle_drawing(circle['x'], circle['y'], circle['radius'], circle['color'])


def update_new_circle_position():
    global new_circle_x, new_circle_y, new_circle_speed_y

    if new_circle_x is not None and new_circle_y is not None:
        new_circle_y += new_circle_speed_y

        if new_circle_y >= height - 50:
            new_circle_x, new_circle_y = None, None


def falling_circle_maker():
    global falling_circles
    if len(falling_circles) < 10:
        circle = {
            'x': random.randint(30, width - 20),
            'y': height,
            'radius': random.randint(10, 30),
            'speed': random.uniform(.5, 2),
            'color': (random.random(), random.random(), random.random())
        }
        falling_circles.append(circle)


def upward_circle_maker():
    global circle_x, circle_radius
    fixed_radius = 5
    circle = {
        'x': circle_x,
        'y': 50 + circle_radius + fixed_radius,
        'radius': fixed_radius,
        'speed': 3,
        'color': (1, 1, 0)
    }
    upward_circles.append(circle)


def falling_circle_movement():
    global falling_circles, total_chances, game_over, circle_x, circle_radius
    for circle in falling_circles:
        circle['y'] -= circle['speed']

        if detect_collision(circle, {'x': circle_x, 'y': 50, 'radius': circle_radius}):
            print("Falling bubble touched the shooter!")
            game_over = True
            print("GAME OVER")
            return

    new_falling_circles = []
    for circle in falling_circles:
        if circle['y'] - circle['radius'] > 0:
            new_falling_circles.append(circle)
        else:
            total_chances -= 1
            if total_chances == 0:
                print(f"Final Score: {score}")
                print("GAME OVER")
                game_over = True
                return
            else:
                print("Missed!!!")
                print(f"Lives Remaining: {total_chances}")
    falling_circles = new_falling_circles


def draw_falling_circles():
    for circle in falling_circles:
        glColor3f(*circle['color'])
        midpoint_circle_drawing(circle['x'], circle['y'], circle['radius'], circle['color'])  # Draw the circle


def detect_collision(circle1, circle2):
    dist_x = circle1['x'] - circle2['x']
    dist_y = circle1['y'] - circle2['y']
    distance = math.sqrt(dist_x ** 2 + dist_y ** 2)
    if distance <= circle1['radius'] + circle2['radius']:
        return True
    return False


def handle_collisions():
    global upward_circles, falling_circles, score

    for upward_circle in upward_circles[:]:
        for falling_circle in falling_circles[:]:
            if detect_collision(upward_circle, falling_circle):
                upward_circles.remove(upward_circle)
                falling_circles.remove(falling_circle)
                score += 1
                print(f"Score: {score}")
                break


def mouse_click(button, state, x, y):
    global paused, game_over, score, total_chances, falling_circles, upward_circles

    if state == GLUT_DOWN:
        margin = 20
        button_height = 25
        button_width = 30

        y = height - y

        restart_x1 = margin
        restart_y1 = height - margin - button_height
        restart_x2 = restart_x1 + button_width
        restart_y2 = height - margin
        if restart_x1 <= x <= restart_x2 and restart_y1 <= y <= restart_y2:
            print("Restarted!")
            restart_game()

        play_pause_x1 = (width // 2) - (button_width // 2)
        play_pause_y1 = height - margin - button_height
        play_pause_x2 = play_pause_x1 + button_width
        play_pause_y2 = height - margin
        if play_pause_x1 <= x <= play_pause_x2 and play_pause_y1 <= y <= play_pause_y2:
            print("Play/Pause!")
            paused = not paused

        exit_x1 = width - margin - button_width
        exit_y1 = height - margin - button_height
        exit_x2 = exit_x1 + button_width
        exit_y2 = height - margin
        if exit_x1 <= x <= exit_x2 and exit_y1 <= y <= exit_y2:
            print("Exit FROM GAME")
            game_over = True
            glutLeaveMainLoop()


def restart_game():
    global score, total_chances, falling_circles, upward_circles, game_over, paused, circles_missed
    score = 0
    total_chances = 3
    circles_missed = 0
    falling_circles = []
    upward_circles = []
    game_over = False
    paused = False


def update_game_state():
    global game_over, paused
    if not game_over and not paused:
        if random.random() < 0.02:
            falling_circle_maker()
        falling_circle_movement()
        upward_circle_movement()
        handle_collisions()
        upward_circle_boundary()
    elif game_over:
        falling_circles.clear()
        upward_circles.clear()


def draw_game_elements():
    global game_over
    draw_buttons_and_boxes()

    if game_over:
        glColor3f(1, 0, 0)
        midpoint_circle_drawing(circle_x, 50, circle_radius, [1, 0, 0])
    else:
        draw_falling_circles()
        draw_upward_circles()
        midpoint_circle_drawing(circle_x, 50, circle_radius, [1, 1, 0])  # Shooter circle


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    if not game_over:
        draw_game_elements()
    else:
        draw_game_elements()
    glutSwapBuffers()


def timer(value):
    update_game_state()
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Catch the Diamonds")
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutSpecialFunc(special_keys)
glutMouseFunc(mouse_click)
glutTimerFunc(16, timer, 0)
glutMainLoop()
