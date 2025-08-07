import pokemon 
import customtkinter as ctk
from PIL import Image, ImageTk







pokemon_elegido = None

def salir_programa():
    ventana.destroy()  # o ventana.quit()
    
    

def elegir_pokemon(nombre):
    
    
    global pokemon_elegido
    pokemon_elegido = nombre
    print("Elegiste:", pokemon_elegido)

    # Limpiar la ventana (destruye todo lo que está dentro)
    for widget in ventana.winfo_children():
        widget.destroy()
    
    imagen_fondo = Image.open("fondo2.png")  
    imagen_fondo = imagen_fondo.resize((1000, 800))
    imagen_tk = ImageTk.PhotoImage(imagen_fondo)

    fondo_label = ctk.CTkLabel(ventana, image=imagen_tk, text="")  
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    
    # Mostrar algo nuevo (texto de confirmación, por ejemplo)
    label = ctk.CTkLabel(ventana, text=(pokemon_elegido[:-4]).upper(), font=("Press Start 2P", 25))
    label.place(x=55,y=400)
    
    label = ctk.CTkLabel(ventana, text="NIVEL: 5", font=("Press Start 2P", 22))
    label.place(x=55,y=450)
    
    label = ctk.CTkLabel(ventana, text="ESTADISTICAS", font=("Press Start 2P", 25))
    label.place(x=400,y=370)
    
    label = ctk.CTkLabel(ventana, text="PERFIL", font=("Press Start 2P", 25))
    label.place(x=400,y=225)
    
    imagen = Image.open(pokemon_elegido)  
    imagen = imagen.resize((200, 200))  
    imagen_tk = ImageTk.PhotoImage(imagen)

    label_imagen = ctk.CTkLabel(ventana, image=imagen_tk, text="")
    label_imagen.image = imagen_tk  # Guardar referencia para que no se pierda
    label_imagen.place(x=75, y=160)
    
    for i in range(6):  
        dato=f"{pokemon.stats1[i]}{pokemon.stats2[i]}"
        label = ctk.CTkLabel(ventana, text=dato, font=("Press Start 2P", 20))
        label.place(x=400, y=450 + i * 30)  # Separación vertical entre ellos
        
    if pokemon_elegido=="charmander.png": 
        label = ctk.CTkLabel(ventana, text="TIPO: Fuego", font=("Press Start 2P", 20))
        label.place(x=400, y=300)
    elif pokemon_elegido=="squirtle.png": 
        label = ctk.CTkLabel(ventana, text="TIPO: Agua", font=("Press Start 2P", 20))
        label.place(x=400, y=300)
    elif pokemon_elegido=="bulbasaur.png": 
        label = ctk.CTkLabel(ventana, text="TIPO: Planta", font=("Press Start 2P", 20))
        label.place(x=400, y=300)
        
        
   
        
# Crear ventana
ventana = ctk.CTk()
ventana.geometry("1000x800")
ventana.title("Ventana moderna con CustomTkinter")

imagen_fondo = Image.open("fondo_inicial.png")  # Asegúrate de tener esta imagen
imagen_fondo = imagen_fondo.resize((1000, 800))
imagen_tk = ImageTk.PhotoImage(imagen_fondo)

# Crear Label con imagen de fondo
fondo_label = ctk.CTkLabel(ventana, image=imagen_tk, text="")  # text="" para que no se superponga nada
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)


# Etiqueta
etiqueta = ctk.CTkLabel(ventana, text="¡Elegir pokemon!", font=("Arial", 100))
etiqueta.pack(pady=20)

ctk.CTkButton(ventana, text="Charmander", command=lambda: elegir_pokemon("charmander.png")).pack(pady=10)
ctk.CTkButton(ventana, text="Squirtle", command=lambda: elegir_pokemon("squirtle.png")).pack(pady=10)
ctk.CTkButton(ventana, text="Bulbasaur", command=lambda: elegir_pokemon("bulbasaur.png")).pack(pady=10)

# Crear botón
boton_salir = ctk.CTkButton(ventana, text="Salir", command=salir_programa)
boton_salir.pack(pady=20)
    


ventana.mainloop()
