# github-monitor-integration-backend
API server for monitoring pull requests

To run the app, first clone it into your working environment.

Then, prepare a .env file in the root folder that contains:

MONGO_INITDB_ROOT_USERNAME=<br>
MONGO_INITDB_ROOT_PASSWORD=<br>
MONGO_URL=<br>
FIREBASE_PRIVATE_KEY_PATH=<br>
FRONTEND_URL=<br>
PORT=<br>


Then, run the following docker commands in the root directory:

docker build -t github-monitor-integration-image .

docker run -p <your_custom_port>:<PORT_ENVIRONMENT_VARIABLE>  --env-file <your_env_path> --rm --name github-monitor-integration-container github-monitor-integration-image
