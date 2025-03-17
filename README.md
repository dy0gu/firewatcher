# Wildfire info with discord! 🔥ℹ️

![logo](src/assets/logo.png)

Firewatcher gets its data from the [fogos.pt](https://fogos.pt/) API and is mostly a simple wrapper around it. Due to the nature of the API, the bot is only able to provide information about wildfires in Portugal.

## Usage 🔦

This bot can be added to discord servers through the following [link](https://discord.com/oauth2/authorize?client_id=999712607227359274&permissions=0&scope=bot).

## Development 🛠️

- ### Requirements 📋

  - Python ([version](pyproject.toml#L5))

- ### Setup ⚙️

  - Clone the repository and open a terminal **inside** it.

  - Install the dependencies:

    ```shell
    # Creating a virtual environment is recommended before installing any project dependencies!

    pip install .
    ```

- Create a `.env` file based on the [`.env.example`](.env.example) file.

  - Start the app:

    ```shell
    python src/bot.py
    ```

- ### Tooling 🧰

  - Ruff is used as a linter and formatter:

    ```shell
    pip install .[check]
    ruff check --fix
    ruff format

    # To automatically lint and format on every commit install the pre-commit hooks:
    pre-commit install

    # When using pre-commit hooks, commits may fail if files with errors are checked.
    # Changed files must be added to the staged area and commited again to apply fixes.
    # If you run into any issues just manually run the linter commands above to address them.
    ```

## Deployment 🚀

The bot is automatically built by a pipeline with every release, so a **Docker** image is available in the **Packages** section of the repository.

- Supply the [required environment variables](.env.example) when running the container, just like in development.

- Start the container using the provided `docker-compose.yaml`:

  ```shell
  # The example compose will try to pull from the registry first, and only builds on fails.
  # To force a build first, simply remove the image key from the service definition.

  docker compose up --build --force-recreate --detach --wait --wait-timeout 120
  ```

- Serve it using your server configuration of choice!
