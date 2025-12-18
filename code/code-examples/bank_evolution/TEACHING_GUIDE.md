# Guía Pedagógica: Arquitectura Progresiva con IBAN

## 🎓 Visión General del Material Creado

Este material enseña evolución de arquitectura de software usando cuentas bancarias con validación IBAN como ejemplo práctico.

## 📂 Estructura Completa

```
CSPy/
├── code/
│   ├── 04-oop_basics.ipynb                    ← Prerrequisito (ya existía)
│   ├── modules/
│   │   └── 07_progressive_architecture.ipynb  ← NUEVO: Notebook principal
│   └── code-examples/
│       └── bank_evolution/                    ← NUEVO: Ejemplos progresivos
│           ├── README.md                      ← NUEVO: Guía de uso
│           ├── v1_monolithic/
│           │   └── bank.py                    ← Todo en una clase
│           ├── v2_functional/
│           │   └── bank.py                    ← Funciones separadas
│           ├── v3_modular/
│           │   ├── bank.py                    ← Clase principal
│           │   └── validators.py              ← Módulo de validación (con MOD-97)
│           └── v4_package/
│               ├── bank.py                    ← Clase principal
│               └── validators/                ← Paquete estructurado
│                   ├── __init__.py
│                   ├── iban.py                ← Validación IBAN
│                   └── amount.py              ← Validación cantidades
```

## 🎯 Objetivos Pedagógicos

### Conceptos Enseñados

1. **Evolución de Código**
   - De monolítico a modular
   - Cuándo y cómo refactorizar
   - Señales de código que necesita organización

2. **Principios de Arquitectura**
   - **DRY** (Don't Repeat Yourself) - No duplicar código
   - **SoC** (Separation of Concerns) - Separar responsabilidades
   - **SRP** (Single Responsibility Principle) - Una responsabilidad por módulo

3. **Organización Python**
   - Funciones vs métodos
   - Módulos (.py files)
   - Paquetes (directorios con __init__.py)
   - Importaciones limpias

4. **Validación Real**
   - IBANs españoles (ES + 22 dígitos)
   - Algoritmo MOD-97 para checksum
   - Diferencia entre formato y validación completa

## 🚀 Flujo de Aprendizaje

### Para Estudiantes

```
1. Estudiar OOP Basics (04-oop_basics.ipynb)
   └─> Entender clases, métodos, self
   
2. Leer Progressive Architecture (07_progressive_architecture.ipynb)
   └─> Ver evolución conceptual con ejemplos
   
3. Ejecutar versiones en orden (v1 → v2 → v3 → v4)
   └─> Comparar código real
   
4. Aplicar en proyectos propios
   └─> Reconocer cuándo refactorizar
```

### Para Profesores

```
Sesión 1: Introducción
├─> Revisar conceptos OOP del notebook 04
├─> Mostrar ejemplo v1 (todo junto)
└─> Discutir: ¿Qué problemas ves?

Sesión 2: Principio SoC
├─> Introducir Separation of Concerns
├─> Refactorizar v1 → v2 en vivo
└─> Ejercicio: estudiantes identifican responsabilidades

Sesión 3: Módulos y DRY
├─> Explicar MOD-97 (complejidad que justifica módulo)
├─> Mostrar v3 con módulo separado
└─> Ejercicio: crear validador de email en módulo

Sesión 4: Paquetes y SRP
├─> Introducir Single Responsibility Principle
├─> Mostrar v4 con estructura de paquete
└─> Proyecto: refactorizar código propio
```

## 💡 Casos de Uso por Versión

### v1 - Monolítica
**Contexto**: Prototipo rápido de MVP

```python
# Un solo archivo, validación básica
class BankAccount:
    def _is_valid_iban(self, iban):
        pattern = r'^ES\d{22}$'
        return bool(re.match(pattern, iban))
```

**Ventajas**: Rápido, todo en un lugar
**Desventajas**: Crece mal, no reutilizable

### v2 - Funcional
**Contexto**: Proyecto pequeño con lógica clara

```python
# Funciones separadas en el mismo archivo
def validate_iban_format(iban): ...
def validate_positive_amount(amount): ...

class BankAccount:
    def __init__(self, iban, balance):
        if not validate_iban_format(iban): ...
```

**Ventajas**: Separación básica, testeable
**Desventajas**: Todo en un archivo aún

### v3 - Modular
**Contexto**: Proyecto mediano, validación compleja

```
v3_modular/
    validators.py  ← Módulo reutilizable con MOD-97
    bank.py        ← Importa desde validators
```

**Ventajas**: Reutilizable, bien organizado
**Desventajas**: Un módulo puede crecer mucho

### v4 - Paquete
**Contexto**: Proyecto grande, múltiples validaciones

```
v4_package/
    validators/
        __init__.py    ← Exporta funciones principales
        iban.py        ← Solo validación IBAN
        amount.py      ← Solo validación cantidades
    bank.py
```

**Ventajas**: Escalable, SRP aplicado
**Desventajas**: Más archivos (no es desventaja en proyectos grandes)

## 📊 Comparación Técnica

### Líneas de Código

| Versión | Total | Validación | Lógica Banco |
|---------|-------|------------|--------------|
| v1      | 150   | ~30 (inline) | 120        |
| v2      | 180   | ~40 (funciones) | 140     |
| v3      | 220   | 100 (módulo) | 120        |
| v4      | 250   | 120 (paquete) | 130       |

### Complejidad de Validación

| Versión | Formato | Checksum | Algoritmo |
|---------|---------|----------|-----------|
| v1      | ✅ Regex | ❌      | -         |
| v2      | ✅ Regex | ❌      | -         |
| v3      | ✅ Regex | ✅      | MOD-97    |
| v4      | ✅ Regex | ✅      | MOD-97    |

## 🔍 Detalles Técnicos

### Validación IBAN MOD-97

El algoritmo completo (implementado en v3 y v4):

```python
def validate_iban_checksum(iban):
    # ES9121000418450200051332
    
    # 1. Mover primeros 4 caracteres al final
    # → 21000418450200051332ES91
    rearranged = iban[4:] + iban[:4]
    
    # 2. Convertir letras a números (E=14, S=28)
    # → 210004184502000513321428 91
    numeric = ""
    for char in rearranged:
        if char.isdigit():
            numeric += char
        else:
            numeric += str(ord(char) - ord('A') + 10)
    
    # 3. MOD 97 debe ser 1
    # → int(numeric) % 97 == 1
    return int(numeric) % 97 == 1
```

### Estructura de __init__.py (v4)

```python
# validators/__init__.py
from .iban import validate_iban, validate_iban_format
from .amount import validate_positive_amount

__all__ = ['validate_iban', 'validate_positive_amount']
```

**Beneficio**: Importaciones limpias
```python
# En vez de:
from validators.iban import validate_iban

# Podemos escribir:
from validators import validate_iban
```

## 📝 Ejercicios Propuestos

### Básico
1. Ejecuta cada versión y compara output
2. Modifica el saldo inicial y prueba operaciones
3. Intenta usar IBANs inválidos

### Intermedio
4. Añade un método `get_formatted_iban()` que devuelva el IBAN con espacios
   - `ES9121000418450200051332` → `ES91 2100 0418 4502 0005 1332`
5. Crea un validador de DNI español en v4
6. Añade logging a las operaciones bancarias

### Avanzado
7. Extiende v4 para soportar IBANs de Francia (FR)
8. Crea tests unitarios para cada validador
9. Implementa un sistema de transacciones con historial
10. Refactoriza tu propio proyecto usando estos patrones

## 🎨 Principios SOLID Aplicados

| Principio | Dónde | Cómo |
|-----------|-------|------|
| **S**ingle Responsibility | v4 | Cada módulo una responsabilidad |
| **O**pen/Closed | v3, v4 | Extensible sin modificar |
| **L**iskov Substitution | - | No aplicado (no hay herencia) |
| **I**nterface Segregation | - | No aplicado (Python duck typing) |
| **D**ependency Inversion | v3, v4 | BankAccount depende de interfaz validate_iban |

## 🔗 Conexiones con Otros Notebooks

### Prerrequisitos
- [03-functions.ipynb](../code/03-functions.ipynb) - Funciones, parámetros, return
- [04-oop_basics.ipynb](../code/04-oop_basics.ipynb) - Clases, objetos, métodos

### Siguientes Pasos
- `05_packages_and_structure.ipynb` - Profundizar en paquetes
- `06_real_world_data_analysis.ipynb` - Aplicar en análisis de datos

## 🚀 Implementación en Clase

### Timing Sugerido (2 horas)

```
0:00-0:15  Revisión OOP (notebook 04)
0:15-0:30  Presentación v1 (problema)
0:30-0:45  Evolución v1→v2 (SoC)
0:45-1:00  Break
1:00-1:20  Evolución v2→v3 (módulos + MOD-97)
1:20-1:40  Evolución v3→v4 (paquetes)
1:40-2:00  Ejercicio práctico + Q&A
```

### Evaluación Sugerida

**Quiz (10 puntos)**
- Nombra 3 principios de arquitectura
- ¿Cuándo usar módulos vs paquetes?
- Explica el algoritmo MOD-97

**Ejercicio Práctico (40 puntos)**
- Refactoriza código dado de v1 a v3
- Añade validador nuevo en v4
- Explica decisiones de diseño

**Proyecto (50 puntos)**
- Refactoriza proyecto propio
- Aplica al menos 2 principios
- Documenta evolución

## 📚 Referencias Adicionales

- [PEP 8](https://peps.python.org/pep-0008/) - Style Guide
- [Python Module Documentation](https://docs.python.org/3/tutorial/modules.html)
- [IBAN Validation](https://en.wikipedia.org/wiki/International_Bank_Account_Number)
- [Clean Code Principles](https://en.wikipedia.org/wiki/SOLID)

---

**Creado**: Diciembre 2025  
**Autor**: Material didáctico para CSPy  
**Versión**: 1.0
