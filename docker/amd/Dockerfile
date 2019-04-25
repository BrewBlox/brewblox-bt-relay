FROM python:3.7 as base

COPY ./dist /app/dist
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install wheel \
    && pip3 wheel --wheel-dir=/wheeley -r /app/requirements.txt \
    && pip3 wheel --wheel-dir=/wheeley --find-links=/wheeley --no-index /app/dist/*

FROM python:3.7-slim
EXPOSE 5010
WORKDIR /app

COPY --from=base /wheeley /wheeley
COPY ./config /app/config

RUN pip3 install --no-index --find-links=/wheeley brewblox-bt-relay \
    && rm -rf /wheeley \
    && pip3 freeze \
    && apt-get clean \
    && apt-get update \
    && apt-get install -y \
    libglib2.0-dev \
    libatlas3-base

ENTRYPOINT ["python3", "-m", "brewblox_bt_relay"]
