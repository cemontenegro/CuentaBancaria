from cuentaBancaria import CuentaBancaria

class Usuario:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.cuenta = CuentaBancaria(tasa_interes=0.02,balance=0)

	def _metodo_ejemplo(self):
		pass