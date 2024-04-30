FROM python:3.10.12
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 80
ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT
CMD ["uvicorn", "main:fastapi_app", "--host", "0.0.0.0", "--port", "80"]