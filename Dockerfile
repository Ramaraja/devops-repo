FROM centos:latest
MKDIR testapp
COPY webapp testapp
WORKDIR testapp
CMD ["python3", "app.py"]
