import pygame
import numpy as np
import pyaudio
import pygame_gui

# Inicialização do Pygame e Pygame GUI
pygame.init()

# Configurações da janela
window_width, window_height = 1280, 720
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Visualizador de Áudio")

# Cores
grid_color = (20, 20, 20)
block_color = (0, 0, 0)
background_color = (200, 200, 200)  # Cinza claro

# Inicialização do gerenciador da UI do pygame_gui
manager = pygame_gui.UIManager((window_width, window_height))

# Criação dos campos de entrada de texto
fps_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((10, 10), (150, 30)), manager=manager)
block_size_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((10, 50), (150, 30)), manager=manager)
block_spacing_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((10, 90), (150, 30)), manager=manager)
rows_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((10, 130), (150, 30)), manager=manager)
columns_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((10, 170), (150, 30)), manager=manager)

# Definições dos blocos e fileiras
block_size = 25
block_spacing = 0.10
rows = 10
columns = 25
visualizer_width = block_size * columns + block_spacing * (columns - 1)
visualizer_height = block_size * rows + block_spacing * (rows - 1)

# Calcula o deslocamento para centralizar os blocos
offset_x = (window_width - visualizer_width) // 2
offset_y = (window_height - visualizer_height) // 2

# Configurações de áudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Controlando a taxa de atualização
clock = pygame.time.Clock()
fps = 30  # Definindo a taxa de quadros por segundo

def draw_grid_and_border():
    window.fill(background_color)
    pygame.draw.rect(window, grid_color, [offset_x-5, offset_y-5, visualizer_width+10, visualizer_height+10], 5)
    for x in range(columns):
        for y in range(rows):
            rect = pygame.Rect(offset_x + x * (block_size + block_spacing), offset_y + y * (block_size + block_spacing), block_size, block_size)
            pygame.draw.rect(window, block_color, rect, 1)

def calculate_fire_color(intensity):
    if intensity < 0.3:
        color = (255, 140, 0)
    elif intensity < 0.6:
        color = (255, 85, 0)
    else:
        color = (255, 0, 0)
    return color

def color_block(x, y, color):
    rect = pygame.Rect(offset_x + x * (block_size + block_spacing), offset_y + y * (block_size + block_spacing), block_size, block_size)
    pygame.draw.rect(window, color, rect)

# Loop principal
running = True
while running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)

    manager.update(time_delta)

    draw_grid_and_border()

    # Captura de áudio e processamento
    data = np.frombuffer(stream.read(1024), dtype=np.int16)
    volume = np.abs(np.fft.rfft(data)).astype(np.float32)
    activation_threshold = 7000  # Limiar de ativação para o volume
    sensitivity_scale = 1.0  # Variável de sensibilidade

    if np.max(volume) > activation_threshold:
        for i in range(len(volume)):
            intensity = (volume[i] / np.max(volume)) * sensitivity_scale
            color = calculate_fire_color(intensity)
            blocks_to_color = int(np.ceil(intensity * rows))
            for y in range(blocks_to_color):
                color_block(i % columns, rows - y - 1, color)

    manager.draw_ui(window)

    pygame.display.flip()

pygame.quit()
stream.stop_stream()
stream.close()
p.terminate()
