// Hacktoberfest dvd screensaver
// It uses the p5.js library (https://p5js.org/)
// Author: David Anastasov
// Github: https://github.com/davidanastasov

const speed = {
  x: 2,
  y: 1,
};

const direction = {
  x: 1,
  y: 1,
};

const textBoundingBox = {
  x: 0,
  y: 0,
  width: 295,
  height: 38,
};

const textColor = {
  r: 0,
  g: 0,
  b: 0,
};

function setup() {
  const windowWidth = window.innerWidth;
  const windowHeight = window.innerHeight;
  createCanvas(windowWidth, windowHeight);

  // Pick random starting position
  textBoundingBox.x = random(width - textBoundingBox.width);
  textBoundingBox.y = random(height - textBoundingBox.height);

  pickRandomTextColor();
  pickRandomSpeed();
}

function pickRandomTextColor() {
  textColor.r = random(255);
  textColor.g = random(255);
  textColor.b = random(255);
}

function pickRandomSpeed() {
  speed.x = random(1, 5);
  speed.y = random(0.5, 2.5);
}

function draw() {
  background(0);

  textSize(48);
  fill(textColor.r, textColor.g, textColor.b);
  text(
    "Hacktoberfest",
    textBoundingBox.x,
    textBoundingBox.y,
    textBoundingBox.width
  );

  textBoundingBox.x += speed.x * direction.x;
  textBoundingBox.y += speed.y * direction.y;

  let bounced = false;

  // Left
  if (textBoundingBox.x < 0) {
    textBoundingBox.x = 0;
    direction.x *= -1;
    bounced = true;
  }

  // Top
  if (textBoundingBox.y < 0) {
    textBoundingBox.y = 0;
    direction.y *= -1;
    bounced = true;
  }

  // Right
  if (textBoundingBox.x + textBoundingBox.width > width) {
    textBoundingBox.x = width - textBoundingBox.width;
    direction.x *= -1;
    bounced = true;
  }

  // Bottom
  if (textBoundingBox.y + textBoundingBox.height > height) {
    textBoundingBox.y = height - textBoundingBox.height;
    direction.y *= -1;
    bounced = true;
  }

  if (bounced) {
    pickRandomTextColor();
    pickRandomSpeed();
  }
}
