const dispensaryList = document.querySelector('#navBarMap');

function renderDispensary(doc) {
    let li = document.createElement('li');
    let building = document.createElement('span');

    li.setAttribute('data-id', doc.id);
    name.textContent = doc.data().building;

    li.appendChild(building);

    dispensaryList.appendChild(li);
}

db.collection('dispensaries').get().then((snapshot) => {
    snapshot.docs.forEach(doc => {
        renderDispensary(doc);
    })

})