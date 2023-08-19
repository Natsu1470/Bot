from tkinter import Tk, Label
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from tkinter import *
from tkinter import Tk, Button
import subprocess
from tkinter import Tk, Entry


def ejecutar_programa():
    # Variables
    megusta = []
    usuarios = []
    contrasenias = []
    link = campo_link.get()

    # Leer los archivos
    with open('users.txt', 'r') as file1:
        usuarios = [line.strip() for line in file1.readlines()]

    with open('pass.txt', 'r') as file2:
        contrasenias = [line.strip() for line in file2.readlines()]

    print(usuarios)
    print(contrasenias)

    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
    opts.add_argument("--disable-notifications")
    opts.add_argument("--maximized--")

    # Hasta que línea ejecuta
    linea_limite = int(campo_linea_limite.get())

    ## Desde qué cuenta comienza
    index = 0
    linea_actual = int(campo_linea_actual.get())
    if campo_linea_actual.get() == "0":
        linea_actual = 1
    else:
        linea_actual = int(campo_linea_actual.get())
    

    while linea_actual <= linea_limite:
        usuario = usuarios[index]
        contrasenia = contrasenias[index]

        driver = webdriver.Chrome('chromedriver-linux64/chromedriver', options=opts)

        ## Log In
        driver.get('https://facebook.com')

        # Pone el correo
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#email'))).send_keys(usuario)
        time.sleep(2)

        # Pone la contraseña
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#pass'))).send_keys(contrasenia)
        time.sleep(2)
        ## da click inicio sesion
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._42ft._4jy0._6lth._4jy6._4jy1.selected._51sy'))).click()
        time.sleep(2)

        ### FOTO
        try:
            driver.get(link)
            sleep(3)
            foto_xpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]'
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, foto_xpath)))
            element.click()
            sleep(2)

            driver.quit()
       
        except Exception as f:
         driver.get(link)
         sleep (2)
         foto_xpath = '/html/body//div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div[1]/div[1]'
         element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,foto_xpath)))
         element.click()
         sleep(2)      
         driver.quit()

        except Exception as g:
         driver.get(link)
         sleep (2)
         foto_xpath = '/html/body//div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[3]/div/div[2]/div/div[1]'
         element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,foto_xpath)))
         element.click()
         sleep(2)      
         driver.quit()
       
        except Exception as e:
         driver.get(link)
         sleep(3)
         foto_xpath = '/html/body//div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]'
         element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, foto_xpath)))
         element.click()
         sleep(2)
         driver.quit()
        # Actualizar el índice y la línea actual
        index += 1
        linea_actual += 1

        # Verificar si se llegó al final de las listas
        if index >= len(usuarios) or index >= len(contrasenias):
            break


def asignar_link():
    link = campo_link.get()
    print("Link asignado:", link)

# Crear la ventana
ventana = Tk()

# Configurar la ventana
ventana.title("Seguidores mexicanos")
ventana.geometry("7000x1500")
ventana.configure(bg="Blue")

# Crear un campo de entrada de texto para línea límite
hasta="Desde"
etiqueta = Label(ventana, text=hasta)
etiqueta.pack()
etiqueta.place(x=160, y=10)
campo_linea_actual = Entry(ventana, bg="white", fg="black")
campo_linea_actual.pack(pady=10)

# Crear un campo de entrada de texto para línea límite
hasta="Hasta"
etiqueta = Label(ventana, text=hasta)
etiqueta.pack()
etiqueta.place(x=160, y=57)
campo_linea_limite = Entry(ventana, bg="white", fg="black")
campo_linea_limite.pack(pady=20)

# Crear un botón para ejecutar el programa
boton_ejecutar = Button(ventana, text="Ejecutar programa", command=ejecutar_programa, bg="white", fg="black")
boton_ejecutar.pack()

# Etiqueta y campo de entrada para el link
etiqueta_link = Label(ventana, text="Link", bg="white", fg="black")
etiqueta_link.pack()

def dar_like_foto():
    # Código para dar like a una foto en Facebook
    print("Dando like a una foto en Facebook")

def dar_like_video():
    # Código para dar like a un video en Facebook
    print("Dando like a un video en Facebook")


# Configurar la ventana
ventana.title("SMM JON")
ventana.geometry("600x400")

texto = "Imagenes"
etiqueta = Label(ventana, text=texto, bg= "white" ,fg= "black")
etiqueta.pack()
etiqueta.place(x=10, y=ventana.winfo_height() // 2)
campo_link = Entry(ventana, bg="white", fg="black",width= 90)
campo_link.pack(pady=10)
# Crear los botones
def ejecutar_archivo_py(archivo):
    subprocess.Popen(['python', archivo])


boton_like_video = Button(ventana, text="Like a video", command=lambda: ejecutar_archivo_py("BotLikeVideo.py"))
boton_like_video.pack(pady=20)

boton_like_video = Button(ventana, text="Like a pagina", command=lambda: ejecutar_archivo_py("BotLikePaginas.py"))
boton_like_video.pack(pady=25)

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()