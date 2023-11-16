from django.contrib import admin
from .models import MM
admin.site.register(MM)

from .models import Almacen
admin.site.register(Almacen)

from .models import Aparatos
admin.site.register(Aparatos)

from .models import Cliente
admin.site.register(Cliente)

from .models import Inventario
admin.site.register(Inventario)

from .models import Pedido
admin.site.register(Pedido)

from .models import Plan
admin.site.register(Plan)

from .models import PE
admin.site.register(PE)

from .models import PP
admin.site.register(PP)

from .models import Proveedores
admin.site.register(Proveedores)

from .models import Trabajador
admin.site.register(Trabajador)

from .models import Venta
admin.site.register(Venta)

from .models import Inscripcion
admin.site.register(Inscripcion)

from .models import Rutinas
admin.site.register(Rutinas)

from .models import Registro
admin.site.register(Registro)


from .models import Compra
admin.site.register(Compra)