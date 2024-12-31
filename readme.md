docker build -t usd-to-inr-converter .
docker run -d -p 5000:5000 usd-to-inr-converter
curl "http://localhost:5000/convert?usd=100"
