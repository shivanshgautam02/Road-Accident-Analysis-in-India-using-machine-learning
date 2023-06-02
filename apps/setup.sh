mkdir -p ~/.streamlit/

echo "\
[server]\n\
port=$PORT\n\
enableesCORS= false\n\
headless=true\n\
\n\
" > ~/.streamlit/config.toml