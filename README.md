# 🎵 Trivia Musical (Django)

Juego de trivia que reproduce fragmentos de audio, ofrece opciones de respuesta múltiple y lleva el puntaje en la sesión.

## Ejecutar en local (VS Code, terminal integrada)

```bash
python -m venv venv
venv\Scripts\activate          # Windows   (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py poblar_trivia  # carga las preguntas de ejemplo
python manage.py runserver
```

Abre http://127.0.0.1:8000/ (redirige a `/start/`).
Panel de administración: `python manage.py createsuperuser` y entra a `/admin/`.

## Rutas

| Ruta | Vista | Descripción |
|---|---|---|
| `/start/` | `start_game` | Inicio; reinicia `score` y `answered_question_ids` |
| `/play/` | `play_trivia` | Pregunta aleatoria aún no respondida |
| `/submit/` | `submit_answer` | Recibe la respuesta por POST |
| `/game-over/` | `game_over` | Resultado final |

## Audios

`generate_sample_audio.py` crea 4 melodías de dominio público (WAV) en `media/music_snippets/`.
Para usar tus propios `.mp3`, cópialos a esa carpeta y edita la lista `PREGUNTAS` en
`trivia_game/management/commands/poblar_trivia.py` (o súbelos desde `/admin/`).

## Pruebas

```bash
python manage.py test
```

## Despliegue en Render

| Parámetro | Valor |
|---|---|
| Build Command | `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate && python manage.py poblar_trivia` |
| Start Command | `gunicorn music_trivia_project.wsgi:application` |
| `SECRET_KEY` | cadena aleatoria larga |
| `DEBUG` | `False` |

Render define `RENDER_EXTERNAL_HOSTNAME` automáticamente; `settings.py` lo agrega a `ALLOWED_HOSTS`.
El disco gratuito es efímero: por eso el build vuelve a migrar y poblar la base.

## Flujo de ramas sugerido

`main` ← `release/*` ← `develop` ← `feature/*` (ver documento PDF del caso práctico).
