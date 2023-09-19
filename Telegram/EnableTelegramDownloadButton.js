// Function to remove the "hide" class from the third button
function removeHideClassFromThirdButton() {
    var buttonElements = document.querySelectorAll('.btn-icon.hide');
    if (buttonElements.length >= 3) {
      // Remove the "hide" class from the third button element
      buttonElements[2].classList.remove('hide');
      console.log('The "hide" class has been removed from the third button element.');
    }
    else {
    console.log('There are not enough elements with the class "btn-icon hide."');
    }
  }
  
  // Create a MutationObserver to monitor changes in the DOM
  var observer = new MutationObserver(function (mutationsList) {
    for (var mutation of mutationsList) {
      // Check if any mutation added the "hide" class to the third button
      if (
        mutation.type === 'attributes' &&
        mutation.attributeName === 'class' &&
        mutation.target.classList.contains('btn-icon') &&
        mutation.target.classList.contains('hide')
      ) {
        removeHideClassFromThirdButton();
      }
    }
  });
  
  // Configure the observer to watch for changes in the attributes of the third button
  var buttonElements = document.querySelectorAll('.btn-icon.hide');
  if (buttonElements.length >= 3) {
    observer.observe(buttonElements[2], { attributes: true });
  }
  
  // You can stop observing by calling observer.disconnect() when needed.
  // observer.disconnect();