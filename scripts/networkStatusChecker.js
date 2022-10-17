// LANGUAGE: Javascript
// ENV: JavaScript
// AUTHOR: Mohasin Haque
// GITHUB: https://github.com/Mohasin-Haque


if(window.navigator.onLine){
    setOnline()
}else{
    setOffline()
}

window.addEventListener('online', () => {
    setOnline()
})

window.addEventListener('offline', () => {
    setOffline()
})

function setOnline() {
    titleTarget.textContent = 'Online 😊'
    titleTarget.style.color = 'green'
}
function setOffline() {
    titleTarget.textContent = 'Offline 😢'
    titleTarget.style.color = 'green'
}