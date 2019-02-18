FROM jfloff/alpine-python

RUN  pip install pyowm

COPY getweather.py /tmp/getweather.py

ENTRYPOINT ["/usr/bin/python"]
CMD ["/tmp/getweather.py"]
