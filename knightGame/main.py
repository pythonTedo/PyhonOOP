import pygame
import random
import button

pygame.init()
pygame.font.init()

bottom_panel = 150
WIDTH, HEIGHT = 800, 400 + bottom_panel
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle")

#define fonts
font = pygame.font.SysFont("Times New Roman", 26)
red = (255, 0, 0)
green = (0, 255, 0)

#define game variables
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90
attack = False
potion = False
potion_effect = 15
clicked = False
game_over = 0  # 1:win game -1: lost


# Load IMGs
# background
BG_img = pygame.image.load('img/Background/background.png').convert_alpha()
PANEL_img = pygame.image.load('img/Icons/panel.png').convert_alpha()
SWORD_img = pygame.image.load('img/Icons/sword.png').convert_alpha()
potion_img = pygame.image.load("img/Icons/potion.png").convert_alpha()
restart_img = pygame.image.load("img/Icons/restart.png").convert_alpha()
#load victory and defeat
VICTORY_img = pygame.image.load('img/Icons/victory.png').convert_alpha()
DEFEAT_img = pygame.image.load("img/Icons/defeat.png").convert_alpha()

# keep the window running
FPS = 60
run = True
clock = pygame.time.Clock()

class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.x = x
        self.y = y
        self.name = name
        self.max_hp = max_hp
        self.strength = strength
        self.potions = potions
        self.hp = max_hp
        self.start_potion = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0  #to control the animation
        self.action = 0       #0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()  # keep in track with the time since the instance is created


        # load idle images
        temp_list = []
        for i in range(8):
            image = pygame.image.load("img/%s/Idle/%s.png" % (self.name, i))
            image = pygame.transform.scale(image, (image.get_width() * 3, image.get_height() * 3))
            temp_list.append(image)
        self.animation_list.append(temp_list)   #index 0 list is my idle images...

        #load attack images
        temp_list = []
        for i in range(8):
            image = pygame.image.load("img/%s/Attack/%s.png" % (self.name, i))
            image = pygame.transform.scale(image, (image.get_width() * 3, image.get_height() * 3))
            temp_list.append(image)
        self.animation_list.append(temp_list)   #index 1 list is my attack images...

        # load hurt animation
        temp_list = []
        for i in range(3):
            image = pygame.image.load("img/%s/%s/%s.png" % (self.name, "Hurt", i))
            image = pygame.transform.scale(image, (image.get_width() * 3, image.get_height() * 3))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        #load dead animation
        temp_list = []
        for i in range(10):
            image = pygame.image.load("img/%s/%s/%s.png" % (self.name, "Death", i))
            image = pygame.transform.scale(image, (image.get_width() * 3, image.get_height() * 3))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()  #take widths and heights of the pict
        self.rect.center = (x, y)

    def update(self):  # animation update
        animation_cooldown = 100  ## ms time measure
        # handle animation
        self.image = self.animation_list[self.action][self.frame_index]
        # take current time - take the time when instance is created > time measure update index
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out of images, redo them
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()

    #resets animation to idle station after action
    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        #deal dmg to enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        #run enemy hurt animation
        target.hurt()

        #check if target is dead
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.dead()

        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)

        #set var for attack animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def dead(self):
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def reset(self):
        self.alive = True
        self.potions = self.start_potion
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.rect)



class HealthBar:
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        self.hp = hp
        # calculate health ration
        ratio = self.hp/self.max_hp

        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        #move damage text up
        self.rect.y -= 1
        #delete the text after few sec
        self.counter += 1
        if self.counter > 30:
            self.kill()

damage_text_group = pygame.sprite.Group()

knight = Fighter(200, 260, "Knight", 5, 12, 3)
bandit1 = Fighter(550, 270, "Bandit", 30, 10, 1)
bandit2 = Fighter(700, 270, "Bandit", 30, 10, 1)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

knight_health_bar = HealthBar(100, HEIGHT - bottom_panel + 40, knight.hp, knight.max_hp)
bandit1_health_bar = HealthBar(550, HEIGHT - bottom_panel + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = HealthBar(550, HEIGHT - bottom_panel + 100, bandit2.hp, bandit2.max_hp)

#create buttons
potion_button = button.Button(screen,100, HEIGHT - bottom_panel + 70, potion_img, 64, 64)
restart_button = button.Button(screen,330, 120, restart_img, 120, 30)

# draw text
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def draw_panel():
    screen.blit(PANEL_img, (0, HEIGHT - bottom_panel))
    #show knight stats
    draw_text("%s HP: %d" % (knight.name, knight.hp), font, red, 100, HEIGHT - bottom_panel + 10)
    #show bandit stats
    for count, bandit in enumerate(bandit_list):
        draw_text("%s HP: %d" % (bandit.name, bandit.hp), font, red, 550, (HEIGHT - bottom_panel + 10) + count * 60)
        #beacuse i have multiple bandits y axis is going to move down for each bandit


def draw():

    screen.blit(BG_img, (0, 0))
    draw_panel()


    knight.update()  # first update then draw
    knight.draw()
    knight_health_bar.draw(knight.hp)
    bandit1_health_bar.draw(bandit1.hp)
    bandit2_health_bar.draw(bandit2.hp)

    for bandit in bandit_list:
        bandit.update()
        bandit.draw()


while run:
    clock.tick(FPS)

    draw()

    #draw damage text
    damage_text_group.update()  #inherited methods
    damage_text_group.draw(screen)

                                                # SECTION 1 LOOKING FOR ACTIONS
    #player actions control
    #reset action vars
    attack = False
    potion = False
    target = None
    #make sure mouse is visible
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()
    for count, bandit in enumerate(bandit_list):
        if bandit.rect.collidepoint(pos):
            #hide mouse
            pygame.mouse.set_visible(False)
            #show sword in place of mouse cursor
            screen.blit(SWORD_img, pos)
            if clicked == True and bandit.alive == True: # can click only on alive bandit
                attack = True
                target = bandit_list[count]
    if potion_button.draw():
        potion = True
    #show nums of potions
    draw_text(str(knight.potions), font, red, 150, HEIGHT - bottom_panel + 70)


    if game_over == 0:                                          # SECTION 2 EXECUTE ACTIONS
        # player action
        if knight.alive:
            if current_fighter == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    #look for player action
                    #attack
                    if attack == True and target != None:
                        knight.attack(target)
                        current_fighter += 1
                        action_cooldown = 0
                    #potion
                    if potion == True:
                        if knight.potions > 0:
                            #check if hp is enought for a potion
                            if knight.max_hp - knight.hp > potion_effect:
                                heal_amount = potion_effect
                            else:
                                heal_amount = knight.max_hp - knight.hp
                            knight.hp += heal_amount
                            knight.potions -= 1
                            damage_text = DamageText(knight.rect.centerx, knight.rect.y, str(heal_amount), green)
                            damage_text_group.add(damage_text)
                            #count as an action
                            current_fighter += 1
                            action_cooldown = 0
        else:
            game_over = -1

        # enemy action
        for count, bandit in enumerate(bandit_list):
            if current_fighter == 2 + count:
                if bandit.alive:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        # look for player action
                        #pcheck if needs to heal
                        if (bandit.hp / bandit.max_hp) < 0.5 and bandit.potions > 0:
                            # check if hp is enought for a potion
                            if bandit.max_hp - bandit.hp > potion_effect:
                                heal_amount = potion_effect
                            else:
                                heal_amount = bandit.max_hp - bandit.hp
                            bandit.hp += heal_amount
                            bandit.potions -= 1
                            damage_text = DamageText(bandit.rect.centerx, bandit.rect.y, str(heal_amount), green)
                            damage_text_group.add(damage_text)
                            # count as an action
                            current_fighter += 1
                            action_cooldown = 0
                        # attack
                        else:
                            bandit.attack(knight)
                            current_fighter += 1
                            action_cooldown = 0
                else:
                    current_fighter += 1

    #if all the fighters had a turn then reset
    if current_fighter > total_fighters:
        current_fighter = 1

    #check if all bandits are dead
    alive_bandits = 0
    for bandit in bandit_list:
        if bandit.alive == True:
            alive_bandits += 1
    if alive_bandits == 0:
        game_over = 1

    #check if game is over
    if game_over != 0:
        if game_over == 1:
            screen.blit(VICTORY_img, (255, 50))
        if game_over == -1:
            screen.blit(DEFEAT_img, (290, 50))
        if restart_button.draw():
            knight.reset()
            for bandit in bandit_list:
                bandit.reset()
            current_fighter = 1
            action_cooldown
            game_over = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    pygame.display.update() ## when drawing updates the screen
pygame.quit()