// Get the Count
fetch("https://cdrcecountapp.azurewebsites.net/count",{
    method: 'GET',
}).then(function (response) {
    return response.json();
}).then(function (responseJson) {
    document.getElementById("count").innerHTML = responseJson.count;
}).catch(function (error) {
    console.log(error);
});

// Add Visitors
fetch('http://ip-api.com/json/',{
    method: 'GET'
}).then(function (response) {
    return response.json();
}).then(function (responseJson) {    
    fetch("https://cdrcecountapp.azurewebsites.net/add",{
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ip: responseJson.query,
            timestamp: new Date().toISOString(),
            country: responseJson.country,
            city: responseJson.city,
        })
    }).then(function (response) {
        return response.json();
    }).then(function (responseJson) {
        console.log(responseJson);
    }).catch(function (error) {
        console.log(error);
    });
}).catch(function (error) {
    console.log(error);
});