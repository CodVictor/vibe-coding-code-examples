# Vibe Coding & Software Quality - Grupo 6 (URJC)

Este repositorio contiene el código de la demostración práctica para la presentación oral de la asignatura **Calidad del Software** (2025-2026).

## Contenido del Repositorio
El proyecto compara dos enfoques para implementar un sistema de autorización por roles en **FastAPI**:

*   **`CMS_Humano.py`**: Versión desarrollada de forma tradicional, aplicando principios de responsabilidad única (SRP), tipos estrictos con Enums y centralización de políticas.
*   **`CMS_IA.py`**: Versión generada mediante **Vibe Coding** con un único prompt, analizando la aparición de lógica anidada y "magic strings".

## Objetivo del Análisis
Siguiendo los requisitos de la práctica, evaluamos ambos archivos utilizando métricas de calidad como:
1. **Bugs y Code Smells** (vía SonarQube).
2. **Complejidad Ciclomática**.
3. **Cobertura de Tests**.

---
**Curso:** 3º Ingeniería del Software - Universidad Rey Juan Carlos.