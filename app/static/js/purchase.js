function initinventory() {
  fetch('/init-inventory', {
    method: 'POST',
  })
}

function updateinventory() {
  fetch('/update-inventory', {
    method: 'POST',
  })
  .then(function (response){
    console.log(response)
    return response.json()  
  })
  .then(function (jsonResponse) {
    const result = document.getElementById('result')
    if(jsonResponse.success){
      result.innerHTML = ''
    }
    else {
      result.innerHTML = jsonResponse.message
    }
    //result.innerHTML = jsonResponse.message
  })
    
} 