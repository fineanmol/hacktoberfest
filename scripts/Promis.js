const myPromise = new Promise((resolve, reject) => {
    // Asynchronous operation
    setTimeout(() => {
        const success = true;
        if (success) {
            resolve('Promise resolved successfully'); // Fulfill the promise
        } else {
            reject('Promise rejected'); // Reject the promise
        }
    }, 2000); // Simulating an asynchronous operation with a delay of 2 seconds
});

// Handling the promise
myPromise
    .then(result => {
        console.log('Success:', result); // Called if the promise is resolved
    })
    .catch(error => {
        console.error('Error:', error); // Called if the promise is rejected
