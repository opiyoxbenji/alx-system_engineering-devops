0x1A-Application Server Project (Holberton School)
Deadline: Feb 23, 2024, 6:00 AM

Concepts: Web server, server, web stack debugging

Tasks:

Dev env: Set up dev env on web-01 for testing/debugging (Python3, comments in config files).
Prod with Gunicorn: Install Gunicorn & libs, configure Gunicorn instance on web-01 (port 5000).
Nginx & page serving: Configure Nginx to serve page locally/publicly (port 80), proxy to Gunicorn (port 5000).
Add route with params: Expand app with /airbnb-dynamic/number_odd_or_even/(int), configure Nginx to proxy to Gunicorn (port 5001).
Serve API: Serve Airbnb clone v3 API on web-01. Configure Nginx to route /api/ to Gunicorn (port 5002).
Serve Airbnb clone: Serve Airbnb clone - Web dynamic on web-01. Configure Gunicorn (port 5003), Nginx to route /, serve static assets.
Resources:

Application server vs web server
Serve Flask app with Gunicorn & Nginx: [https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04]
Important:

Use Python3, comment config files, follow Bash script formatting.
Include required files (Nginx configs) in specified directories.
Use checker/auto review before deadline.
