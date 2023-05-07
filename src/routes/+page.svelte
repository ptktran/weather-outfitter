<!-- +page.svelte -->
<script>
// @ts-nocheck

  import Geolocation from 'svelte-geolocation';
  import { onMount }  from 'svelte'
  import Loader from './lib/Loader.svelte';
  import Navbar from './lib/Navbar.svelte';
  import { json } from '@sveltejs/kit';

  let loading = true;
  let date = new Date();
  let coords;
  let userLocation;
  
  onMount(() => {
    const interval = setInterval(() => {
      date = new Date();
      formattedTime = getTime();
    }, 1000);
    return () => clearInterval(interval);
  })

  onMount(async () => {
    if (localStorage.getItem('userLocation')) {
      userLocation = localStorage.getItem('userLocation');
    }
    else {
      try {
        coords = await getLocation();
        console.log(coords);
        const response = await fetch(`https://geocode.maps.co/reverse?lat=${coords.latitude}&lon=${coords.longitude}`);
        const data = await response.json(); 
        userLocation = await data.address.city;
        localStorage.setItem('userLocation', userLocation);
      } catch (error) {
        console.log(error);
      }
    }
    loading = false;
  })

  function getLocation() {
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

  function getDate() {
    return `${date.getMonth() + 1}/${date.getDate()}/${date.getFullYear()}`
  }

  $: formattedTime = getTime()
  function getTime() {
    var time = date.toString().split(' ')[4].slice(0,5);
    if (parseInt(time.slice(0,2)) > 12 && parseInt(time.slice(0,2)) < 24) {
      time += ' PM';
    }  else {
      time += ' AM';
    }
    return time;
  }
</script>

<div class="h-screen bg-gradient-to-b from-blue-600 to-sky-400">
  <Navbar />
  <main>
    <div class="md:h-96 sm:h-72">
      <div class="sm:w-5/6 h-full p-9 bg-gray-200 border rounded-lg shadow m-auto my-7 text-center">        
        {#if loading}
          <h1 class="sm:text-xl text-2xl font-univers text-white m-2">Getting your location...</h1>
          <Loader />
        {:else}
          <h1 class="sm:text-8xl md:text-9xl font-univers text-white"></h1>
          <h1 class="sm:text-2xl text-3xl font-univers text-white">
            {userLocation}
          </h1>
          <h1 class="sm:text-2xl text-3xl font-univers text-white">
            {formattedTime}
          </h1>
        {/if}
      </div>
    </div>

    <div />

    <div />
  </main>
</div>
