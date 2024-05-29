def agregar_descripcion(diccionario, punto_ejecucion, descripcion):
    diccionario[punto_ejecucion] = descripcion
    log_text = f"Se agregó el punto de ejecución {punto_ejecucion} con la descripción: {descripcion}"
    registrar_log(log_text)
    return diccionario

def registrar_log(log_text):
    # Inserta el nuevo texto al final del Text
    log_textbox.insert(tk.END, log_text + "\n")
    # Hace que el scroll se mueva al final
    log_textbox.see(tk.END)

def imprimir_numeros():
    for i in range(1, 151):
        registrar_log("Estoy en el ciclo: " + str(i))