# Celery Demo

## Overview

**Celery** is a distributed task queue system written in Python. It allows you to run **time-consuming tasks asynchronously** in the background, so users don’t have to wait for them to complete.  

### Example Use Cases
- Sending bulk emails  
- Processing uploaded images  
- Verifying documents  

By offloading these tasks to Celery, your application remains responsive while tasks are handled in the background.

---

## How It Works

1. **Broker:** A message queue (e.g., Redis) where tasks are sent. Workers pick up tasks from the broker and execute them.  
2. **Backend:** Stores task results, allowing your code to retrieve them using `.get()`.  
3. **Task:** A Python function decorated with `@app.task` that runs asynchronously.

---

## Installation

```bash
pip install celery redis

---


from celery import Celery

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",  # Queue for tasks
    backend="redis://localhost:6379/0", # Stores results
)

@app.task
def add(x, y):
    return x + y
