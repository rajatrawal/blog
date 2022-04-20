forCheckInput(false);
function forCheckInput(arg) {
  val = true;
  Array.from(document.getElementsByTagName('input')).forEach(e => {
    if (arg === false) {
      e.addEventListener('input', e => {
        checkInput(e.target);
      })
    }
    else {
      checkInput(e);

    }
  });

}
let checkInput = (e) => {

  if (e.value.length != 0) {
    e.classList.add('is-valid');
    e.classList.remove('is-invalid');
    checkPassword(e);
  }
  else {
    e.classList.add('is-invalid');
    e.classList.remove('is-valid');
    val = false;
  }
};
submitBtn.addEventListener('click', (e) => {
  forCheckInput(true);
  if (!val) {
    e.preventDefault();
  }
})
checkPassword = e => {
  if (e.getAttribute("name") == 'comformPassword') {
    password = document.getElementById('validationServer03').value;
    if (password != e.value) {
      e.classList.add('is-invalid');
      e.classList.remove('is-valid');
      val = false;
    }
  }
}