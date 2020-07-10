FROM python:3.7

# Create workdir
RUN mkdir app
WORKDIR /app

# Copy directory into docker filesystem
ADD . .

# Install requirements
RUN pip install -r requirements.txt

# Export

