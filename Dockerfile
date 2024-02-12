FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Amsterdam

RUN apt-get update && \
    apt-get install --no-install-recommends -y python3 python3-pip python3-virtualenv && \
    apt-get install --no-install-recommends -y libopencv-dev python3-opencv && \
    rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/venv
RUN virtualenv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install packaging

WORKDIR /app

COPY . /app/
COPY /data ./data
CMD ln -s /data/checkpoints /app/repositories/Fooocus/models/checkpoints
CMD ln -s /data/loras /app/repositories/Fooocus/models/loras

CMD python main.py --port 7999 --host 0.0.0.0 --apikey 5d1c8432-a0e0-42f9-8d53-c1fd3f301b8f