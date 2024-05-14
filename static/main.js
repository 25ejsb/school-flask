$(async function() {
    response = await fetch("/gettime")
    let promise = Promise.resolve(response.json())
    promise.then(data => {
        document.querySelector("main .cal-right h2").textContent = data['Content']
    })
})
setInterval(async function() {
    response = await fetch("/gettime")
    let promise = Promise.resolve(response.json())
    promise.then(data => {
        document.querySelector("main .cal-right h2").textContent = data['Content']
        var caltext = ata["Content"].split(", ")[3].split(" ")[0]
        var ampm = data["Content"].split(", ")[3].split(" ")[1]
        console.log(caltext)
        if (["02:59:50", "02:59:51", "02:59:52", "02:59:53", "02:59:54", "02:59:55", "02:59:56", "02:59:57", "02:59:58", "02:59:59"].includes(caltext) && ampm === "PM") {
            console.log("hi")
            document.querySelector("main .cal-right h2").style = `color: rgb(${Math.round(Math.random()*255)}, ${Math.round(Math.random()*255)}, ${Math.round(Math.random()*255)});`
        } else if (["03:00:00"].includes(caltext) && ampm === "PM") {
            document.querySelector("main .cal-right h2").style = `color: #BBA53D;`
        } {
            document.querySelector("main .cal-right h2").style = `color: rgb(255, 255, 255);`
        }
    })
}, 1000);

$(async function() {
    response = await fetch("https://api.openweathermap.org/data/2.5/weather?appid=02d5313f254a2c3a43eb6e398fb5c9a7&q=Marblehead")
    .then((response) => response.json())
    .then((responseJson) => {
        console.log(responseJson)
        document.querySelector(".weather-min h1").innerHTML = `${Math.round((+responseJson["main"]["temp_min"] - 273.15) * 9/5 + 32)}°`
        document.querySelector(".weather-current h1").innerHTML = `${Math.round((+responseJson["main"]["temp"] - 273.15) * 9/5 + 32)}°`
        document.querySelector(".weather-max h1").innerHTML = `${Math.round((+responseJson["main"]["temp_max"] - 273.15) * 9/5 + 32)}°`
        document.querySelector(".weather-feeling").innerHTML = `${Math.round((+responseJson["main"]["feels_like"] - 273.15) * 9/5 + 32)}°`
    });
})

setInterval(async function() {
    response = await fetch("https://api.openweathermap.org/data/2.5/weather?appid=02d5313f254a2c3a43eb6e398fb5c9a7&q=Marblehead")
    .then((response) => response.json())
    .then((responseJson) => {
        console.log(responseJson)
        document.querySelector(".weather-min h1").innerHTML = `${Math.round((+responseJson["main"]["temp_min"] - 273.15) * 9/5 + 32)}°`
        document.querySelector(".weather-current h1").innerHTML = `${Math.round((+responseJson["main"]["temp"] - 273.15) * 9/5 + 32)}°`
        document.querySelector(".weather-max h1").innerHTML = `${Math.round((+responseJson["main"]["temp_max"] - 273.15) * 9/5 + 32)}°`
        document.querySelector(".weather-feeling").innerHTML = `${Math.round((+responseJson["main"]["feels_like"] - 273.15) * 9/5 + 32)}°`
    });
}, 10000)