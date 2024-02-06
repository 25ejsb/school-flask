$(async function() {
    response = await fetch("/gettime")
    let promise = Promise.resolve(response.json())
    promise.then(data => {
        document.querySelector("main h2").textContent = data['Content']
    })
})
setInterval(async function() {
    response = await fetch("/gettime")
    let promise = Promise.resolve(response.json())
    promise.then(data => {
        document.querySelector("main h2").textContent = data['Content']
    })
}, 1000);