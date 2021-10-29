import pygame, sys
import pandas as pd
import math
from config import *

game = pd.read_csv("../Exports/" + str(GAME_NUMBER) + ".csv")


def field_background():
    screen.fill((0, 153, 0))
    myfont = pygame.font.SysFont('Times New Romans', 30)
    pygame.draw.rect(screen, white, (0, 0, width, height), COEFFICIENT)
    pygame.draw.line(screen, white, (10 * COEFFICIENT, 0), (10 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (15 * COEFFICIENT, 0), (15 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (20 * COEFFICIENT, 0), (20 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (25 * COEFFICIENT, 0), (25 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (30 * COEFFICIENT, 0), (30 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (35 * COEFFICIENT, 0), (35 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (40 * COEFFICIENT, 0), (40 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (45 * COEFFICIENT, 0), (45 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (50 * COEFFICIENT, 0), (50 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (55 * COEFFICIENT, 0), (55 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (60 * COEFFICIENT, 0), (60 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (65 * COEFFICIENT, 0), (65 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (70 * COEFFICIENT, 0), (70 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (75 * COEFFICIENT, 0), (75 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (80 * COEFFICIENT, 0), (80 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (85 * COEFFICIENT, 0), (85 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (90 * COEFFICIENT, 0), (90 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (95 * COEFFICIENT, 0), (95 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (100 * COEFFICIENT, 0), (100 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (105 * COEFFICIENT, 0), (105 * COEFFICIENT, height), 5)
    pygame.draw.line(screen, white, (110 * COEFFICIENT, 0), (110 * COEFFICIENT, height), 5)
    screen.blit(myfont.render("<1 0", False, white), (20 * COEFFICIENT - 25, height - 5 * COEFFICIENT))
    screen.blit(myfont.render("<2 0", False, white), (30 * COEFFICIENT - 25, height - 5 * COEFFICIENT))
    screen.blit(myfont.render("<3 0", False, white), (40 * COEFFICIENT - 25, height - 5 * COEFFICIENT))
    screen.blit(myfont.render("<4 0", False, white), (50 * COEFFICIENT - 25, height - 5 * COEFFICIENT))
    screen.blit(myfont.render("5 0", False, white), (60 * COEFFICIENT - 12, height - 5 * COEFFICIENT))
    screen.blit(myfont.render("4 0>", False, white), (70 * COEFFICIENT - 12, height - 5 * COEFFICIENT))
    screen.blit(myfont.render("3 0>", False, white), (80 * COEFFICIENT - 12, height - 5 * COEFFICIENT))
    screen.blit(myfont.render("2 0>", False, white), (90 * COEFFICIENT - 12, height - 5 * COEFFICIENT))
    screen.blit(myfont.render("1 0>", False, white), (100 * COEFFICIENT - 12, height - 5 * COEFFICIENT))
    pygame.display.update()


pygame.init()
size = width, height = round(120 * COEFFICIENT), round(53.3 * COEFFICIENT)
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
            pygame.draw.circle(screen, red, (round(row["x"])*COEFFICIENT, round(row["y"])*COEFFICIENT), HUMAN_SIZE)
            pygame.draw.circle(screen, (150, 0, 255), (round(row["x"])*COEFFICIENT+math.sin(math.radians(int(row["dir"])))*COEFFICIENT, round(row["y"])*COEFFICIENT+math.cos(math.radians(int(row["dir"])))*COEFFICIENT), DIR_ORI_SIZE)
            pygame.draw.circle(screen, black, (round(row["x"])*COEFFICIENT+math.sin(math.radians(int(row["o"])))*COEFFICIENT, round(row["y"])*COEFFICIENT+math.cos(math.radians(int(row["o"])))*COEFFICIENT), DIR_ORI_SIZE)
            screen.blit(myfont_2.render(str(int(row["jerseyNumber"])), False, white), (round(row["x"])*COEFFICIENT-5, round(row["y"])*COEFFICIENT-5))
        elif row["team"] == "away":
            pygame.draw.circle(screen, blue, (round(row["x"])*COEFFICIENT, round(row["y"])*COEFFICIENT), HUMAN_SIZE)
            pygame.draw.circle(screen, (150, 0, 255), (round(row["x"])*COEFFICIENT+math.sin(math.radians(int(row["dir"])))*COEFFICIENT, round(row["y"])*COEFFICIENT+math.cos(math.radians(int(row["dir"])))*COEFFICIENT), DIR_ORI_SIZE)
            pygame.draw.circle(screen, black, (round(row["x"])*COEFFICIENT+math.sin(math.radians(int(row["o"])))*COEFFICIENT, round(row["y"])*COEFFICIENT+math.cos(math.radians(int(row["o"])))*COEFFICIENT), DIR_ORI_SIZE)
            screen.blit(myfont_2.render(str(int(row["jerseyNumber"])), False, white), (round(row["x"])*COEFFICIENT-5, round(row["y"])*COEFFICIENT-5))
        elif row["team"] == "football":
            pygame.draw.circle(screen, brown, (round(row["x"])*COEFFICIENT, round(row["y"])*COEFFICIENT), 5)

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
            if event.key == pygame.K_ESCAPE:
                sys.exit()
