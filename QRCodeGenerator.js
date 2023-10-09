import inquirer from "inquirer";
import qr from "qr-image";
import fs from "fs";
inquirer
  .prompt([
    {
      message: "Type the URL for which you want to generate the QR",
      name: "URL",
    },
  ])
  .then((answers) => {
    const url = answers.URL;

    var qr_svg = qr.image(url); // We have removed the "type" because by default it is ".png" and we are passing "url" as "text" input because we want to create QR for for our url only, if we give any text then it will show the text message if we scan our QR which will be generated
    qr_svg.pipe(fs.createWriteStream("URL_2.png")); // with "fs" native module of Node we save the QR which is generated as ".png" image file and save it in our computer inside our current directory
    fs.writeFile("./url_2.txt", url, (err) => {
      //One mistake we did is we didn't add "fs" before "writeFile" so no text file was being generated but as we corrected it as "fs.writeFile()" we got our desired text file which we wanted.
      // We passed our "url" in "data" parameter as here want to create a file named "url.txt" which will store the url or any message or text which the user inputs as text in this file.
      if (err) throw err;
      console.log("The file has been saved!");
    });
  })
  .catch((error) => {
    if (error.isTtyError) {
      // Prompt couldn't be rendered in the current environment
    } else {
      // Something else went wrong
    }
  });
