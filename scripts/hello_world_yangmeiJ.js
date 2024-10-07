//Langauge: Javascript
//ENV : Node.js
//Author: YangmeiJ
//GITHUB: https://github.com/Apecool

import http from 'http';
import figlet from 'figlet';
import chalk from 'chalk';

const PORT = 3000;

const requestHandler = (req, res) => {
    // Generate ASCII art
    const asciiArt = figlet.textSync('Hello, World!', {
        font: 'Standard',
        horizontalLayout: 'default',
        verticalLayout: 'default'
    });

    // Create a styled HTML response
    const htmlResponse = `
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Fancy Hello World</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background: linear-gradient(135deg, #f3ec78, #af4261);
                    font-family: 'Courier New', monospace;
                    color: #fff;
                    white-space: pre;
                }
                h1 {
                    font-size: 2rem;
                    text-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
                }
            </style>
        </head>
        <body>
            <h1>${asciiArt.replace(/ /g, '&nbsp;').replace(/\n/g, '<br>')}</h1>
        </body>
        </html>
    `;

    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(htmlResponse);
};

const server = http.createServer(requestHandler);

server.listen(PORT, () => {
    console.log(chalk.bgGreen.black(`Server is running on http://localhost:${PORT}`));
    console.log(chalk.blue('Visit your browser and see the ASCII art magic!'));
});
