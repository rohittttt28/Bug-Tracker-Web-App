# Bug Tracker Web App

A simple bug tracking application built with Python Flask.

## Manual Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment
```bash
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize Database and Add Sample Data
```bash
python -c "from app import init_db; init_db()"
python add_dummy_data.py
```

### 5. Run the Application
```bash
python app.py
```

Then open: http://127.0.0.1:5000