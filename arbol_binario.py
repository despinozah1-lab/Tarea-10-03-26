import graphviz


# ==============================
# Clase Nodo
# ==============================
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


# ==============================
# Clase Arbol Binario de Busqueda
# ==============================
class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None

    # --------------------------
    # Insertar nodo
    # --------------------------
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):

        if valor < nodo.valor:

            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_rec(nodo.izquierda, valor)

        elif valor > nodo.valor:

            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_rec(nodo.derecha, valor)

    # --------------------------
    # Buscar nodo
    # --------------------------
    def buscar(self, valor):
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, nodo, valor):

        if nodo is None:
            return False

        if nodo.valor == valor:
            return True

        if valor < nodo.valor:
            return self._buscar_rec(nodo.izquierda, valor)

        else:
            return self._buscar_rec(nodo.derecha, valor)

    # --------------------------
    # Eliminar nodo
    # --------------------------
    def eliminar(self, valor):
        self.raiz = self._eliminar_rec(self.raiz, valor)

    def _eliminar_rec(self, nodo, valor):

        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_rec(nodo.izquierda, valor)

        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_rec(nodo.derecha, valor)

        else:

            # Caso 1: sin hijos
            if nodo.izquierda is None and nodo.derecha is None:
                return None

            # Caso 2: un hijo
            if nodo.izquierda is None:
                return nodo.derecha

            if nodo.derecha is None:
                return nodo.izquierda

            # Caso 3: dos hijos
            sucesor = self._minimo(nodo.derecha)
            nodo.valor = sucesor.valor
            nodo.derecha = self._eliminar_rec(nodo.derecha, sucesor.valor)

        return nodo

    def _minimo(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo

    # --------------------------
    # Cargar desde archivo
    # --------------------------
    def cargar_archivo(self, ruta):

        try:

            with open(ruta, "r") as archivo:

                for linea in archivo:

                    numero = int(linea.strip())
                    self.insertar(numero)

            print("Datos cargados correctamente.")

        except Exception as e:
            print("Error al leer archivo:", e)

    # --------------------------
    # Generar Graphviz
    # --------------------------
    def graficar(self):

        dot = graphviz.Digraph()

        self._graficar_rec(self.raiz, dot)

        dot.render("arbol_binario", format="png", view=True)

    def _graficar_rec(self, nodo, dot):

        if nodo is None:
            return

        dot.node(str(nodo.valor))

        if nodo.izquierda:
            dot.edge(str(nodo.valor), str(nodo.izquierda.valor))
            self._graficar_rec(nodo.izquierda, dot)

        if nodo.derecha:
            dot.edge(str(nodo.valor), str(nodo.derecha.valor))
            self._graficar_rec(nodo.derecha, dot)


# ==============================
# Menu CLI
# ==============================
def menu():

    arbol = ArbolBinarioBusqueda()

    while True:

        print("\n===== MENU ARBOL BINARIO =====")
        print("1. Insertar numero")
        print("2. Buscar numero")
        print("3. Eliminar numero")
        print("4. Cargar desde archivo")
        print("5. Visualizar arbol (Graphviz)")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            numero = int(input("Ingrese numero: "))
            arbol.insertar(numero)

        elif opcion == "2":

            numero = int(input("Numero a buscar: "))

            if arbol.buscar(numero):
                print("Numero encontrado")
            else:
                print("Numero NO encontrado")

        elif opcion == "3":

            numero = int(input("Numero a eliminar: "))
            arbol.eliminar(numero)

        elif opcion == "4":

            ruta = input("Ingrese ruta del archivo .txt: ")
            arbol.cargar_archivo(ruta)

        elif opcion == "5":

            arbol.graficar()

        elif opcion == "6":

            print("Saliendo del programa...")
            break

        else:
            print("Opcion invalida")


# ==============================
# Ejecutar programa
# ==============================
if __name__ == "__main__":
    menu()
