import pygame

pygame.init()
win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Jumping!!!!!")

walkRight = [pygame.image.load('sprites/R1.png'), pygame.image.load('sprites/R2.png'),
             pygame.image.load('sprites/R3.png'), pygame.image.load('sprites/R4.png'),
             pygame.image.load('sprites/R5.png'), pygame.image.load('sprites/R6.png'),
             pygame.image.load('sprites/R7.png'), pygame.image.load('sprites/R8.png'),
             pygame.image.load('sprites/R9.png')]

walkLeft = [pygame.image.load('sprites/L1.png'), pygame.image.load('sprites/L2.png'),
            pygame.image.load('sprites/L3.png'), pygame.image.load('sprites/L4.png'),
            pygame.image.load('sprites/L5.png'), pygame.image.load('sprites/L6.png'),
            pygame.image.load('sprites/L7.png'), pygame.image.load('sprites/L8.png'),
            pygame.image.load('sprites/L9.png')]
bg = pygame.image.load(f'Backgrounds/bg.jpg')
char = pygame.image.load(f'sprites/standing.png')

bulletSound = pygame.mixer.Sound('Sounds/pew.mp3')
enemyHitSound = pygame.mixer.Sound('Sounds/bruh.mp3')
playerHitSound = pygame.mixer.Sound('Sounds/uwu.mp3')
deathsound = pygame.mixer.Sound('Sounds/runesound.mp3')
music = pygame.mixer.music.load('Sounds/music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.10)

clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.health = 10
        self.invincible = False

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if self.health > 0:
            playerHitSound.play()
            self.health -= 1
            man.invincible = True
        if self.health == 0:
            pygame.mixer.music.fadeout(500)
            deathsound.play()
            self.health -= 1


class enemy():
    walkRight = [pygame.image.load('sprites/R1E.png'), pygame.image.load('sprites/R2E.png'),
                 pygame.image.load('sprites/R3E.png'), pygame.image.load('sprites/R4E.png'),
                 pygame.image.load('sprites/R5E.png'), pygame.image.load('sprites/R6E.png'),
                 pygame.image.load('sprites/R7E.png'), pygame.image.load('sprites/R8E.png'),
                 pygame.image.load('sprites/R9E.png'), pygame.image.load('sprites/R10E.png'),
                 pygame.image.load('sprites/R11E.png')]

    walkLeft = [pygame.image.load('sprites/L1E.png'), pygame.image.load('sprites/L2E.png'),
                pygame.image.load('sprites/L3E.png'), pygame.image.load('sprites/L4E.png'),
                pygame.image.load('sprites/L5E.png'), pygame.image.load('sprites/L6E.png'),
                pygame.image.load('sprites/L7E.png'), pygame.image.load('sprites/L8E.png'),
                pygame.image.load('sprites/L9E.png'), pygame.image.load('sprites/L10E.png'),
                pygame.image.load('sprites/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.vel = 5
        self.walkCount = 0
        self.path = [self.x, self.y]
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 9

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 255, 0),
                         (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - (self.health + 1))), 10))
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        global score
        global goblins
        global man
        if man.health > 0:
            score += 1
            if self.health > 0:
                enemyHitSound.play()
                self.health -= 1
            else:
                goblins = []


class Projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    global man
    win.blit(bg, (0, 0))
    text = scoreFont.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (350, 10))
    if man.health <= 0:
        death_text = deadFont.render('YOU ARE DEAD!!!', 1, (255, 0, 0))
        win.blit(death_text, (150, 120))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# mainloop
scoreFont = pygame.font.SysFont('comicsans', 30, True)
deadFont = pygame.font.SysFont('comicsans', 30, True)
damageTime = 0
resolveTime = 0
man = Player(300, 410, 64, 64)
goblins = []
bullets = []
shootLoop = 0
score = 0
run = True
while run:
    clock.tick(27)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if len(goblins) == 0:
        goblin = enemy(100, 410, 64, 64, 450)
        goblins.append(goblin)

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[
            1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + \
                    goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))
        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if not man.invincible:
        for goblin in goblins:
            if man.y - man.height < goblin.hitbox[1] + goblin.hitbox[3] and man.y + man.height > goblin.hitbox[1]:
                if man.hitbox[0] <= goblin.hitbox[0] + goblin.hitbox[2] <= man.hitbox[0] + man.hitbox[2] or \
                        man.hitbox[0] <= goblin.hitbox[0] <= man.hitbox[0] + man.hitbox[2]:
                    man.hit()
                    damageTime = pygame.time.get_ticks()
    else:
        resolveTime = pygame.time.get_ticks()
        if resolveTime - damageTime > 700:
            man.invincible = False
            damageTime = resolveTime = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.health > 0:
            bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0),
                                      facing))
        shootLoop = 1

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= man.jumpCount ** 2 / 3 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
