FROM python:3.8-slim

LABEL "com.github.actions.name"="PR Handler"
LABEL "com.github.actions.description"="Create/trigger companion PR in a parent repository"
LABEL "com.github.actions.icon"="activity"
LABEL "com.github.actions.color"="orange"

RUN pip install requests

COPY pr-handler.py /pr-handler.py

ENTRYPOINT ["/pr-handler.py"]
