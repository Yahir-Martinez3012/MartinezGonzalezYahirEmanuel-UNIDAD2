# Conecta UTC

Bolsa de trabajo universitaria para estudiantes y egresados de la Universidad Tecnológica de Coahuila (UTC), desarrollada con Django.

## Problemática

Las vacantes dirigidas a los estudiantes se comparten principalmente por correo institucional, donde se pierden, no se pueden buscar ni filtrar y no permiten dar seguimiento a las postulaciones.

## Solución

Una plataforma web donde los estudiantes consultan, buscan, filtran, guardan y se postulan a vacantes; las empresas publican y administran ofertas y candidatos; y el administrador UTC supervisa el sistema.

## Estructura de aplicaciones

| App | Responsabilidad |
|---|---|
| `config` | Configuración del proyecto |
| `core` | Inicio y estadísticas |
| `cuentas` | Usuario personalizado y roles |
| `catalogo` | Carreras y habilidades |
| `estudiantes` | Perfil del estudiante y CV |
| `empresas` | Perfil de empresa |
| `vacantes` | Vacantes, filtros y favoritos |
| `postulaciones` | Postulaciones y sus estados |

## Ejecutar en local (Windows)

    python -m venv venv
    venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Copia `.env.example` a `.env` para definir variables de entorno. Nunca subas `.env` al repositorio.

## Flujo de trabajo

GitHub Flow: rama `main` estable y ramas `feature/*` integradas mediante pull requests.
