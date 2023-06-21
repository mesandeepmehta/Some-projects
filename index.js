// Word bank
const words = ["hangman", "javascript", "programming", "openai", "coding"];

let chosenWord;
let hiddenWord;
let wrongGuesses;

function initGame() {
    // Randomly choose a word from the word bank
    chosenWord = words[Math.floor(Math.random() * words.length)];

    // Initialize hidden word with underscores
    hiddenWord = "_".repeat(chosenWord.length);

    // Initialize wrong guesses
    wrongGuesses = "";

    // Display initial state
    document.getElementById("word").textContent = hiddenWord;
    document.getElementById("wrongGuesses").textContent = wrongGuesses;
    document.getElementById("hangman").style.backgroundImage = "url('hangman.png')";
    document.getElementById("message").textContent = "";
}

function updateWord(letter) {
    let newHiddenWord = "";

    for (let i = 0; i < chosenWord.length; i++) {
        if (chosenWord[i] === letter) {
            newHiddenWord += letter;
        } else {
            newHiddenWord += hiddenWord[i];
        }
    }

    hiddenWord = newHiddenWord;
    document.getElementById("word").textContent = hiddenWord;
}

function updateWrongGuesses(letter) {
    wrongGuesses += letter;
    document.getElementById("wrongGuesses").textContent = wrongGuesses;

    // Update hangman image
    const hangmanImages = [
        "hangman.png",
        "hangman1.png",
        "hangman2.png",
        "hangman3.png",
        "hangman4.png",
        "hangman5.png",
        "hangman6.png",
    ];
    const numWrongGuesses = wrongGuesses.length;

    if (numWrongGuesses < hangmanImages.length) {
        document.getElementById("hangman").style.backgroundImage =
            "url('" + hangmanImages[numWrongGuesses] + "')";
    }
}

function checkGameState() {
    if (hiddenWord === chosenWord) {
        document.getElementById("message").textContent = "Congratulations! You won!";
    } else if (wrongGuesses.length === 6) {
        document.getElementById("message").textContent =
            "Game Over! The word was: " + chosenWord;
    }
}

function makeGuess() {
    const guess = prompt("Enter a letter:").toLowerCase();

    if (guess && guess.match(/^[a-z]$/)) {
        if (chosenWord.includes(guess)) {
            updateWord(guess);
        } else {
            updateWrongGuesses(guess);
        }
    }

    checkGameState();
}

// Start the game
initGame();