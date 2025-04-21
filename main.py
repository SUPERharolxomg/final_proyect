from datetime import datetime
from controller.controller import Controller

def main():
    c = Controller()
    while True:
        try:
            print("\n--- MENÚ ---")
            print("1. Ver tareas")
            print("2. Agregar tarea")
            print("3. Completar tarea")
            print("4. Eliminar tarea")
            print("5. Salir")
            opcion = input("Selecciona una opción: ").strip()

            if opcion == '1':
                c.mostrar_tareas()
            elif opcion == '2':
                titulo = input("Título: ")
                descripcion = input("Descripción: ")
                fecha = input("Fecha límite (YYYY-MM-DD): ")
                try:
                    datetime.strptime(fecha, "%Y-%m-%d")
                    c.agregar_tarea(titulo, descripcion, fecha)
                except ValueError:
                    print("Formato de fecha incorrecto.")
            elif opcion == '3':
                indice = input("Índice de la tarea a completar: ")
                if indice.isdigit():
                    c.completar_tarea(int(indice))
                else:
                    print("Por favor, introduce un número válido.")
            elif opcion == '4':
                indice = input("Índice de la tarea a eliminar: ")
                if indice.isdigit():
                    c.eliminar_tarea(int(indice))
                else:
                    print("Por favor, introduce un número válido.")
            elif opcion == '5':
                print("Saliendo de la aplicación.")
                break
            else:
                print("Opción inválida.")
        except (KeyboardInterrupt, EOFError):
            print("\nAplicación interrumpida por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ocurrió un error crítico: {e}")
