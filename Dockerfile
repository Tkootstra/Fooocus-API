FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai

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

CMD python main.py --port 8000 --host 0.0.0.0 --apikey 5d1c8432-a0e0-42f9-8d53-c1fd3f301b8f