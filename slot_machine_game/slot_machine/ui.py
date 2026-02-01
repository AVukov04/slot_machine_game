import pygame
from .game_logic import SlotMachine

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (52, 58, 64)

class SlotMachineUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 400))
        pygame.display.set_caption("Slot Machine")

        self.machine = SlotMachine()
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

        self.message = "Press SPACE to spin"

    def draw(self):
        self.screen.fill(GRAY)

        symbols = self.machine.last_symbols or ["?", "?", "?"]
        for i in range(3):
            x = 100 + i * 120
            pygame.draw.rect(self.screen, WHITE, (x, 120, 100, 80))
            text = self.font.render(symbols[i], True, BLACK)
            self.screen.blit(text, (x + 10, 145))

        balance_text = self.font.render(f"Balance: ${self.machine.balance}", True, WHITE)
        self.screen.blit(balance_text, (20, 20))

        msg_text = self.font.render(self.message, True, WHITE)
        self.screen.blit(msg_text, (120, 280))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False

                    if event.key == pygame.K_SPACE:
                        try:
                            symbols, winnings = self.machine.spin()
                            if winnings > 0:
                                self.message = f"You won ${winnings}!"
                            else:
                                self.message = "No win"
                        except ValueError as e:
                            self.message = str(e)

            self.draw()
            self.clock.tick(60)

        pygame.quit()

