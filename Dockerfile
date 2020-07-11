FROM python:3.7

# Create workdir
RUN mkdir app
WORKDIR /app

ENV PYTHONUNBUFFERED 1

# Copy directory into docker filesystem
ADD . .

# Install requirements
RUN pip install -r requirements.txt

## Expose ports
#EXPOSE 8080 80 443



