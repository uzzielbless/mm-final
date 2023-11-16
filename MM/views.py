from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MM
from .forms import MMForm
from .models import Almacen
from .forms import AlmacenForm
from .models import Aparatos
from .forms import AparatosForm
from .models import Cliente
from .forms import ClienteForm
from .models import Inventario
from .forms import InventarioForm
from .models import Pedido
from .forms import PedidoForm
from .models import Plan
from .forms import PlanForm
from .models import PE
from .forms import PEForm
from .models import PP
from .forms import PPForm
from .models import Proveedores
from .forms import ProveedoresForm
from .models import Trabajador
from .forms import TrabajadorForm
from .models import Venta
from .forms import VentaForm
from .models import Inscripcion
from .forms import InscripcionForm
from .models import Rutinas
from .forms import RutinasForm
from .models import Registro
from .forms import RegistroForm
from .models import Compra
from .forms import CompraForm


def inicio(request):
    return HttpResponse("<h1> Hola mundo </h1>")

def inicio(request):
    return render(request, 'inicio.html')

def index(request):
    mm= MM.objects.all()
    return render(request, 'index.html', {'mm':mm})

def crear(request):
    formulario = MMForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index')
    return render (request, 'crear.html', {'formulario':formulario})

def eliminar (request,idproducto):
    mm = MM.objects.get(idproducto=idproducto)
    mm.delete()
    return redirect ('index')



def QuienesS(request):
    return render(request, 'QuienesS.html')

def ubicacion(request):
    return render(request, 'ubicacion.html')

def CVitae(request):
    return render(request, 'CVitae.html')

def formsIn(request):
    return render(request, 'formsIn.html')

#FORMULARIOS

#almacen
def index_almacen(request):
    almacen= Almacen.objects.all()
    return render(request, 'index_almacen.html', {'almacen':almacen})

def almacen(request):
    formulario = AlmacenForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_almacen')
    return render (request, 'almacen.html', {'formulario':formulario})

def eliminarAlmacen (request,nproductos):
    almacen = Almacen.objects.get(nproductos=nproductos)
    almacen.delete()
    return redirect ('index_almacen')

#aparatos
def index_aparatos(request):
    aparatos= Aparatos.objects.all()
    return render(request, 'index_aparatos.html', {'aparatos':aparatos})

def aparatos(request):
    formulario = AparatosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_aparatos')
    return render (request, 'aparatos.html', {'formulario':formulario})

def eliminarAparatos (request,n_aparato):
    aparatos = Aparatos.objects.get(n_aparato=n_aparato)
    aparatos.delete()
    return redirect ('index_aparatos')

#cliente
def index_cliente(request):
    cliente= Cliente.objects.all()
    return render(request, 'index_cliente.html', {'cliente':cliente})

def cliente(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_cliente')
    return render (request, 'cliente.html', {'formulario':formulario})

def eliminarCliente (request,cve_cliente):
    cliente = Cliente.objects.get(cve_cliente=cve_cliente)
    cliente.delete()
    return redirect ('index_cliente')


#inventario
def index_inventario(request):
    inventario= Inventario.objects.all()
    return render(request, 'index_inventario.html', {'inventario':inventario})

def inventario(request):
    formulario = InventarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_inventario')
    return render (request, 'inventario.html', {'formulario':formulario})

def eliminarInventario (request, cve_inventario):
    inventario = Inventario.objects.get(cve_inventario=cve_inventario)
    inventario.delete()
    return redirect ('index_inventario')


#pedido
def index_pedido(request):
    pedido= Pedido.objects.all()
    return render(request, 'index_pedido.html', {'pedido':pedido})

def pedido(request):
    formulario = PedidoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_pedido')
    return render (request, 'pedido.html', {'formulario':formulario})

def eliminarPedido (request,cve_p):
    pedido = Pedido.objects.get(cve_p=cve_p)
    pedido.delete()
    return redirect ('index_pedido')



#plan_p
def index_plan_p(request):
    plan= Plan.objects.all()
    return render(request, 'index_plan_p.html', {'plan':plan})

def plan_p(request):
    formulario = PlanForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_plan_p')
    return render (request, 'plan_p.html', {'formulario':formulario})

def eliminarPlan (request,cve_pp):
    plan = Plan.objects.get(cve_pp=cve_pp)
    plan.delete()
    return redirect ('index_plan_p')


#proveedor equipo
def index_proveedor_equipo(request):
    pequipo= PE.objects.all()
    return render(request, 'index_proveedor_equipo.html', {'pequipo':pequipo})

def proveedor_equipo(request):
    formulario = PEForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_proveedor_equipo')
    return render (request, 'proveedor_equipo.html', {'formulario':formulario})

def eliminarPE (request,servicioreq):
    pequipo = PE.objects.get(servicioreq=servicioreq)
    pequipo.delete()
    return redirect ('index_proveedor_equipo')


#proveedor producto
def index_proveedor_producto(request):
    pproducto= PP.objects.all()
    return render(request, 'index_proveedor_producto.html', {'pproducto':pproducto})

def proveedor_producto(request):
    formulario = PPForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_proveedor_producto')
    return render (request, 'proveedor_producto.html', {'formulario':formulario})

def eliminarPP (request,cve_producto):
    pproducto = PP.objects.get(cve_producto=cve_producto)
    pproducto.delete()
    return redirect ('index_proveedor_producto')

#proveedores
def index_proveedores(request):
    proveedores= Proveedores.objects.all()
    return render(request, 'index_proveedores.html', {'proveedores':proveedores})

def proveedores(request):
    formulario = ProveedoresForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_proveedores')
    return render (request, 'proveedores.html', {'formulario':formulario})

def eliminarProveedor (request,numerop):
    proveedores = Proveedores.objects.get(numerop=numerop)
    proveedores.delete()
    return redirect ('index_proveedores')


#trabajador
def index_trabajador(request):
    trabajador= Trabajador.objects.all()
    return render(request, 'index_trabajador.html', {'trabajador':trabajador})

def trabajador(request):
    formulario = TrabajadorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_trabajador')
    return render (request, 'trabajador.html', {'formulario':formulario})

def eliminarTrabajador (request,cve_socio):
    trabajador = Trabajador.objects.get(cve_socio=cve_socio)
    trabajador.delete()
    return redirect ('index_trabajador')


#venta
def index_venta(request):
    venta= Venta.objects.all()
    return render(request, 'index_venta.html', {'venta':venta})

def venta(request):
    formulario = VentaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_venta')
    return render (request, 'venta.html', {'formulario':formulario})

def eliminarVenta (request,foliov):
    venta = Venta.objects.get(foliov=foliov)
    venta.delete()
    return redirect ('index_venta')


#inscripcion
def index_inscripcion(request):
    inscripcion= Inscripcion.objects.all()
    return render(request, 'index_inscripcion.html', {'inscripcion':inscripcion})

def inscripcion(request):
    formulario = InscripcionForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_inscripcion')
    return render (request, 'inscripcion.html', {'formulario':formulario})

def eliminarInscripcion (request,folio):
    inscripcion = Inscripcion.objects.get(folio=folio)
    inscripcion.delete()
    return redirect ('index_inscripcion')


#rutinas
def index_rutinas(request):
    rutinas= Rutinas.objects.all()
    return render(request, 'index_rutinas.html', {'rutinas':rutinas})

def rutinas(request):
    formulario = RutinasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_rutinas')
    return render (request, 'rutinas.html', {'formulario':formulario})

def eliminarRutina (request,cve_rutina):
    rutinas = Rutinas.objects.get(cve_rutina=cve_rutina)
    rutinas.delete()
    return redirect ('index_rutinas')


#registro
def index_registro(request):
    registro= Registro.objects.all()
    return render(request, 'index_registro.html', {'registro':registro})

def registro(request):
    formulario = RegistroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_registro')
    return render (request, 'registro.html', {'formulario':formulario})

def eliminarRegistro (request,tipo_usuario):
    registro = Registro.objects.get(tipo_usuario=tipo_usuario)
    registro.delete()
    return redirect ('index_registro')


def index_compra(request):
    compra= Compra.objects.all()
    return render(request, 'index_compra.html', {'compra':compra})

def compra(request):
    formulario = CompraForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect ('index_compra')
    return render (request, 'compra.html', {'formulario':formulario})