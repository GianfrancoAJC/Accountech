function updateInventoryClient(event) {
  event.preventDefault(); 
  const form = document.getElementById('UpdateInventoryClient');
  const formData = new FormData(form);
  fetch('/update-inventory-client', {
    method: 'POST',
    body: formData,
  })
  .then(function (response){
    console.log(response)
    return response.json()  
  })
  .then(function (jsonResponse) {
    const result = document.getElementById('result')
    if(jsonResponse.success){
      result.innerHTML = jsonResponse.message
      setTimeout(() => {
        form.reset()
        result.innerHTML = ''
      }, 3000)
    }
    else {
      result.innerHTML = jsonResponse.message
    }
    //result.innerHTML = jsonResponse.message
  })
    
} 