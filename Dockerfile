FROM python:3.7

# Create workdir
RUN mkdir app
WORKDIR /app

#ENV PYTHONUNBUFFERED 1

# Copy directory into docker filesystem
ADD . .

# Install requirements
RUN pip install -r requirements.txt

## Expose ports
EXPOSE 80

# Command
#CMD bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]



