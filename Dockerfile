# Base image
FROM python:3.11-slim

# Install required Python packages
RUN pip install --no-cache-dir \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    scikit-learn \
    scipy \
    requests

# Create working directory
RUN mkdir -p /app/pipeline/

# Copy project files into the container
COPY . /app/pipeline/

# Set working directory
WORKDIR /app/pipeline/

# Start interactive bash shell
CMD ["bash"]