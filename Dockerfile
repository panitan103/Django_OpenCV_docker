FROM  python

COPY django_opencv/requirements.txt .

RUN pip3 install -U -r requirements.txt

ADD django_opencv/ /django_opencv

WORKDIR /django_opencv 

EXPOSE 8001

RUN python3 manage.py collectstatic --noinput