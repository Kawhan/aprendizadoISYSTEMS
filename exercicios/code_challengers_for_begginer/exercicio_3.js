// Create a length converter function

function converter_km_miles(km) {
    const miles = 0.621371;

    return (miles * km).toFixed(5);
}

console.log(converter_km_miles(3));
