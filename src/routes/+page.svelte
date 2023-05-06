<!-- +page.svelte -->
<script>
  import { onMount }  from 'svelte'

  let date = new Date()
  
  function getDate() {
    return `${date.getMonth() + 1}/${date.getDate()}/${date.getFullYear()}`
  }

  $: formattedTime = getTime()
  let getTime = () => date.toString().split(' ')[4].slice(0,5)
  
  onMount(() => {
    const interval = setInterval(() => {
      date = new Date();
      formattedTime = getTime();
    }, 1000);
    return () => clearInterval(interval);
  })
</script>
<div class="h-screen bg-gradient-to-b from-blue-600 to-sky-400">
  <nav class="flex justify-between items-center bg-gray-100 backdrop-blur-xl py-2">
    <div class="flex justify-center items-center mx-2">
      <img src="src/assets/app-logo.svg" alt="app logo" class="mx-2">
      <p class="text-white font-welbut" id="logo">weather outfitter</p>
    </div>
    <div class="flex justify-center items-center mx-2">
      <img src="src/assets/help-icon.svg" class="mx-1" alt="help icon">
      <img src="src/assets/dark-icon.svg" class="mx-1" alt="dark mode icon">
      <img src="src/assets/light-icon.svg" class="mx-1" alt="light mode icon">
    </div>
  </nav>
  <main>
  </main>
</div>
