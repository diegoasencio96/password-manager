FROM python:3.7
MAINTAINER Diego Alejandro Asencio Cuellar <diegoasencio96@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install gdal-bin -y
COPY . code
WORKDIR code
RUN pip install -r requirements.txt
EXPOSE 8000
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
CMD ["sh", "/docker-entrypoint.sh"]