server {
    listen 80;
    server_name memesim.fun www.memesim.fun;

    # Serve static files
    location /static/ {
        alias /usr/src/tbull/static/;
    }

    # Proxy pass to Django application
    location / {
        proxy_pass http://web:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;  # Since we're using HTTP, this will be 'http'
    }
}
