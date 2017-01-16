FROM python:3.6
RUN apt-get install curl
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs
RUN mkdir /code
WORKDIR /code
RUN mkdir requirements
ADD bikeshop_project /code
COPY requirements /code/requirements
RUN pip install -r requirements/production.txt
RUN npm cache clean
RUN npm install bower -g
RUN bower install
RUN npm install --unsafe-perm
RUN npm run build-production
RUN DJANGO_SETTINGS_MODULE=bikeshop.settings.production python manage.py collectstatic --no-input
