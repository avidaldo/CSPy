# Evolución de Arquitectura Bancaria

Este directorio contiene 4 versiones del mismo código de cuenta bancaria, mostrando cómo evoluciona la arquitectura desde código monolítico hasta una estructura profesional con paquetes.

## 📚 Material Didáctico

**Notebook principal**: [`../modules/07_progressive_architecture.ipynb`](../modules/07_progressive_architecture.ipynb)

Este notebook explica cada versión en detalle, introduciendo los principios de arquitectura limpia.

## 📁 Versiones

### v1_monolithic/ - Todo en un archivo
- ✅ Rápido de empezar
- ❌ Código mezclado
- ❌ Difícil de reutilizar
- **Archivo**: `bank.py` (150 líneas)

**Validación**: Solo formato IBAN con regex

### v2_functional/ - Funciones separadas
- ✅ Separación de responsabilidades (SoC)
- ✅ Funciones testeables
- ⚠️ Aún todo en un archivo
- **Archivo**: `bank.py` (180 líneas)

**Validación**: Solo formato IBAN con regex

### v3_modular/ - Módulos separados
- ✅ Código en múltiples archivos
- ✅ Módulo reutilizable
- ✅ Validación completa de IBAN (MOD-97)
- **Archivos**: `bank.py`, `validators.py`

**Validación**: Formato + checksum MOD-97

### v4_package/ - Estructura de paquete
- ✅ Arquitectura profesional
- ✅ Máxima escalabilidad
- ✅ Cada módulo una responsabilidad (SRP)
- **Estructura**:
  ```
  validators/
      __init__.py
      iban.py
      amount.py
  bank.py
  ```

**Validación**: Formato + checksum MOD-97

## 🎯 Principios Enseñados

| Principio | Descripción | Aplicado en |
|-----------|-------------|-------------|
| **DRY** | Don't Repeat Yourself | v2, v3, v4 |
| **SoC** | Separation of Concerns | v2, v3, v4 |
| **SRP** | Single Responsibility Principle | v4 |

## 🚀 Cómo Usar

### Ejecutar cada versión

```bash
# Versión 1
cd v1_monolithic
python bank.py

# Versión 2
cd v2_functional
python bank.py

# Versión 3
cd v3_modular
python bank.py

# Versión 4
cd v4_package
python bank.py
```

### Probar validadores independientemente

```bash
# v3
cd v3_modular
python validators.py

# v4
cd v4_package
python -m validators.iban
python -m validators.amount
```

## 📖 Flujo de Aprendizaje Recomendado

1. **Lee** el [notebook de OOP](../04-oop_basics.ipynb) primero
2. **Estudia** el [notebook de arquitectura progresiva](../modules/07_progressive_architecture.ipynb)
3. **Ejecuta** cada versión en orden (v1 → v2 → v3 → v4)
4. **Compara** los archivos para ver las diferencias
5. **Aplica** estos principios en tus propios proyectos

## 🔍 Diferencias Clave

### Importaciones

```python
# v1: No hay importaciones internas
import re

# v2: No hay importaciones internas
import re

# v3: Importa desde módulo
from validators import validate_iban

# v4: Importa desde paquete
from validators import validate_iban
# (internamente: from validators.iban import validate_iban)
```

### Validación IBAN

```python
# v1, v2: Solo formato
pattern = r'^ES\d{22}$'
return bool(re.match(pattern, iban))

# v3, v4: Formato + checksum MOD-97
def validate_iban(iban):
    return validate_iban_format(iban) and validate_iban_checksum(iban)
```

## 💡 Casos de Uso

| Versión | Cuándo Usar |
|---------|-------------|
| v1 | Scripts rápidos, prototipos, <100 líneas |
| v2 | Separar lógica, archivos <500 líneas |
| v3 | Proyectos medianos, código reutilizable |
| v4 | Proyectos grandes, librerías, múltiples colaboradores |

## 📝 Ejercicios Sugeridos

1. **Añade un nuevo validador** de DNI español en v4
2. **Refactoriza** código monolítico tuyo usando estos patrones
3. **Crea tests** para cada módulo de validación
4. **Extiende** para soportar IBANs de otros países (FR, DE, IT)

## 🔗 Referencias

- [Notebook 04: OOP Basics](../04-oop_basics.ipynb)
- [Notebook 07: Progressive Architecture](../modules/07_progressive_architecture.ipynb)
- [IBAN Validation Algorithm](https://en.wikipedia.org/wiki/International_Bank_Account_Number#Validating_the_IBAN)
- [Python Packages Documentation](https://docs.python.org/3/tutorial/modules.html#packages)
