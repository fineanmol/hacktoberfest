document.addEventListener('DOMContentLoaded', () => {
    const board = document.getElementById('game-board');
    const gridSize = 20;
    const snakeSpeed = 200; // milliseconds
    const snake = [{ x: 10, y: 10 }];
    let direction = 'right';
    let food = generateFood();

    function generateFood() {
        const food = {
            x: Math.floor(Math.random() * gridSize),
            y: Math.floor(Math.random() * gridSize)
        };
        return food;
    }

    function draw() {
        // Clear previous state
        board.innerHTML = '';

        // Draw snake
        snake.forEach(segment => {
            const snakeSegment = document.createElement('div');
            snakeSegment.className = 'snake';
            snakeSegment.style.gridRowStart = segment.y + 1;
            snakeSegment.style.gridColumnStart = segment.x + 1;
            board.appendChild(snakeSegment);
        });

        // Draw food
        const foodElement = document.createElement('div');
        foodElement.className = 'food';
        foodElement.style.gridRowStart = food.y + 1;
        foodElement.style.gridColumnStart = food.x + 1;
        board.appendChild(foodElement);
    }

    function move() {
        const head = { ...snake[0] };

        // Move the head in the current direction
        switch (direction) {
            case 'up':
                head.y = (head.y - 1 + gridSize) % gridSize;
                break;
            case 'down':
                head.y = (head.y + 1) % gridSize;
                break;
            case 'left':
                head.x = (head.x - 1 + gridSize) % gridSize;
                break;
            case 'right':
                head.x = (head.x + 1) % gridSize;
                break;
        }

        // Check for collisions with food
        if (head.x === food.x && head.y === food.y) {
            snake.unshift(generateFood());
        } else {
            // Remove the tail of the snake
            snake.pop();
        }

        // Update the direction
        snake.unshift(head);

        // Check for collisions with the snake's body
        if (checkCollision()) {
            alert('Game Over!');
            resetGame();
        }

        // Draw the updated state
        draw();
    }

    function checkCollision() {
        // Check if the head collides with any other segment of the snake
        return snake.slice(1).some(segment => segment.x === snake[0].x && segment.y === snake[0].y);
    }

    function resetGame() {
        snake.length = 1;
        snake[0] = { x: 10, y: 10 };
        direction = 'right';
        food = generateFood();
    }

    function handleKeyPress(event) {
        switch (event.key) {
            case 'ArrowUp':
                direction = 'up';
                break;
            case 'ArrowDown':
                direction = 'down';
                break;
            case 'ArrowLeft':
                direction = 'left';
                break;
            case 'ArrowRight':
                direction = 'right';
                break;
        }
    }

    // Event listeners
    document.addEventListener('keydown', handleKeyPress);

    // Game loop
    setInterval(move, snakeSpeed);

    // Initial draw
    draw();
});
