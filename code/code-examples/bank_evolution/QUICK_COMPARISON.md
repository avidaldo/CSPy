# Comparación Rápida: v1 vs v2 vs v3 vs v4

## Tabla de Decisión Rápida

| Criterio | v1 | v2 | v3 | v4 | Recomendación |
|----------|----|----|----|----|---------------|
| **Líneas de código total** | <150 | <200 | <500 | >500 | Empieza v1, evoluciona según crezca |
| **Número de archivos** | 1 | 1 | 2-3 | 4+ | Más archivos = mejor organización |
| **Reutilización** | ❌ | ⚠️ | ✅ | ✅✅ | v3+ para código reutilizable |
| **Trabajo en equipo** | ❌ | ⚠️ | ✅ | ✅✅ | v3+ para múltiples desarrolladores |
| **Complejidad validación** | Básica | Básica | Completa | Completa | MOD-97 solo en v3+ |
| **Tiempo implementación** | 30 min | 45 min | 1-2h | 2-3h | Más tiempo = mejor arquitectura |
| **Facilidad de testing** | ❌ | ✅ | ✅✅ | ✅✅ | v2+ permite tests unitarios |
| **Principios aplicados** | - | SoC | SoC+DRY | SoC+DRY+SRP | Más principios = código más limpio |

## Cuándo Usar Cada Versión

### ✅ Usa v1 si:
- [ ] Estás prototipando rápido
- [ ] Es un script de una sola vez
- [ ] El código no superará 150 líneas
- [ ] Solo tú trabajarás en esto
- [ ] No necesitas reutilizar el código

### ✅ Usa v2 si:
- [ ] Identificaste código duplicado en v1
- [ ] Quieres separar lógica de validación
- [ ] El código está entre 150-500 líneas
- [ ] Quieres empezar a aplicar buenas prácticas
- [ ] Aún es un proyecto pequeño/mediano

### ✅ Usa v3 si:
- [ ] La validación es compleja (ej: MOD-97)
- [ ] Quieres reutilizar validadores en otros proyectos
- [ ] El proyecto tiene >500 líneas
- [ ] Varias personas trabajan en el código
- [ ] Necesitas organización clara

### ✅ Usa v4 si:
- [ ] Tienes múltiples tipos de validaciones
- [ ] El módulo de validación crece demasiado
- [ ] Vas a distribuir esto como librería
- [ ] Necesitas estructura escalable
- [ ] Aplicas SOLID en serio

## Código Comparado

### Crear una cuenta

```python
# v1
account = BankAccount("ES9121000418450200051332", 1000)
# Validación: solo formato (regex)

# v2
account = BankAccount("ES9121000418450200051332", 1000)
# Validación: solo formato (regex) pero en función separada

# v3
account = BankAccount("ES9121000418450200051332", 1000)
# Validación: formato + checksum MOD-97

# v4
account = BankAccount("ES9121000418450200051332", 1000)
# Validación: formato + checksum MOD-97 (misma funcionalidad que v3)
```

**Diferencia clave v1/v2 vs v3/v4**: Solo v3 y v4 validan el checksum

### Validar IBAN directamente

```python
# v1
# ❌ No puedes - está dentro de la clase
account = BankAccount(iban, balance)  # Solo aquí se valida

# v2
# ⚠️ Puedes pero limitado
from bank import validate_iban_format
if validate_iban_format("ES123"):  # Solo formato
    ...

# v3
# ✅ Puedes y completo
from validators import validate_iban
if validate_iban("ES9121000418450200051332"):  # Formato + checksum
    ...

# v4
# ✅✅ Puedes, completo y organizado
from validators import validate_iban
if validate_iban("ES9121000418450200051332"):  # Formato + checksum
    ...
```

### Añadir nueva validación (ej: DNI)

```python
# v1
# Añadir método en BankAccount
class BankAccount:
    def _is_valid_dni(self, dni):
        # ❌ Responsabilidad incorrecta

# v2
# Añadir función global
def validate_dni(dni):
    # ⚠️ Archivo crece

# v3
# Añadir en validators.py
def validate_dni(dni):
    # ⚠️ Módulo crece

# v4
# Crear validators/dni.py
def validate_dni(dni):
    # ✅✅ Cada tipo su módulo
```

## Importaciones

```python
# v1
import re
# Todo interno

# v2
import re
# Todo en el mismo archivo

# v3
from validators import validate_iban, validate_positive_amount
import re  # solo en validators.py

# v4
from validators import validate_iban, validate_positive_amount
# validators/__init__.py gestiona las importaciones internas
```

## Estructura de Directorios

```
v1/
└── bank.py                     (todo aquí)

v2/
└── bank.py                     (funciones + clase)

v3/
├── validators.py               (todas las validaciones)
└── bank.py                     (solo lógica bancaria)

v4/
├── validators/
│   ├── __init__.py            (exporta funciones)
│   ├── iban.py                (validación IBAN)
│   └── amount.py              (validación cantidades)
└── bank.py                     (solo lógica bancaria)
```

## Señales de que Necesitas Evolucionar

### De v1 a v2
🚨 Copias y pegas código de validación  
🚨 La clase `BankAccount` tiene métodos que no son sobre "cuenta"  
🚨 Quieres testear validación sin crear cuenta completa  

### De v2 a v3
🚨 El archivo supera 300-500 líneas  
🚨 Necesitas validación compleja (MOD-97)  
🚨 Quieres usar validadores en otro proyecto  
🚨 Difícil encontrar funciones en el archivo  

### De v3 a v4
🚨 El módulo `validators.py` supera 500 líneas  
🚨 Tienes muchos tipos de validación diferentes  
🚨 Quieres distribuir como librería  
🚨 Necesitas subcategorías (iban, tarjeta, dni, email...)  

## Ejemplos de IBANs para Probar

```python
# Válidos (formato + checksum correcto)
"ES9121000418450200051332"  # ✅ v1, v2, v3, v4
"ES7921000813610123456789"  # ✅ v1, v2, v3, v4

# Formato correcto pero checksum incorrecto
"ES1234567890123456789012"  # ✅ v1, v2 | ❌ v3, v4

# Formato incorrecto
"ES123"                      # ❌ Todas las versiones
"FR1234567890123456789012"  # ❌ Todas (solo soportan ES)
```

## Tests Que Deberían Pasar

```python
# Todos deben pasar
assert BankAccount("ES9121000418450200051332", 1000)  # OK

# v1, v2 pasan | v3, v4 fallan
try:
    BankAccount("ES1234567890123456789012", 1000)
    print("v1 o v2: acepta checksum incorrecto")
except ValueError:
    print("v3 o v4: rechaza checksum incorrecto")

# Todas fallan
try:
    BankAccount("ES123", 1000)
    print("ERROR: debería fallar")
except ValueError:
    print("OK: formato inválido detectado")
```

## Complejidad del Código

### Cyclomatic Complexity (aproximado)

| Función/Método | v1 | v2 | v3 | v4 |
|----------------|----|----|----|----|
| validate_iban | 2 | 2 | 8 | 8 |
| BankAccount.__init__ | 4 | 4 | 3 | 3 |
| Total módulo bank | 15 | 18 | 12 | 12 |
| Total validación | - | - | 10 | 10 |

**Interpretación**: Complejidad individual baja, pero total distribuida mejor en v3/v4

## Métricas de Mantenibilidad

| Métrica | v1 | v2 | v3 | v4 |
|---------|----|----|----|----|
| Acoplamiento | Alto | Medio | Bajo | Muy Bajo |
| Cohesión | Baja | Media | Alta | Muy Alta |
| Testabilidad | Baja | Alta | Muy Alta | Muy Alta |
| Reutilización | 0% | 30% | 80% | 95% |
| Mantenibilidad | 40% | 60% | 80% | 90% |

## Resumen: ¿Cuál Elegir?

```
Proyecto Personal Pequeño (<500 líneas)    → v1 o v2
Proyecto Mediano (500-2000 líneas)         → v3
Proyecto Grande (>2000 líneas)             → v4
Librería para Distribuir                   → v4
Aprendiendo arquitectura                   → Empieza v1, evoluciona a v4
```

## Tiempo de Desarrollo Estimado

```
v1: 30 minutos  (empezar rápido)
v2: +15 minutos (refactorizar a funciones)
v3: +1 hora     (crear módulo, implementar MOD-97)
v4: +1 hora     (crear paquete, organizar submódulos)

Total acumulado:
v1: 30 min
v2: 45 min
v3: 1h 45min
v4: 2h 45min
```

**Conclusión**: La inversión de tiempo vale la pena en proyectos grandes o reutilizables.

---

**Usa esta tabla como referencia rápida al decidir cómo organizar tu código.**
