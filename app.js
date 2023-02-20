fetch('http://127.0.0.1:8000/in-progress')
.then((response) => response.json())
.then((data) => {
  for(let i = 0; i < 900; i++){
    const inProgress = document.getElementById("inProgressDiv")
    let btn2 = document.createElement("button");
    try{
      btn2.innerHTML = data[i].id;
      btn2.type = "button";
      btn2.id = data[i].id;
      btn2.className = "during-button"
      btn2.setAttribute('onClick', 'addToDone(this.id);removeFromProgress(this.id);window.location.reload()');
      inProgress.appendChild(btn2);
    }
    catch (e) {
   }

  }
});

fetch('http://127.0.0.1:8000/done')
.then((response) => response.json())
.then((data) => {
  for(let i = 0; i < 900; i++){
    const doneSh = document.getElementById("doneDiv")
    let btn2 = document.createElement("button");
    try{
      btn2.innerHTML = data[i].id;
      btn2.type = "button";
      btn2.id = data[i].id;
      btn2.className = "during-button";
      btn2.setAttribute('onClick', 'removeFromDone(this.id)');
      doneSh.appendChild(btn2);
    }
    catch (e) {
   }

  }
});

// function addToProgress(){
//   const textInput = document.getElementById("inputOrder")
//   text = textInput.value
//   textInput.value = ""
//   var myHeaders = new Headers();
//   myHeaders.append("accept", "application/json");
//   myHeaders.append("Content-Type", "application/json");

//   var raw = JSON.stringify({
//   "name": "Shawarmaland",
//   "id": text
//   });

//   var requestOptions = {
//   method: 'POST',
//   headers: myHeaders,
//   body: raw,
//   redirect: 'follow'
// };

//   fetch("http://127.0.0.1:8000/in-progress", requestOptions)
//     .then(response => response.text())
//     .then(result => console.log(result))
//     .catch(error => console.log('error', error));
// }

function removeFromProgress(id){
  var myHeaders = new Headers();
  myHeaders.append("accept", "application/json");

  var requestOptions = {
    method: 'DELETE',
    headers: myHeaders,
    redirect: 'follow'
  };

  fetch("http://127.0.0.1:8000/in-progress/" + id, requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
}

function addToDone(id){
  var myHeaders = new Headers();
  myHeaders.append("accept", "application/json");
  myHeaders.append("Content-Type", "application/json");

  var raw = JSON.stringify({
    "name": "Shawarmaland",
    "id": id
  });

  var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
  };

  fetch("http://127.0.0.1:8000/done", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
  }

function removeFromDone(id){
  var myHeaders = new Headers();
  myHeaders.append("accept", "application/json");
  
  const removeBT = document.getElementById(id)
  removeBT.remove()

  var requestOptions = {
    method: 'DELETE',
    headers: myHeaders,
    redirect: 'follow'
  };

  fetch("http://127.0.0.1:8000/done/" + id, requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
}

setInterval(function() {
  window.location.reload();
}, 20000); 