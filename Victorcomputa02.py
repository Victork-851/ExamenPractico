nom=input("ingrese su nombre")
cant=(int("Cuantos pantalones solicita"))
precio=(160.50)
subtotal=(precio*cant)
if cant>10:
    mensaje=("El descuento a pagar es: ",(int(subtotal * 0.25)))
    desc=(subtotal*0.25)
    total=(" El total a pagar es", (int(desc - subtotal)))
else: cant>7
    mensaje = ("El descuento a pagar es: ", (int(subtotal * 0.10)))
    desc=(subtotal*0.25)
    total=(" El total a pagar es",(int(desc-subtotal)))
else: subtotal>700
     mensaje=("el descuento es:",(int(subtotal * 0.05)))
     desc=(subtotal*0.25)
     total=(" El total a pagar es",(int(desc-subtotal)))
else:cant<7
  mensaje=("Total a Pagar es:",subtotal)

print(mensaje,desc)
