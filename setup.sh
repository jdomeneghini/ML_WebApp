mkdir -p .streamlit/
printf "[general]\n\
email=\"jessicadomeneghini@gmail.com\"\n" > .streamlit/credentials.toml

printf "[server]\n\
headless=true\n\
enableCORS=true\n\
port = $PORT\n" > .streamlit/config.toml

