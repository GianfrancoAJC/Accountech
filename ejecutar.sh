echo " "
echo "Running backend..."
export FLASK_APP=backend/app/
export FLASK_DEBUG=true
flask run --port=5002
echo " "

echo "Starting frontend..."
./frontend/execute_frontend.sh
echo " "