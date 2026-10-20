# Author: Mbiaya Andy Lee Franck
from __future__ import annotations
import pygame
import math
import os
import time
#os.chdir(r"C:\Users\andym\OneDrive\Bureau\Python\NSI_Classe\Python_classe\Introduction aux bases python\Les classes")
pygame.init()

# Phase I : Initialization

# 1. Creating the class that I will need: Projectile and button

class Projectile:
    def __init__(self, x_0, y_0, speed, angle, frame: dict, other: dict,image:str):
        self.x = x_0
        self.y = y_0
        self.speed = speed
        self.speed_x, self.speed_y = speed_x_y(speed, angle)
        self.speed_y *= -1
        self.rotation = math.atan2(self.speed_y, self.speed_x)
        self.aero = ((-1/2)*1.225*other["drag_coef"]
                     * other["Frontal area"])/other["mass"]# comes from the formula to calulate the aerodynamic drag froce : F = 1/2*air density*drag_coef*Frontal area*speed^2/mass
        self.original = (x_0,
                         y_0, 
                         speed_x_y(speed, angle)[
                         0], 
                         -1*speed_x_y(speed, angle)[1])#We keep a copy of the original speeds and coordinates to reset if it crosses the frame's borders
        self.frame_x = frame["x"]
        self.frame_y = frame["y"]
        self.in_frame = (self.frame_x[0] < self.x < self.frame_x[1]) and (
            self.frame_y[0] < self.y < self.frame_y[1])
        self.bg= image

    def update_frame_status(self):
        self.in_frame = (self.frame_x[0] < self.x < self.frame_x[1]) and (
            self.frame_y[0] < self.y < self.frame_y[1])

    def move(self, dt):
        PIXELS_PER_METER =100
        # Convert pixel velocity to metres per second
        velocity_x = self.speed_x / PIXELS_PER_METER
        velocity_y = self.speed_y / PIXELS_PER_METER
        velocity = math.sqrt(velocity_x**2 + velocity_y**2)

        # Drag acceleration in metres per second squared: We decompose the speed in the x and the y axis so we don't multiply by velocity^2 but by velocity*velocity_x or y depending on the axis
        drag_x = self.aero * velocity * velocity_x 
        drag_y = self.aero * velocity * velocity_y

        # Convert acceleration back to pixels per second squared
        acceleration_x = drag_x * PIXELS_PER_METER
        acceleration_y = drag_y * PIXELS_PER_METER

        self.speed_x += acceleration_x * dt
        self.speed_y += (g * PIXELS_PER_METER + acceleration_y) * dt # we convert g to an accleration in pixels then sum the accelerations to find the new position of the object

        self.x += self.speed_x * dt
        self.y += self.speed_y * dt

        self.update_frame_status()

    # Use of AI for the rotation of the badminton shuttle, for esthetic purpose    
    def update_rotation(self, dt):
        self.rotation = math.atan2(self.speed_y, self.speed_x)

    def draw_shuttle(self, surface):
        length = 90
        width = 34
        local_points = [
            (length / 2, 0),
            (-length / 2, -width / 2),
            (-length / 2, width / 2),
        ]
        cos_rotation = math.cos(self.rotation)
        sin_rotation = math.sin(self.rotation)
        points = []
        for local_x, local_y in local_points:
            points.append((
                self.x + local_x * cos_rotation - local_y * sin_rotation,
                self.y + local_x * sin_rotation + local_y * cos_rotation,
            ))
        pygame.draw.polygon(surface, (235, 235, 235), points)
        pygame.draw.polygon(surface, (40, 40, 40), points, 2)

    def reset(self):
        self.x = self.original[0]
        self.y = self.original[1]
        self.speed_x = self.original[2]
        self.speed_y = self.original[3]
        self.rotation = math.atan2(self.speed_y, self.speed_x)
        self.angular_speed = 0
        self.in_frame = True
        # time.sleep(3)
        
    def draw_bg(self):
        img=pygame.image.load(self.bg)
        rect= pygame.Rect(self.frame_x[0],
        self.frame_y[0],
        self.frame_x[1] - self.frame_x[0],
        self.frame_y[1] - self.frame_y[0]
        )# We get the dimensions and position of the frame
        img_scaled= pygame.transform.smoothscale(img,rect.size)# We scale the image to the size of the frame
    
       
        screen.blit(img_scaled,rect)# We draw the background on the frame

class button:
    
    def __init__(self, x: float, y: float, length: float, width: float, text: str, color: tuple[int, int, int]):
        self.rect = pygame.Rect(x, y, length, width)
        self.text = text
        self.color = color
    

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, self.rect)# Creation of the button

        police = pygame.font.SysFont("Arial", 30)
        text_surface = police.render(self.text, True, (255, 255, 255))# We create the text box
        text_rect = text_surface.get_rect(center=self.rect.center)# We center the text on the button
        surface.blit(text_surface, text_rect)# We write the text onto the button

    


def speed_x_y(speed, angle):
    speed_x = speed * math.cos((angle*math.pi)/180)
    speed_y = speed * math.sin((angle*math.pi)/180)
    return speed_x, speed_y


# Phase 2: Defining the screens parameters and the clock

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
on = True
info = pygame.display.Info()
width = info.current_w
height = info.current_h

# The constant of gravitation
g = 9.81 




tennis_ball = Projectile(60,
                         (height/2)-200,
                         900,
                         45,
                         {"x": [0, width/2],
                          "y": [0, height/2]},
                         {"drag_coef": 0.52,
                          "Frontal area": 0.0034,
                          "mass": 0.057},
                         "Tennis_bg.jpg"
                         )

button_tennis= button(70,41,100,42,"Tennis",(220, 190, 0))


ping_pong = Projectile(50,
                       height-300,
                       1200,
                       25,
                       {"x": [0, width/2],
                        "y": [height/2, height]},
                       {"drag_coef": 0.43,
                        "Frontal area": 0.00126,
                        "mass": 0.0027},
                       "Ping pong_bg.webp"
                       )

button_ping_pong= button(70,(height/2)-10,250,42,"Ping Pong",(100, 180, 255))


volleyball = Projectile((width/2)+90,
                        height-90,
                        900,
                        40,
                        {"x": [width/2, width],
                         "y": [height/2, height]},
                        {"drag_coef": 0.17,
                        "Frontal area": 0.0346,
                         "mass": 0.270},
                        "Volleyball_bg.jpg"
                        )

button_volleyball= button((width/2)+80,(height/2)+20,250,42,"Volleyball",(220, 90, 80))


badminton_shuttle = Projectile((width/2)+50,
                              (height/2)-50,
                              1950,
                              65,
                              {"x": [width/2, width],
                               "y": [0, height/2]},
                              {"drag_coef": 0.60,
                              "Frontal area": 0.0034,
                               "mass": 0.005},
                              "Badminton_bg.webp")

button_badminton = button((width/2)+80,41,230,42,"Badminton",(0, 150, 150))




while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            on = False
    dt = clock.tick(60) / 1000
    screen.fill((245, 245, 245))
    
    
    #Drawing the brackgrounds
    
    tennis_ball.draw_bg()
    ping_pong.draw_bg()
    volleyball.draw_bg()
    badminton_shuttle.draw_bg()
    
    #Drawing the projectiles
    
    # Tennis
    
    tennis_image = pygame.image.load("Tennis_img.png").convert_alpha()
    tennis_image = pygame.transform.smoothscale(tennis_image, (80, 80))
    
    tennis_rect = tennis_image.get_rect(
    center=(round(tennis_ball.x), round(tennis_ball.y))
    )
    screen.blit(tennis_image, tennis_rect)
    
    # Ping pong
    
    pygame.draw.circle(screen, (255, 170, 0), (ping_pong.x, ping_pong.y), 20)
    
    # Volleyball
    
    volleyball_image = pygame.image.load("Volleyball_img.webp").convert_alpha()
    volleyball_image = pygame.transform.smoothscale(volleyball_image, (160, 160))
    
    volleyball_rect = volleyball_image.get_rect(
    center=(round(volleyball.x), round(volleyball.y))
    )
    screen.blit(volleyball_image, volleyball_rect)
    
    # Badminton
    
    badminton_shuttle.draw_shuttle(screen)
    
    # moving the projectiles
    
    tennis_ball.move(dt)
    
    ping_pong.move(dt)
    
    volleyball.move(dt)
    
    badminton_shuttle.move(dt)
    badminton_shuttle.update_rotation(dt)
    
    #We reset if the projectile crosses the frame's borders
    if not tennis_ball.in_frame:
        tennis_ball.reset()
    if not ping_pong.in_frame:
        ping_pong.reset()
    if not volleyball.in_frame:
        volleyball.reset()
    if not badminton_shuttle.in_frame:
        badminton_shuttle.reset()
        
    # Drawing the buttons   
     
    button_badminton.draw(screen)
    button_tennis.draw(screen)
    button_volleyball.draw(screen)
    button_ping_pong.draw(screen)
    

    pygame.display.flip()# To update the screen according to the changements made


pygame.quit()
