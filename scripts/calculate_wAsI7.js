const { google } = require('googleapis');
const sheets = google.sheets('v4');
const key = require('./credentials.json/sheetKey.json');

const express = require('express');
const app = express();
const port = 3000;

let goldPrice18K;

const jwtClient = new google.auth.JWT(
    key.client_email,
    null,
    key.private_key,
    ['https://www.googleapis.com/auth/spreadsheets']
);

jwtClient.authorize((err) => {
    if (err) {
        console.error('Authorization failed:', err);
        return;
    }

    sheets.spreadsheets.values.get({
        auth: jwtClient,
        spreadsheetId: '1LYmg6F0AtZelZC2RdITRioRGJigqFLMC3saVDzoeV08',
        range: 'Price'
    }, (err, response) => {
        if (err) {
            console.error('The API returned an error:', err);
            return;
        }

        goldPrice18K = response.data.values;

        if (goldPrice18K.length) {
            console.log('Data from Google Sheet:');
            goldPrice18K.forEach((row) => {
                console.log(row);
            });

            delayedExecution();
        } else {
            console.log('No data found in Google Sheet.');
        }
    });
});

async function delayedExecution() {
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Your function to calculate the price
    const calculatePrice = () => {
        // For example, calculate the price based on some logic
        const basePrice = 100;
        const calculatedPrice = basePrice * 1.5;

        return calculatedPrice;
    }

    app.get('/', (req, res) => {
        const calculatedPrice = calculatePrice();
        res.send(`
            <script>
                document.getElementById('displayedPrice').textContent = 'Calculated Price: Rs ${calculatedPrice.toFixed(2)}';
            </script>
        `);
    });

    app.listen(port, () => {
        console.log(`Server running at http://localhost:${port}`);
    });
}

const twentyTwoCarat = (price18Carat) => {
    return Math.floor(1.221 * price18Carat);
}

const twentyFourCarat = (price18Carat) => {
    return Math.floor(1.332 * price18Carat);
}