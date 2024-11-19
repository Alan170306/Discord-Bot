# Discord-Bot

This guide will help you set up and run the Discord bot.

---

## Prerequisites

- **Python**: Check if Python is installed on your system by running the following command:

  ```bash
  python --version
  ```
  If Python is not installed, download the correct version from the official [Python website](https://www.python.org/downloads/) and install it. Verify the installation again with the command above.
   
- **Pip**: Pip is the package management system for Python. If it wasn’t installed automatically with Python, follow one of these tutorials to install it:
  - Linux: [Installationsanleitung für Linux](https://www.geeksforgeeks.org/how-to-install-pip-in-linux/)
  - Windows: [Installationsanleitung für Windows](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)


## Create a Virtual Environment and Install Packages

1. **Create a Virtual Environment**  
   Navigate to the root folder of this project and run the following command:
   
   ```bash
   python -m venv .venv
   ```
   
2. **Activate the Virtual Environment**
    - Linux
      
      ```bash
      source .venv/bin/activate
      ```
      
    - Windows
      
      ```bash
      .\.venv\bin\activate
      ```
3. **Install the discord.py Package**  
   Once the virtual environment is activated, install the required package by running:
   ```bash
   pip install discord.py
   ```

## Run the Bot

1. **Activate the Virtual Environment**  
   If the virtual environment is not already active, activate it using the commands described above.

2. **Run the Bot**
   Start the bot by executing the following command:
   ```bash
   python bot.py
   ```
    

   
