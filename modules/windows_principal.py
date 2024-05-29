import tkinter as tk

def agregar_descripcion(diccionario, punto_ejecucion, descripcion):
    diccionario[punto_ejecucion] = descripcion
    log_text = f"Se agregó el punto de ejecución {punto_ejecucion} con la descripción: {descripcion}"
    registrar_log(log_text, log_textbox)  # Pasar log_textbox como argumento
    return diccionario

def registrar_log(log_text, textbox):
    # Inserta el nuevo texto al final del Text
    textbox.config(state=tk.NORMAL)  # Habilitar el Text para escribir
    textbox.insert(tk.END, log_text + "\n")
    textbox.config(state=tk.DISABLED)  # Deshabilitar el Text nuevamente
    # Hace que el scroll se mueva al final
    textbox.see(tk.END)

def main():
    global log_textbox
    
    root = tk.Tk()
    root.title("Mi Proyecto Tkinter")
    root.geometry("800x600")
    root.resizable(False, False)

    lbl = tk.Label(root, text="¡Hola, Mundo!")
    lbl.pack(pady=10)

    # Contenedor Frame para el Text y el Scrollbar
    log_frame = tk.Frame(root, bg="white", bd=2, relief=tk.SOLID)  # No es necesario deshabilitar el Frame
    log_frame.pack()

    # Scrollbar vertical
    scrollbar = tk.Scrollbar(log_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Textbox para el log
    global log_textbox  # Definir log_textbox globalmente
    log_textbox = tk.Text(log_frame, width=95, height=35, yscrollcommand=scrollbar.set)
    log_textbox.pack(pady=5)

    # Configura el scrollbar para que se mueva con el texto
    scrollbar.config(command=log_textbox.yview)

    registrar_log("P01" + "  " +"INICIA PROGRAMA", log_textbox)  # Pasar log_textbox como argumento

    root.mainloop()

if __name__ == "__main__":
    main()
