class Vista:
    def mostrar_tareas(self, tareas):
        if not tareas:
            print("No hay tareas.")
            return
        for i, tarea in enumerate(tareas):
            print(f"[{i}] {tarea}")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
