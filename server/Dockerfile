    FROM python:3.10.12

    ENV PYTHONBUFFERED 1
    ENV PYTHONWRITEBYCODE 1

    ENV APP=/app 

    WORKDIR ${APP}

    COPY requirements.txt ${APP}

    RUN pip3 install -r requirements.txt

    COPY . ${APP}

    EXPOSE 8000

    RUN chmod +x /app/entrypoint.sh

    ENTRYPOINT [ "/bin/bash", "/app/entrypoint.sh" ]

    CMD ["gunicorn", "--bind", ":8000", "--workers", "3","djangoproj.wsgi"]