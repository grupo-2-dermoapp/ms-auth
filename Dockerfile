#FROM python:3.9.16-alpine3.16
FROM python:3.9.9-slim-buster

COPY . .

# WORKDIR /backend/

RUN pip install -r requirements.txt
# cambiar el puerto
EXPOSE 3010
# cambiar el puerto
# CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "3010" ]

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]