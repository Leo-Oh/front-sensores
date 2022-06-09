const logs = document.getElementById('logs');

const btn_upate = document.getElementById('btn-upate')


btn_upate.addEventListener('click', () => {
  fetch('http://34.94.79.113:9095/api/logs')
    .then(response => response.json())
    .then(json => {
      console.log(json)
      for (var index in json) {

        const tr = document.createElement('tr');
        tr.setAttribute("id", "row");

        const tdId = document.createElement('td');
        tdId.textContent = json[index].id
        tr.appendChild(tdId);

        const tdtopic = document.createElement('td');
        tdtopic.textContent = json[index].topic
        tr.appendChild(tdtopic);

        const tdvalue = document.createElement('td');
        tdvalue.textContent = json[index].value
        tr.appendChild(tdvalue);

        const tdDate = document.createElement('td');
        tdDate.textContent = json[index].date
        tr.appendChild(tdDate);

        const tdTime = document.createElement('td');
        tdTime.textContent = json[index].time
        tr.appendChild(tdTime);


        logs.appendChild(tr);
      }
    })

});


