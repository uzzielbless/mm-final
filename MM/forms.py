from django import forms
from .models import MM
class MMForm (forms.ModelForm):
    class Meta:
        model= MM
        fields='__all__'

from .models import Almacen
class AlmacenForm (forms.ModelForm):
    class Meta:
        model= Almacen
        fields='__all__'


from .models import Aparatos
class AparatosForm (forms.ModelForm):
    class Meta:
        model= Aparatos
        fields='__all__'

from .models import Cliente
class ClienteForm (forms.ModelForm):
    class Meta:
        model= Cliente
        fields='__all__'

from .models import Inventario
class InventarioForm (forms.ModelForm):
    class Meta:
        model= Inventario
        fields='__all__'

from .models import Pedido
class PedidoForm (forms.ModelForm):
    class Meta:
        model= Pedido
        fields='__all__'

from .models import Plan
class PlanForm (forms.ModelForm):
    class Meta:
        model= Plan
        fields='__all__'

from .models import PE
class PEForm (forms.ModelForm):
    class Meta:
        model= PE
        fields='__all__'

from .models import PP
class PPForm (forms.ModelForm):
    class Meta:
        model= PP
        fields='__all__'

from .models import Proveedores
class ProveedoresForm (forms.ModelForm):
    class Meta:
        model= Proveedores
        fields='__all__'

from .models import Trabajador
class TrabajadorForm (forms.ModelForm):
    class Meta:
        model= Trabajador
        fields='__all__'

from .models import Venta
class VentaForm (forms.ModelForm):
    class Meta:
        model= Venta
        fields='__all__'

from .models import Inscripcion
class InscripcionForm (forms.ModelForm):
    class Meta:
        model= Inscripcion
        fields='__all__'

from .models import Rutinas
class RutinasForm (forms.ModelForm):
    class Meta:
        model= Rutinas
        fields='__all__'

from .models import Registro
class RegistroForm (forms.ModelForm):
    class Meta:
        model= Registro
        fields='__all__'


from .models import Compra
class CompraForm (forms.ModelForm):
    class Meta:
        model= Compra
        fields='__all__'

