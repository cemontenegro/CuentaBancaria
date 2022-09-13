from usuarios import Usuario
from cuentaBancaria import CuentaBancaria

cuenta1 = CuentaBancaria(0.15, 100)
#print("Balance previo al deposito",cuenta1.balance)
cuenta1.deposito(300).deposito(500).deposito(400).retiro(300).generar_interes().mostrar_info_cuenta()
print("Balance previo al deposito", cuenta1.balance)

cuenta2 = CuentaBancaria(0.15, 50)


print(CuentaBancaria.todas_las_cuentas)
CuentaBancaria.imprimir_todas_cuentas()

# print("DESDE AQUI USUARIO CON CUENTA BANCARIAS")

#usuario1 = Usuario("marioBros", "mb@blbla.com")
#print(usuario1.__dict__)
#usuario1.cuenta.deposito(500).mostrar_info_cuenta()