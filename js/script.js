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
// function for validating email
function validateEmail() {
    var email = document.getElementById('contact-email').value;
  
    if(email.length == 0) {
      emailError.innerHTML = "Email is required"
      return false;
    }
    if(!email.match(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/)){
      emailError.innerHTML = 'Email Invalid'
      return false;
    }
    
    emailError.innerHTML = '<i class="fa-solid fa-circle-check"></i>';
    return true;
  }

//  fucntion for validation for entering a message
  function validateMessage() {
    var message = document.getElementById('contact-me').value;
    var required = 30;
    var left = required - message.length;
  
    if(left > 0){
      messageError.innerHTML = " more characters required";
      return false;
    }
    messageError.innerHTML = '<i class="fa-solid fa-circle-check"></i>';
    return true;
  }
  
  // If user does not enter valid info the pop-up 'Please fix error' appears
  function validateForm() {
    if(!validateName() || !validateEmail() || !validateMessage()){
      submitError.style.display = 'block';
      submitError.innerHTML = 'Please fix error to proceed';
      setTimeout(function(){submitError.style.display = 'none';}, 3000)
      return false;
    }
  
  }