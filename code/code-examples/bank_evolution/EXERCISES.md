# Cuaderno de Ejercicios: Arquitectura Progresiva

## 📝 Instrucciones Generales

Este cuaderno contiene ejercicios prácticos para aplicar lo aprendido sobre arquitectura de código. Completa los ejercicios en orden, ya que cada uno construye sobre el anterior.

---

## Ejercicio 1: Análisis de Código (15 min)

### Tarea
Analiza el siguiente código y responde las preguntas:

```python
class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, email, password):
        # Validar email
        if "@" not in email or "." not in email.split("@")[1]:
            raise ValueError("Email inválido")
        
        # Validar contraseña
        if len(password) < 8:
            raise ValueError("Contraseña muy corta")
        if not any(c.isupper() for c in password):
            raise ValueError("Contraseña sin mayúscula")
        if not any(c.isdigit() for c in password):
            raise ValueError("Contraseña sin número")
        
        # Guardar
        self.users.append({"email": email, "password": password})
    
    def send_welcome_email(self, email):
        # Simular envío de email
        print(f"Enviando email de bienvenida a {email}")
```

### Preguntas

1. **¿Qué principios arquitectónicos se violan?**
   - [ ] DRY
   - [ ] SoC
   - [ ] SRP
   - [ ] Todos los anteriores

2. **¿Cuál es el problema principal?**
   
   Tu respuesta:
   _________________________________________________________________
   _________________________________________________________________

3. **¿Qué versión de arquitectura es esto (v1, v2, v3, v4)?**
   
   Respuesta: _______________

4. **¿A qué versión debería evolucionar primero?**
   
   Respuesta: _______________

---

## Ejercicio 2: Refactorización a v2 (20 min)

### Tarea
Refactoriza el código del Ejercicio 1 aplicando arquitectura v2 (funcional).

```python
# Extrae las validaciones a funciones separadas

def validate_email(email):
    """Valida formato de email."""
    # TODO: Tu código aquí
    pass


def validate_password_length(password):
    """Valida longitud mínima de contraseña."""
    # TODO: Tu código aquí
    pass


def validate_password_uppercase(password):
    """Valida que tenga mayúscula."""
    # TODO: Tu código aquí
    pass


def validate_password_digit(password):
    """Valida que tenga dígito."""
    # TODO: Tu código aquí
    pass


def validate_password(password):
    """Validación completa de contraseña."""
    # TODO: Usa las funciones anteriores
    pass


class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, email, password):
        # TODO: Usa las funciones de validación
        pass
    
    def send_welcome_email(self, email):
        print(f"Enviando email de bienvenida a {email}")
```

### Auto-evaluación
- [ ] Las funciones están separadas de la clase
- [ ] Cada función hace una sola cosa
- [ ] `add_user()` usa las funciones de validación
- [ ] El código es más fácil de testear

---

## Ejercicio 3: Identificar Señales de Refactorización (10 min)

### Tarea
Para cada caso, indica si necesitas refactorizar y a qué versión:

| Caso | ¿Refactorizar? | ¿A qué versión? | ¿Por qué? |
|------|----------------|-----------------|-----------|
| Archivo con 100 líneas, una clase | | | |
| Archivo con 600 líneas, muchas funciones | | | |
| Módulo con 15 tipos de validaciones | | | |
| Copias el mismo regex en 5 lugares | | | |
| Quieres usar validadores en otro proyecto | | | |

---

## Ejercicio 4: Validador de DNI Español (30 min)

### Contexto
El DNI español tiene este formato: 8 dígitos + 1 letra
- Ejemplo: `12345678Z`
- La letra se calcula: `resto de (número ÷ 23)` da el índice en `"TRWAGMYFPDXBNJZSQVHLCKE"`

### Tarea
Implementa un validador de DNI siguiendo la arquitectura v3 (modular).

#### Archivo: `validators.py`
```python
def validate_dni_format(dni):
    """
    Valida formato: 8 dígitos + 1 letra.
    
    Args:
        dni: String con el DNI
    
    Returns:
        bool: True si el formato es correcto
    
    Ejemplos:
        >>> validate_dni_format("12345678Z")
        True
        >>> validate_dni_format("123Z")
        False
    """
    # TODO: Tu código aquí
    pass


def validate_dni_letter(dni):
    """
    Valida que la letra sea correcta según el algoritmo.
    
    Args:
        dni: String con DNI en formato válido
    
    Returns:
        bool: True si la letra es correcta
    
    Algoritmo:
        1. Extraer número (primeros 8 dígitos)
        2. Calcular: resto de (número ÷ 23)
        3. Usar índice en "TRWAGMYFPDXBNJZSQVHLCKE"
        4. Comparar con la letra del DNI
    
    Ejemplos:
        >>> validate_dni_letter("12345678Z")
        True
    """
    LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"
    # TODO: Tu código aquí
    pass


def validate_dni(dni):
    """
    Validación completa: formato + letra.
    
    Args:
        dni: String con el DNI
    
    Returns:
        bool: True si el DNI es válido
    """
    # TODO: Tu código aquí
    pass


# Pruebas
if __name__ == "__main__":
    # Casos de prueba
    assert validate_dni("12345678Z") == True  # TODO: Calcular DNI válido
    assert validate_dni("12345678A") == False  # Letra incorrecta
    assert validate_dni("123Z") == False  # Formato incorrecto
    
    print("✓ Todas las pruebas pasaron")
```

### Auto-evaluación
- [ ] `validate_dni_format()` valida solo el formato
- [ ] `validate_dni_letter()` valida el algoritmo de la letra
- [ ] `validate_dni()` combina ambas validaciones
- [ ] Los asserts pasan correctamente

---

## Ejercicio 5: Evolucionando a v4 (Paquete) (45 min)

### Tarea
Convierte el código de los ejercicios 2 y 4 en un paquete v4.

#### Estructura objetivo:
```
validators/
    __init__.py
    email.py       ← Del ejercicio 2
    password.py    ← Del ejercicio 2
    dni.py         ← Del ejercicio 4
```

### Paso 1: Crear `validators/email.py`
```python
"""Validación de emails."""

def validate_email_format(email):
    """Valida formato básico de email."""
    # TODO: Mover código del ejercicio 2
    pass


def validate_email(email):
    """Validación completa de email."""
    return validate_email_format(email)


if __name__ == "__main__":
    # Pruebas
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False
    print("✓ Validación de email OK")
```

### Paso 2: Crear `validators/password.py`
```python
"""Validación de contraseñas."""

def validate_password_length(password, min_length=8):
    """Valida longitud mínima."""
    # TODO: Mover código del ejercicio 2
    pass


def validate_password_uppercase(password):
    """Valida presencia de mayúscula."""
    # TODO: Mover código del ejercicio 2
    pass


def validate_password_digit(password):
    """Valida presencia de dígito."""
    # TODO: Mover código del ejercicio 2
    pass


def validate_password(password):
    """Validación completa de contraseña."""
    # TODO: Combinar validaciones
    pass


if __name__ == "__main__":
    # Pruebas
    assert validate_password("SecurePass1") == True
    assert validate_password("weak") == False
    print("✓ Validación de contraseña OK")
```

### Paso 3: Crear `validators/dni.py`
```python
"""Validación de DNI español."""

# TODO: Copiar código del ejercicio 4
```

### Paso 4: Crear `validators/__init__.py`
```python
"""
Paquete de validaciones.

Exporta las funciones principales de cada submódulo.
"""

from .email import validate_email
from .password import validate_password
from .dni import validate_dni

__all__ = [
    'validate_email',
    'validate_password',
    'validate_dni'
]
```

### Paso 5: Probar el paquete
```python
# test_validators.py
from validators import validate_email, validate_password, validate_dni

# Probar importaciones
print("Probando email:", validate_email("test@example.com"))
print("Probando password:", validate_password("SecurePass1"))
print("Probando DNI:", validate_dni("12345678Z"))  # Ajustar DNI válido

print("✓ Paquete funcionando correctamente")
```

### Auto-evaluación
- [ ] Estructura de directorios correcta
- [ ] Cada submódulo funciona independientemente
- [ ] `__init__.py` exporta correctamente
- [ ] Las importaciones desde fuera funcionan

---

## Ejercicio 6: Aplicación Real (60 min)

### Tarea
Crea una aplicación de gestión de usuarios usando el paquete `validators` del ejercicio 5.

```python
# user_manager.py

from validators import validate_email, validate_password, validate_dni


class InvalidUserDataError(Exception):
    """Error cuando los datos del usuario son inválidos."""
    pass


class User:
    """Representa un usuario del sistema."""
    
    def __init__(self, email, password, dni):
        """
        Crea un nuevo usuario.
        
        Args:
            email: Email del usuario
            password: Contraseña
            dni: DNI español
        
        Raises:
            InvalidUserDataError: Si algún dato es inválido
        """
        # TODO: Validar cada campo usando el paquete validators
        # TODO: Si todo es válido, guardar los atributos
        pass
    
    def __str__(self):
        # TODO: Retornar representación string del usuario
        pass


class UserManager:
    """Gestiona una colección de usuarios."""
    
    def __init__(self):
        self.users = []
    
    def register_user(self, email, password, dni):
        """
        Registra un nuevo usuario.
        
        Returns:
            User: El usuario creado
        
        Raises:
            InvalidUserDataError: Si los datos son inválidos
            ValueError: Si el email ya existe
        """
        # TODO: Verificar que el email no existe
        # TODO: Crear usuario
        # TODO: Añadir a la lista
        # TODO: Retornar usuario
        pass
    
    def find_by_email(self, email):
        """
        Busca un usuario por email.
        
        Returns:
            User o None
        """
        # TODO: Buscar en self.users
        pass
    
    def list_all(self):
        """Lista todos los usuarios."""
        # TODO: Iterar y mostrar
        pass


# Programa principal
if __name__ == "__main__":
    manager = UserManager()
    
    # Caso 1: Registro exitoso
    try:
        user1 = manager.register_user(
            "alice@example.com",
            "SecurePass1",
            "12345678Z"  # Ajustar DNI válido
        )
        print(f"✓ Usuario registrado: {user1}")
    except (InvalidUserDataError, ValueError) as e:
        print(f"✗ Error: {e}")
    
    # Caso 2: Email duplicado
    try:
        user2 = manager.register_user(
            "alice@example.com",  # Duplicado
            "AnotherPass1",
            "87654321X"  # Ajustar DNI válido
        )
    except ValueError as e:
        print(f"✓ Error esperado: {e}")
    
    # Caso 3: Datos inválidos
    try:
        user3 = manager.register_user(
            "invalid-email",  # Inválido
            "weak",  # Inválida
            "123"  # Inválido
        )
    except InvalidUserDataError as e:
        print(f"✓ Error esperado: {e}")
    
    # Listar usuarios
    print("\n--- Usuarios registrados ---")
    manager.list_all()
```

### Auto-evaluación
- [ ] La aplicación usa el paquete `validators`
- [ ] Los errores se manejan correctamente
- [ ] El código está bien organizado (SoC)
- [ ] Cada clase tiene una responsabilidad (SRP)

---

## Ejercicio 7: Reflexión Final (15 min)

### Preguntas de reflexión

1. **¿Qué ventajas tiene la arquitectura v4 sobre v1?**
   
   Tu respuesta:
   _________________________________________________________________
   _________________________________________________________________
   _________________________________________________________________

2. **¿Cuándo usarías v2 en lugar de v4?**
   
   Tu respuesta:
   _________________________________________________________________
   _________________________________________________________________

3. **¿Qué principio te parece más importante y por qué?**
   
   Principio: ________________
   
   Por qué:
   _________________________________________________________________
   _________________________________________________________________

4. **Describe un proyecto tuyo que se beneficiaría de refactorización:**
   
   Proyecto: ________________
   
   Estado actual: ________________
   
   Versión objetivo: ________________
   
   Razón:
   _________________________________________________________________
   _________________________________________________________________

---

## 🎯 Soluciones y Respuestas

*(Las soluciones se proporcionarán en una sesión de revisión)*

### Criterios de evaluación

**Ejercicio 1**: 10 puntos
- Identificar violaciones: 5 pts
- Explicar problema: 3 pts
- Identificar versión: 2 pts

**Ejercicio 2**: 20 puntos
- Funciones correctas: 10 pts
- Integración en clase: 5 pts
- Código limpio: 5 pts

**Ejercicio 3**: 10 puntos
- Identificación correcta: 10 pts

**Ejercicio 4**: 25 puntos
- Validación formato: 8 pts
- Algoritmo letra: 12 pts
- Pruebas: 5 pts

**Ejercicio 5**: 20 puntos
- Estructura paquete: 8 pts
- Submódulos funcionan: 8 pts
- `__init__.py` correcto: 4 pts

**Ejercicio 6**: 15 puntos
- Uso del paquete: 5 pts
- Manejo errores: 5 pts
- Código organizado: 5 pts

**Total**: 100 puntos

---

**Tiempo estimado total**: 3-4 horas
**Nivel**: Intermedio
**Prerrequisito**: Haber completado notebooks 04 (OOP) y 07 (Progressive Architecture)
