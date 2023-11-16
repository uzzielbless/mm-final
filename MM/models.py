from django.db import models
class MM(models.Model):
    idproducto = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=100, verbose_name='Producto')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripción',null=True)
    precio = models.DecimalField(decimal_places=2, max_digits= 10, verbose_name='Precio',null=True)

# Create your models here.

class Almacen(models.Model):
    nproductos = models.AutoField(primary_key=True)
    tipoproducto = models.CharField(max_length=100, verbose_name='Tipo de producto')
    idproductofk = models.IntegerField(verbose_name='Id de producto', null=True)


class Aparatos(models.Model):
    n_aparato = models.AutoField(primary_key=True)
    uso = models.CharField(max_length=100, verbose_name='Uso')
    cve_rutinafk= models.IntegerField(verbose_name='Clave rutina', null=True)


class Cliente(models.Model):
    cve_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')   
    ape_pa = models.CharField(max_length=100, verbose_name='Apellido paterno')  
    ape_ma = models.CharField(max_length=100, verbose_name='Apellido Materno') 
    edad = models.IntegerField(verbose_name='Edad') 
    email = models.EmailField(verbose_name='Email')
    certi_med = models.CharField(max_length=100, verbose_name='Certificado médico')

class Trabajador(models.Model):
    cve_socio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')   
    ape_pa = models.CharField(max_length=100, verbose_name='Apellido paterno')  
    ape_ma = models.CharField(max_length=100, verbose_name='Apellido materno') 
    edad = models.IntegerField(verbose_name='Edad') 
    email = models.EmailField(verbose_name='Email')
    cliente_asig = models.CharField(max_length=100, verbose_name='Cliente asignado')
    horario = models.DateTimeField(verbose_name='Horario')
    salario = models.DecimalField(decimal_places=2, max_digits= 10, verbose_name='Salario')
    cve_clientefk= models.IntegerField(verbose_name='Clave cliente', null=True)


class Inventario(models.Model):
    cve_inventario = models.AutoField(primary_key=True)
    productostotales = models.IntegerField(verbose_name='Productos totales')   
    consumo = models.IntegerField(verbose_name='Consumo')  
    ganancia = models.DecimalField(decimal_places=2, max_digits= 10, verbose_name='Ganancia') 
    cantidadventa = models.DecimalField(decimal_places=2, max_digits= 10, verbose_name='Cantidad de venta') 
    cve_sociofk= models.IntegerField(verbose_name='Clave socio', null=True)


class Pedido(models.Model):
    cve_p = models.AutoField(primary_key=True)
    cantidad_ped = models.IntegerField(verbose_name='Cantidad pedido')   
    oferta_desc = models.DecimalField(decimal_places=2, max_digits= 10, verbose_name='Descuento')  
    totalP = models.DecimalField(decimal_places=2, max_digits= 10, verbose_name='Total') 
    idproductofk= models.IntegerField(verbose_name='Id de producto', null=True)
    numeropfk= models.IntegerField(verbose_name='Numero de producto',null=True)
    servicioreqfk= models.IntegerField(verbose_name='Servicio',null=True)
    cve_productofk= models.IntegerField(verbose_name='Clave del producto',null=True)

class Plan(models.Model):
    cve_pp = models.AutoField(primary_key=True)
    rutina = models.CharField(max_length=100, verbose_name='Rutina')   
    horario = models.DateTimeField(verbose_name='Horario')  
    instructor = models.CharField(max_length=100, verbose_name='Instructor',null=True) 
    costo_extra= models.DecimalField(decimal_places=2, max_digits= 10, verbose_name='Costo extra') 
    cve_clientefk= models.IntegerField(verbose_name='Clave cliente', null=True)


class PE(models.Model):
    servicioreq = models.AutoField(primary_key=True)
    refaccion = models.CharField(max_length=100, verbose_name='Refaccion')   
    costoserv = models.DecimalField(decimal_places=2, max_digits= 10, verbose_name='Costo del servicio')  
    total = models.DecimalField(decimal_places=2, max_digits= 10, verbose_name='Total') 


class PP(models.Model):
    cve_producto = models.AutoField(primary_key=True)
    costoproducto = models.DecimalField(decimal_places=2, max_digits= 10, verbose_name='Costo del producto')  
    total = models.DecimalField(decimal_places=2, max_digits= 10, verbose_name='Total') 


class Proveedores(models.Model):
    numerop = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100, verbose_name='Direccion')  
    telefono = models.IntegerField(verbose_name='Telefono') 
    servicioreqfk= models.IntegerField(verbose_name='Servicio requerido',null=True)
    cve_productofk= models.IntegerField(verbose_name='Clave del producto',null=True)


class Venta(models.Model):
    foliov = models.AutoField(primary_key=True)
    fecha = models.DateField(verbose_name='Fecha')  
    cve_producto = models.CharField(max_length=100, verbose_name='Clave del producto') 
    total = models.DecimalField(decimal_places=2, max_digits= 10, verbose_name='Total') 
    idproductofk= models.IntegerField(verbose_name='Id de producto',null=True)
    cve_clientefk= models.IntegerField(verbose_name='Clave cliente',null=True)


class Inscripcion(models.Model):
    folio = models.AutoField(primary_key=True)
    fecha= models.DateField(verbose_name='Fecha') 
    membresia = models.CharField(max_length=100, verbose_name='Membresia') 
    tipo_inscrip = models.CharField(max_length=100, verbose_name='Tipo de inscripción') 
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')  
    fecha_fin = models.DateField(verbose_name='Fecha de termino') 
    monto = models.DecimalField( decimal_places=2, max_digits= 10, verbose_name='Monto') 
    cve_clientefk= models.IntegerField(verbose_name='Clave cliente',null=True)


class Rutinas(models.Model):
    cve_rutina = models.AutoField(primary_key=True) 
    descripcion = models.CharField(max_length=100, verbose_name='Descripción') 
    cve_clientefk= models.IntegerField(verbose_name='Clave cliente',null=True)

class Registro(models.Model):
    tipo_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre') 
    telefono = models.IntegerField(verbose_name='Telefono') 
    email = models.EmailField(verbose_name='Email')   
    cve_sociofk= models.IntegerField(verbose_name='Clave socio',null=True) 


class Compra(models.Model):
    compra = models.AutoField(primary_key=True) 
    cantidad = models.CharField(max_length=100, verbose_name='Cantidad') 
    producto = models.CharField(max_length=100, verbose_name='Producto') 
    nombre = models.CharField(max_length=100, verbose_name='Nombre') 
    telefono = models.IntegerField(verbose_name='Telefono') 
     

