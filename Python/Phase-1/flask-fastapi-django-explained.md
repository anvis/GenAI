# Flask vs FastAPI vs Django: A Practical Guide with Code

Python offers three dominant web frameworks, each built with a different philosophy. This article walks through each one — what it is, a working code example, and how they compare — so you can pick the right tool for your next project.

---

## 1. Flask — The Minimalist

Flask is a **microframework**. It gives you routing and request handling, and nothing more — you add databases, validation, and auth yourself, usually via extensions. This makes it flexible but also means more manual setup as your app grows.

### Example: A simple API endpoint

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
users = {1: {"name": "Anvi", "role": "Engineer"}}

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_id = max(users.keys()) + 1
    users[new_id] = data
    return jsonify({"id": new_id, **data}), 201

if __name__ == "__main__":
    app.run(debug=True)
```

Run it, and `GET /api/users/1` returns:

```json
{"name": "Anvi", "role": "Engineer"}
```

Notice there's no built-in data validation — if you `POST` malformed JSON, Flask won't stop you. You'd need to write those checks yourself, or bring in an extension like Marshmallow.

**Best for:** small services, prototypes, and situations where you want full control over your stack without extra abstraction.

---

## 2. FastAPI — The Modern API Framework

FastAPI is built specifically for APIs, with two standout features: **native async support** and **automatic validation using Python type hints** (via Pydantic). It also generates interactive API documentation for free.

### Example: The same API in FastAPI

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic model = automatic validation + docs
class User(BaseModel):
    name: str
    role: str

users = {1: User(name="Anvi", role="Engineer")}

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/api/users", status_code=201)
async def create_user(user: User):
    new_id = max(users.keys()) + 1
    users[new_id] = user
    return {"id": new_id, **user.dict()}
```

Run this with `uvicorn main:app --reload`, and two things happen automatically that Flask doesn't give you for free:

1. **Validation** — if someone POSTs `{"name": "Anvi"}` without `role`, FastAPI rejects it with a clear 422 error before your code even runs.
2. **Docs** — visiting `/docs` gives you an interactive Swagger UI where you can test every endpoint directly in the browser.

**Best for:** APIs, especially ones needing async performance — this includes most modern LLM/ML serving use cases (e.g., streaming responses from a LangChain pipeline), since async support matters for handling concurrent, long-running requests efficiently.

---

## 3. Django — The Full-Stack Framework

Django is **batteries-included**. It ships with an ORM, an admin panel, authentication, forms, and templating out of the box. You get a lot for free, but you also work within its structure and conventions.

### Example: A model + view (Django's structure)

```python
# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

# views.py
from django.http import JsonResponse
from django.views import View
from .models import User

class UserDetailView(View):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            return JsonResponse({"name": user.name, "role": user.role})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

# urls.py
from django.urls import path
from .views import UserDetailView

urlpatterns = [
    path("api/users/<int:user_id>/", UserDetailView.as_view()),
]
```

Run `python manage.py migrate` and `python manage.py createsuperuser`, and you instantly get a working **admin dashboard** at `/admin` where you can view and edit `User` records through a UI — no extra code required. Flask and FastAPI have no equivalent to this without third-party add-ons.

**Best for:** larger applications with a database, user accounts, and admin needs — e.g., a content management system or e-commerce platform.

---

## Side-by-Side Comparison

| | Flask | FastAPI | Django |
|---|---|---|---|
| **Type** | Microframework | Microframework (API-focused) | Full-stack framework |
| **Async support** | Limited (bolted on) | Native (built on ASGI/Starlette) | Partial (since 3.0+) |
| **Data validation** | Manual / extensions | Built-in (Pydantic) | Via Forms / Django REST Framework |
| **Auto API docs** | No | Yes — Swagger/OpenAPI built in | No (needs DRF) |
| **Built-in ORM** | No (use SQLAlchemy) | No (use SQLAlchemy/Tortoise) | Yes |
| **Admin panel** | No | No | Yes, auto-generated |
| **Learning curve** | Low | Low–Medium | Medium–High |
| **Performance** | Moderate | High | Moderate |
| **Best for** | Small apps, prototypes, microservices | APIs, ML/LLM serving, high-performance backends | Large apps, content-heavy sites, admin-driven systems |

---

## Which Should You Choose?

- **Pick Flask** if you want minimal structure, full control, and you're building something small or experimental.
- **Pick FastAPI** if you're building an API — especially one serving an ML or LLM pipeline — and want async performance plus built-in validation and docs with almost no extra effort.
- **Pick Django** if you're building a complete web application with a database, user management, and admin needs, and you'd rather use a proven, all-in-one structure than assemble one yourself.

For AI-focused backend work — wrapping a model, a LangChain chain, or a LangGraph agent behind an endpoint — **FastAPI** has become the de facto standard in most modern stacks, largely due to its async-first design and clean request/response typing.
