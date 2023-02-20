let progressList = []
let progressList2 = []

let doneList = []
let doneList2 = []

function loadProgress(progressList){
    fetch('http://127.0.0.1:8000/in-progress')
    .then((response) => response.json())
    .then((data) => {
        for(let i = 0; i < 900; i++){
            try{
                let x = data[i].id
                if(progressList.includes(x)){
                    let o = x
                }
                else{
                    progressList.push(x)
                }
            }
            catch(e){

            }

        }
});
addToProgressUser();
}

function addToProgressUser(){
    const inProgress = document.getElementById("inProgressList")
    for (i = 0; i < progressList.length; i++) {
        let listItem = document.createElement("li");
        let x = progressList[i]
        if(progressList2.includes(x)){
            let o = 2
        }
        else{
            listItem.id = x;
            listItem.innerHTML = x;
            inProgress.appendChild(listItem);
            progressList2.push(x)
        }

    }
}

let x = 0

function loadDone(doneList){
fetch('http://127.0.0.1:8000/done')
.then((response) => response.json())
.then((data) => {
    let replaceList = []
    for(let i = 0; i < 900; i++){
        try{
            let x = data[i].id
            if(doneList.includes(x)){
                let o = x
            }
            else{
                doneList.push(x);
                replaceList.push(x);
            }
            let removeNum = document.getElementById(x);
            removeNum.remove();
            progressList.remove(x);
            progressList2.remove(x);
        }
        catch(e){

        }

    }
    for(i = 0; i < doneList.length; i++){
        let elementList = doneList[i]
        if(data[elementList] === undefined){
            console.log("araa " + elementList)
            if(doneList.includes(elementList)){
                const index = doneList.indexOf(elementList);
                const x = doneList.splice(index, 1);
                console.log(`myArray values: ${doneList}`);
                console.log(`variable x value: ${x}`);

                const index2 = doneList2.indexOf(elementList);
                const x2 = doneList2.splice(index2, 1);
                console.log(`myArray values2: ${doneList2}`);
                console.log(`variable x value2: ${x2}`);
            }
            let removeId = elementList + "done"
            let removableText = document.getElementById(removeId)
            try{
                removableText.remove();
                removableText.remove();
                removableText.remove();
                removableText.remove();
                removableText.remove();
                removableText.remove();
                removableText.remove();

            }
            catch(e){

            }
            
        }
        else{
            let j = 2
        }
    }

});
addToDoneUser();
}



function addToDoneUser(){
const inDone = document.getElementById("doneList")
for (i = 0; i < doneList.length; i++) {
    let listItem2 = document.createElement("li");
    let x = doneList[i]
    if(doneList2.includes(x)){
        let o = 2
    }
    else{
        listItem2.id = doneList[i] + "done"
        listItem2.innerHTML = doneList[i];
        inDone.appendChild(listItem2);
        doneList2.push(x)
    }
}

}

 function yourFunction(){
    loadProgress(progressList);
    loadDone(doneList);
    console.log("1 seconds passed")

    setTimeout(yourFunction, 1000);
}

yourFunction();