import pygame, sys
import pandas as pd
import math
from config import *

game = pd.read_csv("../Exports/" + str(GAME_NUMBER) + ".csv")


def field_background():
    screen.fill((0, 153, 0))
    myfont = pygame.font.SysFont('Times New Romans', 30)
    pygame.draw.rect(screen, white, (0, 0, width, height), coefficient)
    pygame.draw.line(screen, white, (10 * coefficient, 0), (10 * coefficient, height), 5)
    pygame.draw.line(screen, white, (15 * coefficient, 0), (15 * coefficient, height), 5)
    pygame.draw.line(screen, white, (20 * coefficient, 0), (20 * coefficient, height), 5)
    pygame.draw.line(screen, white, (25 * coefficient, 0), (25 * coefficient, height), 5)
    pygame.draw.line(screen, white, (30 * coefficient, 0), (30 * coefficient, height), 5)
    pygame.draw.line(screen, white, (35 * coefficient, 0), (35 * coefficient, height), 5)
    pygame.draw.line(screen, white, (40 * coefficient, 0), (40 * coefficient, height), 5)
    pygame.draw.line(screen, white, (45 * coefficient, 0), (45 * coefficient, height), 5)
    pygame.draw.line(screen, white, (50 * coefficient, 0), (50 * coefficient, height), 5)
    pygame.draw.line(screen, white, (55 * coefficient, 0), (55 * coefficient, height), 5)
    pygame.draw.line(screen, white, (60 * coefficient, 0), (60 * coefficient, height), 5)
    pygame.draw.line(screen, white, (65 * coefficient, 0), (65 * coefficient, height), 5)
    pygame.draw.line(screen, white, (70 * coefficient, 0), (70 * coefficient, height), 5)
    pygame.draw.line(screen, white, (75 * coefficient, 0), (75 * coefficient, height), 5)
    pygame.draw.line(screen, white, (80 * coefficient, 0), (80 * coefficient, height), 5)
    pygame.draw.line(screen, white, (85 * coefficient, 0), (85 * coefficient, height), 5)
    pygame.draw.line(screen, white, (90 * coefficient, 0), (90 * coefficient, height), 5)
    pygame.draw.line(screen, white, (95 * coefficient, 0), (95 * coefficient, height), 5)
    pygame.draw.line(screen, white, (100 * coefficient, 0), (100 * coefficient, height), 5)
    pygame.draw.line(screen, white, (105 * coefficient, 0), (105 * coefficient, height), 5)
    pygame.draw.line(screen, white, (110 * coefficient, 0), (110 * coefficient, height), 5)
    screen.blit(myfont.render("<1 0", False, white), (20 * coefficient - 25, height - 5 * coefficient))
    screen.blit(myfont.render("<2 0", False, white), (30 * coefficient - 25, height - 5 * coefficient))
    screen.blit(myfont.render("<3 0", False, white), (40 * coefficient - 25, height - 5 * coefficient))
    screen.blit(myfont.render("<4 0", False, white), (50 * coefficient - 25, height - 5 * coefficient))
    screen.blit(myfont.render("5 0", False, white), (60 * coefficient - 12, height - 5 * coefficient))
    screen.blit(myfont.render("4 0>", False, white), (70 * coefficient - 12, height - 5 * coefficient))
    screen.blit(myfont.render("3 0>", False, white), (80 * coefficient - 12, height - 5 * coefficient))
    screen.blit(myfont.render("2 0>", False, white), (90 * coefficient - 12, height - 5 * coefficient))
    screen.blit(myfont.render("1 0>", False, white), (100 * coefficient - 12, height - 5 * coefficient))
    pygame.display.update()


pygame.init()

coefficient = 15
human_size = 15
way_size = 4


size = width, height = round(120 * coefficient), round(53.3 * coefficient)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
brown = (102, 51, 0)
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
field_background()
myfont_2 = pygame.font.SysFont('Times New Romans', 15)

unique_time = game["time"].unique()
unique_time_index = 0



def draw_players():
    point = game[game["time"] == unique_time[unique_time_index]]

    for index, row in point.iterrows():
        if row["team"] == "home":
            pygame.draw.circle(screen, red, (round(row["x"])*coefficient, round(row["y"])*coefficient), human_size)
            pygame.draw.circle(screen, (150, 0, 255), (round(row["x"])*coefficient+math.sin(math.radians(int(row["dir"])))*coefficient, round(row["y"])*coefficient+math.cos(math.radians(int(row["dir"])))*coefficient), way_size)
            pygame.draw.circle(screen, black, (round(row["x"])*coefficient+math.sin(math.radians(int(row["o"])))*coefficient, round(row["y"])*coefficient+math.cos(math.radians(int(row["o"])))*coefficient), way_size)
            screen.blit(myfont_2.render(str(int(row["jerseyNumber"])), False, white), (round(row["x"])*coefficient-5, round(row["y"])*coefficient-5))
        elif row["team"] == "away":
            pygame.draw.circle(screen, blue, (round(row["x"])*coefficient, round(row["y"])*coefficient), human_size)
            pygame.draw.circle(screen, (150, 0, 255), (round(row["x"])*coefficient+math.sin(math.radians(int(row["dir"])))*coefficient, round(row["y"])*coefficient+math.cos(math.radians(int(row["dir"])))*coefficient), way_size)
            pygame.draw.circle(screen, black, (round(row["x"])*coefficient+math.sin(math.radians(int(row["o"])))*coefficient, round(row["y"])*coefficient+math.cos(math.radians(int(row["o"])))*coefficient), way_size)
            screen.blit(myfont_2.render(str(int(row["jerseyNumber"])), False, white), (round(row["x"])*coefficient-5, round(row["y"])*coefficient-5))
        elif row["team"] == "football":
            pygame.draw.circle(screen, brown, (round(row["x"])*coefficient, round(row["y"])*coefficient), 5)

    first_row = point.iloc[0]
    print("Time: " + first_row["time"] + " Event: " + first_row["event"])
    _, time = first_row["time"].split("T")
    pygame.display.set_caption("Game ID: " + str(GAME_NUMBER) + " | Time: " + time + " | Event: " + first_row["event"] + " | " + first_row["home"] + "-" + first_row["away"])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RIGHT:
                unique_time_index += 1
                field_background()
                draw_players()
                pygame.display.update()
            if event.key == pygame.K_LEFT:
                unique_time_index -= 1
                field_background()
                draw_players()
                pygame.display.update()
