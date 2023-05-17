function showinventory() {
    fetch('/showinventory')
      .then((response) => response.json())
      .then((jsonResponse) => {
        if (jsonResponse.success) {
          const InventoryTableBody = document.getElementById(
            'InventoryTableBody',
          )
          const products = jsonResponse.products
          if (products.length == 0) {
            InventoryTableBody.innerHTML = 'No inventory found'
          } 
          else {
            InventoryTableBody.innerHTML = ''
            products.forEach((product) => {
              const tr = document.createElement('tr')
              tr.innerHTML = `
                      <td>${product.name}</td>
                      <td>${product.stock}</td>
                      <td>${product.PCompra}</td>
                      <td>${product.CVu}</td>
                      <td>${product.PVu}</td>
                    `
                InventoryTableBody.appendChild(tr)
            })
          }
        }
      })
    }
    function mostrarhola() {
      console.log("Hola")
    }