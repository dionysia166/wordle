# Wordle Web Server

## Project Overview

This project focuses on developing a **web server version** of the popular game **Wordle**, designed to maintain individual game sessions for each player. The game session is preserved even after a page refresh, providing a smooth and uninterrupted experience for users. 

Collaborating with a teammate, I was able to hone my skills in project planning, branch management, and version control using **Git**. This project also gave me the opportunity to deepen my understanding of **session management** and **server-side logic** while applying best practices in web development.

### Key Technologies Used:
- **Python**
- **Flask** (Web framework)
- **HTML/CSS** (Front-end)
- **Session Management** (for saving game state)
- **Unit Testing** with **Pytest**
- **Git** (Version control)

## How to Run Locally

To run this project locally, follow these steps:

1. **Clone the Repository:**
   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/dionysia166/wordle.git
   ```

2. **Install Dependencies:**
   Install the required dependencies. Use **`uv`** to run the app:

   ```bash
   uv run flask run --debug
   ```

3. **Start the Server:**
   The app will be accessible in your browser at `http://127.0.0.1:5000/`.

## Game Features
- **Individual Game Sessions:** Each player has their own game session, allowing the progress to be saved even after a page refresh.
- **Gameplay:** The game follows the core mechanics of Wordle, where users guess a 5-letter word in up to 6 attempts.
- **Server-Side Logic:** The game state (e.g., attempts, target word, win/loss conditions) is handled on the server side using Flask sessions.
- **Feedback:** The app provides feedback for each guess, indicating whether the letters are in the correct position or part of the word.
  
## Testing

This project includes unit tests using **Pytest** to ensure the game's logic works as expected. To run the tests, simply use:

```bash
pytest
```