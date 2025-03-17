# Wildfire info with discord! 🔥ℹ️

![logo](src/assets/logo.png)

Firewatcher gets its data from the [fogos.pt](https://fogos.pt/) API and is mostly a simple wrapper around it. Due to the nature of the API, the bot is only able to provide information about wildfires in Portugal.

## Installation 🛠️

- Clone the repository:

  ```shell
  git clone https://github.com/Dy0gu/Firewatcher.git
  ```

- Install Python 3.12 or higher.

- Install all dependencies:

  ```shell
  pip install -r requirements.txt
  ```

- Create a `.env` file based on the `.env.example` file.

## Usage 💻

- Run the app:

  ```shell
  python bot.py
  ```

## Containerization 📦

To run in a containerized environment use the provided `Dockerfile`, the runner machine only needs to have Docker installed.
There is still the need to create a `.env` file before the build, since its contents need to be included in the image.

- Build the image:

  ```shell
  docker build -t firewatcher .
  ```

- Run the container:

  ```shell
  docker run -d firewatcher
  ```
