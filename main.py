# busqueda binaria

def main():
    lista = [1, 2, 3, 5, 8, 9, 11]

    # encontrar b
    b = int(input("Buscar un numero en la lista > "))

    # print the array and b
    print(f"- Lista: {lista}\n- Numero a encontrar: {b}")


    found = False  # determines whether the number was found
    start_index = 1
    end_index = len(lista) - 1

    # funcion de buscar
    while end_index > start_index:
        mid_index = (end_index + start_index - 1) // 2
        if lista[mid_index] == b:
            found = True
            break
        elif lista[mid_index] > b:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

    # resultado
    if found:
        print(f"\nResultado:\nEl numero {b} si existe en la lista!")
    else:
        print(f"\nResultado:\nEl numero {b} no existe en la lista!")

if __name__ == "__main__":
    main()