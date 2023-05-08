const pendingForms = new WeakMap()

function showContent(index) {
  const sections = document.querySelectorAll('.body__item')
  for (let i = 0; i < sections.length; i++) {
    const section = sections[i]
    if (i === index) {
      section.classList.add('body__item__active')

      if (i == 0) {
        //handle display employees
        fetchEmployees()
      } else if (i == 1) {
        //handle create new employee
        createEmployee()
      }
    } else {
      section.classList.remove('body__item__active')
    }
  }
}

function fetchEmployees() {
  fetch('/employees')
    .then(function (response) {
      return response.json()
    })
    .then(function (employees) {
      const employeesTableBody = document.getElementById('employeesTableBody')
      if (employees.length == 0) {
        employeesTableBody.innerHTML = 'No employees found'
      } else {
        employeesTableBody.innerHTML = ''
        employees.forEach((employee) => {
          const tr = document.createElement('tr')
          tr.innerHTML = `
                <td>${employee.firstname}</td>
                <td>${employee.lastname}</td>
                <td>${employee.age}</td>
                <td><img src="/static/employees/${employee.id}/${employee.image}" alt="Image" style="height:50;"/></td>
              `
          employeesTableBody.appendChild(tr)
        })
      }
    })
}

function createEmployee() {
  const formCreateEmployeeId = document.getElementById('formCreateEmployeeId')
  formCreateEmployeeId.addEventListener('submit', handlingSubmit)
}

function handlingSubmit(e) {
  e.preventDefault()
  e.stopPropagation()

  const submitFormButton = document.getElementById('submitFormButton')
  submitFormButton.disabled = true

  //Handle abort previous request
  const form = e.currentTarget
  const previousController = pendingForms.get(form)
  if (previousController) {
    previousController.abort()
  }

  const controller = new AbortController()
  pendingForms.set(form, controller)

  const formData = new FormData(formCreateEmployeeId)
  fetch('/create-employee', {
    method: 'POST',
    body: formData,
    signal: controller.signal,
  })
    .then(function (response) {
      console.log('response', response)
      return response.json()
    })
    .then(function (responseJson) {
      if (!responseJson.success) {
        const errorMessage = document.getElementById('errorMessage')
        errorMessage.style.display = 'block'
        errorMessage.innerHTML = responseJson.message
        submitFormButton.disabled = false
      } else {
        console.log('responseJson', responseJson)
        const successMessage = document.getElementById('successMessage')

        successMessage.style.display = 'block'
        successMessage.innerHTML = responseJson.message

        setTimeout(() => {
          formCreateEmployeeId.reset()
          successMessage.style.display = 'none'
          submitFormButton.disabled = false
        }, 3000)
      }
    })
}
