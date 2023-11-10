## souschef-ai-server

### installation

```
poetry install
```

or

```
docker build -t souschef_ai .
```

### running

```
docker run -network <network_name> --env-file <env> souschef_ai
```

### env

OPENAI_API_KEY: private openai api key
