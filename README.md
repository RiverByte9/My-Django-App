# My-Django-App
💡 What I Built:

1️⃣ A basic Django app with a custom homepage styled with HTML and CSS.
2️⃣ A Dockerfile to containerize the application.
3️⃣ A running Docker container successfully serving the homepage on http://localhost:8000.

⚙️ Key Steps:
# Setting up a virtual environment (best practice!)
python -m venv venv
 venv\Scripts\activate

# Building the Docker image
docker build -t django-app .

# Running the container and mapping port 8000
docker run -p 8000:8000 django-app

🚧 Challenges I Faced (and Solved!):
TemplateDoesNotExist:
 My app initially couldn’t locate the homepage/index.html. After debugging, I realized the TEMPLATES_DIR in settings.py wasn’t pointing to the correct path inside the container. The fix? I verified that the templates folder was correctly located in /app/templates (where it was copied during the Docker build).
![Screenshot 2025-01-28 144335](https://github.com/user-attachments/assets/848c998e-d9b7-4681-9a8a-a5e0c579512a)
