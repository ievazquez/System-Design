for i in {1..7}; do
  echo "\n--- Petición $i ---"
  curl -s -i http://localhost:8000/protegido
done
