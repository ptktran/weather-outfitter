<!-- +page.svelte -->
<script>
  import { onMount }  from 'svelte'
  import Loader from '../lib/Loader.svelte';
  import Navbar from '../lib/Navbar.svelte';
  import { getCoords, getCityName, getWeatherData, getCurrentWeather } from '../api/api.js';

  let mode = 'light'
  let date = new Date()
  let loading = true;
  let latitude, longitude
  let coords
  let weatherData
  let userLocation
  let icon = 'src/assets/animated/clear-night.svg'
  
  function getTime() {
    var time = date.toString().split(' ')[4].slice(0,5);
    if (parseInt(time.slice(0,2)) > 12 && parseInt(time.slice(0,2)) < 24) {
      time += ' PM';
    }  else {
      time += ' AM';
    }
    return time;
  }

  onMount(() => {
    const interval = setInterval(() => {
      date = new Date();
      formattedTime = getTime(date);
    }, 1000);
    return () => clearInterval(interval);
  })

  onMount(async () => {
    // if (localStorage.getItem('userLocation')) {
    //   userLocation = localStorage.getItem('userLocation');
    // }
    // else {
    try {
      coords = await getCoords()
      latitude = coords.latitude 
      longitude = coords.longitude
      userLocation = await getCityName(latitude, longitude);
      localStorage.setItem('userLocation', userLocation);
      localStorage.setItem('userCoords', [latitude, longitude]);
      weatherData = await getCurrentWeather(latitude, longitude)
      console.log(weatherData)
    } catch (error) {
      console.log(error);
    }
    loading = false;
  })
  // function getDate() {
  //   return `${date.getMonth() + 1}/${date.getDate()}/${date.getFullYear()}`
  // }
  $:formattedTime = getTime()
</script>
<div class="h-screen bg-gradient-to-b from-darkblue-600 to-darkblue-200">
  <Navbar />
  <main>
    <div class="h-full border border-black md:flex">
      <div class="sm:w-0 md:w-1/6"></div>
      <div class="sm:w-6/6 md:w-2/6 h-max p-9 bg-gray-200 border rounded-lg shadow mx-2 my-7 text-center">        
        {#if loading}
          <h1 class="sm:text-xl text-2xl font-univers text-white m-2">Getting your location...</h1>
          <Loader />
        {:else}
          <div class="flex w-fit items-center m-auto">
            <img src={icon} class="m-auto w-28 border">
            <h1 class="sm:text-4xl md:text-6xl font-univers text-white">
              {Math.round(weatherData.temperature)}°C
            </h1>
          </div>
          <h1 class="sm:text-2xl text-3xl font-univers text-white">
            {userLocation}
          </h1>
          <h1 class="sm:text-2xl text-3xl font-univers text-white">
            {formattedTime}
          </h1>
        {/if}
      </div>

      <div class="sm:w-6/6 md:w-2/6 h-max p-9 bg-gray-200 border rounded-lg shadow mx-2 my-7 text-center">
        Hello
      </div>
      <div class="sm:w-0 md:w-1/6"></div>
    </div>
  </main>
</div>
