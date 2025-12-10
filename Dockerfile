FROM nginx:alpine

# Удаляем стандартную страницу nginx
RUN rm -rf /usr/share/nginx/html/*

# Копируем файлы сайта
COPY . /usr/share/nginx/html/

# Открываем порт 80
EXPOSE 80
