# a. Clases de la jerarquía multimedia

class Documento:
    def __init__(self, titulo: str, autores: str, ano_publicacion: int):
        self._titulo = titulo
        self._autores = autores
        self._ano_publicacion = ano_publicacion

    def getTitulo(self): return self._titulo
    def getAutores(self): return self._autores
    def getAnoPublicacion(self): return self._ano_publicacion

    def __str__(self):
        return f"Documento: '{self._titulo}', Autor(es): {self._autores}, Año: {self._ano_publicacion}"


class Libro(Documento):
    def __init__(self, titulo: str, autores: str, ano_publicacion: int, editorial: str):
        super().__init__(titulo, autores, ano_publicacion)
        self._editorial = editorial

    def getEditorial(self): return self._editorial

    def __str__(self):
        return f"Libro: '{self._titulo}', Autor(es): {self._autores}, Editorial: {self._editorial}, Año: {self._ano_publicacion}"


class Revista(Libro):
    def __init__(self, titulo: str, autores: str, ano_publicacion: int, editorial: str, volumen: int, numero: int, mes_salida: str):
        super().__init__(titulo, autores, ano_publicacion, editorial)
        self._volumen = volumen
        self._numero = numero
        self._mes_salida = mes_salida

    def getVolumen(self): return self._volumen
    def getNumero(self): return self._numero
    def getMesSalida(self): return self._mes_salida

    def __str__(self):
        return f"Revista: '{self._titulo}', Vol: {self._volumen}, Nro: {self._numero}, Mes: {self._mes_salida}, Editorial: {self._editorial}, Año: {self._ano_publicacion}"


class DocumentoCD(Documento):
    def __init__(self, titulo: str, autores: str, ano_publicacion: int, formato_cd: str, tipo_licencia: str, tipo_contenido: str):
        super().__init__(titulo, autores, ano_publicacion)
        self._formato_cd = formato_cd
        self._tipo_licencia = tipo_licencia
        self._tipo_contenido = tipo_contenido  # "Libros" o "Software"

    def getFormatoCD(self): return self._formato_cd
    def getTipoLicencia(self): return self._tipo_licencia
    def getTipoContenido(self): return self._tipo_contenido

    def __str__(self):
        return f"CD ({self._tipo_contenido}): '{self._titulo}', Formato: {self._formato_cd}, Licencia: {self._tipo_licencia}, Año: {self._ano_publicacion}"


class RevistaInvestigacion(Revista):
    def __init__(self, titulo: str, autores: str, ano_publicacion: int, editorial: str, volumen: int, numero: int, mes_salida: str, campo_investigacion: str):
        super().__init__(titulo, autores, ano_publicacion, editorial, volumen, numero, mes_salida)
        self._campo_investigacion = campo_investigacion

    def getCampoInvestigacion(self): return self._campo_investigacion

    def __str__(self):
        return f"Revista Investigación: '{self._titulo}', Campo: {self._campo_investigacion}, Vol: {self._volumen}, Nro: {self._numero}, Año: {self._ano_publicacion}"


class Biblioteca:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._documentos = []

    def agregarDocumento(self, doc: Documento):
        self._documentos.append(doc)

    def eliminarDocumento(self, doc: Documento):
        if doc in self._documentos:
            self._documentos.remove(doc)

    def getNombre(self): return self._nombre
    def getDocumentos(self): return self._documentos

    def contarDocumentos(self) -> int:
        return len(self._documentos)

    def contarRevistas(self) -> int:
        return sum(1 for d in self._documentos if isinstance(d, Revista))

    def contarLibros(self) -> int:
        return sum(1 for d in self._documentos if isinstance(d, Libro) and not isinstance(d, Revista))

    def mostrarContenido(self):
        print(f"\n--- Contenido de {self._nombre} ({len(self._documentos)} documentos) ---")
        for doc in self._documentos:
            print("  *", doc)

    # d. Copia de seguridad dato a dato
    def copiaDeSeguridad(self, nuevo_nombre: str) -> 'Biblioteca':
        copia_bib = Biblioteca(nuevo_nombre)
        for doc in self._documentos:
            # Creación dato a dato de un nuevo objeto independiente según su tipo
            if isinstance(doc, RevistaInvestigacion):
                nuevo_doc = RevistaInvestigacion(doc.getTitulo(), doc.getAutores(), doc.getAnoPublicacion(),
                                                 doc.getEditorial(), doc.getVolumen(), doc.getNumero(),
                                                 doc.getMesSalida(), doc.getCampoInvestigacion())
            elif isinstance(doc, Revista):
                nuevo_doc = Revista(doc.getTitulo(), doc.getAutores(), doc.getAnoPublicacion(),
                                    doc.getEditorial(), doc.getVolumen(), doc.getNumero(), doc.getMesSalida())
            elif isinstance(doc, Libro):
                nuevo_doc = Libro(doc.getTitulo(), doc.getAutores(), doc.getAnoPublicacion(), doc.getEditorial())
            elif isinstance(doc, DocumentoCD):
                nuevo_doc = DocumentoCD(doc.getTitulo(), doc.getAutores(), doc.getAnoPublicacion(),
                                        doc.getFormatoCD(), doc.getTipoLicencia(), doc.getTipoContenido())
            else:
                nuevo_doc = Documento(doc.getTitulo(), doc.getAutores(), doc.getAnoPublicacion())
            
            copia_bib.agregarDocumento(nuevo_doc)
        return copia_bib


# b. Método que muestra quién tiene más revistas y quién más documentos
def comparar_bibliotecas(b1: Biblioteca, b2: Biblioteca):
    print("\n=== Inciso B: Comparación entre Bibliotecas ===")
    r1, r2 = b1.contarRevistas(), b2.contarRevistas()
    d1, d2 = b1.contarDocumentos(), b2.contarDocumentos()

    # Muestra de Revistas
    if r1 > r2:
        print(f"Biblioteca con MÁS REVISTAS: {b1.getNombre()} ({r1} vs {r2})")
    elif r2 > r1:
        print(f"Biblioteca con MÁS REVISTAS: {b2.getNombre()} ({r2} vs {r1})")
    else:
        print(f"Ambas tienen la misma cantidad de revistas ({r1})")

    # Muestra de Documentos Totales
    if d1 > d2:
        print(f"Biblioteca con MÁS DOCUMENTOS: {b1.getNombre()} ({d1} vs {d2})")
    elif d2 > d1:
        print(f"Biblioteca con MÁS DOCUMENTOS: {b2.getNombre()} ({d2} vs {d1})")
    else:
        print(f"Ambas tienen la misma cantidad total de documentos ({d1})")


# c. Trasladar todas las revistas a la primera biblioteca y todos los libros a la segunda
def trasladar_recursos(b1: Biblioteca, b2: Biblioteca):
    print("\n=== Inciso C: Traslado de Revistas a B1 y Libros a B2 ===")
    
    # 1. Mover revistas de B2 hacia B1
    revistas_b2 = [d for d in b2.getDocumentos() if isinstance(d, Revista)]
    for rev in revistas_b2:
        b2.eliminarDocumento(rev)
        b1.agregarDocumento(rev)

    # 2. Mover libros (libros en papel no revistas) de B1 hacia B2
    libros_b1 = [d for d in b1.getDocumentos() if isinstance(d, Libro) and not isinstance(d, Revista)]
    for lib in libros_b1:
        b1.eliminarDocumento(lib)
        b2.agregarDocumento(lib)


# Pruebas e Instanciaciones
b1 = Biblioteca("Biblioteca Central UMSA")
b2 = Biblioteca("Biblioteca de Informática")

# Documentos para B1
l1 = Libro("Cien Años de Soledad", "G. García Márquez", 1967, "Sudamericana")
r1 = Revista("National Geographic", "Varios", 2023, "RBA", 150, 4, "Abril")
cd1 = DocumentoCD("Linux Ubuntu 24.04", "Canonical", 2024, "ISO-9660", "GPL", "Software")

b1.agregarDocumento(l1)
b1.agregarDocumento(r1)
b1.agregarDocumento(cd1)

# Documentos para B2
l2 = Libro("Estructuras de Datos", "Efraín Oviedo", 2015, "ECOE")
r2 = Revista("IEEE Software", "IEEE", 2022, "IEEE", 39, 2, "Marzo")
rev_inv1 = RevistaInvestigacion("IA y Algoritmos", "D. Liang", 2023, "Pearson", 12, 1, "Enero", "Inteligencia Artificial")

b2.agregarDocumento(l2)
b2.agregarDocumento(r2)
b2.agregarDocumento(rev_inv1)

# b. Mostrar comparación
comparar_bibliotecas(b1, b2)

# Estado inicial
b1.mostrarContenido()
b2.mostrarContenido()

# c. Traslado
trasladar_recursos(b1, b2)

print("\n--- Después del Traslado ---")
b1.mostrarContenido()
b2.mostrarContenido()

# d. Copia de seguridad dato a dato
backup_b1 = b1.copiaDeSeguridad("Backup - Biblioteca Central")
backup_b2 = b2.copiaDeSeguridad("Backup - Biblioteca Informática")

print("\n=== Inciso D: Copia de Seguridad Realizada ===")
backup_b1.mostrarContenido()
backup_b2.mostrarContenido()