function updateInventoryClient() {
    fetch('/update-inventory-client', {
      method: 'POST',
    })
      .then((response) => response.json())
      .then((jsonResponse) => {
        console.log(jsonResponse.message)
      })
  }