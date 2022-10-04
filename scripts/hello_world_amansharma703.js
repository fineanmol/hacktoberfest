// LANGUAGE: Javascript
// ENV: Node.js
// AUTHOR: Aman Sharma
// GITHUB: https://github.com/amansharma703

console.log("Hello, World!");

// Snippet for Uploading Image to AWS S3 Bucket
export const storeScrapedProfilePic = async (username, url) => {
    // Configure aws s3 credentials
    const s3 = new AWS.S3({
        accessKeyId: config.awsS3SecretKey,
        secretAccessKey: config.awsS3KeyId,
    });

    // make get request to download image to your local server
    const res = await axios({
        url,
        method: "GET",
        responseType: "stream",
    });

    // saved to download to images folder
    const imgPath = path.resolve(__dirname, "images", `${username}.jpeg`);
    const writer = fs.createWriteStream(imgPath);
    res.data.pipe(writer);
    const blob = fs.readFileSync(imgPath);

    // upload image to aws s3 bucket
    const uploadedImage = await s3
        .upload({
            Bucket: process.env.AWS_S3_BUCKET_NAME,
            Key: `${username}.jpeg`,
            Body: blob,
        })
        .promise();
    console.log(uploadedImage.Location);
    return uploadedImage.Location;
};
