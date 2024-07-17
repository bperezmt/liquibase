
# Liquibase Script

Este script sencillo está diseñado para facilitar la gestión de cambios en bases de datos utilizando Liquibase. Permite automatizar la generación de snapshots, realizar cambios en la estructura de la base de datos y ejecutar rollbacks a versiones anteriores.

## Objetivo

El objetivo principal de este script es permitir la gestión eficiente de cambios en la base de datos de una manera controlada, aprovechando las capacidades de Liquibase para mantener el estado de la base de datos sincronizado con el código.

## Requisitos

- Python 3.x
- Liquibase instalado y accesible desde la línea de comandos
- Conector JDBC de MySQL
- Archivo `.env` con las siguientes variables configuradas:
  - `LIQUIBASE_PATH`: Ruta al ejecutable de Liquibase.
  - `CHANGELOG_FILE`: Nombre del archivo de changelog (ej. `changelog.xml`).
  - `DB_URL`: URL de conexión a la base de datos.
  - `DB_USERNAME`: Nombre de usuario para la base de datos.
  - `DB_PASSWORD`: Contraseña para la base de datos.
  - `MYSQL_CONNECTOR_PATH`: Ruta al conector JDBC de MySQL.

## Comandos Disponibles

El script permite ejecutar comandos de Liquibase. A continuación, se presentan algunos ejemplos:

1. **Snapshot**: Genera un snapshot de la base de datos actual.
2. **Rollback**: Revierte la base de datos a una versión anterior especificada por un tag o un número de cambios.
3. **Validate**: Valida el changelog y verifica que todos los cambios sean aplicables.
4. **Update**: Aplica los cambios pendientes en la base de datos según el changelog.


## Ejemplo de Uso

1. Al ejecutar el script, se mostrará un menú que permitirá seleccionar la acción que desea realizar.