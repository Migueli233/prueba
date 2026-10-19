from pathlib import Path
archivo = Path("C:\\Users\\ADSO\\Desktop\\tienda-don-pedro\\datos\\productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()
print("=== Inventario Tienda Don Pedro ===")
for linea in lineas [1:]:
    print ("-", linea)

