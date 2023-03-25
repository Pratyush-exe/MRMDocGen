# Use Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Install system packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    virtualenv

# Create a virtualenv
RUN virtualenv -p python3 /opt/venv

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the local directory to the container at /app
COPY . /app

# Activate the virtualenv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the default Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py"]
