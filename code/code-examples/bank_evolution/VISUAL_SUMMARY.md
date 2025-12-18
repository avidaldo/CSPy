# Arquitectura Progresiva - Resumen Visual

## 📖 El Viaje Completo

```
┌─────────────────────────────────────────────────────────────────────┐
│  PUNTO DE PARTIDA: Notebook 04 - OOP Basics                        │
│  Ya sabes: clases, objetos, métodos, self                          │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│  PREGUNTA: ¿Cómo organizo el código cuando crece?                  │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│  RESPUESTA: Notebook 07 - Progressive Architecture                 │
│  + Ejemplos v1 → v2 → v3 → v4                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## 🔄 Las 4 Versiones (Un Vistazo)

### v1: MONOLÍTICA - "Empezamos simple"
```python
┌─────────────────────────┐
│ bank.py (1 archivo)     │
├─────────────────────────┤
│ • Excepciones           │
│ • Clase BankAccount     │
│   ├─ __init__           │
│   ├─ _is_valid_iban ← Validación inline │
│   ├─ deposit            │
│   ├─ withdraw           │
│   └─ transfer           │
└─────────────────────────┘

Problema: Todo mezclado, difícil de reutilizar
```

### v2: FUNCIONAL - "Separamos responsabilidades"
```python
┌─────────────────────────┐
│ bank.py (1 archivo)     │
├─────────────────────────┤
│ FUNCIONES GLOBALES:     │
│ • validate_iban_format()│
│ • validate_positive_amount() │
│                         │
│ EXCEPCIONES             │
│                         │
│ CLASE BankAccount       │
│   ├─ usa funciones ↑    │
│   ├─ deposit            │
│   └─ withdraw           │
└─────────────────────────┘

Mejora: SoC básico, pero aún un archivo
```

### v3: MODULAR - "Validación compleja justifica módulo"
```python
┌─────────────────────────┐  ┌─────────────────────────┐
│ validators.py           │  │ bank.py                 │
├─────────────────────────┤  ├─────────────────────────┤
│ • validate_iban_format()│←─│ from validators import  │
│ • validate_iban_checksum│  │   validate_iban         │
│   (MOD-97 completo!)    │  │                         │
│ • validate_iban()       │  │ class BankAccount:      │
│ • validate_positive...  │  │   • usa validate_iban() │
└─────────────────────────┘  └─────────────────────────┘

Mejora: Módulo reutilizable, validación completa
```

### v4: PAQUETE - "Escalable y profesional"
```python
┌────────────────────────────┐  ┌─────────────────────────┐
│ validators/                │  │ bank.py                 │
├────────────────────────────┤  ├─────────────────────────┤
│ • __init__.py (exporta)    │←─│ from validators import  │
│ • iban.py                  │  │   validate_iban         │
│   ├─ validate_iban_format()│  │                         │
│   ├─ validate_iban_checksum│  │ class BankAccount:      │
│   └─ validate_iban()       │  │   • usa validate_iban() │
│ • amount.py                │  └─────────────────────────┘
│   └─ validate_positive...  │
└────────────────────────────┘

Mejora: SRP aplicado, cada módulo una cosa
```

## 📊 Evolución de Complejidad

```
Validación de IBAN a través de las versiones:

v1, v2: FORMATO SOLO
┌──────────────────────────┐
│ pattern = r'^ES\d{22}$'  │
│ return bool(match(iban)) │
└──────────────────────────┘
Simple regex ← Suficiente al principio

v3, v4: FORMATO + CHECKSUM
┌──────────────────────────────────────────────┐
│ def validate_iban(iban):                     │
│     # 1. Validar formato                     │
│     if not re.match(r'^ES\d{22}$', iban):    │
│         return False                         │
│                                              │
│     # 2. Validar checksum MOD-97             │
│     rearranged = iban[4:] + iban[:4]         │
│     numeric = ""                             │
│     for char in rearranged:                  │
│         if char.isdigit():                   │
│             numeric += char                  │
│         else:                                │
│             numeric += str(ord(char) - 65 + 10) │
│     return int(numeric) % 97 == 1            │
└──────────────────────────────────────────────┘
Algoritmo complejo ← Justifica módulo separado!
```

## 🎯 Principios Aplicados

```
┌────────────┬─────────────────────────────────────────────────┐
│ Principio  │ Cómo se Aplica                                  │
├────────────┼─────────────────────────────────────────────────┤
│ DRY        │ v2: Función validate_iban() en vez de copiar    │
│            │ el regex en 3 lugares                           │
├────────────┼─────────────────────────────────────────────────┤
│ SoC        │ v2: Validación separada de lógica bancaria      │
│            │ v3: Validación en su propio módulo              │
├────────────┼─────────────────────────────────────────────────┤
│ SRP        │ v4: iban.py solo valida IBANs                   │
│            │     amount.py solo valida cantidades            │
│            │     bank.py solo lógica bancaria                │
└────────────┴─────────────────────────────────────────────────┘
```

## 🚨 Señales de Refactorización

```
Estás en v1 → Considera v2 si:
├─ Copias código (mismo regex en varios métodos)
├─ La clase hace "demasiadas cosas"
└─ Difícil de explicar qué hace un método

Estás en v2 → Considera v3 si:
├─ El archivo supera 500 líneas
├─ Quieres reutilizar funciones en otro proyecto
└─ Necesitas validación compleja (MOD-97)

Estás en v3 → Considera v4 si:
├─ Un módulo hace demasiadas cosas distintas
├─ Necesitas jerarquía (subcategorías de validaciones)
└─ Vas a distribuir como librería
```

## 📁 Archivos Creados (Checklist)

```
✅ code/code-examples/bank_evolution/
   ✅ README.md                    ← Guía de uso
   ✅ TEACHING_GUIDE.md            ← Guía pedagógica completa
   ✅ VISUAL_SUMMARY.md            ← Este archivo
   
   ✅ v1_monolithic/
      ✅ bank.py                   ← Todo en uno
   
   ✅ v2_functional/
      ✅ bank.py                   ← Funciones separadas
   
   ✅ v3_modular/
      ✅ bank.py                   ← Clase principal
      ✅ validators.py             ← Módulo con MOD-97
   
   ✅ v4_package/
      ✅ bank.py                   ← Clase principal
      ✅ validators/
         ✅ __init__.py            ← Exporta funciones
         ✅ iban.py                ← Validación IBAN
         ✅ amount.py              ← Validación cantidades

✅ code/modules/
   ✅ 07_progressive_architecture.ipynb  ← Notebook enseñanza

✅ code/04-oop_basics.ipynb
   ✅ (Actualizado con referencia al nuevo material)
```

## 🎓 Cómo Enseñar Esto

### Sesión de 2 Horas

```
┌────────────────┬──────────────────────────────────────────┐
│ Tiempo         │ Actividad                                │
├────────────────┼──────────────────────────────────────────┤
│ 00:00 - 00:15  │ Repaso: OOP del notebook 04              │
│                │ - Clases, métodos, self                  │
├────────────────┼──────────────────────────────────────────┤
│ 00:15 - 00:30  │ v1: El problema del código monolítico    │
│                │ - Mostrar bank.py                        │
│                │ - Discutir: ¿Qué podría mejorar?         │
├────────────────┼──────────────────────────────────────────┤
│ 00:30 - 00:45  │ v2: Separación de responsabilidades      │
│                │ - Live coding: extraer funciones         │
│                │ - Principio SoC                          │
├────────────────┼──────────────────────────────────────────┤
│ 00:45 - 01:00  │ ☕ Break                                  │
├────────────────┼──────────────────────────────────────────┤
│ 01:00 - 01:20  │ v3: Módulos y validación compleja        │
│                │ - Explicar MOD-97 (por qué necesitamos)  │
│                │ - Mostrar validators.py                  │
│                │ - Principio DRY                          │
├────────────────┼──────────────────────────────────────────┤
│ 01:20 - 01:40  │ v4: Paquetes profesionales               │
│                │ - Estructura de directorios              │
│                │ - Rol de __init__.py                     │
│                │ - Principio SRP                          │
├────────────────┼──────────────────────────────────────────┤
│ 01:40 - 02:00  │ Ejercicio: Refactoriza tu código         │
│                │ + Q&A                                    │
└────────────────┴──────────────────────────────────────────┘
```

## 💻 Comandos Rápidos

```bash
# Ejecutar todas las versiones de golpe
cd code/code-examples/bank_evolution
python v1_monolithic/bank.py
python v2_functional/bank.py
python v3_modular/bank.py
python v4_package/bank.py

# Probar validadores independientemente
python v3_modular/validators.py
python -m v4_package.validators.iban
python -m v4_package.validators.amount
```

## 🔗 Referencias Rápidas

| Quieres...                     | Mira...                           |
|--------------------------------|-----------------------------------|
| Entender conceptos             | `07_progressive_architecture.ipynb` |
| Ver código real                | Carpetas `v1/`, `v2/`, `v3/`, `v4/` |
| Guía de uso                    | `README.md`                       |
| Guía de enseñanza              | `TEACHING_GUIDE.md`               |
| Resumen visual                 | `VISUAL_SUMMARY.md` (este)        |
| Prerrequisito OOP              | `../04-oop_basics.ipynb`          |

## 🎉 Resultado Final

Los estudiantes aprenderán:

✅ **CUÁNDO** refactorizar (señales de código problemático)  
✅ **CÓMO** organizar (funciones → módulos → paquetes)  
✅ **POR QUÉ** importa (mantenibilidad, escalabilidad, reutilización)  
✅ **Principios** (DRY, SoC, SRP) con ejemplos prácticos  

Y lo mejor: con un ejemplo **real** (validación IBAN) que muestra por qué la complejidad justifica mejor organización.

---

**Material completo y listo para enseñar** 🚀
