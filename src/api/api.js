import { weatherCodes } from "../lib/Weathercode"

export async function getCoords() {
  return new Promise((resolve, reject) => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        position => resolve(position.coords),
        error => reject(error)
      );
    } else {
      reject(new Error("Geolocation is not supported."));
    }
  });
}

export async function getCityName(latitude, longitude) {
  const response = await fetch(`https://geocode.maps.co/reverse?lat=${latitude}&lon=${longitude}`);
  const data = await response.json(); 
  return data.address.city;
}

export async function getWeatherData(latitude, longitude) {
  const response = await fetch(`https://api.open-meteo.com/v1/forecast?&latitude=${latitude}&longitude=${longitude}&current_weather=true&hourly=temperature_2m,precipitation`)
  const data = await response.json()
  console.log(data)
  return data
}

export async function getCurrentWeather(latitude, longitude) {
  const data = await getWeatherData(latitude, longitude)
  return data.current_weather
}

export function getWeatherIcon(weathercode, isDay) {
  if (weatherCodes[weathercode]) {
    if (isDay == 1) {
      return {
        'condition': weatherCodes[weathercode].condition,
        'icon': weatherCodes[weathercode].day_icon
      }
    } else {
      return {
        'condition': weatherCodes[weathercode].condition,
        'icon': weatherCodes[weathercode].night_icon
      }
    }
  }
}