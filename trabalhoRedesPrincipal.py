import glfw
import OpenGL.GL as gl
import numpy as np
from OpenGL.GL.shaders import compileProgram, compileShader
import time  # Para detectar duplo clique


# Código do shader de vértice
VERTEX_SHADER_SRC = """
#version 330 core
layout (location = 0) in vec3 aPos;
void main() {
    gl_Position = vec4(aPos, 1.0);
}
"""

# Código do shader de fragmento (Triângulo)
FRAGMENT_SHADER_TRIANGLE_SRC = """
#version 330 core
out vec4 FragColor;
void main() {
    FragColor = vec4(1.0, 0.5, 0.2, 1.0);  // Laranja
}
"""

# Código do shader de fragmento (Linha)
FRAGMENT_SHADER_LINE_SRC = """
#version 330 core
out vec4 FragColor;
void main() {
    FragColor = vec4(0.0, 1.0, 0.0, 1.0);  // Verde
}
"""
        
def create_shader_program(vertex_src, fragment_src):
    """Compila e retorna um programa de shader OpenGL."""
    shader = compileProgram(
        compileShader(vertex_src, gl.GL_VERTEX_SHADER),
        compileShader(fragment_src, gl.GL_FRAGMENT_SHADER)
    )
    return shader

def create_object(vertices):
    """Cria um VAO e VBO para os vértices fornecidos e retorna os identificadores."""
    VAO = gl.glGenVertexArrays(1)
    VBO = gl.glGenBuffers(1)

    gl.glBindVertexArray(VAO)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, VBO)
    gl.glBufferData(gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, gl.GL_STATIC_DRAW)

    # Configuração dos atributos do vértice
    gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 3 * 4, None)
    gl.glEnableVertexAttribArray(0)

    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
    gl.glBindVertexArray(0)

    return VAO, VBO

# Lista para armazenar cliques do mouse

click_positions = []
last_click_time = 0

def key_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_P and action == glfw.RELEASE:
        
        #if(checksum = true):
        #O PROTOCOLO DE RECEBER TEM Q PRINTAR AQUI 
        #pois se o checksum falhar ele não vai traçar a linha
        #else: print("calango GAY")
        
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        pontos = np.array([[x, y, 0.0]], dtype=np.float32)

        array = np.loadtxt("pontos.txt", dtype=np.float32)
        pontos_atualizados = np.vstack([array, pontos])
        np.savetxt("pontos.txt", pontos_atualizados, fmt='%f')
        
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        pontos = np.array([[x, y, 0.0]], dtype=np.float32)

        array = np.loadtxt("pontos.txt", dtype=np.float32)
        pontos_atualizados = np.vstack([array, pontos])
        np.savetxt("pontos.txt", pontos_atualizados, fmt='%f')
        
        vertices = np.loadtxt("pontos.txt", dtype=np.float32)
        # Atualiza os dados do VBOk
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, VBO_line)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, gl.GL_STATIC_DRAW)
        
        
def mouse_button_callback(window, button, action, mods):
    global last_click_time, click_positions, VBO_line

    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        current_time = time.time()
        x, y = glfw.get_cursor_pos(window)

        # Converte coordenadas da tela para o espaço OpenGL (-1 a 1)
        width, height = glfw.get_framebuffer_size(window)
        x = (x / width) * 2 - 1  # Normaliza para -1 a 1
        y = -((y / height) * 2 - 1)  # OpenGL tem origem no canto inferior esquerdo

        # Armazena a posição do clique
        click_positions.append((x, y, 0.0))
        pontos = np.array([[x, y, 0.0]], dtype=np.float32)

        array = np.loadtxt("pontos.txt", dtype=np.float32)
        pontos_atualizados = np.vstack([array, pontos])
        np.savetxt("pontos.txt", pontos_atualizados, fmt='%f')
        vertices = np.loadtxt("pontos.txt", dtype=np.float32)
        
        # print("ARRAY DO ARQUIVO - ", vertices)
        # print("LENGHT DO ARQUIVO - ", len(vertices))
        # print("ARRAY DO ARRAY",click_positions)
        # print("LENGHT DO ARRAY - ", len(click_positions))
        
        # Se houver dois cliques, cria a linha
        if len(vertices)%2 == 0:
            global pontos1
            dados = np.array([pontos1, pontos], dtype=np.float32)
            print(dados)
            #O PROTOCOLO DE ENVIAR TEM Q PRINTAR AQUI 
            #NAO PENSEI EM CHECKSUM AQ
            #MAS USE OS DADOS REAIS NA APLICAÇÃO PELO MENOS, SO PEGAR ESSA VARIAVEL dados
            
            vertices = np.loadtxt("pontos.txt", dtype=np.float32)
            # print("QUANTIDADE DE BYTES - ",vertices.nbytes)
            # Atualiza os dados do VBOk
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, VBO_line)
            gl.glBufferData(gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, gl.GL_STATIC_DRAW)
            #click_positions = []  # Reseta para nova linha
        pontos1 = pontos #gambiarra
        # Atualiza o tempo do último clique
        last_click_time = current_time

def main():
    global VBO_line

    # Inicializa o GLFW
    if not glfw.init():
        return

    #inicializand o arquivo com o conjunto vazio
    np.savetxt("pontos.txt", np.empty((0, 3)), fmt='%f')
    pontos = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=np.float32)
    np.savetxt("pontos.txt", pontos, fmt='%f')

    # Configurações da janela
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Criação da janela
    window = glfw.create_window(800, 600, "Triângulo e Linha - OpenGL", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # Registra a função de callback para capturar cliques do mouse
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_key_callback(window, key_callback)
    # Compila os programas de shader
    shader_triangle = create_shader_program(VERTEX_SHADER_SRC, FRAGMENT_SHADER_TRIANGLE_SRC)
    shader_line = create_shader_program(VERTEX_SHADER_SRC, FRAGMENT_SHADER_LINE_SRC)

    # Definição dos vértices do triângulo
    triangle_vertices = np.array([
        -0.5, -0.5, 0.0,  # Vértice inferior esquerdo
         0.5, -0.5, 0.0,  # Vértice inferior direito
         0.0,  0.5, 0.0   # Vértice superior
    ], dtype=np.float32)

    # Definição inicial dos vértices da linha (vazio)
    array = np.loadtxt("pontos.txt", dtype=np.float32)
    line_vertices = np.array([
        array
    ], dtype=np.float32)
    #print("DADOS INICIAIS - ", line_vertices)
    # Criação dos objetos
    VAO_triangle, _ = create_object(triangle_vertices)
    VAO_line, VBO_line = create_object(line_vertices)  # Guarda o VBO da linha para atualizar depois

    # Loop principal
    while not glfw.window_should_close(window):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        # Desenha o triângulo
        gl.glUseProgram(shader_triangle)
        gl.glBindVertexArray(VAO_triangle)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)

        vertices = np.loadtxt("pontos.txt", dtype=np.float32)
        # Desenha a linha se houver dados válidos
        gl.glUseProgram(shader_line)
        gl.glBindVertexArray(VAO_line)
        gl.glDrawArrays(gl.GL_LINES, 0, len(vertices))

        # Atualiza a tela
        glfw.swap_buffers(window)
        glfw.poll_events()

    # Limpeza
    gl.glDeleteVertexArrays(1, [VAO_triangle])
    gl.glDeleteVertexArrays(1, [VAO_line])
    gl.glDeleteProgram(shader_triangle)
    gl.glDeleteProgram(shader_line)

    glfw.terminate()

if __name__ == "__main__":
    main()
