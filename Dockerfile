FROM python:3.12-slim

# Set up a new user named "user" with UID 1000
RUN useradd -m -u 1000 user

# Set environment variables
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Set the working directory
WORKDIR $HOME/app

# Install dependencies
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application code
COPY --chown=user . .

# Expose the port Hugging Face expects (7860)
EXPOSE 7860

# Run the application
CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0", "--port", "7860"]
