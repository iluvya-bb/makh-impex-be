# Makh Impex Backend

Django REST API backend for the MAH IMPEX lottery promotion system.

## Tech Stack

- **Framework:** Django 3.1.7 + Django REST Framework
- **Database:** MySQL 8
- **Cache:** Redis 7
- **Server:** Gunicorn

## Running the Project

### Option 1: Docker (Recommended)

```bash
cd /home/luvya/work/enji/mahimpeks_be
docker-compose up --build
```

This starts MySQL (port 3306), Redis (port 6379), and Django (port 8000).

---

### Option 2: Manual Setup

#### 1. Prerequisites

Make sure MySQL and Redis are running:

```bash
# Start MySQL (if installed locally)
sudo systemctl start mysql

# Start Redis (if installed locally)
sudo systemctl start redis
```

#### 2. Create MySQL Database

```bash
mysql -u root -p
```

```sql
CREATE DATABASE mah_db;
CREATE USER 'django-user'@'localhost' IDENTIFIED BY 'pass1234';
GRANT ALL PRIVILEGES ON mah_db.* TO 'django-user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

#### 3. Setup Python Environment

```bash
cd /home/luvya/work/enji/mahimpeks_be

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 4. Run Migrations

```bash
python manage.py migrate
```

#### 5. Create Admin User (optional)

```bash
python manage.py createsuperuser
```

#### 6. Run Server

```bash
python manage.py runserver 0.0.0.0:8000
```

---

## Endpoints

- **API:** http://localhost:8000/lotteries/
- **Admin:** http://localhost:8000/admin/

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/lotteries/` | List all lottery entries |
| POST | `/lotteries/` | Create new lottery entry |
| GET | `/lotteries/{id}/` | Get specific entry |
| PUT/PATCH | `/lotteries/{id}/` | Update entry |
| DELETE | `/lotteries/{id}/` | Delete entry |

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DEBUG` | `1` | Debug mode (1=on, 0=off) |
| `DB_NAME` | `mah_db` | MySQL database name |
| `DB_USER` | `django-user` | MySQL username |
| `DB_PASSWORD` | `pass1234` | MySQL password |
| `DB_HOST` | `127.0.0.1` | MySQL host |
| `DB_PORT` | `3306` | MySQL port |
| `REDIS_HOST` | `127.0.0.1` | Redis host |
| `REDIS_PORT` | `6379` | Redis port |
