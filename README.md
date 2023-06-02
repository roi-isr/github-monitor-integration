# github-monitor-integration-backend
API server for monitoring pull requests

To run the app, first clone it into your working environment.

Then, prepare a .env file in the project's root directory that contains the following variables:

MONGO_URL=<br>
FIREBASE_PRIVATE_KEY_PATH=<br>
FRONTEND_URL=<br>
PORT=<br>


Finally, run the following Docker commands in the project's root directory (make sure that you have docker install in you environment):

**docker build -t github-monitor-integration-image .**

**docker run -p <your_custom_port>:<PORT_ENVIRONMENT_VARIABLE>  --env-file <your_env_path> --rm --name github-monitor-integration-container github-monitor-integration-image**
