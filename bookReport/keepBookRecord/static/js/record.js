const startDate = document.querySelector('#start-date');
const endDate = document.querySelector('#end-date');
const bookContainer = document.querySelector('.book-container');
const readingTrue = bookContainer.querySelector('#reading-true');
const readingFalse = bookContainer.querySelector('#reading-false');
const quotationBtn = document.querySelector('.quotation-btn');
const impressionBtn = document.querySelector('.impression-btn');

function editImpression(e) {
  e.preventDefault();
  document.querySelector('#impression').readOnly = false;
  e.target.classList.remove('edit');
  e.target.textContent = 'Save';
  e.target.removeEventListener('click', editImpression);
  e.target.addEventListener('click', saveImpression);
  e.target.parentNode.parentNode.querySelector('textarea').focus();
}

function saveImpression(e) {
  e.preventDefault();
  document.querySelector('#impression').readOnly = true;
  e.target.classList.add('edit');
  e.target.textContent = 'Edit';
  e.target.removeEventListener('click', saveImpression);
  e.target.addEventListener('click', editImpression);
}

function setState(e, state) {
  const content = e.target.parentNode.parentNode.querySelector('textarea');
  const page = e.target.parentNode.parentNode.querySelector('input[type="text"]');
  content.readOnly = state;
  page.readOnly = state;
}

function resetId() {
  const quoList = document.querySelector('.quotations-list');
  if (quoList.children.length > 0) {
    for (let i = 0; i < quoList.children.length; i++) {
      quoList.children[i].id = i+1;
    }
  }
}

function deleteQuotation(e) {
  e.preventDefault();
  const delTarget = e.target.parentNode.parentNode;
  e.target.parentNode.parentNode.parentNode.removeChild(delTarget);
  resetId();
}

function createDelBtn() {
  const btn = document.createElement('button');
  btn.type = 'click';
  btn.textContent = 'Delete';
  btn.classList.add('delete');
  btn.addEventListener('click', deleteQuotation);
  return btn;
}

function editQuotation(e) {
  e.preventDefault();
  setState(e, false);
  e.target.classList.remove('edit');
  e.target.textContent = 'Save';
  e.target.removeEventListener('click', editQuotation);
  e.target.addEventListener('click', saveQuotation);
  quotationBtn.classList.add('hide');
  e.target.parentNode.parentNode.querySelector('textarea').focus();
}

function saveQuotation(e) {
  e.preventDefault();
  setState(e, true);
  const btnDiv = e.target.parentNode;
  if (btnDiv.querySelector('.delete') === null) {
    e.target.classList.add('first-btn');
    delBtn = createDelBtn();
    btnDiv.appendChild(delBtn);
  }
  e.target.classList.add('edit');
  e.target.textContent = 'Edit';
  e.target.removeEventListener('click', saveQuotation);
  e.target.addEventListener('click', editQuotation);
  quotationBtn.classList.remove('hide');
}

function addQuotation() {
  quotationBtn.classList.add('hide');
  const quotationList = document.querySelector('.quotations-list');
  const countLi = quotationList.childElementCount;
  const li = document.createElement('li');
  const content = document.createElement('textarea');
  const page = document.createElement('input');
  const span = document.createElement('span');
  const date = document.createElement('input');
  const btnDiv = document.createElement('div');
  const btn = document.createElement('button');
  li.id = countLi + 1;
  content.name = 'q-content-' + (countLi + 1);
  content.id = 'q-content-' + (countLi + 1);
  page.type = 'text';
  page.name = 'q-page-' + (countLi + 1);
  page.id = 'q-page-' + (countLi + 1);
  span.textContent = 'P';
  date.type = 'date';
  date.name = 'q-date-' + (countLi + 1);
  date.id = 'q-date-' + (countLi + 1);
  setDate(date);
  date.readOnly = true;
  btn.type = 'click';
  btn.textContent = 'Save';
  btn.addEventListener('click', saveQuotation);
  btnDiv.appendChild(btn);
  li.appendChild(content);
  li.appendChild(page);
  li.appendChild(span);
  li.appendChild(date);
  li.appendChild(btnDiv);
  quotationList.appendChild(li);
}

function checkRadio(option) {
  if (option.id === 'reading-true') {
    endDate.disabled = true;
    endDate.value = '';
  } else if (option.id === 'reading-false') {
    endDate.removeAttribute('disabled');
    setDate(endDate);
  }
}

function setDefaultRadio() {
  readingTrue.checked = true;
}

function setDate(date) {
  date.value = new Date().toISOString().substring(0, 10);
}

function init() {
  bookContainer.addEventListener('click', function(e) {
    let option = e.target;
    if (option.tagName !== 'INPUT') return;
    checkRadio(option)
  });
  quotationBtn.addEventListener('click', addQuotation);
  if (document.querySelector('.first-btn')) {
    const btn = document.querySelectorAll('.first-btn');
    btn.forEach((item) => {
      item.addEventListener('click', editQuotation);
    })
    impressionBtn.addEventListener('click', editImpression)
  } else {
    setDate(startDate);
    setDefaultRadio();
    impressionBtn.addEventListener('click', saveImpression);
  }
}

init();