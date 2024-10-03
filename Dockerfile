FROM node:14 as builder
WORKDIR /app/static_src
COPY ./theme/static_src/package.json ./theme/static_src/package-lock.json ./
RUN npm install
COPY ./theme/static_src ./
RUN node --max_old_space_size=4096 ./node_modules/tailwindcss/lib/cli.js --postcss -i ./src/styles.css -o ../static/css/dist/styles.css --minify

FROM python:3.9
WORKDIR /app
COPY . .
COPY --from=builder /app/static/css/dist/styles.css ./theme/static/css/dist/styles.css
RUN pip install -r requirements.txt
CMD gunicorn blog_project.wsgi:application --bind 0.0.0.0:8000
