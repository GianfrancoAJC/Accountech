function initinventory() {
  fetch('/init-inventory', {
    method: 'POST',
  })
}

function updateinventory(event) {
  event.preventDefault(); 
  const form = document.getElementById('UpdateInventory');
  const formData = new FormData(form);
  fetch('/update-inventory', {
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