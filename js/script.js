var nameError = document.getElementById('name-error')
var emailError = document.getElementById('email-error')
var messageError = document.getElementById('message-error')
var submitError = document.getElementById('submit-error')

//  function for email validation
function validateName() {
  var name = document.getElementById('contact-name').value;

  if(name.length == 0) {
    nameError.innerHTML = 'Name is required';
    return false;
  }
  if(!name.match(/^[a-zA-Z]+ [a-zA-Z]+$/)) {
    nameError.innerHTML = 'Enter full name please';
    return false;
  }
  nameError.innerHTML = '<i class="fa-solid fa-circle-check"></i>';
  return true;
}