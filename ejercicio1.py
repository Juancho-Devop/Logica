import time

def generacion(edad, gen_num):
    print(f"Generación {gen_num} (Edad: {edad}) comienza")
    
    if gen_num < 3:
        # Llamada recursiva para la siguiente generación
        generacion(edad - 15, gen_num + 1)
    
    for _ in range(edad):
        print(f"Generación {gen_num} (Edad: {edad}) está viviendo...")
        time.sleep(1)  # Simula el paso de un año
        edad -= 1
    
    print(f"Generación {gen_num} ha terminado su vida")

if __name__ == "__main__":
    generacion(75, 1)