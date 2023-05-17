function initinventory() {
  fetch('/init-inventory', {
    method: 'POST',
  })
}

function updateinventory() {
  fetch('/update-inventory', {
    method: 'POST',
  })
    .then((response) => response.json())
    .then((jsonResponse) => {
    })
}